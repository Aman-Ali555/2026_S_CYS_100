s=input("enter anything: ")
if "." in s:
    s=float(s)
    print(type(s))
elif s.isdigit():
    s=int(s)
    print(type(s))
else:
    print(type(s))
