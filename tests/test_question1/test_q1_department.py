import unittest
from question1_university_system.department import Department
from question1_university_system.course import Course
from question1_university_system.faculty import Faculty

class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.head = Faculty("Dr Head", "P100", "head@nibm.lk", "070000000", "F100", "DS", "2024-11-12")
        self.dept = Department("Data Science", self.head)

        self.fac1 = Faculty("Dr A", "P1", "a@nibm.lk", "070100000", "F1", "DS", "2024-11-13")
        self.fac2 = Faculty("Dr B", "P2", "b@nibm.lk", "070200000", "F2", "DS", "2024-11-12")

        self.course1 = Course("DS101", "Intro DS", 3, "Dr A", 30)
        self.course2 = Course("DS102", "ML", 3, "Dr B", 30)

    def test_add_faculty(self):
        self.dept.add_faculty(self.fac1)
        self.assertIn(self.fac1, self.dept.faculty_list)

    def test_no_duplicate_faculty(self):
        self.dept.add_faculty(self.fac1)
        self.dept.add_faculty(self.fac1)
        self.assertEqual(len(self.dept.faculty_list), 1)

    def test_add_course(self):
        self.dept.add_course(self.course1)
        self.assertIn(self.course1, self.dept.course_list)

    def test_no_duplicate_courses(self):
        self.dept.add_course(self.course1)
        self.dept.add_course(self.course1)
        self.assertEqual(len(self.dept.course_list), 1)

    def test_department_info(self):
        self.dept.add_faculty(self.fac1)
        self.dept.add_course(self.course1)

        info = self.dept.get_department_info()
        self.assertIn("Data Science", info)
        self.assertIn("Dr Head", info)
        self.assertIn("DS101", info)

if __name__ == "__main__":
    unittest.main()
