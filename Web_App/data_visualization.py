import matplotlib
matplotlib.use('Agg')  # 强制使用非GUI后端，适配 Flask

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(filepath):
    # Read uploaded CSV
    df = pd.read_csv(filepath)

    # Remove age outliers
    df = df[(df['Age'] > 10) & (df['Age'] < 100)]

    # Set output directory for chart images
    chart_dir = os.path.join('static', 'charts')
    os.makedirs(chart_dir, exist_ok=True)

    chart_paths = []  # List to return relative paths of saved charts

    # ------------------------
    # Does a family history of mental illness affect an employee’s willingness to seek help?
    # ------------------------

    # 1. family_history_vs_seek_help_bar.png
    crosstab = pd.crosstab(df['family_history'], df['seek_help'])
    crosstab.plot(kind='bar', stacked=True)
    plt.title('Family History vs Seek Help')
    plt.xlabel('Family History of Mental Illness')
    plt.ylabel('Number of Employees')
    plt.tight_layout()
    plt.savefig('static/charts/family_history_vs_seek_help_bar.png')
    chart_paths.append('charts/family_history_vs_seek_help_bar.png')
    plt.close()

    # 2. family_history_seek_help_percentage.png
    percent = df.groupby('family_history')['seek_help'].value_counts(normalize=True).unstack() * 100
    percent.plot(kind='bar')
    plt.title('Seek Help Percentage by Family History')
    plt.ylabel('Percentage')
    plt.tight_layout()
    plt.savefig('static/charts/family_history_seek_help_percentage.png')
    chart_paths.append('charts/family_history_seek_help_percentage.png')
    plt.close()

    # ------------------------
    # Does your employer offer mental health services?
    # ------------------------

    # 3. benefits_pie.png
    df['benefits'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Does Employer Provide Mental Health Benefits?')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('static/charts/benefits_pie.png')
    chart_paths.append('charts/benefits_pie.png')
    plt.close()

    # 4. benefits_vs_seek_help_bar.png
    sns.countplot(data=df, x='benefits', hue='seek_help')
    plt.title('Seek Help by Employer Benefits')
    plt.xlabel('Mental Health Benefits Offered')
    plt.ylabel('Number of Employees')
    plt.tight_layout()
    plt.savefig('static/charts/benefits_vs_seek_help_bar.png')
    chart_paths.append('charts/benefits_vs_seek_help_bar.png')
    plt.close()

    # ------------------------
    # Work interference
    # ------------------------

    # 5. work_interfere_vs_treatment_bar.png
    sns.countplot(data=df, x='work_interfere', hue='treatment')
    plt.title('Work Interference vs Mental Health Treatment')
    plt.xlabel('Work Interference')
    plt.xticks(rotation=15)
    plt.ylabel('Number of Employees')
    plt.tight_layout()
    plt.savefig('static/charts/work_interfere_vs_treatment_bar.png')
    chart_paths.append('charts/work_interfere_vs_treatment_bar.png')
    plt.close()

    # 6. correlation_heatmap.png
    numeric_df = df.copy()
    numeric_df['treatment'] = numeric_df['treatment'].map({'Yes': 1, 'No': 0})
    numeric_df['work_interfere'] = numeric_df['work_interfere'].map({'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Often': 3})
    sns.heatmap(numeric_df[['Age', 'treatment', 'work_interfere']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('static/charts/correlation_heatmap.png')
    chart_paths.append('charts/correlation_heatmap.png')
    plt.close()

    # ------------------------
    # Remote work & mental health
    # ------------------------

    # 7. remote_work_distribution_pie.png
    df['remote_work'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Remote Work Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig('static/charts/remote_work_distribution_pie.png')
    chart_paths.append('charts/remote_work_distribution_pie.png')
    plt.close()

    # 8. remote_work_vs_consequence_bar.png
    sns.countplot(data=df, x='remote_work', hue='mental_health_consequence')
    plt.title('Mental Health Consequences by Remote Work Status')
    plt.xlabel('Remote Work')
    plt.ylabel('Number of Employees')
    plt.tight_layout()
    plt.savefig('static/charts/remote_work_vs_consequence_bar.png')
    chart_paths.append('charts/remote_work_vs_consequence_bar.png')
    plt.close()

    # ------------------------
    # Age impact
    # ------------------------

    # 9. age_distribution_hist.png
    df['Age'].plot(kind='hist', bins=20)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.tight_layout()
    plt.savefig('static/charts/age_distribution_hist.png')
    chart_paths.append('charts/age_distribution_hist.png')
    plt.close()

    # 10. age_boxplot_by_mh_view.png
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=df, x='mental_vs_physical', y='Age', inner='quartile')
    plt.title('Age by View on Mental vs Physical Health')
    plt.xlabel('View of Mental vs Physical Health')
    plt.ylabel('Age')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig('static/charts/age_boxplot_by_mh_view.png')
    chart_paths.append('charts/age_boxplot_by_mh_view.png')
    plt.close()

    # ------------------------
    # Gender differences
    # ------------------------

    # 11. gender_distribution_pie.png
    plt.figure(figsize=(8, 5))
    df['gender_cleaned'] = df['Gender'].str.lower().str.strip()
    df['gender_cleaned'] = df['gender_cleaned'].replace({'male': 'Male', 'm': 'Male','female': 'Female', 'f': 'Female'})
    gender_counts = df['gender_cleaned'].value_counts()
    gender_counts.plot(kind='barh', color='skyblue')
    plt.title('Gender Distribution')
    plt.xlabel('Number of Employees')
    plt.ylabel('Gender')
    plt.tight_layout()
    plt.savefig('static/charts/gender_distribution_pie.png')
    chart_paths.append('charts/gender_distribution_pie.png')
    plt.close()

    # 12. gender_vs_seek_help_bar.png
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='gender_cleaned', hue='seek_help')
    plt.title('Seek Help by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Employees')
    plt.xticks(rotation=0, fontsize=10)
    plt.legend(title='Seek Help')
    plt.tight_layout()
    plt.savefig('static/charts/gender_vs_seek_help_bar.png')
    chart_paths.append('charts/gender_vs_seek_help_bar.png')
    plt.close()

    return chart_paths
