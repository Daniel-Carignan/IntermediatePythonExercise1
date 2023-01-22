def get_freq_dict(string):  #our "get_freq_dict" function which will find the 
                            #number of times a letter is repeated in the string
                            #that the user enters 

    string = string.lower() #this ".lower()" method converts all letters in a string to lower case
    string = string.replace(" ", "")#this ".replace()" method eliminates the white
                                    #space in strings
    freq_dict = {}# Creating a new dict for frequency dictionary

    # Calculating the frequency dictionary using loops  
    for i in string:#here we are looping through the string length
        if i in freq_dict:  #conditional statement checking if "i" is holding a
                            #value that is already in out "freq_dict" dict
            freq_dict[i] += 1#adding one to the frequency of a certain character that is
                            #already in the "freq_dict"
        else:
            freq_dict[i] = 1#adding the first count to a character in the string
    return freq_dict#returing the dict back to the method call


user_string = input('Enter a string: ') #setting the input value we get from our user to 
                                        #our new variable "user_string"

print(get_freq_dict(user_string))   #here we print the value that is being returned from
                                    #our "get_freq_dict" function


#                       SOURCES
#
#https://www.w3schools.com/python/python_functions.asp
#  this page explained to me how to make a function in 
# python and how to call them as well
#
#https://www.datacamp.com/tutorial/case-conversion-python
#  this page explains the use of ".lower()" method
#
#https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string
#  this page explins how to remove the white space between strings
#
#
#https://www.chegg.com/homework-help/questions-and-answers/python-1-write-function-takes-two-dict-data-structures-input-dicts-map-str-int-keys-string-q91520656
#  I got the code from this page and added as many comments needed to explain what is going on
#
#
