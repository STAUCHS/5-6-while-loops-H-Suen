num_of_students = int(input("Enter the number of students: "))

sum = 0
i = 1
count = num_of_students 

while num_of_students > 0:
    mark = float(input(f'Enter mark of #{i} student: '))
    i += 1
    sum += mark
    num_of_students -= 1

average = sum/count

print(f"Your class average is {average}")
