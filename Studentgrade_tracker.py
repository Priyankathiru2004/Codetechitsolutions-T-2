# Initialize variables
grades = []
total_marks = 0

# Prompt the user to input grades for different subjects or assignments
num_subjects = int(input("Enter the number of subjects or assignments: "))

for i in range(num_subjects):
    grade = float(input(f"Enter the grade for subject or assignment {i+1}: "))
    grades.append(grade)
    total_marks += grade

# Calculate the average grade
average_grade = total_marks / num_subjects

# Calculate the overall grade
overall_grade = None

if average_grade >= 90:
    overall_grade = "A"
elif average_grade >= 80:
    overall_grade = "B"
elif average_grade >= 70:
    overall_grade = "C"
elif average_grade >= 60:
    overall_grade = "D"
else:
    overall_grade = "F"

# Calculate the GPA
gpa = None

if overall_grade == "A":
    gpa = 4.0
elif overall_grade == "B":
    gpa = 3.0
elif overall_grade == "C":
    gpa = 2.0
elif overall_grade == "D":
    gpa = 1.0
else:
    gpa = 0.0

# Display the results
print("Grades:", grades)
print("Average Grade:", average_grade)
print("Overall Grade:", overall_grade)
print("GPA:", gpa)
