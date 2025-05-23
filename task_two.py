import random #importing library
import string

# TASK

# Write a code, which will:

# 1. create a list of random number of dicts (from 2 to 10)

# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100)

dict_list = [{} for i in range(random.randint(2, 11))] #creating list of dicts with random number of elements
dict_keys = list(string.ascii_lowercase) #creating list of letters for the dicts' keys

for dict_ in dict_list: #for loop to add elements to each dict
    key_list = [dict_keys[random.randint(0, 25)] for i in range(random.randint(1, 26))] #creating list of keys for the dict
    key_list = list(set(key_list)) #making sure the keys are unique
    for key_ in key_list: #for loop to add keys to one dict
        value_ = random.randint(1, 101) #value as random number
        dict_[key_]=value_ #assigning key to value and adding to dict
print (dict_list) #final list on dicts

# 2. get previously generated list of dicts and create one common dict:

# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is

final_dict = {} #final dict with key-value pairs
checked_keys = [] #list to store repeated letters
for dict_ in dict_list: #loop to check each dict in list
    for key, value in dict_.items(): #loop to check keys in each dict
        result_dict = {} #dict to store renamed repeated letters with values
        dict_ind = dict_list.index(dict_) #index of the dict in list of dicts
        for i in range(1, len(dict_list)-dict_ind): #loop to check each key in each dict
            if key in list(dict_list[dict_ind+i].keys()) and key not in checked_keys: #if key exists in other dicts
                result_dict[key+'_'+str(dict_ind+i+1)]= dict_list[dict_ind+i][key] #put to the result_dict this renamed repeated key from original dict
                result_dict[key+'_'+str(dict_ind+1)]=dict_list[dict_ind][key] #put to the result_dict renamed key that was repeated from dict used for comparison
        if len(list(result_dict.values()))>0: #if the key has duplicates (result_dict has elements)
            max_value = max(list(result_dict.values())) #find maximum value between values for the key 
            for key_, value_ in result_dict.items(): #loop for elements in result_dict
                if value_ == max_value: #if the key has maximum value
                    final_dict[key_]=value_ #add key-value pair to final dict
            checked_keys.append(key) #add key to the list of checked letters with duplicates

    for key_,value_ in dict_.items(): #loop for elements in each dict
        if key_ not in checked_keys: #if key was not duplicated between dicts
            final_dict[key_]=value_ #add it to final dict as is

print(final_dict) #final dict of elements

