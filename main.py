name=input("Student name: ")
def mark_grade(mark):
    if mark >90:
        print("Grade A")
    elif mark > 80:
        print("Grade A")
    elif mark > 70:
        print("Grade B")
    elif mark > 60:
        print("Grade C")
    else:
        print("Fail")

print("Enter target grade: ")
target_grade = int(input())
mark = input("Enter actual grade: ")
grade = mark_grade(int(mark))

#extention

if target_grade < int(mark):
    print("you achieved a higher mark than your target grade, well done!")
elif target_grade == int(mark):
    print("You achieved your target grade, good job!")
else:
    print("you did not achieve your target grade, try again next time.")