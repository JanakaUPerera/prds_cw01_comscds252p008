"""
person.py
This module defines the Person class, 
which serves as a base class for both Student, Academic and None Academic Staff.

functions:
- __init__: Initializes a Person object with basic personal attributes.
- get_info: Returns a formatted string with the person's information.
- update_contact: Updates the person's contact information.
"""
class Person:
    def __init__(self, 
                name: str, 
                person_id: int, 
                email: str, 
                phone: str
                ) -> None:
        self.name = name
        self.person_id = person_id
        self.email = email
        self.phone = phone
    
    """
    Returns person information as formatted string.
    """
    def get_info(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"ID: {self.person_id}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )
    
    """
    Updates the person's contact information.
    Parameters:
        email (str, optional): The new email address.
        phone (str, optional): The new phone number.
    """
    def update_contact(self, email: str = None, phone: str = None) -> None:
        if email:
            self.email = email
        if phone:
            self.phone = phone
            
    """
    Returns the general responsibilities in the university.
    """
    def get_responsibilities(self) -> str:
        return "General responsibilities in the university."