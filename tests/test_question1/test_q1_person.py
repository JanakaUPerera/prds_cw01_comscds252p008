import unittest

from question1_university_system.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.s = Person("Test", "P999", "t@nibm.lk", "0700000000")

    def test_valid_initiation(self):
        p = Person("Test", "P999", "t@nibm.lk", "0700000000")
        self.assertEqual(p.email, "t@nibm.lk")
        self.assertEqual(p.phone, "0700000000")
        with self.assertRaises(ValueError):
            Person("Test", "P999", "tnibm.lk", "0700000000")
            Person("Test", "P999", "t@nibm.lk", "07000000@")
            
if __name__ == "__main__":
    unittest.main()