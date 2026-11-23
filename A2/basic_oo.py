import math

### Assignment basic_oo ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################


# Task 1: map/filter/sum/...

# 1a:
def toCelsiusMap(lst):
    return list(map(lambda f: (f - 32) * 5 / 9, lst))


# 1b:
def toCelsiusLC(lst):
    return [(f - 32) * 5 / 9 for f in lst]


# 1c:
def mathFuncMapFilter(lowerBound, upperBound):
    even_numbers = filter(lambda i: i % 2 == 0, range(lowerBound, upperBound + 1))
    cubed_numbers = map(lambda i: i ** 3, even_numbers)
    result = sum(cubed_numbers)
    return result


# 1d:
def mathFuncLC(lowerBound, upperBound):
    return sum([i ** 3 for i in range(lowerBound, upperBound + 1) if i % 2 == 0])


##########################################################################

# Task 2
class Person:
    def __init__(self, name, id, comment=""):
        self.name = name
        self.id = id
        self.comment = comment

    def rename(self, newName):
        self.name = newName

    def __str__(self):
        return f"{self.name} (id={self.id})"


##########################################################################

# Task 3
def toObjectList(names):
    return [Person(name, index) for index, name in enumerate(names)]


##########################################################################

# Task 4
def getDuplicatesAlphabetical(listOfPersonObjects):
    names = [person.name for person in listOfPersonObjects]
    duplicates = {name for name in names if names.count(name) > 1}
    return tuple(sorted(duplicates))


##########################################################################

# Task 5
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFromOrigin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def halfway(self, target):
        mid_x = (self.x + target.x) / 2
        mid_y = (self.y + target.y) / 2
        return Point2D(mid_x, mid_y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"