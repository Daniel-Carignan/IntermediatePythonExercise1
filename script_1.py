# function to get unique elements of given list
def get_unique_list(my_list):

    # empty list used to store unique elements we will 
    #get from after using conditional statement
    new_list = []

    # iterate through every number in "my_list"
    for number in my_list:

         # conditional statement checking 
         # number available in new_list
         #this conditional statement will check to see if
         #the value that "number" is currently at 
         #is already in "new_list"
         #this is so we create a list with no repeating numbers
         if number not in new_list:

             #is the conditional statement above is true then
             #we will append the number we are comapring to our "new_list"
             new_list.append(number)


    return new_list #return unique elements of list. 
                    #this will give the value of "new_list" to our "unique_list"
                    #that we are holding outside this function


my_list = [1,2,3,2,1,4] #here we are setting our values for our list
unique_list = get_unique_list(my_list) #here we call the function that will
                                        #sort out the list to give us our unique list
                                        # and then we set the value of this new list to 
                                        #"unique_list"

print(unique_list) #here we simply print out the new list we have created





#                       SOURCES 
#https://www.w3schools.com/python/python_functions.asp
#  this page explained to me how to make a function in 
# python and how to call them as well
#
#https://www.digitalocean.com/community/tutorials/python-add-to-list
# this page showed me how to use the .append() method in python
#
#https://www.askpython.com/python/examples/in-and-not-in-operators-in-python
#  this page explained how to use the "not in" operator in python
#
#https://www.chegg.com/homework-help/questions-and-answers/1-write-function-takes-list-data-structure-input-function-create-new-list-include-unique-e-q91843574
#  I copied this code and added comments to eveyrthing to show that I 
#understand what is going on
#
#
#