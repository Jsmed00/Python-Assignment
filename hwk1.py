# Homework 1
# Jonathan Smedley
# September 4th 2022
# CSCI 3675

#py documents/python/hwk1.py

# Question 1
# Write a function halveEvensImperative, using an imperative style of programming, that returns
# half of each even number in the list. For example, halveEvensImperative ([0, 2, 1, 7, 8, 56, 17, 18])
# should return [0, 1, 4, 28, 9].

# username = input("Enter username:")
# print("Username is: " + username)





def halveEvensImperative(l):
    #num = int (input("Enter Numbers:"))
    halve = []
    for i in l:
        if ((i % 2) == 0):
            halve.append(i // 2)
    return (halve)


#print(halveEvensImperative([0, 2, 1, 7, 8, 56, 17, 18]))

# Question 2
# Write a recursive function halveEvensRecursive, that returns half of each even number in the list.
# For example, halveEvensRecursive ([0, 2, 1, 7, 8, 56, 17, 18]) should return [0, 1, 4, 28, 9].

def halveEvensRecursive(l):
    if (l == []):
        return []
    i = l[0]
    if ((i % 2) == 0):
        return([i / 2] + halveEvensRecursive(l))
    return halveEvensRecursive(l)
    

#print(halveEvensRecursive([0, 2, 1, 7, 8, 56, 17, 18]))

# Question 3
# Write a function halveEvensComprehension, using list comprehension, that returns half of each even
# number in the list. For example, halveEvensComprehension ([0, 2, 1, 7, 8, 56, 17, 18]) should return
# [0, 1, 4, 28, 9].

def halveEvensComprehension(l):

    halve = [(i // 2) for i in l if i % 2 == 0]
    return(halve)

#print(halveEvensComprehension([0, 2, 1, 7, 8, 56, 17, 18]))


# Question 4
# Write a function capitalizeImperative, using an imperative style of programming, which, given a
# word, will capitalize it. That means that the first character should be made uppercase and any other letters
# should be made lowercase. For example, capitalizeImperative ('grEENVIlle') should return 'Greenville'.
# Your definition should use the functions upper and lower that change the case of a character.

def capitalizeImperative(l):
    for i in l:
        switched = l[0].upper() + l[1:].lower()
    return(switched)


#print(capitalizeImperative("gREENVILLE"))


# Question 5
# Write a function capitalizeComprehension, which, given a word, will capitalize it. That means
# that the first character should be made uppercase and any other letters should be made lowercase. For
# example, capitalizeComprehension ('grEENVIlle') should return 'Greenville'. Your definition should use
# a list comprehension and the functions upper and lower that change the case of a character.

def capitalizeComprehension(input):
    switched = [x.upper() if x is input[0] else x.lower() for x in input]
    switched = "".join(switched)
    return (switched)

#print(capitalizeComprehension("gREENVILLE"))


# Question 6
# Write a function sumImperative, using an imperative style of programming, that returns the sum
# of the numbers in a list. For example, sumImperative ([0, 2, 1, 7, 8, 56, 17, 18]) should return 109,
# and sumImperative ([1, 2.0]) should return 3.0.

def sumImperative(l):
    total = 0
    for i in range(0, len(l)):
        total = total + l[i]
    return(total)

#print(sumImperative([0, 2, 1, 7, 8, 56, 17, 18]))
#print(sumImperative([1, 2.0]))

# Question 7
# Write a recursive function sumRecursive, that returns the sum of the numbers in a list. For example,
# sumRecursive ([0, 2, 1, 7, 8, 56, 17, 18]) should return 109, and sumRecursive ([1, 2.0]) should
# return 3.0.

def sumRecursive(l):
    if (len(l) == 0):
        return 0
    else:
        return l[0] + sumRecursive(l[1:])


#print(sumRecursive ([0, 2, 1, 7, 8, 56, 17, 18]))
#print(sumImperative([1, 2.0]))

# Question 8
# Write a function palindromeImperative, using an imperative style of programming, that returns
# True if the given list is a palindrome (reads the same backward as forward), and False otherwise. For exam-
# ple, palindromeImperative ([0, 2, 0]) should return True, and palindromeImperative ('abb') should
# return False. No other functions should be called from this function; use slicing operations instead.

def palindromeImperative(l):
    for i in range(0, int(len(l) / 2)):
        if l[i] != l[len(l)-i-1]:
            return False
    return True


#print(palindromeImperative ([0, 2, 0]))
#print(palindromeImperative ('abb'))


# Question 9
# Write a recursive function palindromeRecursive, that returns True if the given list is a palindrome
# (reads the same backward as forward), and False otherwise. For example, palindromeRecursive ([0, 2,
# 0]) should return True, and palindromeRecursive ('abb') should return False. No other functions should
# be called from this function; use slicing operations instead.

def palindromeRecursive(l):
    if (len(l) <= 1):
        return True
    if l[0] == l[len(l)-1]:
        return palindromeRecursive(l[1:len(l)-1])
    else:
        return False

#print(palindromeRecursive ([0, 2, 0]))
#print(palindromeRecursive ('abb'))


# Question 10
# Write a recursive function inRangeRecursive, that returns all numbers in the input list within the
# range given by the first two arguments (inclusive). For example, inRangeRecursive (5, 10, range(1, 15))
# should return [5, 6, 7, 8, 9, 10].

def inRangeRecursive(l):
    if (l < 1):
        return ()
    else:
        return inRangeRecursive((l - 1) + (l - 1))

#print(inRangeRecursive (5, 10, range(1, 15)))


# Question 11
# Write a function inRangeComprehension, using list comprehension, that returns
# all numbers in the input list within the range given by the first two arguments (inclusive). For example,
# inRangeComprehension (5, 10, range(1, 15)) should return [5, 6, 7, 8, 9, 10].

def inRangeComprehension(l):
    iR = [x.range for x in l]
    return iR

#print(inRangeComprehension (5, 10, range(1, 15)))