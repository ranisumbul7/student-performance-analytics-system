import numpy as np


def calculate_total(marks):
    return np.sum(marks)


def calculate_average(total):
    return total / 3


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"
    return "Pass"