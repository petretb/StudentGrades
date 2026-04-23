# Student Data Management System

## Overview
This project is a Python-based command-line data management system designed to store, organize, and retrieve structured records efficiently. It demonstrates fundamental concepts in data structures, file handling, and algorithm design, including sorting and searching techniques applied to dataset processing.

---

## Features
- Add student records (ID, name, grade, subject)
- Persistent data storage using CSV files
- Sort records using the insertion sort algorithm
- Search functionality using:
  - Linear search
  - Binary search
- Menu-driven command-line interface

---

## Core Concepts Demonstrated
- File I/O using CSV (reading and writing structured data)
- Data structures (lists and dictionaries)
- Sorting algorithms (Insertion Sort)
- Searching algorithms (Linear Search and Binary Search)
- Basic software system design and user interaction flow

---

## How It Works
1. The user inputs student data through a CLI menu.
2. Data is stored in a CSV file for persistence.
3. The system can read and sort stored data based on grade.
4. Users can search for specific records using either linear or binary search methods.

---

## Engineering Relevance
This system reflects the type of structured data processing used in engineering environments, where large datasets (such as test results, sensor readings, or operational logs) must be efficiently stored, sorted, and queried.

The project demonstrates:
- Data pipeline design (input → storage → processing → output)
- Algorithm selection based on efficiency tradeoffs
- Structured approach to dataset management

---

## Limitations & Future Improvements
- Binary search currently depends on correct sorting by the selected key
- No input validation for incorrect or missing data
- Could be improved by adding:
  - error handling and validation
  - support for additional search filters
  - graphical user interface (GUI)
  - database integration instead of CSV storage

---

## How to Run
```bash
python main.py
