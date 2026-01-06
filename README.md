# Day 2 – Student Marks Processor (Python)

## 📌 Overview
Student Marks Processor is a Python command-line application that reads student marks from a CSV file, processes academic data, and generates a summarized report.

The program handles invalid records gracefully, applies subject-wise pass rules, computes grades, identifies the class topper, calculates class statistics, and saves the final report to a text file.

This project is part of the **30 Days – 30 Projects** challenge.

---

## 🎯 Problem Statement
Build a program that reads student marks from a CSV file and generates totals, averages, grades, and pass/fail results while handling invalid inputs safely.

---

## 🚀 Features
- Reads student data from a CSV file
- Skips invalid or non-numeric records safely
- Calculates total and average marks
- Assigns grades based on average
- Applies subject-wise pass criteria
- Determines overall pass/fail result
- Identifies the class topper
- Computes class average and pass percentage
- Generates grade distribution
- Displays a formatted console report
- Saves the final report to `report.txt`

---

## 📂 Example Input (`students.csv`)
```csv
roll_no,name,maths,science,english
101,Aarav,55,60,48
102,Diya,92,88,95
103,Rohan,60,55,58
104,Ananya,45,50,45
105,Kabir,abc,70,80

## sample ooutput 
Skipping invalid record for student: Kabir

STUDENT MARKS REPORT
-------------------------------------------------------------------------------------
Roll    Name           Total     Average   Grade   Result
-------------------------------------------------------------------------------------
102     Diya           275       91.67     A       PASS
103     Rohan          173       57.67     D       PASS
101     Aarav          163       54.33     D       FAIL
104     Ananya         140       46.67     F       FAIL
-------------------------------------------------------------------------------------

🏆 Class Topper: Diya (Average: 91.67)
📊 Class Average: 62.17
✅ Pass Percentage: 50.0%

Grade Distribution:
A: 1
B: 0
C: 0
D: 2
F: 1

📁 Report generated:
✔ report.txt
