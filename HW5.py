#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Submitted on Fri March 15 19

@author: Angela Corwin
"""
# AC_HW5
# Received additional extension per email with Summer & Robert

# create a file
todo = open("/Users/home/Desktop/ToDo.txt", "w")
# write to the file
todo.write("Clean House,low \nPay Bills,high")
todo.close()

# read text file items in a list
todolist = open("/Users/home/Desktop/ToDo.txt", "r")
lines = todolist.readlines()
print(lines)

# "for loop" to loop through list
for x in todolist:
    print(x)

# print debugging below: printing elements to confirm info is correct
item1 = lines[0]
# print(item1)
item2 = lines[1]
# print(item2)

# slicing: 0 is first character or use negative integers to start from the end of the line
key1 = item1[0:11]
# print(key1)
value1 = item1[-5:-2]
# print(value1)

key2 = item2[0:9]
# print(key2)
value2 = item2[10:14]
# print(value2)

# converting to a dictionary
todo_dict = {key1:value1, key2:value2}
print(todo_dict)


# Menu structure to add or remove tasks to dictionary
while(True):
    print ("""
    Menu of Options
    1: Show current data
    2: Add a new item
    3: Remove an existing item
    4: Save Data to File
    5: Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? 1 to 5 "))
    print()

    # Show the current items in the table
    if (strChoice.strip() == "1"):
        print(todo_dict)
    # Add a new item
    elif(strChoice.strip() == "2"):
        key3 = input("Enter a new key: ")  
        value3 = input("Enter a new value: ")
        todo_dict.update({key3:value3})
        print("The task has been added:")
        print(todo_dict)
    # Remove an item
    elif (strChoice.strip() == "3"):
        remove = input("What task would you like to remove? ")
        if remove in todo_dict:
            del todo_dict[remove]
           # print(todo_dict)
            print("The task has been deleted.")
    elif (strChoice.strip() == "4"):
        with open("todo.txt", "w") as f:
            f.write(str(todo_dict))
            todo.close()
    elif (strChoice.strip() == "5"):
        print("Goodbye")
        break

# break to end a loop



