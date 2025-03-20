from lib.helpers import check_that_these_are_equal



# Title: String Challenge
# Instructions:
# "Have the function StringChallenge(strParam) take the strParam 
# parameter being passed and capitalize the first letter of each word. 
# Words will be separated by only one space."
# 
# 
# Examples:
# Input: "hello world"
# Output: "Hello World"
# Input: "i ran there"
# Output: "I Ran There"




def StringChallenge(strParam):
    # code goes here
    
    return strParam.title()




check_that_these_are_equal(
  StringChallenge("hello world"), "Hello World")
check_that_these_are_equal(
  StringChallenge("i ran there"), "I Ran There")



# keep this function call here
# print StringChallenge(raw_input())