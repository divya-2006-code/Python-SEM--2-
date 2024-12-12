#1.
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
    def validate_details(self):
        if not self.student_id.startswith("STU") or not self.student_id[3:].isdigit(): #Student Id Validation
            return "Invalid student Id format. It must be in the format 'STU1234'."
        
        if len(self.name) < 2 or not (char.isalpha() or char.isspace() for char in self.name): #Name Validation
            return "Invalid name. It must be at least 2 characters long and contain only alphabets and spaces."
        
        if not self.grade.endswith("th Grade") or not self.grade[:-8].isdigit() or int(self.grade[:-8]) not in range(1, 13):#Grade Validation
            return "Invalid grade. It should be in the format '<number>th Grade' (e.g., '1st Grade', '12th Grade')."
        return "Details are valid."
    
    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")
        
student = Student("STU1234", "Lisha", "10th Grade")
validation_result = student.validate_details()
print(validation_result)
if validation_result == "Details are valid.":
 student.display_details()
                  
