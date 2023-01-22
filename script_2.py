def get_combined_dict(my_dict_1, my_dict_2):
    new_dict = {} #new dict that will hold our new combined dicts

    for key, value in my_dict_1.items(): #loop through length of first dict

        if (key in my_dict_2.keys()):   #conditional statement checking if 
                                        #the key that is in my_dict_1 is also in my_dict_2

            new_dict[key] = value + my_dict_2[key]  #adding the key that we find in 
                                                    #my_dict_2[] to new_dict[]

    return new_dict #we return the value we have set for our "new_dict" back to 
                    #our "combined_dict" from outside the fucntion


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9} #here we have our first dictionary
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16} #here we have our second dictionary
combined_dict = get_combined_dict(my_dict_1, my_dict_2) #here we call our "get_combined_dict" 
                                                        #function passing in the two dictionaries that
                                                        #we created in the beginning.
                                                        #then we set what ever value our function has 
                                                        #evluated to the new variable "combined_dict"

print(combined_dict) #here we print out the combined dictionaries


#                       SOURCES
#https://www.geeksforgeeks.org/python-merging-two-dictionaries/
#  this page explains how to combine two different dictionaries
#
#https://www.chegg.com/homework-help/questions-and-answers/python-1-write-function-takes-two-dict-data-structures-input-dicts-map-str-int-keys-string-q91520656
# I got the code from this page and added as many comments 
# needed to explain what is going on
#
#https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
#  this page explains how to loop through a dictionary
#
