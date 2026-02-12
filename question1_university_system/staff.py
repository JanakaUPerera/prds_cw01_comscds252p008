"""
staff.py
This module defines the Staff class, which inherits from the Person class.

functions:
- __init__: Initializes a Staff object with personal and staff-specific attributes.
- get_info: Returns a formatted string with the staff member's information.
"""
from person import Person

class Staff(Person):
    def __init__(self, 
                name: str, 
                person_id: int, 
                email: str, 
                phone: str, 
                employee_id: int, 
                role: str, 
                department: str
                ) -> None:
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.role = role
        self.department = department

    """
    Returns staff member information as a formatted string.
    """
    def get_info(self) -> str:
        info = super().get_info()
        return (
            f"{info}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Role: {self.role}\n"
            f"Department: {self.department}"
        )