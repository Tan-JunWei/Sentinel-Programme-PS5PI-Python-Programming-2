def calculate_average(grades):
    total = 0
    for grade in grades: 
        total += grade
    average = total / (len(grades)) 
    return average

def determine_status(average): 
    if average >= 60:
        return "Pass" 
    else:
        return "Fail"

def analyze_grades(student_grades):
    for student, grades in student_grades.items():
        average = calculate_average(grades)
        status = determine_status(average) 
        print(f"{student}: Average = {average}, Status = {status}")

# Sample student grades data
student_grades = {
    "Alice": [85, 90, 92, 88],
    "Bob": [75, 80, 85, 82],
    "Charlie": [70, 75, 80, 75],
    "David": [60, 65, 55, 62]
}

analyze_grades(student_grades)
