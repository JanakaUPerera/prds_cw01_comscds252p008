from student import Student
from faculty import Faculty
from staff import Staff

class Main:
    def __init__(self):
        pass

    def run(self):
        print("Welcome to the University System!")
        # Create at least 3 objects of each type: Student, Faculty, and Staff
        print("\n--- Creating Students Objects ---")
        students = [
            Student("A. L. Amal Gunarathne", "PS001", "amal.ps001@nibm.lk", "0710000001", "S001", "Artificial Intelligence", "2025-10-01"),
            Student("S. M. Nimali Perera", "PS002", "nimali.ps002@nibm.lk", "0710000002", "S002", "Cyber Security", "2025-10-01"),
            Student("K. Ravi Silva", "PS003", "ravi.ps003@nibm.lk", "0710000003", "S003", "Business Analytics", "2025-10-01"),
            Student("D. N. Chamika Fernando", "PS004", "chamika.ps004@nibm.lk", "0710000004", "S004", "Data Science", "2025-09-15"),
            Student("M. A. Ishara Jayasinghe", "PS005", "ishara.ps005@nibm.lk", "0710000005", "S005", "Statistics", "2025-08-20"),
        ]
        print("\n--- Creating Faculty Objects ---")
        faculty_members = [
            Faculty("Dr. N. K. Perera", "PF001", "nk.perera@nibm.lk", "0721000001", "E001", "DEP-COM", "2021-03-15"),
            Faculty("Ms. S. D. Wijeratne", "PF002", "sd.wijeratne@nibm.lk", "0721000002", "E002", "DEP-COM", "2022-07-01"),
            Faculty("Mr. R. M. Jayasinghe", "PF003", "rm.jayasinghe@nibm.lk", "0721000003", "E003", "DEP-COM", "2020-01-10"),
            Faculty("Ms. P. L. Fernando", "PF004", "pl.fernando@nibm.lk", "0721000004", "E004", "DEP-BUS", "2019-09-05"),
            Faculty("Mr. A. S. Gunawardena", "PF005", "as.gunawardena@nibm.lk", "0721000005", "E005", "DEP-BUS", "2023-02-20"),
        ]
        print("\n--- Creating Staff Objects ---")
        staff_members = [
            Staff("Ms. K. M. Dilrukshi Silva", "PSF001", "dilrukshi.silva@nibm.lk", "0732000001", "ES001", "Lab Assistant", "DEP-COM"),
            Staff("Mr. T. R. Nuwan Perera", "PSF002", "nuwan.perera@nibm.lk", "0732000002", "ES002", "Technical Officer", "DEP-COM"),
            Staff("Ms. H. D. Sachini Fernando", "PSF003", "sachini.fernando@nibm.lk", "0732000003", "ES003", "Program Coordinator", "DEP-COM"),
            Staff("Mr. A. P. Kavindu Jayawardena", "PSF004", "kavindu.j@nibm.lk", "0732000004", "ES004", "Administrative Officer", "DEP-BUS"),
            Staff("Ms. R. S. Oshadi Karunaratne", "PSF005", "oshadi.k@nibm.lk", "0732000005", "ES005", "Student Affairs Executive", "DEP-BUS"),
        ]

        # Demonstrate method inheritance by calling get_info() on one object of each type
        print("\n--- Method Inheritance Demonstration ---")
        # Print the information of all created objects in table format using pandas DataFrame
        print("\n--- Students ---")
        for student in students:
            print(student.get_info())
            print("-" * 50)
        
        print("\n--- Faculty Members ---")
        for faculty in faculty_members:
            print(faculty.get_info())
            print("-" * 50)
            
        print("\n--- Staff Members ---")
        for staff in staff_members:
            print(staff.get_info())
            print("-" * 50)
            
        # Demonstrate enroll a student in 4-5 courses, receiving grades, and displaying academic status.
        student = students[0]  # Select the first student for demonstration
        print(f"\n--- Enrolling Courses for {student.name} ---")
        enroll_semester = "2025S1"
        courses = ['CS101', 'CS102', 'CS103', 'CS104', 'CS105']
        for course in courses:
            student.enroll_course(enroll_semester, course)
        
        grades = [3.5, 3.7, 3.2, 4.0, 3.8]
        for course, grade in zip(courses, grades):
            student.add_grade(enroll_semester, course, grade)
        
        print(f"\n--- Academic Status for {student.name} ---")
        print(f"GPA: {student.gpa}")
        print(f"Academic Status: {student.get_academic_status()}")
        
        # Show error handling by attempting to add invalid data.
        print("\n--- Error Handling Demonstration ---")
        print("Attempting to enroll in more than 6 courses in a semester:")
        try:
            student.enroll_course(enroll_semester, 'CS106')
            student.enroll_course(enroll_semester, 'CS107') # Exceeding course limit
        except ValueError as e:
            print(f"Error: {e}")
            
        print("\nAttempting to add a grade for a course the student is not enrolled in:")
        try:
            student.add_grade(enroll_semester, 'CS999', 3.0) # Course not enrolled
        except ValueError as e:
            print(f"Error: {e}")
            
        print("\nAttempting to add an invalid grade:")
        try:
            student.add_grade(enroll_semester, 'CS101', 4.5) # Invalid grade
        except ValueError as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main = Main()
    main.run()