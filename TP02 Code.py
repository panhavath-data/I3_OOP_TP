# Student class
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)


# student objects
students = [
    Student("Vath", [80, 90, 85]),
    Student("Panha", [10, 15, 32]),
    Student("Jacky", [90, 95, 88])
]

# display students and calculate averages
lowest_average = min(student.average() for student in students)

# display students except the one with the lowest average
for student in students:
    if student.average() == lowest_average:
        continue  # Skip the student with the lowest average

    print(student.name, "Average:", student.average())

# search for a student
search_name = input("Enter student name to search: ")
i = 0

while i < len(students):
    if students[i].name.lower() == search_name.lower():
        print("Found:", students[i].name, "with average score of", students[i].average())
        break
    i += 1
else:
    print("Student not found")

# Pass statement
for student in students:
    if student.name == "Vath":
        pass  # pass does nothing, so Vath is still printed
    print(student.name)
