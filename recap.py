### Assignment recap ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO


#Task 1
#Implement a procedure "process" that takes the following arguments:
# names: a string containing a sequence of comma-separated names
# last: a string that might occur in sequence of the argument <names>; but maybe it doesn't occur 
# notStartingWith: a string
#the return value of this procedure shall be a list of all the names until (but including) the name given in the argument <last>; at this, the returned list must not contain names that begin with the string given in argument <notStartingWith>

#Important: use the slice operator, filter and lambda-expression!

def process(names, last, notStartingWith):
    return None

#Examples: 
process("Thomas, Michael, Thomas, Andrea, Barbara, Susanne, Michael, Fabian, Hans", "Fabian", "A")
#shall return ['Thomas', 'Michael', 'Thomas', 'Barbara', 'Susanne', 'Michael', 'Fabian']

process("Andrea,Barbara", "NotInList", "Bar")
#shall return ['Andrea']


##########################################################################


#Task 2
#Implement a procedure "toDict" that takes a list of names (as returned by "process" from Task1)
#and returns a dictionary containing the names as keys and the number of characters of each respective name as value

def toDict(names):
    return None


#Example:
toDict(['Thomas', 'Michael', 'Thomas', 'Barbara', 'Susanne', 'Michael', 'Fabian'])
#shall return {'Barbara': 7, 'Fabian': 6, 'Michael': 7, 'Susanne': 7, 'Thomas': 6} #note that the order might be different (why is this?)


##########################################################################

#Task 3
#Implement a procedure "toListSkipLowerCase" that uses list comprehension to turn a tuple of strings into a list of strings. At this, strings that start with a lower-case letter shall be skipped.
#

def toListSkipLowerCase(tuple):
    return None
    
#Examples:
toListSkipLowerCase(("hans", "Fritz", "max", "Petra", "Susanne", "toni"))
#shall return ["Fritz","Petra", "Susanne"]

toListSkipLowerCase(("hans", "max"))
#shall return []


##########################################################################


#Task 4
#Implement a procedure "applyFuncToAll" that takes a function "func" and a list of items "lst"
#and returns a list of the results after applying "func" to each item of "lst".

def applyFuncToAll(func, lst):
    return None
    
#Examples:
applyFuncToAll(lambda i: i*2, [1,2,3])
#shall return [2,4,6]

applyFuncToAll(len, ["a","bb","ccc"])
#shall return [1,2,3]


##########################################################################


#Task 5
#Implement a procedure "swallowException" that takes a function "func" and returns the value that is returned when executing "func". In case the execution of func raises a "division-by-zero" execption, the returned value shall be the string "only chuck norris is allowed to divide by zero". In case another exception occurs, the returned value shall be the string "something went wrong".

def swallowException(func):
    v = func()
    return v
    
#Examples:
swallowException(lambda: 100)
#shall return 100

#swallowException(lambda: 100/0)
#shall return "only chuck norris is allowed to divide by zero"

#swallowException(lambda: [1,2,3][5])
#shall return "something went wrong"



#You may use this to test your procedures
if __name__ == "__main__":
  #assert process("Thomas, Michael, Thomas, Andrea, Barbara, Susanne, Michael, Fabian, Hans", "Fabian", "A") == ['Thomas', 'Michael', 'Thomas', 'Barbara', 'Susanne', 'Michael', 'Fabian']
  #assert process("Andrea, Barbara", "NotInList", "Bar") == ['Andrea']
  #assert sorted(toDict(['Thomas', 'Michael', 'Thomas', 'Barbara', 'Susanne', 'Michael', 'Fabian'])) == sorted({'Barbara': 7, 'Fabian': 6, 'Michael': 7, 'Susanne': 7, 'Thomas': 6})
  #assert toListSkipLowerCase(("hans", "Fritz", "max", "Petra", "Susanne", "toni")) == ["Fritz","Petra", "Susanne"]
  #assert toListSkipLowerCase(("hans", "max")) == []
  #assert applyFuncToAll(lambda i: i*2, [1,2,3]) == [2,4,6]
  #assert applyFuncToAll(len, ["a","bb","ccc"]) == [1,2,3]
  #assert swallowException(lambda: 100) == 100
  #assert swallowException(lambda: 100/0) == "only chuck norris is allowed to divide by zero"
  #assert swallowException(lambda: [1,2,3][5]) == "something went wrong"
  pass
    
  
