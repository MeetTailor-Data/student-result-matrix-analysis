# Student Result Matrix Analysis Using NumPy (Python)

## Project Description

The Student Result Matrix Analysis project is a Python application that uses the NumPy library to analyze marks of multiple students across different subjects.
The program performs matrix-based operations such as calculating total marks per student, average marks per subject, identifying top and lowest scoring students, and applying grace marks with value limits.

This project demonstrates how NumPy simplifies multi-dimensional data analysis and is suitable for beginners learning array manipulation and numerical computation in Python.

The application executes once and displays all computed results in the terminal.

---

## Features

* Store student marks using a 2D NumPy array
* Calculate total marks for each student
* Calculate average marks for each subject
* Identify top-performing student
* Identify lowest-performing student
* Apply grace marks to all students
* Limit marks within valid range using clipping

---

## Concepts Used

### Python Fundamentals

* Variables
* Data types (int, float)
* Output formatting

### NumPy Concepts

* Multi-dimensional arrays
* Axis-based aggregation (sum and mean)
* Index identification using argmax and argmin
* Element-wise operations
* Data clipping using clip()

### Programming Concepts

* Matrix-based data representation
* Performance analysis
* Bulk data modification
* Logical result processing

---

## Project Structure

```
student-result-matrix-analysis/
│
├── result_matrix.py
└── README.md
```

---

## How to Run the Program

### Requirements

* Python 3.x installed on the system
* NumPy library installed

### Steps

1. Open terminal or command prompt
2. Navigate to the project directory
3. Run the following command:

```
python result_matrix.py
```

---

## Operations Performed

```
1. Display marks matrix
2. Calculate total marks of each student
3. Calculate average marks of each subject
4. Identify top student
5. Identify lowest student
6. Add grace marks
7. Limit marks between 0 and 100
```

---

## Sample Output

```
Total marks of each student: [255 245 274 207 203]
Average marks of each subject: [78.6 76.6 81.6]
Top student index: 2
Lowest student index: 4
```

---

## Edge Cases Handled

* Proper axis-based aggregation
* Accurate identification of highest and lowest totals
* Grace marks applied without exceeding maximum limit
* Valid mark range enforcement

---

## Author

Meet Tailor

Python Programming Learner

---

## License

This project is created for learning and educational purposes only.

---

## Project Status

Completed

Last Updates: 2026
