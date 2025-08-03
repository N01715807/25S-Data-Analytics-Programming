import pandas as pd
import numpy as np
import os

def clean_and_summarize(filepath):
    print(f"Reading dataset from: {filepath}")
    
    if not os.path.exists(filepath):
        print("Error: File not found.")
        return {}, os.path.basename(filepath)

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        print(f"Failed to read CSV: {e}")
        return {}, os.path.basename(filepath)

    original_shape = df.shape
    nulls_before = df.isnull().sum().to_dict()

    # Drop exact duplicates
    before_dedup = len(df)
    df.drop_duplicates(inplace=True)
    after_dedup = len(df)
    duplicates_removed = before_dedup - after_dedup

    # Fill NAs only for object columns
    for col in df.select_dtypes(include='object'):
        df[col].fillna("N/A", inplace=True)

    # Try converting 'date' columns
    for col in [c for c in df.columns if 'date' in c.lower() or 'timestamp' in c.lower()]:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        except:
            pass

    nulls_after = df.isnull().sum().to_dict()
    cleaned_shape = df.shape

    # Save cleaned data to a new file
    cleaned_path = os.path.join(os.path.dirname(filepath), 'cleaned_' + os.path.basename(filepath))
    df.to_csv(cleaned_path, index=False)

    # Create HTML table for descriptive statistics
    try:
        describe_html = df.describe(include='all').to_html(classes='summary-table', border=1)
    except:
        describe_html = "<p>Summary table could not be generated.</p>"

    summary = {
        'original_shape': original_shape,
        'cleaned_shape': cleaned_shape,
        'duplicates_removed': duplicates_removed,
        'nulls_before': nulls_before,
        'nulls_after': nulls_after,
        'describe': describe_html
    }

    return summary, os.path.basename(cleaned_path)
