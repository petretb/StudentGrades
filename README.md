# Student Data Management System

## Overview
This project is a Python-based command-line system designed to manage structured student records using file-based storage and algorithmic processing. It demonstrates fundamental software engineering concepts including data persistence, sorting algorithms, and search optimization techniques.

---

## Features
- Add student records (ID, name, grade, subject)
- Persistent data storage using CSV files
- Sorting of records using insertion sort
- Search functionality using:
  - Linear search (unsorted data)
  - Binary search (sorted data)
- Menu-driven command-line interface

---

## Core Concepts Demonstrated
- File handling (CSV read/write operations)
- Data structures (lists and dictionaries)
- Sorting algorithms (Insertion Sort)
- Search algorithms (Linear and Binary Search)
- Program design using modular functions
- Basic system workflow architecture

---

## System Workflow
1. User inputs structured data via CLI menu
2. Data is stored persistently in a CSV file
3. Data can be retrieved and sorted for analysis
4. Users can search records using different algorithmic approaches

---

## Engineering Relevance
This system reflects the type of structured data processing used in engineering applications such as:
- Test data logging systems
- Sensor data processing pipelines
- Operational record management systems

It demonstrates how raw data is transformed into structured, searchable information using algorithmic methods.

---

## Limitations & Future Improvements
- Binary search requires correct sorting by the selected key to function properly
- No input validation or error handling for invalid data
- Could be improved by:
  - adding data validation and exception handling
  - integrating database storage instead of CSV
  - expanding search capabilities to multiple fields
  - improving sorting efficiency

---

## How to Run
```bash
python main.py
