"""
course.py
This module defines the Course class, which represents a course in the university.

functions:
- __init__: Initializes a Course object with course-specific attributes.
- is_full: Checks if the course has reached its maximum capacity.
- add_student: Adds a student to the course if there is capacity.
- remove_student: Removes a student from the course.
"""
from question1_university_system.student import Student
from question1_university_system.faculty import Faculty

class Course:
    def __init__(self, 
                course_code: str, 
                course_name: str, 
                credits: int, 
                instructor: Faculty,
                max_capacity: int,
                enrolled_students: list[Student] = None,
                )-> None:
        
        # Validating initial data
        # Check credit value is positive value
        if credits <= 0:
            raise ValueError("Credits must be positive value")
        # Check max capacity value is positive value
        if max_capacity <= 0:
            raise ValueError("Max Capacity must be positive value")
        
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.instructor = instructor
        self.max_capacity = max_capacity
        self.enrolled_students = enrolled_students if enrolled_students is not None else []
    
    """
    Checks if the course has reached its maximum capacity.
    returns:
    - True if the course is full, False otherwise.
    """    
    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.max_capacity  
    
    """
    Add new student
    structure:
    - First, it checks if the course is full. If it is, it raises a ValueError.
    - Then, it checks if the student is already enrolled in the course. If not,
        it adds the student to the enrolled_students list.
    """
    def add_student(self, student: Student) -> None:
        if self.is_full():
            raise ValueError(f"Cannot add student: course {self.course_code} is at full capacity of {self.max_capacity}.")
        
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
    
    """
    Remove the specified student from the course.
    structure:
    - It checks if the student is enrolled, if so, removes the student from the enrolled students list.
    """
    def remove_student(self, student: Student) -> None:
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            
    def __str__(self) -> str:
        instructor_name = self.instructor.name
        return (
            f"{self.course_code} - {self.course_name} ({self.credits} credits) | "
            f"Instructor: {instructor_name} | Enrolled: {len(self.enrolled_students)}/{self.max_capacity}"
        )