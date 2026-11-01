student_profile = ("Nivya", "Grade 11", "Section B", 10)
print("Student Profile:", student_profile)
 
student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]
 
print("\nStudent Name:", student_name)
print("Grade:", grade)
print("Section:", section)
print("Total Subjects:", total_subjects)
 
print("First two details:", student_profile[0:2])
 
monday_subjects = {"Math", "Physics", "English", "Computer", "P.T"}
tuesday_subjects = {"Math", "History", "English", "Chemistry", "Economics"}
wednesday_subjects = {"Geography", "Physics", "English", "Biology","Commerce"}
 
print("\nMonday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print("Wednesday Subjects:", wednesday_subjects)
 
 
tuesday_subjects.add("Biology")
print("\nAfter adding Biology to Tuesday:", tuesday_subjects)
 
monday_subjects.discard("P.T")
print("After removing P.T from Monday:", monday_subjects)
 
wednesday_subjects.add("P.T")
print("After adding P.T to Wednesday:", wednesday_subjects)
 
wednesday_subjects.discard("Commerce")
print("After removing Commerce from Wednesday:", wednesday_subjects)
 
all_subjects = monday_subjects.union(tuesday_subjects).union(wednesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects).intersection(wednesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects).difference(wednesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects).difference(wednesday_subjects)
only_wednesday = wednesday_subjects.difference(monday_subjects).difference(tuesday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects).symmetric_difference(wednesday_subjects)
 
print("\nAll Subjects:", all_subjects)
print("Common Subjects:", common_subjects)
print("Only Monday Subjects:", only_monday)
print("Only Tuesday Subjects:", only_tuesday)
print("Only Wednesday Subjects:", only_wednesday)
print("Different Subjects:", different_subjects)
 

print("SCHOOL SUBJECT PLANNER")
print("Student:", student_name)
print("Grade:", grade)
print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print("Wednesday Subjects:", wednesday_subjects)
print("Subjects on Both Days:", common_subjects)
print("All Unique Subjects:", all_subjects)
