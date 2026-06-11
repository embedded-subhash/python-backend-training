"""
Employee Management Console Application
Manages employee records using a list of dictionaries.
"""

employees = []


def get_next_id():
    """Generate the next employee ID."""
    if not employees:
        return 1
    return max(emp["id"] for emp in employees) + 1


def add_employee():
    """Add a new employee to the records."""
    print("\n--- Add New Employee ---")
    try:
        name = input("Enter Name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        email = input("Enter Email: ").strip()
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

        department = input("Enter Department: ").strip()
        if not department:
            raise ValueError("Department cannot be empty.")

        salary = float(input("Enter Salary: "))
        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        experience = int(input("Enter Experience (in years): "))
        if experience < 0:
            raise ValueError("Experience cannot be negative.")

        employee = {
            "id": get_next_id(),
            "name": name,
            "email": email,
            "department": department,
            "salary": salary,
            "experience": experience,
        }

        employees.append(employee)
        print(f"\n✅ Employee '{name}' added successfully with ID: {employee['id']}")

    except ValueError as e:
        print(f"\n❌ Invalid input: {e}")


def view_all_employees():
    """Display all employees in a formatted table."""
    print("\n--- All Employees ---")

    if not employees:
        print("No employees found.")
        return

    # Header
    print(f"{'ID':<6} {'Name':<20} {'Email':<28} {'Department':<15} {'Salary':>10} {'Exp (yrs)':>10}")
    print("-" * 92)

    for emp in employees:
        print(
            f"{emp['id']:<6} {emp['name']:<20} {emp['email']:<28} "
            f"{emp['department']:<15} {emp['salary']:>10.2f} {emp['experience']:>10}"
        )

    print(f"\nTotal Employees: {len(employees)}")


def search_employee():
    """Search for an employee by their ID."""
    print("\n--- Search Employee by ID ---")
    try:
        emp_id = int(input("Enter Employee ID: "))
        found = None

        for emp in employees:
            if emp["id"] == emp_id:
                found = emp
                break

        if found:
            print(f"\n{'Field':<15} {'Value'}")
            print("-" * 40)
            print(f"{'ID':<15} {found['id']}")
            print(f"{'Name':<15} {found['name']}")
            print(f"{'Email':<15} {found['email']}")
            print(f"{'Department':<15} {found['department']}")
            print(f"{'Salary':<15} {found['salary']:.2f}")
            print(f"{'Experience':<15} {found['experience']} years")
        else:
            print(f"\n⚠️  No employee found with ID: {emp_id}")

    except ValueError:
        print("\n❌ Invalid ID. Please enter a numeric value.")


def update_employee():
    """Update details of an existing employee."""
    print("\n--- Update Employee Details ---")
    try:
        emp_id = int(input("Enter Employee ID to update: "))
        target = None

        for emp in employees:
            if emp["id"] == emp_id:
                target = emp
                break

        if not target:
            print(f"\n⚠️  No employee found with ID: {emp_id}")
            return

        print(f"\nUpdating details for: {target['name']} (ID: {emp_id})")
        print("Press Enter to keep the current value.\n")

        # Name
        new_name = input(f"Name [{target['name']}]: ").strip()
        if new_name:
            target["name"] = new_name

        # Email
        new_email = input(f"Email [{target['email']}]: ").strip()
        if new_email:
            if "@" not in new_email or "." not in new_email:
                raise ValueError("Invalid email format.")
            target["email"] = new_email

        # Department
        new_dept = input(f"Department [{target['department']}]: ").strip()
        if new_dept:
            target["department"] = new_dept

        # Salary
        new_salary = input(f"Salary [{target['salary']}]: ").strip()
        if new_salary:
            salary = float(new_salary)
            if salary < 0:
                raise ValueError("Salary cannot be negative.")
            target["salary"] = salary

        # Experience
        new_exp = input(f"Experience [{target['experience']} yrs]: ").strip()
        if new_exp:
            experience = int(new_exp)
            if experience < 0:
                raise ValueError("Experience cannot be negative.")
            target["experience"] = experience

        print(f"\n✅ Employee ID {emp_id} updated successfully.")

    except ValueError as e:
        print(f"\n❌ Invalid input: {e}")


def delete_employee():
    """Delete an employee record by ID."""
    print("\n--- Delete Employee ---")
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
        target = None

        for emp in employees:
            if emp["id"] == emp_id:
                target = emp
                break

        if not target:
            print(f"\n⚠️  No employee found with ID: {emp_id}")
            return

        confirm = input(f"Are you sure you want to delete '{target['name']}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            employees.remove(target)
            print(f"\n✅ Employee '{target['name']}' (ID: {emp_id}) deleted successfully.")
        else:
            print("\nDeletion cancelled.")

    except ValueError:
        print("\n❌ Invalid ID. Please enter a numeric value.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("    EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Add Employee")
    print("  2. View All Employees")
    print("  3. Search Employee by ID")
    print("  4. Update Employee Details")
    print("  5. Delete Employee")
    print("  6. Exit")
    print("=" * 40)


def main():
    """Main loop for the Employee Management Console."""
    print("\nWelcome to the Employee Management System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("\nThank you for using Employee Management System. Goodbye! 👋\n")
            break
        else:
            print("\n⚠️  Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
