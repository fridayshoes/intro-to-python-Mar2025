from lib.helpers import check_that_these_are_equal

# Title: String Challenge
# Instructions:
# "Have the function StringChallenge(sen) take the sen parameter being 
# passed and return the longest word in the string. If there are two or 
# more words that are the same length, return the first word from the 
# string with that length. Ignore punctuation and assume sen will not be empty. 
# Words may also contain numbers, for example "Hello world123 567""   
# 
# 
# 
# Examples:
# Input: "fun&!! time"
# Output: "time"
# Input: "I love dogs"
# Output: "love"



def StringChallenge(sen):
    # code goes here
    newstr = ""
    longest_word =""
    for char in sen:
        if char.isalnum() or char == " ":
            newstr = newstr + char
    print(newstr)
    words = newstr.split()
    print(words)
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    sen = longest_word        
    
    return sen







check_that_these_are_equal(
  StringChallenge("fun&!! time"), "time")
check_that_these_are_equal(
  StringChallenge("I love dogs"), "love")