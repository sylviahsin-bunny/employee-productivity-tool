# Employee Productivity Tool

A Python package that reads employee data, calculates productivity
(tasks ÷ hours), categorises performance, and saves a weekly report.

## How to use
from hr_tools.employee_tools import main
main("employee_data.txt", "weekly_report.txt")

## Input format
The CSV must have the columns: EmpID, Name, HoursWorked, TasksCompleted
