student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

number = 0

for num in student_scores:
    if (number == 0 or num > number):
        number = num

print(number)

