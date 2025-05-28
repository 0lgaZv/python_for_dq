#task two

import random #importing library
import string

# TASK

# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)

# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100)

def dicts_list_creation():
    #creating list of dicts with random number of elements
    dict_list = [{} for i in range(random.randint(2, 11))]
    return dict_list

def list_of_keys(key_list):
    #creating list of letters for the dicts' keys
    random_key_list = [key_list[random.randint(0, 25)] for i in range(random.randint(1, 26))] #creating list of keys for the dict
    unique_key_list = list(set(random_key_list)) #making sure the keys are unique
    return unique_key_list

def dicts_with_elems(dict_list):
    #add elements to dictionaries
    for dict_ in dict_list: #loop for going through all dicts
        for key_ in list_of_keys(list(string.ascii_lowercase)): #for loop to add keys to one dict
            value_ = random.randint(1, 101) #value as random number
            dict_[key_]=value_ #assigning key to value and adding to dict
    return dict_list


#calling dicts_with_elems with result of list_of_keys function for lowcase unique letters 
# and result of dicts_list_creation with list of empty dicts
dict_list = dicts_with_elems(dicts_list_creation())
print(dict_list)


# # 2. get previously generated list of dicts and create one common dict:

# # if dicts have same key, we will take max value, and rename key with dict number with max value
# # if key is only in one dict - take it as is

global final_dict
final_dict = {} #final dictionary with all keys from all dicts

global checked_keys
checked_keys = [] #list to store repeated letters

def get_index(one_list, one_item):
    #to get the index of element in list
    one_index = one_list.index(one_item)
    return one_index

def get_new_name(one_key, dict_index):
    #to get the name of the key for repeated values
    return one_key+'_'+str(dict_index+1)

def append_to_dict(one_key, one_value, one_dict):
    #add new element to dict
    one_dict[one_key]=one_value
    
def get_max_value(one_list):
    #return max value for list if it is not empty
    if len (one_list) > 0:
        return max(one_list)
    
def check_value_in_list(one_value, one_list):
    #check if the value in the list
    if one_value in one_list:
        return True
    else:
        return False
    
def append_key_with_max_value_to_final_dict(one_dict):
    #add to final list duplicate key with maximum value
    max_value = get_max_value(list(one_dict.values())) #find maximum value for the key
    for key_, value_ in one_dict.items(): #loop for elements in result_dict
        if value_ == max_value: #if the key has maximum value
            append_to_dict(key_, value_, final_dict) #add key-value pair to final dict
        

def get_duplucate_keys(list_of_dicts, one_dict_index):
    #check all dicts for duplicate keys and add them to the final dict
    for key in list(list_of_dicts[one_dict_index].keys()): #loop to check keys in each dict
        result_dict = {} #dict to store renamed repeated letters with values
        for i in range(1, len(list_of_dicts)-one_dict_index): #loop to check each key in each dict
            if check_value_in_list(key, list(list_of_dicts[one_dict_index+i].keys())) and not check_value_in_list(key,checked_keys): #if key exists in other dicts
                append_to_dict(get_new_name(key, one_dict_index+i), list_of_dicts[one_dict_index+i][key], result_dict) #put to the result_dict this renamed repeated key from dict used for comparison 
                append_to_dict(get_new_name(key, one_dict_index), list_of_dicts[one_dict_index][key], result_dict) #put to the result_dict renamed key that was repeated from original dict    
        if len(list(result_dict.keys()))>0: #if there are duplicates
            checked_keys.append(key) #add the key to the special list
        append_key_with_max_value_to_final_dict(result_dict) #add to final list duplicate key with maximum value

def get_unique_keys(one_dict, one_list):
    #add to final list keys without duplicates
    for key_,value_ in one_dict.items(): #loop for elements in each dict
        if key_ not in one_list: #if key was not duplicated between dicts
            final_dict[key_]=value_ #add it to final dict as is
        





for dict_ in dict_list: #loop to check each dict in list
    get_duplucate_keys(dict_list, get_index(dict_list, dict_)) #get duplicated keys
    get_unique_keys(dict_, checked_keys) #add unique keys to final dict

print(final_dict) #final dict of elements



# Task three
#it uses some functions that were declared above

def change_case_to_lower(one_string):
    #to change case to lower
    return one_string.lower()

def split_string_by_comma(one_string):
    #to split string by comma
    return one_string.split('.')

def replace_list_element(old_elem, new_elem, one_list):
    #to replace old element with changed one
    old_elem_index = get_index(one_list, old_elem)
    one_list[old_elem_index]=new_elem

def normalize_letter_cases_return_list(one_string):
    #to normalize letter cases for each sentence in string
    one_string = change_case_to_lower(one_string) #changing all letters to lower case
    one_list = split_string_by_comma(one_string) #creating list with sentences 

    for line in one_list: #for loop to take each sentence
        for sym in line: #check each symbol in line 
            if check_value_in_list(sym, list(string.ascii_lowercase)): #if it is alphabet letter
                new_line = line.replace(sym, sym.capitalize(), 1) #create new line with capitalised letter
                replace_list_element (line, new_line, one_list) #replace old line with new one
                break #stop working with this sentence and come to next one
    return one_list

def create_new_sentence(one_list):
    #create new sentence from last words of each line in list
    new_line = [] #creating list for new line words
    for line in one_list: #for loop to take each sentence
        line_list = line.split() #create a list of words for each line
        if len(line_list)>0: #to catch the item that consists of \n only
            new_line.append(line_list[-1]) #add the last word to new_line list  
    one_new_sent = ' '.join(new_line).capitalize() #create a new sentence with the words from list

    return one_new_sent

def insert_elem_to_specific_place_in_list(target_elem, new_elem, one_list):
    #to add element to specific place in list, place is found by key words
    for line in one_list: #check each sentence
        if check_value_in_list(target_elem, line): #if it has specific end
            line_index = get_index(one_list,line) #take its index
            
    one_list.insert(line_index+1,new_elem) #add new string after the specified line to the list

def replace_substring_in_all_list_item(old_string, new_string, one_list):
    #to replace substring with another one in each list element
    for line in one_list: #check each line in the string
        new_line = line.replace(old_string, new_string) #and replace needed elements
        replace_list_element (line, new_line, one_list) #replace old line with new one

def create_commas_separated_text_from_list(one_list):
   #to create text with commas from list
   one_string = '.'.join(one_list) #create string with sentences from list
   return one_string

def count_whitespaces(one_string):
    whitespace = [i for i in one_string if i in string.whitespace] #create the list of all whitespaces from the string
    spaces_count = len(whitespace) #count them as the length of list
    return spaces_count


#variable with home task string
task_string = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

task_list = normalize_letter_cases_return_list(task_string) #make all letters lowercase

new_sent = create_new_sentence(task_list) #create new sentence from the last words of all other sentences

insert_elem_to_specific_place_in_list('add it to the end of this paragraph', new_sent, task_list) #insert new sentence to specific place

replace_substring_in_all_list_item(' iz ', ' is ', task_list) #replace all mistaken IZ with IS

task_string = create_commas_separated_text_from_list(task_list) #create final string

print(task_string)

print(f'Whitespaces count in {count_whitespaces(task_string)}') #count whitespaces(likely more then expected 87)


    



