from lib.helpers import check_that_these_are_equal

# Title: String Challenge
# Instructions:
# "Have the function StringChallenge(strParam) take the str string 
# parameter being passed and return the number of consonants the string contains."
# 
# 
# 
# Examples:
# Input: "Hello World"
# Output: 7
# Input: "Alphabets"
# Output: 6   




def StringChallenge(strParam):
    # code goes here
    consonants = 0
    for char in strParam:
        if char.lower() not in "aeiou ":
            consonants += 1
    strParam = consonants
    
    
    return strParam









check_that_these_are_equal(
  StringChallenge("Hello World"), 7)
check_that_these_are_equal(
  StringChallenge("Alphabets"), 6)

