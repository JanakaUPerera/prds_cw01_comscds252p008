import unittest
from question1_university_system.course import Course
from question1_university_system.student import Student

class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course(
            course_code="DS101",
            course_name="Intro to Data Science",
            credits=3,
            instructor="Dr. Smith",
            max_capacity=2
        )

        self.s1 = Student("A", "P1", "a@nibm.lk", "070100000", "S1", "DS", "2025-01-01")
        self.s2 = Student("B", "P2", "b@nibm.lk", "070200000", "S2", "DS", "2025-01-01")
        self.s3 = Student("C", "P3", "c@nibm.lk", "070300000", "S3", "DS", "2025-01-01")

    def test_valid_initiation(self):
        c = Course(
            course_code="DS101",
            course_name="Intro to Data Science",
            credits=3,
            instructor="Dr. Smith",
            max_capacity=2
        )
        self.assertEqual(c.credits, 3)
        self.assertEqual(c.max_capacity, 2)
        
        with self.assertRaises(ValueError):
            Course(
                course_code="DS101",
                course_name="Intro to Data Science",
                credits=-1,
                instructor="Dr. Smith",
                max_capacity=2
            )
        with self.assertRaises(ValueError):
            Course(
            course_code="DS101",
            course_name="Intro to Data Science",
            credits=3,
            instructor="Dr. Smith",
            max_capacity=0
        )

    def test_add_student(self):
        self.course.add_student(self.s1)
        self.assertIn(self.s1, self.course.enrolled_students)

    def test_no_duplicate_students(self):
        self.course.add_student(self.s1)
        self.course.add_student(self.s1)
        self.assertEqual(len(self.course.enrolled_students), 1)

    def test_course_capacity(self):
        self.course.add_student(self.s1)
        self.course.add_student(self.s2)
        with self.assertRaises(ValueError):
            self.course.add_student(self.s3)

    def test_is_full(self):
        self.course.add_student(self.s1)
        self.course.add_student(self.s2)
        self.assertTrue(self.course.is_full())

    def test_remove_student(self):
        self.course.add_student(self.s1)
        self.course.remove_student(self.s1)
        self.assertNotIn(self.s1, self.course.enrolled_students)

if __name__ == "__main__":
    unittest.main()
