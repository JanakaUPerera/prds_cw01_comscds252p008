import unittest

from question1_university_system.student import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s = Student("Test", "P999", "t@nibm.lk", "0700000000", "S999", "Data Science", "2025-10-01")

    def test_valid_initiation(self):
        s = Student("Test", "P999", "t@nibm.lk", "0700000000", "S999", "Data Science", "2025-10-01")
        self.assertEqual(s.email, "t@nibm.lk")
        self.assertEqual(s.phone, "0700000000")
        self.assertEqual(s.enrollment_date, "2025-10-01")
        with self.assertRaises(ValueError):
            Student("Test", "P999", "tnibm.lk", "0700000000", "S999", "Data Science", "2025-10-01")
            Student("Test", "P999", "t@nibm.lk", "0700000000", "S999", "Data Science", "202510-01")
            Student("Test", "P999", "t@nibm.lk", "07000000@", "S999", "Data Science", "2025-10-01")

    def test_course_limit(self):
        for i in range(6):
            self.s.enroll_course("2025S1", f"DS10{i}")
        with self.assertRaises(ValueError):
            # 7th course should fail
            self.s.enroll_course("2025S1", "DS999")
    
    def test_grade_validation(self):
        self.s.enroll_course("2025S1", "DS101")
        with self.assertRaises(ValueError):
            self.s.add_grade("2025S1", "DS101", 4.5)  # invalid
        self.s.add_grade("2025S1", "DS101", 3.5)  # valid
        self.assertAlmostEqual(self.s.gpa, 3.5)
    
    def test_gpa_read_only(self):
        self.s.enroll_course("2025S1", "DS101")
        self.s.add_grade("2025S1", "DS101", 3.0)
        with self.assertRaises(AttributeError):
            # should fail because property has no setter
            self.s.gpa = 4.0
            
if __name__ == "__main__":
    unittest.main()