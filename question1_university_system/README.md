# Coursework NIB7143CEM - Programming for Data Science
## Question 1: University Management System (OOP)

This folder contains the implementation for **Question 1** of the coursework: an **Object-Oriented University Management System** demonstrating:
- Inheritance (`Person` → `Student`, `Faculty`, `Staff`)
- Encapsulation & validation (`@property` for read-only GPA, input validation with `ValueError`)
- Polymorphism (`get_responsibilities()` overridden in derived classes)
- Additional classes for academic structure (`Course`, `Department`)

---

## Folder Structure (Question 1)
question1_university_system
 ┣ course.py
 ┣ department.py
 ┣ faculty.py
 ┣ main.py
 ┣ person.py
 ┣ README.md
 ┣ staff.py
 ┗ student.py

## Technologies Used
- Python 3.13+
- Standard Library only for core OOP logic

## Installation
1. Open a terminal in this folder: prds_cw01_comscds252p008
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
3. Run: pip install -r requirements.txt

## How to Run
1. Open a terminal in this folder: question1_university_system
2. Run the demo: python .\main.py


---

## What the Demo Shows (as required)
When you run `main.py`, the output demonstrates:

### A) Inheritance
- Creates at least **3 Student**, **3 Faculty**, **3 Staff** objects
- Prints each object using `get_info()`

### B) Student Academic Features
- Enrolls a student in **4–5 courses**
- Adds grades and calculates GPA
- Prints academic status:
- GPA ≥ 3.5 → Dean’s List
- GPA ≥ 2.0 → Good Standing
- GPA < 2.0 → Probation

### C) Encapsulation & Validation
- GPA is **read-only** (`@property`)
- Grades must be in **0.0 to 4.0**
- Course limit is **maximum 6 per semester**
- Invalid operations raise `ValueError` and are demonstrated in `main.py`

### D) Polymorphism
- Uses a mixed list of `Student`, `Faculty`, and `Staff`
- Calls `get_responsibilities()` to show runtime polymorphism

### E) Course & Department
- Creates **2 departments**
- Adds **3 courses** to each
- Assigns instructors, enrolls students
- Prints department summaries and course details

---

## Notes
- The `try/except` blocks are placed in `main.py` to demonstrate error handling
while keeping the core classes clean and reusable.

---

## Author
- Student ID: COMSCDS252P-008
- Module: Programming for Data Science
- Course Work: NIB7143CEM
