from lib.helpers import check_that_these_are_equal

# String Challenge
# Have the function StringChallenge(str) take the str parameter being 
# passed and return the string in reversed order. For example, if the input 
# string is "Hello World and Coders" then your program should return the 
# string "sredoC dna dlroW olleH".

# Examples:
# Input: "coderbyte"
# Output: "etybredoc"

# Input: "I Love Code"
# Output: "edoC evoL I"

example1 = "coderbyte"
example2 = "I Love Code"


def StringChallenge(strParam):
    # code goes here
  RevStrParam = ""
  for char in strParam:
    RevStrParam = char + RevStrParam
  strParam = RevStrParam  
  
  
  return strParam





check_that_these_are_equal(
  StringChallenge("coderbyte"), "etybredoc")
check_that_these_are_equal(
  StringChallenge("I Love Code"), "edoC evoL I")




print("Example 1")
print(StringChallenge(example1))

print("Example 2")
print(StringChallenge(example2))