import unittest

from question1_university_system.staff import Staff

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.s = Staff("Test", "P999", "t@nibm.lk", "0700000000", "S999", "Lab Assistant", "DEP-COM")

    def test_valid_initiation(self):
        s = Staff("Test", "P999", "t@nibm.lk", "0700000000", "S999", "Lab Assistant", "DEP-COM")
        self.assertEqual(s.email, "t@nibm.lk")
        self.assertEqual(s.phone, "0700000000")
        with self.assertRaises(ValueError):
            Staff("Test", "P999", "tnibm.lk", "0700000000", "S999", "Lab Assistant", "DEP-COM")
            Staff("Test", "P999", "t@nibm.lk", "07000000@", "S999", "Lab Assistant", "DEP-COM")
            
if __name__ == "__main__":
    unittest.main()