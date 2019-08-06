#Week 4: Introduction to List

#List can hold multiple points of data and store them to "memory" to be used later on in our program

#below is a hand-populated list (not from file) 
#list1 holds a series of name

list1 = ["Sam", "Mary", "Bill", "Adam", "Betty"]  #flat brackets are list 
                                                  #notice they are seperated by , 
                                                  # " " represents a <--- string value

#print full list- looks like print(rec) in data import demo

print(list1)

#LIST: store multiplr data values (of the same type!) to RAM (memory) in our program can remember a group of values, as long as they have a position (index) in the list

#print the list each data point at a time 
#0--> FIRST INDEX (positon)

print(list1[0]) #Sam
print(list1[1]) #Mary
print(list1[2]) #Bill
print(list1[3]) #Adam
print(list1[4]) #Betty

num_records = len(list1) #len() is a LENGTH FUNCTION 
#len() returns the length of the list/item you pass it
print("\nNUM RECORDS in List1", num_records)

print() #for console space
print()

# a BETTER way to print (and PROCESS) a full list w contents is using the ... F O R L O O P!

#for loops were made for lists 

print("Printing from a FOR LOOP!!\n")

for index in range(0, num_records):
    #the loop start at index 0 ( [ 0 ] ) and it will run for num_records # of times (includes 0)
    #IE the loop will run num_records number of times, or for each position held by a list item

    print("INDEX", index, "\t", list1[index])
    #index MUST be used in combo with list1 (or other list names) in order to find specific value in list at that position
    #index is the position of the stored values
    #each index reps a different value position in the list
    
#---------------------------------------------------------------------------------

#three new lists, now with DIFFEReNT types of data

list2 = ["Sam", "18", "32000"]

list3 = ["Mary", "21", "34000"]

list4 = ["Tom", "24", "38000"]

#list above ^ look like a RECORD as opposed to a FIELD when cosidering a text file

#RECORDS --> multiple data values, all different kinds
#FILED --> multiple data values, all same kind


#to store a data file's records (which are read as list) into actual lists (values stored to RAM):

#STEP 1: CREATE EMPTY LISTS
#each FIELD should have its own list

name = [] #empty list called 'name'
age = [] #empty list called 'age'
salary = [] #empty list called 'salary'

#the above lists are EMPTY -- they have no vales stored in them 

#STEPP 2: ADD ELEMENTS TO THE LIST  (POPULATING THE LISTS)
name.append(list2[0]) #ADD index0 of list2 to 'name'
name.append(list3[0])
name.append(list4[0])
    
print()
print("Array 'name' contents: ", name)
print("name[1]:", name[1])

#REMEMBER: it's easier/more efficient to do this in a FOR LOOP

for index in range(0,3): #START at 0 and run 3 times
    print(name[index])

print("PART 1  of demo complete...\n\n")

#PART 2 -----------FILE IMPORT REVIEW / APPENDING DATA FROM FILES TO LISTS!!!!!!

print("--------------------------------")
print("\n\n")


#STEP 1: IMPORT CSV library

import csv 

#STEP 2: initialize num_records to 0

num_records = 0 

#STEP 3: create empty lists to populate with text file data

name = []

age = []

salary = []

#NOTE: there is an arrays for each field in the text file

#STEP 4: connect to data file

#with open ("?C:/Users/008003941/Desktop/Python/example.csv") as csvfile:
with open("C:/Users/008003941/Desktop/Python/example.csv") as csvfile:

    #STEP 5: allow data to be "read"
    file = csv.reader(csvfile)

    #STEP 6: process data in a for loop
    
    for rec in file:

        #STEP 7: increment (+1) num_records
        num_records += 1 #num_records = num_records + 1

        #STEP 8: append (add) values from each field to its corresponding list
        #each field gets its own name

        name.append(rec[0]) #name is held in 1st field
        age.append(int(rec[1])) #age is held in 2nd field
        salary.append(float(rec[2])) #salary is held in the 3rd field

        #rec[1] and rec[2] have been CAST as they are appended for easier numeric processing
        #rec[#] represents the FIELD of data, rec is one full record of data

    print("Finished processing file. \n\n")


#process = for loop related to list ---> need to happen in the for loop

#once values has been stored into the lists, now you can process them as many tiumes as you'd like!
#when you hear "process" in relation to lists think FOR LOOP!!!!

#processing of thr lists should happen AFTER with open() statements (no longer indented)

#how to get one value for each record data

for index in range (0, num_records):
    print("INDEX: ", index, "\t", name[index], "\t", age [index], "\t$", salary[index])

print("Finished processing list for: printing \n\n")

#process the age list to find the avg age:

age_total = 0 #need a sum total var for avrg

for index in range (0, num_records):
    age_total += age[index] #age_total = age_total + age[index] 
    #adds each value of age stored in list to age_total
print("Finished processing age list forL avg age. \n")
avg_age = age_total / num_records
print("AVG AGE IN FILE:", avg_age, "yrs\n\n\n")

#process the salary list to find average salary:

salary_total = 0

for index in range (0, num_records):
    
    salary_total = salary[index] #salary_total = salary_total + salary

print ("Finished processing for avg salary")

avg_sal = salary_total / num_records

print("AVG SALATY IN FILE: ${:2f}".format(avg_sal))



    

        

        
    




