"""
student.py
This module defines the Student class, which inherits from the Person class.

functions:
- __init__: Initializes a Student object with personal and student-specific attributes.
- get_info: Returns a formatted string with the student's information.
- enroll_course: Enrolls the student in a course for a specific semester.
- add_grade: Adds a grade for a course in a specific semester.
- calculate_gpa: Calculates the cumulative GPA for the student based on their grades.
- gpa: A property that returns the calculated GPA.
- get_academic_status: Determines the academic status of the student based on their GPA.
"""
from person import Person

class Student(Person):
    MAX_COURSES_PER_SEMESTER = 6
    
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
        
        self.enrolled_courses: dict[str, list[str]] = {} # {semester: [course_code1, course_code2]}
        self.grades: dict[str, dict[str, float]] = {} # {semester: {course_code: grade}}
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
    
    """
    Enrolls the student in a course
    Parameters:
        semester (str): The semester in which to enroll the student.
        course_code (str): The code of the course to enroll in.
    structure:
    - First, it checks if the semester is already in the enrolled_courses dictionary. 
        If not, it initializes an empty list for that semester.
    - Then, it checks if the number of courses for that semester has reached the maximum limit. 
        If it has, it raises a ValueError.
    - If the course is not already in the enrolled_courses list, 
        it adds the course code to the list.
    """
    def enroll_course(self, semester: str, course_code: str) -> None:
        if semester not in self.enrolled_courses:
            self.enrolled_courses[semester] = []

        if len(self.enrolled_courses[semester]) >= self.MAX_COURSES_PER_SEMESTER:
            raise ValueError(f"Cannot enroll: The maximum number of courses for a semester is {self.MAX_COURSES_PER_SEMESTER}, and has been reached.")
        
        if course_code not in self.enrolled_courses[semester]:
            self.enrolled_courses[semester].append(course_code)
    
    """
    Adds a grade for a course
    Parameters:
        semester (str): The semester in which the course was taken.
        course_code (str): The code of the course for which to add the grade.
        grade (float): The grade to add for the course.
    structure:
    - First, it checks if the student is enrolled in the specified course for the given semester. 
        If not, it raises a ValueError.
    - Then, it checks if the grade is between 0.0 and 4.0. 
        If not, it raises a ValueError.
    - If the student is enrolled, it adds or updates the grade for the semester and course
    """        
    def add_grade(self, semester: str, course_code: str, grade: float) -> None:
        if course_code not in self.enrolled_courses[semester]:
            raise ValueError(f"Cannot add grade: student is not enrolled in semester {semester} course {course_code}")
        
        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0")
        
        if semester not in self.grades:
            self.grades[semester] = {}
        self.grades[semester][course_code] = grade
    
    """
    Calculate the cumulative GPA for the student based on the grades.
    structure:
    - Iterates through semester and their courses, calculate total points and total courses.
    - Calculate GPA by dividing total points by total courses.
    - Rounds the GPA to two decimal places.
    returns:
    - The calculated GPA as a float.
    """
    def calculate_gpa(self) -> float:
        if not self.grades:
            return 0.0
        
        total_points = 0
        total_courses = 0
        for semester, courses in self.grades.items():
            total_courses += len(courses)
            for grade in courses.values():
                total_points += grade
        
        if total_courses == 0:
            return 0.0
        
        gpa = total_points / total_courses
        return round(gpa, 2)
    
    """
    Property to get the GPA of the student.
    Read-Only and not directly settable.
    """
    @property
    def gpa(self) -> float:
        return self.calculate_gpa()
    
    """
    Determines the academic status of the student based on their GPA.
    structure:
    - If the GPA is 3.5 or higher, returns "Dean's List".
    - If the GPA is between 2.0 and 3.5, returns "Good Standing".
    - If the GPA is below 2.0, returns "Probation".
    returns:
    - A string representing the academic status.
    """
    def get_academic_status(self) -> str:
        gpa = self.gpa
        if gpa >= 3.5:
            return "Dean's List"
        if gpa >= 2.0:
            return "Good Standing"
        return "Probation"