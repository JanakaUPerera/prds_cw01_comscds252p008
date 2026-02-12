"""
faculty.py
This module defines the Faculty class, which inherits from the Person class.

functions:
- __init__: Initializes a Faculty object with personal and faculty-specific attributes.
- get_info: Returns a formatted string with the faculty member's information.
"""
from person import Person

class Faculty(Person):
    def __init__(self, 
                name: str, 
                person_id: int, 
                email: str, 
                phone: str, 
                employee_id: int,
                department: str, 
                hire_date: str):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department = department
        self.hire_date = hire_date

    """
    Returns faculty information as a formatted string.
    """
    def get_info(self) -> str:
        info = super().get_info()
        return (
            f"{info}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Department: {self.department}\n"
            f"Hire Date: {self.hire_date}"
        )