import random #importing library

#TASK:
#Create a python script:

#create list of 100 random numbers from 0 to 1000

n = 100  # count of random numbers
target_list = random.sample(range(1, 1001), 100) # generate a list of unique random numbers

#sort list from min to max (without using sort())

list_length=len(target_list) #variable to store list length
for i in range(0, list_length): #range for index of the first element in comparison, from list start to list end
    for j in range(i+1, list_length): #range for second element, from second element of the list to list end
        if target_list[i] >= target_list[j]: #if first element bigger or equal than the second element
            target_list[i], target_list[j] = target_list[j],target_list[i] #we swap elements' indexes

#calculate average for even and odd numbers

odd_sum = 0 #sum of odd numbers
odd_count = 0 #count of odd numbers
even_sum = 0 #sum of even numbers
even_count = 0 #count of even numbers
for i in target_list: #for number in list
    if i%2 ==0: #if number is even 
        even_sum += i #add number to even sum 
        even_count += 1 #raise count of even numbers by 1
    else: #if number is odd
        odd_sum += i #add number to odd_sum
        odd_count += 1 #raise count of odd numbers by 1

even_avg = even_sum/even_count #average for even number
odd_avg = odd_sum/odd_count #average for odd numbers

#print both average result in console 

print (f'Even number average is {even_avg}') #printing out even numbers average 
print (f'Odd number average is {odd_avg}') #printing out odd numbers average 
