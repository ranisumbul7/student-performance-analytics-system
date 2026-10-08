# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based data analysis project developed using **Python, NumPy, and Pandas**.

The system analyzes student academic performance and attendance data. It calculates total and average marks, assigns grades, determines pass/fail status, performs subject-wise analysis, identifies top performers, and provides attendance statistics.

## 🎯 Objective

The main objectives of this project are:

* Analyze student performance data
* Calculate total and average marks
* Assign grades based on average marks
* Determine pass/fail status
* Perform subject-wise performance analysis
* Identify highest and lowest performing students
* Find the top 5 performers
* Analyze grade distribution
* Analyze student attendance
* Generate a clear performance summary

##  Technologies Used

* Python
* Pandas
* NumPy
* CSV Dataset

## Project Structure

```text
Student Performance Analytics System/
│
├── main.py
├── functions.py
├── students.csv
└── README.md
```

## Dataset

The project uses a CSV file named `students.csv` containing 20 student records.

Each record contains:

* Student ID
* Name
* Department
* Python marks
* Data Analysis marks
* Mathematics marks
* Attendance percentage

## Implementation

The project uses reusable functions for:

### 1. Total Marks

NumPy is used to calculate the total marks obtained by a student.

### 2. Average Marks

The average is calculated using the total marks obtained in three subjects.

### 3. Grade Assignment

Grades are assigned according to the following rules:

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A+    |
| 80–89.99      | A     |
| 70–79.99      | B     |
| 60–69.99      | C     |
| 50–59.99      | D     |
| Below 50      | F     |

### 4. Pass/Fail Rule

A student passes if they score at least **40 marks in every subject**.

If the student scores below 40 in any subject, the result is marked as **Fail**.

## 🔍 Key Features

* Student performance calculation
* Total and average marks
* Grade assignment
* Pass/fail analysis
* Class average calculation
* Highest and lowest performer identification
* Top 5 performer analysis
* Subject-wise average analysis
* Grade distribution
* Attendance analysis
* Low attendance student identification
* Final performance summary

## Sample Analysis Results

Based on the current dataset:

* **Total Students:** 20
* **Overall Class Average:** 79.50%
* **Pass Percentage:** 100%
* **Best Performing Subject:** Mathematics
* **Highest Performer:** Neha Kumari
* **Highest Average:** 95.00%
* **Average Attendance:** 87.40%
* **Students Below 75% Attendance:** 2

## How to Run

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install pandas numpy
```

Then open the project folder in the terminal:

```bash
cd "F:\Student Performance Analytics System"
```

Run the project:

```bash
python main.py
```

The program will display the complete student performance analysis in the terminal.

## Learning Outcomes

Through this project, I practiced:

* Python variables and data types
* Conditional statements
* Loops
* Functions
* NumPy operations
* Pandas DataFrames
* Data filtering and sorting
* Data analysis
* CSV file handling
* Basic statistical calculations
* Project organization

## ✅ Final Outcome

The Student Performance Analytics System successfully processes student data and generates meaningful academic and attendance insights using Python, NumPy, and Pandas.

## Author

**Sumbul Rani**

B.Tech Computer Science Engineering Graduate
