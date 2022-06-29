# python | Day 29
# GPA Calculator.
# Write a function that:
# 1) Takes as parameters, a list of tuples, containing grades and their corresponding units.
# (E.G: [ ("A", 2), ("A",3), ("B", 2),...etc])
# 2) Computes and returns the student GPA, based on the values provides.
# *Note: Handle All necessary exceptions and/or edge cases.

gc_tuple = ()


def collect_result():
    """A function that collects user grades and course unit."""

    global gc_tuple
    user_result = []

    print("Enter your grades and their respective units. If there are no more grades, press Enter to continue.")

    try:
        while True:
            grade = str(input("Enter grade: ")).upper()
            if grade != "":
                course_unit = int(input("Enter course unit: "))
                gc_tuple = (grade, course_unit)
            elif grade == "":
                break
            user_result.append(gc_tuple)
        return user_result
    except ValueError:
        print("Invalid number entered for course unit! Please try again.")


def gpa_calc(results):
    """A function to calculate the user GPA."""

    try:
        grade_weights = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1, "F": 0}
        units_taken = 0
        total_grade_units = 0

        for i in results:
            units_taken += i[1]
            total_grade_units += grade_weights[i[0]] * i[1]

        gpa = total_grade_units / units_taken

        return gpa
    except KeyError:
        print("Please enter a valid grade. Accepted grades are A,B,C,D,E and F.")
    except ZeroDivisionError:
        print("Course unit cannot be zero if you take only a single course!")


try:
    student_res = gpa_calc(collect_result())
    print(f"Your GPA is: {student_res: 0.2f}")
except TypeError:
    print("Please enter correct values for your results(grades and units).")
