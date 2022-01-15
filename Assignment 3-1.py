# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:36:21 2022
Assignment 3-1 for Smoothstack

@author: Grant Huang
"""

#Question 1

multiplesOf35 = [n for n in range(1500, 2701) if n%35 == 0]
print(multiplesOf35)

#%%
#Question 2

#converts temperature from fahrenheit to celsius
#@celsius - celsius temperature
#outputs fahrenheit equivalent
def toFahrenheit(celsius):
    #c/5 = (f-32)/9
    return celsius*9/5 + 32

#converts temperature from celsius to fahrenheit
#@fahrenheit - fahrenheit temperature
#outputs celsius equivalent
def toCelsius(fahrenheit):
    #c/5 = (f-32)/9
    return round(5*(fahrenheit-32)/9)

c1 = 60
f1 = toFahrenheit(c1)
degree = "\N{DEGREE SIGN}"
print(degree)

print(f"{c1}{degree}C is {f1} in Fahrenheit")

f2 = 45
c2 = toCelsius(f2)
print(f"{f2}{degree}F is {c2} in Celsius")

#%%
#Question 3

import random

number = random.randrange(1, 10)
guess = 0

#having user guess the number until they get it right
while guess != number:
    guess = int(input("Guess my number! It's from 1-9.\n"))
    
print("Well guessed!")

#%%
#Question 4/5

k = -4

#creating triangle out of *s
for a in range(9):
    row = []
  
    #creating row of 5 + k stars
    for b in range(5 - abs(k)):
        row.append("*")
    
    print("".join(row))
    k += 1
    
#%%
#Question 6
    
word = input("Input word: \n")
reverse = word[::-1]
print(reverse)

#%%
#Question 7

numbers = tuple([n for n in range(1, 10)])
print(numbers)

even = 0
odd = 0

#counting even and odd numbers
for n in numbers:
    #even number
    if n%2 == 0:
        even += 1
    else:
        odd += 1
        
print("Number of even numbers: " + str(even))
print("Number of odd numbers: " + str(odd))

#%%
#Question 8

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

#printing type of each element in list
for element in datalist:
    elemType = type(element)
    print(f"type of {element} is {elemType}")
    
#%%
#Question 9
    
numbers = []
    
#recording numbers from 0-6 except 3 and 6
for n in range(7):
    #number is 3 or 6, skipping
    if n == 3 or n == 6:
        continue
    else:
        numbers.append(str(n))
        
print(" ".join(numbers))