def print_grade(mark):
    if mark >= 80:
        print("HD")
    if (mark >= 70) and (mark < 80):
        print("D")
    if (mark >= 60) and (mark < 70):
        print("Cr")
    if (mark >= 50) and (mark < 60):
        print("P")
    if mark < 50:
        print("Fail")

print_grade(90)
print_grade(75)
print_grade(65)
print_grade(55)
print_grade(45)
print_grade(200)



def print_grade2(mark):
    if mark >= 80:
        print("HD")
    elif mark >= 70:
        print("D")
    elif mark >= 60:
        print("Cr")
    elif mark >= 50:
        print("P")
    else:
        print("Fail")
        
print("\n")
print_grade2(90)
print_grade2(75)
print_grade2(65)
print_grade2(55)
print_grade2(45)
print_grade2(200)