import json

DATA_FILE = "records.json"
MIN_AGE, MAX_AGE = 5, 100
MIN_MARKS, MAX_MARKS = 0.0, 100.0

def load_records(filename=DATA_FILE):
    """Load records from a JSON file. Returns a dict keyed by student ID."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            raise ValueError("Data file has an unexpected format.")
        return data
    except FileNotFoundError:
        # First run: no file yet, start with an empty database.
        return {}
    except json.JSONDecodeError:
        print(f"Warning: '{filename}' is corrupted. Starting with empty records.")
        return {}
    except (OSError, ValueError) as error:
        print(f"Warning: could not read '{filename}': {error}")
        return {}


def save_records(records, filename=DATA_FILE):
    """Write all records to a JSON file. Returns True on success."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)
        return True
    except OSError as error:
        print(f"Error: could not save records: {error}")
        return False


def get_text(prompt, allow_blank=False):
    """Prompt until the user enters non-empty text (or blank if allowed)."""
    while True:
        value = input(prompt).strip()
        if value or allow_blank:
            return value
        print("  Input cannot be empty. Please try again.")


def get_int(prompt, low, high, allow_blank=False):
    """Prompt until the user enters an integer within [low, high]."""
    while True:
        raw = input(prompt).strip()
        if raw == "" and allow_blank:
            return None
        try:
            number = int(raw)
        except ValueError:
            print("  Invalid input. Please enter a whole number.")
            continue
        if low <= number <= high:
            return number
        print(f"  Value must be between {low} and {high}.")


def get_float(prompt, low, high, allow_blank=False):
    """Prompt until the user enters a number within [low, high]."""
    while True:
        raw = input(prompt).strip()
        if raw == "" and allow_blank:
            return None
        try:
            number = float(raw)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if low <= number <= high:
            return number
        print(f"  Value must be between {low} and {high}.")


def generate_id(records):
    """Create the next sequential ID, e.g. S001, S002, ..."""
    numbers = [int(key[1:]) for key in records if key[1:].isdigit()]
    return f"S{(max(numbers) + 1 if numbers else 1):03d}"


def print_table(rows):
    """Print a list of (id, record) pairs as a formatted table."""
    header = f"{'ID':<6}{'Name':<22}{'Age':<6}{'Course':<20}{'Marks':<8}{'Grade':<6}"
    print("\n" + header)
    print("-" * len(header))
    for rec_id, rec in rows:
        print(
            f"{rec_id:<6}{rec['name']:<22}{rec['age']:<6}"
            f"{rec['course']:<20}{rec['marks']:<8.1f}{calculate_grade(rec['marks']):<6}"
        )
    print(f"\nTotal: {len(rows)} record(s)")


def calculate_grade(marks):
    """Return a letter grade for the given marks."""
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"

def add_record(records):
    """Create a new student record."""
    print("\n--- Add New Record ---")
    rec_id = generate_id(records)
    records[rec_id] = {
        "name": get_text("Name: "),
        "age": get_int(f"Age ({MIN_AGE}-{MAX_AGE}): ", MIN_AGE, MAX_AGE),
        "course": get_text("Course: "),
        "marks": get_float(f"Marks ({MIN_MARKS:.0f}-{MAX_MARKS:.0f}): ", MIN_MARKS, MAX_MARKS),
    }
    if save_records(records):
        print(f"Record added successfully with ID {rec_id}.")


def view_records(records):
    """Display all records."""
    print("\n--- All Records ---")
    if not records:
        print("No records found.")
        return
    print_table(sorted(records.items()))


def search_records(records):
    """Search by ID or by (partial) name / course."""
    print("\n--- Search Records ---")
    if not records:
        print("No records to search.")
        return
    term = get_text("Enter ID, name, or course to search: ").lower()
    matches = []
    for rec_id, rec in records.items():
        if (term == rec_id.lower()
                or term in rec["name"].lower()
                or term in rec["course"].lower()):
            matches.append((rec_id, rec))
    if matches:
        print_table(sorted(matches))
    else:
        print(f"No records match '{term}'.")


def update_record(records):
    """Update fields of an existing record. Press Enter to keep a value."""
    print("\n--- Update Record ---")
    rec_id = get_text("Enter the ID to update (e.g. S001): ").upper()
    if rec_id not in records:
        print(f"No record found with ID {rec_id}.")
        return

    rec = records[rec_id]
    print("Leave a field blank to keep its current value.")

    name = get_text(f"Name [{rec['name']}]: ", allow_blank=True)
    age = get_int(f"Age [{rec['age']}]: ", MIN_AGE, MAX_AGE, allow_blank=True)
    course = get_text(f"Course [{rec['course']}]: ", allow_blank=True)
    marks = get_float(f"Marks [{rec['marks']}]: ", MIN_MARKS, MAX_MARKS, allow_blank=True)

    if name:
        rec["name"] = name
    if age is not None:
        rec["age"] = age
    if course:
        rec["course"] = course
    if marks is not None:
        rec["marks"] = marks

    if save_records(records):
        print("Record updated successfully.")


def delete_record(records):
    """Delete a record after confirmation."""
    print("\n--- Delete Record ---")
    rec_id = get_text("Enter the ID to delete (e.g. S001): ").upper()
    if rec_id not in records:
        print(f"No record found with ID {rec_id}.")
        return

    print_table([(rec_id, records[rec_id])])
    confirm = get_text("Are you sure you want to delete this record? (y/n): ").lower()
    if confirm == "y":
        del records[rec_id]
        if save_records(records):
            print("Record deleted successfully.")
    else:
        print("Deletion cancelled.")


def display_menu():
    """Print the main menu."""
    print("\n" + "=" * 36)
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 36)
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Records")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")


def main():
    """Program entry point: load data, then loop on the menu until exit."""
    records = load_records()
    print(f"Loaded {len(records)} record(s) from '{DATA_FILE}'.")

    actions = {
        1: add_record,
        2: view_records,
        3: search_records,
        4: update_record,
        5: delete_record,
    }

    running = True
    while running:
        display_menu()
        try:
            choice = get_int("Enter your choice (1-6): ", 1, 6)
            if choice == 6:
                save_records(records)
                print("Data saved. Goodbye!")
                running = False
            else:
                actions[choice](records)
        except (KeyboardInterrupt, EOFError):
            print("\nInterrupted. Saving data and exiting...")
            save_records(records)
            running = False
        except Exception as error:  # last-resort safety net
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
