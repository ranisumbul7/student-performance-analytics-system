# Student Performance Analytics System

## 1. Student Details

**Student Name:** Sumbul Rani
**Course:** B.Tech Computer Science Engineering
**Project Title:** Student Performance Analytics System

---

## 2. Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that can analyze student academic performance and attendance data.

The system calculates total marks, average marks, grades, pass/fail status, subject-wise performance, grade distribution, top performers, and attendance statistics.

---

## 3. Technologies Used

The following technologies and concepts were used:

* Python
* NumPy
* Pandas
* CSV
* Variables and Data Types
* Conditional Statements
* Loops
* Functions
* Data Analysis

---

## 4. Dataset Description

The project uses a CSV dataset named `students.csv`.

The dataset contains **20 student records**.

### Dataset Fields

| Field         | Description                     |
| ------------- | ------------------------------- |
| Student_ID    | Unique ID of each student       |
| Name          | Student name                    |
| Department    | Student department              |
| Python        | Marks obtained in Python        |
| Data_Analysis | Marks obtained in Data Analysis |
| Mathematics   | Marks obtained in Mathematics   |
| Attendance    | Attendance percentage           |

---

## 5. Implementation

The project is divided into two Python files:

### `main.py`

The main program:

* Reads the student dataset using Pandas
* Processes each student's marks
* Calculates total and average marks
* Assigns grades
* Determines pass/fail status
* Performs class-level analysis
* Performs subject-wise analysis
* Analyzes attendance
* Displays the final project summary

### `functions.py`

This file contains reusable functions:

* `calculate_total()`
* `calculate_average()`
* `assign_grade()`
* `check_result()`

NumPy is used for numerical calculations such as sum and average.

Pandas is used for DataFrame operations, filtering, sorting, and analysis.

---

## 6. Grading and Pass/Fail Rules

### Grading Rule

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A+    |
| 80–89.99      | A     |
| 70–79.99      | B     |
| 60–69.99      | C     |
| 50–59.99      | D     |
| Below 50      | F     |

### Pass/Fail Rule

A student is considered **Pass** if they score at least 40 marks in every subject.

If the student scores below 40 in any subject, the result is **Fail**.

---

## 7. Key Features

The system provides the following features:

1. Student performance analysis
2. Total marks calculation
3. Average marks calculation
4. Automatic grade assignment
5. Pass/fail determination
6. Overall class average
7. Highest performing student
8. Lowest performing student
9. Top 5 performing students
10. Subject-wise average analysis
11. Grade distribution
12. Attendance analysis
13. Identification of students with attendance below 75%
14. Final project summary

---

## 8. Output and Analysis

The program successfully analyzed 20 students.

### Final Results

* **Total Students:** 20
* **Overall Class Average:** 79.50%
* **Passed Students:** 20
* **Failed Students:** 0
* **Pass Percentage:** 100%
* **Best Performing Subject:** Mathematics
* **Mathematics Average:** 80.50
* **Highest Performer:** Neha Kumari
* **Highest Average:** 95.00%
* **Lowest Performer:** Ayush Verma
* **Lowest Average:** 57.67%
* **Average Attendance:** 87.40%
* **Students Below 75% Attendance:** 2

### Top 5 Performers

| Student      | Average | Grade |
| ------------ | ------: | ----- |
| Neha Kumari  |   95.00 | A+    |
| Ananya Singh |   91.67 | A+    |
| Tanya Singh  |   91.67 | A+    |
| Pooja Kumari |   91.00 | A+    |
| Riya Singh   |   90.33 | A+    |

### Subject-wise Performance

| Subject       | Average Marks |
| ------------- | ------------: |
| Python        |         79.15 |
| Data Analysis |         78.85 |
| Mathematics   |         80.50 |

---

## 9. Challenges and Learning

During the development of this project, I learned how to work with CSV datasets using Pandas and perform numerical calculations using NumPy.

I also practiced Python loops, conditional statements, functions, DataFrame filtering, sorting, and basic data analysis.

One of the main challenges was organizing the analysis into reusable functions and generating multiple performance statistics from the same dataset.

This project improved my understanding of how Python can be used for real-world data analysis tasks.

---

## 10. Final Outcome

The Student Performance Analytics System successfully analyzes student academic and attendance data and generates useful performance insights.

The project demonstrates the practical use of **Python, NumPy, and Pandas** for data processing and analysis.

The system is simple, reusable, and can be extended in the future with additional subjects, graphical visualizations, larger datasets, or a web-based interface.

---

## GitHub Repository

**GitHub Repository:**
To be added after uploading the project to GitHub.
