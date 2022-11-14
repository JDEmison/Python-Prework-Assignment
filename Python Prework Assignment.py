#Python Prework 
#Question 1
def hello_name(user_name):
    "Use the function to print hello_USERNAME!"
    print("hello_"+ user_name.upper() + "!")

hello_name("USERNAME")

#Question 2
def first_odds():
    "first_odds needs to print odd numbers from 1-100 and returns nothing"
    current_number = 1
    while current_number <= 100:
        print(current_number)
        current_number += 2

first_odds()

#Question 3
def max_num_in_list(a_list):
    a_list = [1,2,3,4,5]
    big = max(a_list)
    print(big)

max_num_in_list(1)
        





#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        print("True")
    else:
        print("False")
is_leap_year(2016)    



#Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(full_list), max(full_list)+1))


    
full_list= [1,2,3,4,5]
print(is_consecutive(full_list))
