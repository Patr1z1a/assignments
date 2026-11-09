### Assignment recapApp ###

# s123456_s56789, Moser_Lacher       ##TODO
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


# ================================
# Task 2: Filtering and Transformations
# the parameter 'students' is a list
# ================================

def filter_passing(students:list[tuple[int,str,int]]):
    """
    Filters and returns students with grade >= 60.
    """
    passing:list[tuple[int,str,int]] = []
    for i in students:
        if i[2] >= 60:
            passing.append(i)
    return passing


def to_name_grade_dict(students:list[tuple[int,str,int]]):
    """
    Converts list of tuples to a dictionary {name: grade}.
    """
    studic:dict[str, int] = {}
    for i in students:
        student_name:str = i[1]
        student_grade:int = i[2]
        studic.update({student_name: student_grade})
    return studic


def curve_grades(students:list[tuple[int,str,int]], curve_by:int):
    """
    Returns a new list of tuples with grades increased by curve_by (max 100).
    """
    curvedstulist:list[tuple[int,str,int]] = []
    for i in students:
        student_id:int = i[0]
        student_name:str = i[1]
        student_grade:int = i[2]+curve_by
        if student_grade >= 100:
            student_grade = 100
        tup = (student_id, student_name, student_grade)
        curvedstulist.append(tup)
    return curvedstulist


# ================================
# Task 3: Summary Statistics
# ================================

def print_statistics(students:list[tuple[int,str,int]]):
    """
    Prints number of students, average grade, min, and max. Use the formatting in the example:
    Example:
    Number of students: 5
    Average grade: 82.6
    Lowest grade: 59 (David)
    Highest grade: 100 (Eve)
    """
    try:
        num:int = len(students)
        addedgrades:int = 0
        lowest:int = 9999
        lowest_name:str = str("x")
        highest:int = 0
        highest_name:str = "y"
        for i in students:
            addedgrades += i[2]
            if i[2] <= lowest:
                lowest = i[2]
                lowest_name = i[1]
            if i[2] >= highest:
                highest = i[2]
                highest_name = i[1]
        average:float = addedgrades/num

        print(f"""
            Number of students: {num}
            Average grade: {average}
            Lowest grade: {lowest} ({lowest_name})
            Highest grade: {highest} ({highest_name})
            """)

        
    except Exception as e:
        print (e)

    

# ================================
# Task 4: File Writing
# ================================

def write_grades(filename:str, students:list[tuple[int,str,int]]):
    """
    Writes the list of student tuples back to a CSV file.
    Sort by name before writing.
    """
    def myFunc(tup:tuple[int,str,int]):
        return tup[1]
    students.sort(key=myFunc)

    with open(filename, "w") as f:
        for i in students:
            f.write(f"{i[0]};{i[1]};{i[2]}\n")


# ================================
# Task 5: Putting It All Together
# ================================

def main():

    # 1. Read file
    line = read_grades("A3/grades.csv")
    # 2. Print stats
    print_statistics(line)
    # 3. Filter failing
    filtered = filter_passing(line)
    # 4. Curve grades +5
    curved = curve_grades(filtered, 5)
    # 5. Print stats again
    print_statistics(curved)
    # 6. Write curved grades
    write_grades("A3/grades_curved.csv", curved)


if __name__ == "__main__":
    main()
  

