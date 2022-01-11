#Input a list of student heights separate by blank space. 178 177 188 160 177 190

student_heights = input("Input a list of student heights separate by blank space. ").split()
#Iterate list item in for loop
for n in range(0,len(student_heights)):
    student_heights[n]
    print(student_heights[n])

#Write code without use len() and sum() function
total_height = 0 # total heights of all students
number_of_student = 0 # caculate how many students in list
for height in student_heights:
    #print(int(height))
    total_height = total_height + int(height)
    number_of_student +=1
print(f"total_height={total_height}")
print(f"total_student={number_of_student}")
average_height = round(total_height / number_of_student,2)
print(f"average_height={average_height}")

