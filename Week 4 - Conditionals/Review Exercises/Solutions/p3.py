def gpa_calculator():
    marks_1 = int(input())
    marks_2 = int(input())
    marks_3 = int(input())

    #data validation
    if marks_1 < 0 or marks_2 < 0 or marks_3 < 0:
        print("Error in Data Entry!")
        return
    if marks_1 > 100 or marks_2 > 100 or marks_3 > 100:
        print("Error in Data Entry!")
        return

    #output grades + calculate total grade points
    gradePoints = 0
    gradePoints += gradePoint(marks_1)
    gradePoints += gradePoint(marks_2)
    gradePoints += gradePoint(marks_3)
    print()

    #calculate gpa
    gpa = round(gradePoints / 3, 2)
    print(gpa)

#outputs the grade for a certain mark value and returns the number of grade points earned
def gradePoint(marks):
    if marks >= 90:
        print("A+", end=" ")
        return 4.00
    elif marks >= 80:
        print("A", end=" ")
        return 3.25
    elif marks >= 70:
        print("B", end=" ")
        return 2.50
    elif marks >= 60:
        print("C", end=" ")
        return 1.75
    elif marks >= 50:
        print("D", end=" ")
        return 1.00
    else:
        print("F", end=" ")
        return 0.00

gpa_calculator()