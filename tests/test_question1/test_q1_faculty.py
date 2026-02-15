import unittest

from question1_university_system.faculty import Faculty

class TestFaculty(unittest.TestCase):
    def setUp(self):
        self.s = Faculty("Test", "P999", "t@nibm.lk", "0700000000", "E001", "DEP-COM", "2021-03-15")

    def test_valid_initiation(self):
        f = Faculty("Test", "P999", "t@nibm.lk", "0700000000", "E001", "DEP-COM", "2021-03-15")
        self.assertEqual(f.email, "t@nibm.lk")
        self.assertEqual(f.phone, "0700000000")
        self.assertEqual(f.hire_date, "2021-03-15")
        with self.assertRaises(ValueError):
            Faculty("Test", "P999", "tnibm.lk", "0700000000", "E001", "DEP-COM", "2021-03-15")
            Faculty("Test", "P999", "t@nibm.lk", "0700000000", "E001", "DEP-COM", "2021-03-15")
            Faculty("Test", "P999", "t@nibm.lk", "07000000@", "E001", "DEP-COM", "2021-03-15")
            
if __name__ == "__main__":
    unittest.main()