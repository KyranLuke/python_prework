#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name():
        username = input("Enter your username").upper()
        print(f'"hello_{username}!"')
hello_name()  

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    oddnum =list(range(1,100,2))
    print(oddnum)
first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(list):
    for number in list:       
        return max(list)
number_list = (7,27,22,15,32,81,92,56,71)  
print(max_num_in_list(number_list)) 

#Question 4
#Write a function to return if the given year is a leap year. 

def is_leap_year(a_year):
    if a_year % 4 == 0:
       print("True")
    else:
       print("False")   
a_year= int(input("Enter a year here to find out if it's a leap year or not. "))   
is_leap_year(a_year) 

#  Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list): 
        if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):  
            print("True")                     
        else:
            print("false") 
a_list = [72,73,74,75,76]        
is_consecutive(a_list) 