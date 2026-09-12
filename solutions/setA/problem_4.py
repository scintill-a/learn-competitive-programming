grade = float(input(""))

if (grade <= 100 and grade >= 90):
    print("Grade: A (Excellent)")
elif (grade < 90 and grade >= 80):
    print("Grade: B (Good)")
elif (grade < 80 and grade >= 70):
    print("Grade: C (Satisfactory)")
elif (grade >= 60 and grade < 70):
    print("Grade: D (Needs Improvement)")
elif (grade >= 0 and grade < 60):
    print("Grade: F (Fail)")
else:
    print("Invalid Score")


