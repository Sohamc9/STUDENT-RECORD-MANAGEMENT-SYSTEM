# Student Record Management System

A menu-driven console application in Python that lets you add, view, search, update and delete student records. Records are saved to a JSON file, so nothing is lost when the program closes.

## Project Description

This mini project combines the core Python fundamentals into one working application: data types and variables, conditionals and loops, functions, exception handling, file I/O and menu-driven design. Each student record stores an ID, name, age, course and marks, and the program calculates a letter grade from the marks.

## Features

- Menu-driven interface (options 1-6) that repeats until the user exits
- **Add** a record with an auto-generated ID (S001, S002, ...)
- **View** all records in a formatted table with letter grades
- **Search** by ID, or by part of a name or course (case-insensitive)
- **Update** any field of a record; press Enter to keep the current value
- **Delete** a record, with a confirmation prompt
- Input validation for empty text, non-numeric values and out-of-range numbers
- Automatic saving after every change; data is reloaded at the next start
- Graceful handling of a missing file, a corrupted file, save failures and Ctrl+C / Ctrl+D

## Technologies / Concepts Used

| Concept | How it is used |
|---|---|
| Data types and variables | `dict` of records keyed by ID, `str`, `int`, `float`, `bool` flag, constants such as `DATA_FILE` |
| Conditionals and loops | `if/elif/else` for grading and validation; `while` for the menu and re-prompting; `for` for searching and printing |
| Functions | One function per task (`add_record`, `search_records`, `load_records`, ...) with `main()` as the entry point |
| Exception handling | `ValueError`, `FileNotFoundError`, `json.JSONDecodeError`, `OSError`, `KeyboardInterrupt`, `EOFError` |
| File I/O | Reading and writing `records.json` with the `json` module and `with open(...)` |
| Menu-driven design | Numbered menu with a dispatch dictionary mapping choices to functions |

- Language: Python 3.8 or later
- Libraries: standard library only (`json`), nothing to install

## Project Structure

```
student-record-management/
├── student_records.py      # Application source code
├── records.json            # Sample data file used by the application
├── README.md               # This file
├── sample_session.txt      # Full text of the sample runs
├── docs/
│   └── REPORT.md           # Complete assignment report
└── screenshots/            # Screenshots of the application running
```

## How to Run

1. Install Python 3.8 or later (check with `python --version`).
2. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repository-name>.git
   cd <your-repository-name>
   ```
3. Run the application:
   ```bash
   python student_records.py
   ```
   (Use `python3` on macOS or Linux if `python` does not work.)

The program creates `records.json` in the folder you run it from if it does not exist. The included sample file has three records so you can try search, update and delete straight away.

## Sample Input / Output

```
====================================
   STUDENT RECORD MANAGEMENT SYSTEM
====================================
1. Add Record
2. View All Records
3. Search Records
4. Update Record
5. Delete Record
6. Exit
Enter your choice (1-6): 2

--- All Records ---

ID    Name                  Age   Course              Marks   Grade
--------------------------------------------------------------------
S001  Asha Rao              20    Python              88.5    A
S002  Vikram Singh          23    Data Science        76.5    B
S003  Meera Iyer            19    Web Development     94.5    A+

Total: 3 record(s)
```

Validation example:

```
Age (5-100): abc
  Invalid input. Please enter a whole number.
Age (5-100): 150
  Value must be between 5 and 100.
Age (5-100): 18
```

The complete runs are in `sample_session.txt`.

## Screenshots

| Add records | View records |
|---|---|
| ![Add](screenshots/01_add_records.png) | ![View](screenshots/02_view_records.png) |

| Search records | Update a record |
|---|---|
| ![Search](screenshots/03_search_records.png) | ![Update](screenshots/04_update_record.png) |

| Input validation | Persistence after restart |
|---|---|
| ![Validation](screenshots/05_input_validation.png) | ![Persistence](screenshots/06_persistence_restart.png) |

**Delete a record (cancel, then confirm)**

![Delete](screenshots/07_delete_record.png)

## Documentation

The full report (objectives, design, function descriptions, test cases, limitations) is in [docs/REPORT.md](docs/REPORT.md).

## GitHub Repository Details

- **Repository name:** `<your-repository-name>`
- **Repository link:** `https://github.com/<your-username>/<your-repository-name>`
- **Author:** `<your-name>`
- **Course / Assignment:** Mini Project: Console Record-Management Application
