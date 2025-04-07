import random
import pandas

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]

doubled_list = [number * 2 for number in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 40}


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in student_data_frame.iterrows():
    print(row.student)