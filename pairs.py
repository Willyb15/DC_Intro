students = [
	"Marissa",
	"Merliee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew",
	"Guido",
	"Porscha",
	"Carla",
	"YingRong",
	"Ian",
	"Nick",
	"Michael",
	"Hayes"
]
# Take the list "students", randomly pair 2 until all students have been paired
import random
# 1. Grab a random index from students
# 2. then remove that student from the list
# 3. Repeat until len(list) = 0


def getRand():
    rand_num = random.randint(0,len(students)-1)
    current_student = students[rand_num]
    students.remove(current_student)
    return current_student
    # print students

while students:
    student1 = getRand()
    student2 = getRand()
    print ("%s is paired with %s") % (student1,student2)
# getRand()
