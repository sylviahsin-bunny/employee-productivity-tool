import csv


def read_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def calculate_productivity(hours, tasks):
    if hours == 0:
        return 0.0
    return tasks / hours


def categorize_employee(prod, sat_threshold=0.5, high_threshold=0.8):
    if prod >= high_threshold:
        return "high performer"
    elif prod >= sat_threshold:
        return "Satisfactory"
    else:
        return "Require further assistance"


def display_all(data):
    print("--- All Employees ---")
    for emp in data:
        score = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
        category = categorize_employee(score)
        print(f"{emp['Name']:<6} | {score:.2f} | {category}")


def write_summary(filename, data):
    with open(filename, 'w') as file:
        file.write("EmpID,Name,Productivity,Category\n")
        for emp in data:
            score = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
            category = categorize_employee(score)
            file.write(f"{emp['EmpID']},{emp['Name']},{score:.2f},{category}\n")


def find_extremes(data):
    print("\n--- Performance Extremes ---")
    for emp in data:
        emp["Productivity"] = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
    top = max(data, key=lambda emp: emp["Productivity"])
    lowest = min(data, key=lambda emp: emp["Productivity"])
    print(f"Top Performer: {top['Name']} ({top['Productivity']:.2f})")
    print(f"Lowest Performer: {lowest['Name']} ({lowest['Productivity']:.2f})")


def team_summary(data):
    print("\n----Team Summary-----")
    total = 0
    high = 0
    satisfactory = 0
    assistance = 0
    for emp in data:
        score = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
        total = total + score
        category = categorize_employee(score)
        if category == "high performer":
            high = high + 1
        elif category == "Satisfactory":
            satisfactory = satisfactory + 1
        else:
            assistance = assistance + 1
    average = total / len(data)
    print(f"Average Productivity: {average:.2f}")
    print(f"High Performers: {high}")
    print(f"Satisfactory: {satisfactory}")
    print(f"Require Further Assistance: {assistance}")


def sort_by_productivity(data, descending=True):
    print("\n----Ranked Employees---")
    for emp in data:
        emp["Productivity"] = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
    ranked = sorted(data, key=lambda emp: emp["Productivity"], reverse=descending)
    print("Ranked Employees:")
    for emp in ranked:
        score = calculate_productivity(int(emp["HoursWorked"]), int(emp["TasksCompleted"]))
        category = categorize_employee(score)
        print(f"{emp['Name']:<6} | {score:.2f} | {category}")




def main(input_file, output_file):
    employees = read_data(input_file)
    display_all(employees)
    find_extremes(employees)
    team_summary(employees)
    sort_by_productivity(employees)
    write_summary(output_file, employees)
    print(f"\nReport saved to {output_file}")


if __name__ == "__main__":
    input_file = input("Data file name: ")
    output_file = input("Report name: ")
    main(input_file, output_file)
