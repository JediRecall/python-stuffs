# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

Q1 = int(raw_input("Enter a number"))

fibnum =1
prevnum=0


#while Q1 > 0:
   # print fibnum
    #newnum = fibnum + prevnum
   # prevnum = fibnum
   # fibnum = newnum
    #Q1 -= 1

for number in range (Q1):
     print fibnum
     newnum = fibnum + prevnum
     prevnum = fibnum
     fibnum = newnum
     #Q1 -= 1