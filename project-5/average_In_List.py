student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

totalHeight = 0
numOfStudents = 0

for i in student_heights:
    numOfStudents += 1
    totalHeight += i
averageHeight = totalHeight / numOfStudents
print(averageHeight)

"""

"""


