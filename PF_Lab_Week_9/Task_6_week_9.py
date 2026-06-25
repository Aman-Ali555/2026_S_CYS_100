marks = int(input("Enter your marks: "))
total = int(input("Enter total marks: "))
perc = (marks/total)*100
print(perc,"%")
if perc > 90:
    print("A")
elif perc > 85:
    print("-A")
elif perc > 80:
    print("B")
elif perc > 75:
    print("-B")
elif perc > 70:
    print("C")
elif perc > 65:
    print("-C")
elif perc > 60:
    print("D")
elif perc > 55:
    print("-D")
else:
    print("F")
