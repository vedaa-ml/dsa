# Problem Description: You are given an integer n. 
# Your task is to return a square pattern of size n x n made up of the character '*',
# represented as a list of strings.



def pattern1(n):
	l = []
    for i in range(0,n):
      l.append("*"*n)
n = int(input("enter the number : "))
pattern1(n)