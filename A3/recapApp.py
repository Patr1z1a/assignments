### Assignment recapApp ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO
# Implement a console-based Student Grades Manager.
# The program reads data from a CSV file, allows some data processing and summary operations, and writes results back to another file.

# ================================
# Task 1: File Reading
# ================================

def read_grades(filename:str)->list[tuple[int,str,int]]:
    """
        Reads the CSV file and returns a list of tuples (student_id, name, grade).
        Handles file-not-found gracefully: Log the error to the console and return an empty list.
    """
    ls:list[tuple[int,str,int]] = []
    try:
        with open(filename, "r") as f:
            for line in f:
                cells = line.split(";")
                if len(cells) == 3:
                    student_id:int = int(cells[0])
                    student_name:str = cells[1]
                    student_grade:int = int(cells[2])
                    tup = (student_id,student_name, student_grade)
                    ls.append(tup)
    except FileNotFoundError as f:
        print(f)
    return ls

line = read_grades("A3/grades.csv")
# ================================
# Task 2: Filtering and Transformations
# the parameter 'students' is a list
# ================================

def filter_passing(students:list[tuple[int,str,int]]):
    """
    Filters and returns students with grade >= 60.
    """
    passing:list[tuple[int,str,int]] = []
    for i in line:
        if i[2] >= 80:
            passing.append(i)
    return passing
filter_passing(line)



def to_name_grade_dict(students:list[tuple[int,str,int]]):
    """
    Converts list of tuples to a dictionary {name: grade}.
    """
    suddic:dict[str, int] = {}
    for i in line:
        student_name:str = i[1]
        student_grade:int = i[2]
        suddic.update({student_name: student_grade})
    print(suddic)
    return suddic

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
  

