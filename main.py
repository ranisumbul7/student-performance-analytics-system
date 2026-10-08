import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    check_result
)

# ==============================
# LOAD DATASET
# ==============================

df = pd.read_csv("students.csv")


# ==============================
# CALCULATE PERFORMANCE
# ==============================

total_marks = []
average_marks = []
grades = []
results = []


for index, row in df.iterrows():

    marks = [
        row["Python"],
        row["Data_Analysis"],
        row["Mathematics"]
    ]

    total = calculate_total(marks)
    average = calculate_average(total)

    grade = assign_grade(average)
    result = check_result(marks)

    total_marks.append(total)
    average_marks.append(round(average, 2))
    grades.append(grade)
    results.append(result)


# ==============================
# ADD RESULTS TO DATAFRAME
# ==============================

df["Total_Marks"] = total_marks
df["Average_Marks"] = average_marks
df["Grade"] = grades
df["Result"] = results


# ==============================
# DISPLAY RESULTS
# ==============================

print("\n========== STUDENT PERFORMANCE ==========")

print(
    df[
        [
            "Student_ID",
            "Name",
            "Total_Marks",
            "Average_Marks",
            "Grade",
            "Result"
        ]
    ]
)

# ==============================
# CLASS PERFORMANCE ANALYSIS
# ==============================

# Overall class average
class_average = np.mean(df["Average_Marks"])

# Highest performing student
highest_index = df["Average_Marks"].idxmax()
highest_student = df.loc[highest_index]

# Lowest performing student
lowest_index = df["Average_Marks"].idxmin()
lowest_student = df.loc[lowest_index]


# ==============================
# TOP PERFORMERS
# ==============================

top_performers = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)


# ==============================
# DISPLAY ANALYSIS
# ==============================

print("\n========== CLASS PERFORMANCE ANALYSIS ==========")

print(f"Overall Class Average: {class_average:.2f}")

print("\nHighest Performing Student:")
print(
    f"Name: {highest_student['Name']}"
    f" | Average: {highest_student['Average_Marks']}"
)

print("\nLowest Performing Student:")
print(
    f"Name: {lowest_student['Name']}"
    f" | Average: {lowest_student['Average_Marks']}"
)


print("\nTop 5 Performing Students:")

print(
    top_performers[
        [
            "Student_ID",
            "Name",
            "Average_Marks",
            "Grade"
        ]
    ].to_string(index=False)
)

# ==============================
# SUBJECT-WISE PERFORMANCE
# ==============================

subjects = [
    "Python",
    "Data_Analysis",
    "Mathematics"
]

subject_averages = []

for subject in subjects:
    average = np.mean(df[subject])
    subject_averages.append(round(average, 2))


# Create subject performance table
subject_analysis = pd.DataFrame({
    "Subject": subjects,
    "Average_Marks": subject_averages
})


# Find best performing subject
best_subject_index = subject_analysis["Average_Marks"].idxmax()
best_subject = subject_analysis.loc[best_subject_index]


# ==============================
# DISPLAY SUBJECT ANALYSIS
# ==============================

print("\n========== SUBJECT-WISE PERFORMANCE ==========")

print(subject_analysis.to_string(index=False))

print(
    f"\nBest Performing Subject: "
    f"{best_subject['Subject']} "
    f"({best_subject['Average_Marks']} average marks)"
)

# ==============================
# PASS / FAIL STATISTICS
# ==============================

total_students = len(df)

passed_students = (df["Result"] == "Pass").sum()
failed_students = (df["Result"] == "Fail").sum()

pass_percentage = (passed_students / total_students) * 100
fail_percentage = (failed_students / total_students) * 100


# ==============================
# GRADE DISTRIBUTION
# ==============================

grade_counts = df["Grade"].value_counts()


# ==============================
# DISPLAY PASS / FAIL STATISTICS
# ==============================

print("\n========== PASS / FAIL STATISTICS ==========")

print(f"Total Students: {total_students}")
print(f"Passed Students: {passed_students}")
print(f"Failed Students: {failed_students}")
print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Fail Percentage: {fail_percentage:.2f}%")


# ==============================
# DISPLAY GRADE DISTRIBUTION
# ==============================

print("\n========== GRADE DISTRIBUTION ==========")

for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} students")

    # ==============================
# ATTENDANCE ANALYSIS
# ==============================

average_attendance = np.mean(df["Attendance"])
highest_attendance = df["Attendance"].max()
lowest_attendance = df["Attendance"].min()

# Students with attendance below 75%
low_attendance_students = df[df["Attendance"] < 75]


# ==============================
# DISPLAY ATTENDANCE ANALYSIS
# ==============================

print("\n========== ATTENDANCE ANALYSIS ==========")

print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Highest Attendance: {highest_attendance}%")
print(f"Lowest Attendance: {lowest_attendance}%")

print("\nStudents with Attendance Below 75%:")

if len(low_attendance_students) == 0:
    print("No student has attendance below 75%.")
else:
    print(
        low_attendance_students[
            ["Student_ID", "Name", "Attendance", "Average_Marks"]
        ].to_string(index=False)
    )

    # ==============================
# FINAL PROJECT SUMMARY
# ==============================

print("\n========== FINAL PROJECT SUMMARY ==========")

print(f"Total Students Analyzed: {total_students}")
print(f"Overall Class Average: {class_average:.2f}%")
print(f"Pass Percentage: {pass_percentage:.2f}%")
print(f"Best Performing Subject: {best_subject['Subject']}")
print(f"Highest Performer: {highest_student['Name']}")
print(f"Highest Average: {highest_student['Average_Marks']:.2f}")
print(f"Average Attendance: {average_attendance:.2f}%")

print("\nAnalysis completed successfully!")