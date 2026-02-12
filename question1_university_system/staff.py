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
    
    """Staff-specific responsibilities in the university.
    returns:
    - A string describing the role specific responsibilities
    """
    def get_responsibilities(self) -> str:
        role_responsibilities = {
            "Lab Assistant": "Assist labs and maintain equipment.",
            "Technical Officer": "Provide technical and system support.",
            "Program Coordinator": "Coordinate academic programs.",
            "Administrative Officer": "Handle administrative operations.",
            "Student Affairs Executive": "Manage student services and welfare."
        }
        return f"{role_responsibilities.get(
            self.role,
            "Support academic and administrative activities."
        )} As a {self.role} in the {self.department} department."