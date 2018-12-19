print('-' * 80)
print('Narrative Bot')
print()
name = input('Student Name ')
grade = input('Grade ')
grade = int(grade)
if grade >= 65:
	grade = str(grade)
	print(name + ', your final grade in AP Computer Science is ' + grade + '%.')
	print('You have excelled in all components of the class!')
	print('I wish you continued success in the next semester of AP Computer Science!')

else:
	grade = str(grade) 
	print(name + ', your final grade in AP Computer Science is ' + grade + '%')
	print('This is largely a result of missing projects and homework assignments.')
	print('Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester')
print('-' * 80)