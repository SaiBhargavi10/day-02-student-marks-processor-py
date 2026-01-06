# Day 2 – Student Marks Processor (Python)

## Overview
Student Marks Processor is a Python command-line application that reads student marks from a CSV file, processes the data, and generates a summarized academic report.

The program handles invalid records gracefully, applies subject-wise pass rules, computes grades, identifies the class topper, and exports the final report to a file.

This project is part of a **30 Days – 30 Projects** challenge.

---

## Problem Statement
Build a program that reads student marks from a CSV file and generates totals, averages, grades, and pass/fail results while handling invalid inputs safely.

---

## Features
- Reads student data from a CSV file
- Skips invalid or non-numeric records
- Calculates total, average, grade, and result
- Applies subject-wise pass criteria
- Identifies the class topper
- Generates grade distribution
- Displays a formatted report
- Saves the report to `report.txt`

---

### Example Input (`students.csv`)
```csv
roll_no,name,maths,science,english
101,Aarav,55,60,48
102,Diya,92,88,95
103,Rohan,60,55,58
104,Ananya,45,50,45
105,Kabir,abc,70,80

Skipping invalid record for student: Kabir

Student Marks Report
----------------------------------------------------------------------
Roll    Name           Total     Average   Grade   Result
----------------------------------------------------------------------
101     Aarav          163       54.33     D       FAIL
102     Diya           275       91.67     A       PASS
103     Rohan          173       57.67     D       PASS
104     Ananya         140       46.67     F       FAIL
----------------------------------------------------------------------

Class Topper: Diya (Average: 91.67)

Grade Distribution:
A: 1
B: 0
C: 0
D: 2
F: 1

Report saved to report.txt

---
## Program Logic
- Read data using `csv.DictReader`
- Validate and convert marks
- Skip invalid records
- Compute totals and averages
- Assign grades and pass/fail status
- Identify topper and grade distribution
- Display and save the report

---

## How to Run
```bash
python student_marks.py