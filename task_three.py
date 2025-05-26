import string #importing library

#variable with home task string
task_string = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

task_string = task_string.lower() #changing all letters to lower case
task_list = task_string.split('.') #creating list with sentences 

for line in task_list: #for loop to take each sentence
    for sym in line: #check each symbol in line 
        if sym in list(string.ascii_lowercase): #if it is alphabet letter
            new_line = line.replace(sym, sym.capitalize(), 1) #create new line with capitalised letter
            line_index = task_list.index(line) #get index of the line
            task_list[line_index]=new_line #replace old line with new one
            break #stop working with this sentence and come to next one

new_line = [] #creating list for new line words
for line in task_list: #for loop to take each sentence
    line_list = line.split() #create a list of words for each line
    if len(line_list)>0: #to catch the item that consists of \n only
        new_line.append(line_list[-1]) #add the last word to new_line list

new_sent = ' '.join(new_line).capitalize() #create a new sentence with the words from list

for line in task_list: #check each sentence
    if 'add it to the end of this paragraph' in line: #if it has specific end
        line_index = task_list.index(line) #take its index
        
task_list.insert(line_index+1,new_sent) #add new string after the specified line to the list

for line in task_list: #check each line in the string
    new_line = line.replace(' iz ', ' is ') #and replace IZ with IS, if it is a mistake (IZ as version of the verb 'to be')
    line_index = task_list.index(line) #get index of the line
    task_list[line_index]=new_line #replace old line with new one

target_string = '.'.join(task_list) #create the final string from final list
print (target_string) # print the corrected string


whitespace = [i for i in target_string if i in string.whitespace] #create the list of all whitespaces from the string
spaces_count = len(whitespace) #count them as the length of list
print(f'Whitespaces count in {spaces_count}') #print the result (likely bigger then expected 87)


    





    # line = line.replace(u'\xa0', '').capitalize()
    # task_list_2.append(line)

# print (task_list_2)

# task_list_3 = []

# for line in task_list_2:
#     line = line.split()
#     task_list_3.append(line)

# new_sent = []
# for list in task_list_3:
#     print(list[-1])
#     #new_sent.append(list[-1])

# #new_sent = ' '.join(new_sent)

# #print(new_sent)


