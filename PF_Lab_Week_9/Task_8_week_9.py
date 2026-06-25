num_stu = int(input("Enter number of students: "))
n = 1
while n <= num_stu:
    name = input("Enter Student Name: ")
    roll_no = (input("Enter the Student Roll no: "))
    obt_marks = int(input("Enter Obtained marks: "))
    total = 300
    perc = (obt_marks/total)*100
    print(f"Student Name: {name}")
    print(f"Roll No: {roll_no}")
    print(f"Total Marks: {total}")
    print(perc,"%")
    if perc > 90:
        print("Grade: A")
    elif perc > 85:
        print("Grade: -A")
    elif perc > 80:
        print("Grade: B")
    elif perc > 75:
        print("Grade: -B")
    elif perc > 70:
        print("Grade: C")
    elif perc > 65:
        print("Grade: -C")
    elif perc > 60:
        print("Grade: D")
    elif perc > 55:
        print("Grade: -D")
    else:
        print("Grade: F")
    n=n+1


