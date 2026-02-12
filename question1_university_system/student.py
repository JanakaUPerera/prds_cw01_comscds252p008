"""
student.py
This module defines the Student class, which inherits from the Person class.

functions:
- __init__: Initializes a Student object with personal and student-specific attributes.
- get_info: Returns a formatted string with the student's information.
"""
from person import Person

class Student(Person):
    def __init__(self, 
                name: str, 
                person_id: int, 
                email: str, 
                phone: str, 
                student_id: str, 
                major: str, 
                enrollment_date: str):
        super().__init__(name, person_id, email, phone)
        self.student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date
        
    """
    Returns student information as a formatted string.
    """
    def get_info(self) -> str:
        info = super().get_info()
        return (
            f"{info}\n"
            f"Student ID: {self.student_id}\n"
            f"Major: {self.major}\n"
            f"Enrollment Date: {self.enrollment_date}"
        )