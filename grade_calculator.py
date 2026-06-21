def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep it up! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Keep practicing and improving! 💪"
    else:
        return "F", "Don't give up! Work harder and try again! 📚"

name = input("Enter student name: ")

while True:
    marks = int(input("Enter marks (0-100): "))

    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")

grade, message = calculate_grade(marks)

print("\n RESULT FOR", name.upper())
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)
