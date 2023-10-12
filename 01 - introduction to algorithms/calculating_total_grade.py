"""
simple program to calculate the total grade of a student

formula = 40% * x + 30% * y + 30% * z
x = assignment grade
y = midterm grade
z = final exam grade
"""
x = int(input("Assignment grade : "))
y = int(input("Midterm grade    : "))
z = int(input("Final exam grade : "))

finalGrade = 0.4 * x + 0.3 * y + 0.3 * z

print("\nFinal grade = %.2f"%finalGrade)
