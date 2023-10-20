






class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_student(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students =                   sorted(student_list,
                        key=lambda                 student: student.cgpa,             
reverse=True)
#Syntax-lambda arg:ex  return sorted_students                             
  return sorted_students


#Example usage:
student = [
   Student("Hari", "A123", 7.8),
   Student("Srikanth", "A124", 8.9),
   Student("Saumya", "A125", 9.1),
   Student("Mahidhar", "A126", 9.9),
]

sorted_students =                          sort_student(student)        

#print the soted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}",format(student.Name,
                                                     student.roll_number, 
                                           
          student.cgpa))
                        
        




