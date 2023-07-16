#   new_dict={new_key:new_value for item in list if test}
#   new_list=[new_item for item in list if test]



from random import randint
list1=["aniket","rahul","sumit","pranav"]

students={ i:randint(1,100) for i in list1 if i!="pranav"}
failed_students=[ i for i in students.keys() if students[i] <20 ]

#*************************************************************************************
passed_students={ student : score for (student,score) in students.items() if score>20}
print(students,failed_students,passed_students)