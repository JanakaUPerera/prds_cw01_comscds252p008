from question1_university_system.faculty import Faculty
from question1_university_system.course import Course

class Department:
    def __init__(self, 
                dept_name: str, 
                dept_head: Faculty, 
                faculty_list: list[Faculty] = None, 
                course_list: list[Course] = None) -> None:
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.faculty_list = faculty_list if faculty_list is not None else []
        self.course_list = course_list if course_list is not None else []
        
    def add_faculty(self, faculty: Faculty) -> None:
        if faculty not in self.faculty_list:
            self.faculty_list.append(faculty)
            
    def add_course(self, course: Course) -> None:
        if course not in self.course_list:
            self.course_list.append(course)
            
    def get_department_info(self) -> str:
        faculty_names = ", ".join([f.name for f in self.faculty_list])
        course_codes = ", ".join([c.course_code for c in self.course_list])
        return (
            f"Department: {self.dept_name}\n"
            f"Head: {self.dept_head.name}\n"
            f"Faculty: {faculty_names}\n"
            f"Courses: {course_codes if course_codes else 'None'}"
        )