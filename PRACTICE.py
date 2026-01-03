
# user_name=input("enter your first and last name: ").title()

# day=input("enter the day you were born(1-31): ")
# month=input("enter the month you were born(1-12): ")
# year=input("enter the year you were born:")


# print(f"{user_name}  was born on {day}/{month}/{year}")




# name="frank is  is agyekum"

# print(name[7])


# name="python"

# name_copy=name
# name="science"
# print(name_copy)
# print(name)


# names=["frank","john","doe"]

# names_copy= [] + names
# names_copy[1]="brian"

# print((names_copy))
# print((names))
# print(len(names))
# print("Fred " in names)
# print(names.index("doe"))

# names.append("AMA")
# print(names)

# names.append("JOGI")

# sentence="i love python"

# print(sentence.split())
# print("-".join(sentence))




# user_words=input("enter 4 words :" ).split()

# another_word=input("enter another word: ")

# user_words.append(another_word)

# print("\n"* 100)

# guess=input("enter a word to see if its in the list: ")

# print(guess in user_words)
# # if guess in user_words:
# #     print("hurray you got it 😁")
# # else:
# #     print("oops not found 🤣🤣")    



# name="This is not an advertisement"

# new_name=name.replace(" is", " was")
# print(new_name)




# test_scores=int(input("enter your score: "))

# if test_scores >=90:
#     print("you got an  A")

# elif test_scores >= 80:
#     print("B")    

# elif test_scores >= 70 :
#     print("C")   

# elif test_scores >=60:
#     print("D")    

# else:
#     print("F")    

# user_words= input("enter 4 words : ").split()

# another_word=input("enter another word : ")


# user_words.insert(0,another_word)


# print("\n"*100)

# playing=True

# while playing:

#     guess=input("enter a word to guess if its in the list: ")


#     messages=["sorry ,wrong guess","Congratulations"]


#     print(messages[guess in user_words])


#     break 


# grades=int(input("enter your grade: "))

# if grades> 60:
#     print("you have passed")
#     if grades< 70:
#         print("D")

#     elif grades<80: 
#         print ("C")   


#     elif grades<90:
#         print("B")    


#     else:
#         print("Your grade is A")    
# else:
#     print("You have failed")



# temperature=int(input("enter today's temperature: "))
# weather=input("enter the weather condition : ").strip().lower()

# if temperature< 0: 
#     if  weather =="snowy":
#         print("Wear a heavy cloth and snow boot")

#     else:

#         print("wear a heavy coat")

        

# elif 0<= temperature<=20:
    
#     if weather=="rainy" :
#         print("Wear a raincoat")  
#     else:
#         print("wear a jacket")      



# else: #to check if temperature is greator than 20
#     if weather=="sunny":
#         print("Wear a T-shirt")

#     else:
#         print("Wear light clothing")    



# guess=int(input("enter a number: "))

# if  guess>7 and guess >0 : 
#     print("True")
# else:
#     print("False")    


# x=True
# y=False
# z=False


# print(x or not y and z)



# donut=50

# student=int(input('enter thr number of students : '))

# if student>0 and donut/student<1:
#     print("insufficient funds")

# else:
#     print(donut/student)    

# for i in range(1,100):


#     if i%3==0 and i%5==0:


#         print("FIZZ BUZZ")


#     elif i%3==0:
#         print("FIZZ")    


#     elif i%5==0:
#         print("BUZZ")    


#     else:
#         print(i)   

# message="lbh zhfg unir fbzr jvyg zvtnzvguba. gvzr geniry? frvbhlfyl!!! arirevznq, yrfg gnxr n oerx abj. ohg ubyq ba, bar zber guvat. lbhe svfg ubzrjbx nfvtazrag jvyy or eryrnfgrq gbqnl ba oevtugcnpr. vg vf rapelgrq jvgu ebg13."



# message = "lbh zhfg unir fbzr jvyg zvtnzvguba. gvzr geniry? frvbhlfyl!!! arirevznq, yrfg gnxr n oerx abj. ohg ubyq ba, bar zber guvat. lbhe svfg ubzrjbx nfvtazrag jvyy or eryrnfgrq gbqnl ba oevtugcnpr. vg vf rapelgrq jvgu ebg13."

# Rot13 = [


# for char in message:
#     # Check if character is a letter
#     if 'a' <= char <= 'z':
#         # Shift lowercase letters by 13, wrap around
#         Rot13.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
#     elif 'A' <= char <= 'Z':
#         # Shift uppercase letters by 13, wrap around
#         Rot13.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
#     else:
#         # Keep non-letters unchanged
#         Rot13.append(char)

# decoded_message = ''.join(Rot13)
# print(decoded_message)


# alphabet=[]
# for i in range(0,26):
#     alphabet.append(chr(97+i))

# print(alphabet)    



# rot13=[chr((i +13)% 26 +97) for i in range(26)]
# print(rot13)


# for outer_num in range(2):
#     for inner_num in range(3):
#         print(outer_num,inner_num,sep=" ")


# table=[]

# row_list0=[]
# row_list0.append(1)
# row_list0.append(2)
# row_list0.append(3)

# table.append(row_list0)

# row_list1=[]
# row_list1.append(4)
# row_list1.append(5)
# row_list1.append(6)

# table.append(row_list1)

# row_list2=[]

# row_list2.append(7)
# row_list2.append(8)
# row_list2.append(9)

# table.append(row_list2)


# cnt=1
# table=[]
# row_list=[]
# for row in range(3):
    
#     for col in range(3):
#         row_list.append(cnt)
#         cnt=cnt +1
#     table.append(row_list)   



# print(table)

# def border():
#     print("+---+---+---+")



# for row in table:
#     border()
#     print("|",end=" ")

#     for item in row:
#        print(item,end=" | ")


#     print()   

        
# border()
# table=[]
# for i in range(2):
#     info=[]
#     info.append(input("enter the name of student: "))
#     info.append(input("enter the student age: "))
#     info.append(input("enter the course he or she studies: "))

#     table.append(info)

# col_width=[7,3,6]# name ,age and course
# def border():
#     print("+" + "+".join(["-"*w for w in col_width])+ "+")




# for row in table:
#     border()

#     print("|",end=" ")

#     for i,value in enumerate(row):

#         print(f"{value:<{col_width[i]}}|",end="")


#     print()    


# border()





# cnt=1
# table=[]

# for row in range(4):
#     row_list=[]
#     for col in range(4):
#         row_list.append(cnt)
#         cnt=cnt+1
#     table.append(row_list)

# col_width=[2,2,2,]
# def border():
#     print("+--+--+--+--+")

#     # print("+"+ "+" .join(["-"*w for w in col_width]) +"+")


# for row in table:
#     border()
#     print("|",end="")

#     for items in row:
#         print(items,end=" |")


# for row in range(3):
#     for col in range(3):
#         print(table[row][col],end=" ")

#     print()    




# num_student=2
# student_list=[]


# for i in range(num_student):
#     student_info=[]
#     student_info.append(input('enter the name of student:'))
#     student_info.append(input('enter the programme of student:'))
#     student_info.append(input('enter the graduation year of student:'))

#     student_list.append(student_info)

# # print(student_list)    



# for student in student_list:
#     for info in student:
#               print(info,end=" ")



#     print("\n---------------")    



# student_grades=[]


# row_list1=[]

# row_list1.append(input("enter the name of student:"))
# row_list1.append(input("enter the 1stgrade of student:"))
# row_list1.append(input("enter the 2nd grade of student:"))
# row_list1.append(input("enter the 3rd grade of student:"))
# row_list1.append(input("enter the 4th grade of student:"))

# student_grades.append(row_list1)



# row_list2=[]
# row_list2.append(input("enter the name of student:"))
# row_list2.append(input("enter the 1stgrade of student:"))
# row_list2.append(input("enter the 2nd grade of student:"))
# row_list2.append(input("enter the 3rd grade of student:"))


# student_grades.append(row_list2)

# row_list3=[]

# row_list3.append(input("enter the name of student:"))
# row_list3.append(input("enter the 1stgrade of student:"))
# row_list3.append(input("enter the 2nd grade of student:"))


# student_grades.append(row_list3)

# row_list4=[]

# row_list4.append(input("enter the name of student:"))
# row_list4.append(input("enter the 1stgrade of student:"))
# row_list4.append(input("enter the 2nd grade of student:"))
# row_list4.append(input("enter the 3rd grade of student:"))
# row_list4.append(input("enter the 4th grade of student:"))
# row_list4.append(input("enter the 5th grade of student:"))

# student_grades.append(row_list4)

# student_grades=[['John', '9', '10', '7', '6'], ['Mary', '9', '8', '8'], ['Smith', '8', '4'], ['Adam', '6', '4', '7', '5', '10']]

# # avg=student_grades[0][1:5]

# # print(f"{student_grades[0][0]} 's grade is  { (int(student_grades[0][1]) +int(student_grades[0][2]) + int(student_grades[0][3]) +int (student_grades[0][4]))/len(avg)}")

# all_grades=[]

# for row in student_grades:
#     name=row[0]
#     grades=row[1:]

#     grades_int=[int(g) for g in grades]


#     average_grade_per_student= sum(grades_int)/len(grades_int)

#     all_grades=[int(g) for row in student_grades for g in  row[1:]]

#     overall_average=sum(all_grades)/len(all_grades)

#     print(f"{name} 's  average grade is {average_grade_per_student}")


#     print(f"the overall average is {overall_average}")


# table=[]
# num_rows=8
# num_cols=8


# for r in range(num_rows):
#     row_list=[]

#     for c in range(num_cols):
#         row_list.append(". ")

#     table.append(row_list)


# def borders():
#     print("+---+ " "---+ ---+ ---+ ---+ ---+ ---+ ---+")


# for r in range(num_rows):
#     borders()
#     print("|",end=" ")

#     for col in range(num_cols):
#         print(table[r][col]+ "| ",end=" ")

#     print() 

# borders()





# count=0

# while count<6:
#     print(f"the count is : {count}")

#     count=count+1


# print("😁")    

# student_list=[]
# typing=True
# while typing:
#     student=input("enter the name of student: ")
#     student_list.append(student)

#     response=input("do you want to add (y/n: )").lower()

#     if response!="yes":
#         typing=False

# print("goodbye")        




import random





while True:
        dice=random.randint(1,6)
        guess=(input("enter the dice number you think it is : "))


        if not guess.isdigit():
            print("enter a valid number!")

            continue

        guess=int(guess)

        if  guess< 1 or guess>6:
            print("its not in range")
            continue

    


        if guess!=dice:
            print("oppps wrong")
            print(f"dice number was {dice}")

        else:
            print("you got is kid")  
            print(f"dice number was {dice}")  

            break

