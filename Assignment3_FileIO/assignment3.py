import re

with open("big_data_students.csv") as file:
    lines=file.readlines()
    print(lines)
    student_lines=lines[1:]

    top_students = []

    for line in student_lines:
        name, email, grade = line.strip().split(',')
        grade = int(grade)
        print(f"Name:{name},Email:{email},Grade: {grade}")
        
        if grade > 80:
            top_students.append(name)

    student_data = []

    for line in student_lines:
        name, email, grade = line.strip().split(',')
        grade = int(grade)
        student_data.append((name, email, grade))

with open ("top_students.txt","w") as output_file:
    for name in top_students:
        output_file.write(name + "\n")

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    for name,email, grade in student_data:
        if re.search(pattern, email):
            print(email)

    pattern = r"^[AP]"
    for name,email,grade in student_data:
        if re.match(pattern,name):
            print(name)

    pattern = r"@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    domain_count = {}
    for name,email,grade in student_data:
        match=re.search(pattern,email)
        if match:
            domain = match.group()
            if domain in domain_count:
                domain_count[domain] += 1
            else:
                domain_count[domain] = 1
    print("Email domain counts:")
    for domain, count in domain_count.items():
        print(f"{domain}: {count}")

    pattern = r"^[a-z]+\.[a-z]+@"
    for name, email, grade in student_data:
        if re.match(pattern,email):
            print(email)

    pattern = r"\d+"
    for name, email, grade in student_data:
        digits = re.findall(pattern, email)
        if digits:
            print(f"{email} → {digits}")
        else:
            print(f"{email} → No digits")

    updated_lines = []
    for name, email, grade in student_data:
        if grade < 60:
            line_string = f"{name},{email},{grade}"
            update_line = re.sub(r"\d+", "Fail", line_string)
        else:
            updated_line = f"{name},{email},{grade}"
        updated_lines.append(updated_line)

with open("updated_students.csv", "w") as f_out:
    f_out.write("Name,Email,Grade\n")
    for line in updated_lines:
        f_out.write(line + "\n")