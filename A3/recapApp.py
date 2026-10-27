### Assignment recapApp ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO
# Implement a console-based Student Grades Manager.
# The program reads data from a CSV file, allows some data processing and summary operations, and writes results back to another file.

# ================================
# Task 1: File Reading
# ================================

def read_grades(filename):
    """
    Reads the CSV file and returns a list of tuples (student_id, name, grade).
    Handles file-not-found gracefully: Log the error to the console and return an empty list.
    """
    # TODO: Implement
    return []


# ================================
# Task 2: Filtering and Transformations
# the parameter 'students' is a list
# ================================

def filter_passing(students):
    """
    Filters and returns students with grade >= 60.
    """
    # TODO: Implement
    return []

def to_name_grade_dict(students):
    """
    Converts list of tuples to a dictionary {name: grade}.
    """
    # TODO: Implement
    return {}

def curve_grades(students, curve_by):
    """
    Returns a new list of tuples with grades increased by curve_by (max 100).
    """
    # TODO: Implement
    return []


# ================================
# Task 3: Summary Statistics
# ================================

def print_statistics(students):
    """
    Prints number of students, average grade, min, and max. Use the formatting in the example:
    Example:
    Number of students: 5
    Average grade: 82.6
    Lowest grade: 59 (David)
    Highest grade: 100 (Eve)

    """
    # TODO: Implement
    pass


# ================================
# Task 4: File Writing
# ================================

def write_grades(filename, students):
    """
    Writes the list of student tuples back to a CSV file.
    Sort by name before writing.
    """
    # TODO: Implement
    pass


# ================================
# Task 5: Putting It All Together
# ================================

def main():
    # TODO: Implement program flow:
    # 1. Read file
    # 2. Print stats
    # 3. Filter failing
    # 4. Curve grades +5
    # 5. Print stats again
    # 6. Write curved grades
    pass


if __name__ == "__main__":
    main()
  

