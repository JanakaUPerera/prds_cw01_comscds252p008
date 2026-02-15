# Coursework NIB7143CEM - Programming for Data Science
## MSc Data Science – NIBM Sri Lanka
Awarding Body: Coventry University (UK)

---

## Coursework Overview

This repository contains the complete submission for the module:

**Programming for Data Science (NIB7143CEM)**

The coursework consists of three major components:

1. Question 1 – Object-Oriented University Management System
2. Question 2 – Data Analysis & Predictive Modeling
3. Question 3 – Ethical Considerations in Healthcare Data

A structured technical report is also included as required.

---

## Project Structure
```txt
prds_cw01_comscds252p008
 ┣ question1_university_system
 ┃ ┣ course.py
 ┃ ┣ department.py
 ┃ ┣ faculty.py
 ┃ ┣ main.py
 ┃ ┣ person.py
 ┃ ┣ README.md
 ┃ ┣ staff.py
 ┃ ┗ student.py
 ┣ question2_data_analysis
 ┃ ┣ data
 ┃ ┃ ┣ cleaned
 ┃ ┃ ┃ ┗ cleaned_books_data_500.csv
 ┃ ┃ ┣ raw
 ┃ ┃ ┃ ┗ books_data_500.csv
 ┃ ┃ ┗ visualizations
 ┃ ┃ ┃ ┣ bar_avg_rating_top8.html
 ┃ ┃ ┃ ┣ boxplot_price_top5_categories.html
 ┃ ┃ ┃ ┣ histogram_price.html
 ┃ ┃ ┃ ┣ interactive_bar_avg_rating_selector.html
 ┃ ┃ ┃ ┣ interactive_scatterplot_price_vs_rating_selector.html
 ┃ ┃ ┃ ┣ scatterplot_price_vs_rating.html
 ┃ ┣ advance_visualize_plotly.ipynb
 ┃ ┣ data_analyzer.py
 ┃ ┣ data_cleaner.py
 ┃ ┣ data_predictor.py
 ┃ ┣ data_scraper.py
 ┃ ┣ data_visualizer.py
 ┃ ┗ interactive_dashboard.ipynb
 ┣ tests
 ┃ ┗ test_question1
 ┃ ┃ ┣ test_q1_course.py
 ┃ ┃ ┣ test_q1_department.py
 ┃ ┃ ┣ test_q1_faculty.py
 ┃ ┃ ┣ test_q1_person.py
 ┃ ┃ ┣ test_q1_staff.py
 ┃ ┃ ┣ test_q1_student.py
 ┃ ┃ ┗ __init__.py
 ┣ .gitignore
 ┣ README.md
 ┗ requirements.txt
```

 ---

# Question 1 – Object-Oriented Programming: University Management System

Implements an Object-Oriented system demonstrating:

- Inheritance (Person → Student, Faculty, Staff)
- Encapsulation and validation
- Polymorphism
- Course and Department relationships

**To run Question 1 (University System):** 
Read the [Installation](#installation) and [How to Run](#how-to-run) sections in [question1_university_system/README.md](question1_university_system/README.md).

# Question 2 – Data Analysis: E-commerce Data Analysis

Implements a full data science pipeline:

### A. Web Scraping
- Scraped 100+ books from http://books.toscrape.com
- Used requests + BeautifulSoup4
- Implemented delay and retry logic
- Saved to CSV

### B. Data Cleaning
- Standardized prices
- Converted ratings
- Handled missing values
- Removed duplicates
- Created derived columns

### C. Statistical Analysis
- Descriptive statistics
- Inferential statistics (IQR, correlation, t-test)

### D. Visualization - Using Plotly
- Histogram
- Box plot
- Scatter plot with regression
- bar chart
- Interactive Scatter Plot
- Interactive bar chart

### E. Predictive Analysis
- Linear Regression model
- R² score and MAE evaluation
- Feature influence interpretation

**Execution order:**
cd question2_data_analysis
python data_scraper.py
python data_cleaner.py
python data_analyzer.py
python data_visualizer.py
python data_predictor.py

### Unit Test
Test each classes
Run: python -m unittest discover -s tests -p "test_*.py" -v

# Question 3 – Data Ethics: AI Ethics in Healthcare

Discusses:
- GDPR vs HIPAA
- Bias in AI systems
- Ethical checklist
- Stakeholder impact in healthcare AI

**Submitted as:**
at technical_report.pdf under Data Ethics: AI Ethics in Healthcare

## Technologies Used
- Python 3.13+
- pandas
- NumPy
- SciPy
- scikit-learn
- Plotly
- BeautifulSoup4
- requests
- tqdm

## Installation
1. Open a terminal in this folder: prds_cw01_comscds252p008
2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
3. Run: pip install -r requirements.txt