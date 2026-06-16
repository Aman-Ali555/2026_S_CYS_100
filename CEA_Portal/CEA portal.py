import time
from operator import index
exam_time = time.strftime("%d/%m/%Y %H:%M:%S")
questions = [{'subject': "Math", "question": "What is the value of π (pi) approximately?", "options": {"A": "3.14", "B": "3.41", "C": "3.12", "D": "3.16"}, "answer": "A"},
             {"subject": "Math", "question": "If x² = 49, what is x?", "options": {"A": "6", "B": "7", "C": "8", "D": "9"}, "answer": "B"},
             {"subject": "Math", "question": "What is the sum of angles in a triangle?", "options": {"A": "90°", "B": "270°", "C": "360°", "D": "180°"}, "answer": "D"},
             {"subject": "Physics", "question": "Unit of force is?","options": {"A": "Joule", "B": "Newton", "C": "Watt", "D": "Pascal"}, "answer": "B"},
             {"subject": "Math", "question": "Value of sin(90°) is?","options": {"A": "0", "B": "0.5", "C": "1", "D": "-1"}, "answer": "C"},
             {"subject": "Computer", "question": "Which gate gives output 1 only when all inputs are 1?", "options": {"A": "OR", "B": "AND", "C": "NOT", "D": "XOR"}, "answer": "B"},
             {"subject": "Physics", "question": "Speed of light is approximately?","options": {"A": "3×10⁶ m/s", "B": "3×10⁸ m/s", "C": "3×10¹⁰ m/s", "D": "3×10⁴ m/s"}, "answer": "B"},
             {"subject": "Math", "question": "What is √144?", "options": {"A": "11", "B": "12", "C": "13", "D": "14"},"answer": "B"},
             {"subject": "Computer", "question": "Which of the following is a primary memory?", "options": {"A": "Hard Disk", "B": "USB", "C": "RAM", "D": "CD"}, "answer": "C"},
             {"subject": "Physics", "question": "SI unit of current is?","options": {"A": "Volt", "B": "Ohm", "C": "Ampere", "D": "Watt"}, "answer": "C"}]
# The list of questions...
answers = []
result = []
percentage = []
grades = []
all_results = []
def numbers():
    num = 0
    print(f"Your answers: {answers}")
    for i in range(len(answers)):
        if answers[i] == questions[i]['answer']:
            num = num + 4
        elif answers[i] == "S":
            num = num + 0
        else:
            num = num - 1
    result.append(num)
    print(f"You got {num} marks.")
def results():
    total = len(questions)*4
    per = 0
    for k in result:
        per = (k/total)*100
    print(f"Your total percentage is: {per:.2f}%")
    if per >= 80:
        print(f"Grade: EXCELLENT")
        grade = "EXCELLENT"
    elif per >= 65:
        print("Grade: GOOD")
        grade = "GOOD"
    elif per >= 50:
        print("Grade: AVERAGE")
        grade = "AVERAGE"
    else:
        print("Grade: BELOW AVERAGE")
        grade = "BELOW AVERAGE"
    percentage.append(per)
    grades.append(grade)
def review():
    while True:
        x = input('To review Your answers Type "REVIEW", To exit Type "EXIT": ').upper()
        if x == "REVIEW":
            print("QUESTION REVIEW")
            for a in range(len(answers)):
                print(f"The Question: {questions[a]['question']}")
                for key, value in questions[a]["options"].items():
                    print(f"{key}. {value}")
                if answers[a] == questions[a]['answer']:
                    print(f"your answer: {questions[a]['answer']} is correct. | +4")
                elif answers[a] == "S":
                    print(f"You skipped the answer. | 0")
                else:
                    print(f"Your answer {answers[a]} is Wrong! | -1")
                    print(f"The correct answer is {questions[a]['answer']}.")
        elif x == "EXIT":
            break
        break
def inst():
    print(f"Total Number of questions to attempt:\t{len(questions)}\t\t|\tTotal Numbers:\t{len(questions) * 4}\nMarking scheme:\n\t\tCorrect Answer | +4 marks\tWrong Answer | -1 mark\tSkip | 0 marks\nInstructions:\n\t\t"
        f"Read the instructions carefully before starting the exam. No advanced calculators are allowed in exam center."
        f"Your mobile phone should be powered off...\nType the option A/B/C/D to answer, type S to skip the question or type SUBMIT to end early.")
    if input("If you have read all the instructions carefully type OK. ").upper() == "OK":
        for j in range(3):
            start = input("To start Type START: ").upper()
            if start == "START":
                print("Your Exams starts now...")
                exam()
                break
            else:
                print("Follow the instructions and try again!!!")
        else:
            print("Something went wrong. Try again!!!")
    else:
        print("Follow the instructions and try again!!!")
        # I am "The Monster".
def exam():
    n = 1
    for i in range(len(questions)):
        print(f"{n}. {questions[i]['question']}")
        for key, value in questions[i]["options"].items():
            print(f"{key}. {value}")
        ans = input("write the Answer: ").upper()
        if ans == "SUBMIT" or ans == "submit":
            break
        answers.append(ans)
        n += 1
def view_que():
    print("=== QUESTION VIEW ===")
    n = 1
    for w in range(len(questions)):
        print(f"Question no.{n}: \t|\tSubject:{questions[w]['subject']}\n{questions[w]['question']}")
        for kiy, val in questions[w]["options"].items():
            print(f"{kiy}. {val}")
        print(f"Correct Answer: {questions[w]['answer']}")
        n+=1
def add_new_que():
    print("=== ADD NEW QUESTIONS ===")
    for m in range(int(input("How many questions do you want to add: "))):
        sub = input("Enter the Subject name: ")
        que = input("Enter your question: ")
        opt = {"A":input("Enter your option: "),"B":input("Enter your option: "),"C":input("Enter your option: "),"D":input("Enter your option: ")}
        corr = input("Enter the correct answer: ")
        temp = {"subject":sub,"question":que,"option":opt,"answer":corr}
        questions.append(temp)
def del_que():
    print("=== DELETE THE QUESTIONS ===")
    x = int(input("Write the question number to delete it: "))
    for i in range(len(questions)):
        if index(i) == x-1:
            del questions[i]
def que_stats():
    print("=== QUESTIONS BANK STATISTICS ===")
    print(f"Total Questions: {len(questions)}")
    math = 0
    c = 0
    p = 0
    e = 0
    for b in questions:
        if b['subject'] == "Math":
            math += 1
        if b['subject'] == "Computer":
            c += 1
        if b['subject'] == "Physics":
            p += 1
        if b['subject'] == "English":
            e += 1
    print(f"Math Questions: {math}")
    print(f"Computer Questions: {c}")
    print(f"Physics Questions: {p}")
    print(f"English Questions: {e}")
def stu_results():
    print("=== VIEW ALL STUDENT RESULTS ===")
    for f in all_results:
        print(f"name: {f['name']}")
        print(f"roll: {f['roll']}")
        print(f"score: {f['score'][0]}")
        print(f"percentage: {f['percentage'][0]}")
        print(f"grades: {f['grades'][0]}")
        print(f"time: {f['time'][0]}")
def detailed_result():
    print("=== VIEW DETAILED RESULT ===")
    if not all_results:
        print("No results available!")
        return
    for i, student in enumerate(all_results):
        print(f"{i+1}. {student['name']} | Roll: {student['roll']}")
    choice = int(input("Enter student number: ")) - 1
    student = all_results[choice]
    print(f"\nName: {student['name']} | Roll: {student['roll']}")
    print(f"Score: {student['score']} | Percentage: {student['percentage']}% | Grade: {student['grades']}")
    print(f"Time: {student['time']}")
def class_statistics():
    print("=== CLASS RESULT STATISTICS ===")
    if not all_results:
        print("No results available!")
        return

    scores = []
    for s in all_results:
        if isinstance(s['score'], list):
            if len(s['score']) > 0:
                scores.append(s['score'][-1])
        else:
            scores.append(s['score'])

    if not scores:
        print("No scores found!")
        return

    grades_list = []
    for s in all_results:
        if isinstance(s['grades'], list):
            if len(s['grades']) > 0:
                grades_list.append(s['grades'][-1])
        else:
            grades_list.append(s['grades'])

    print(f"Highest Score: {max(scores)}")
    print(f"Lowest Score: {min(scores)}")
    print(f"Average Score: {sum(scores) / len(scores):.2f}")
    print(f"Excellent: {grades_list.count('EXCELLENT')}")
    print(f"Good: {grades_list.count('GOOD')}")
    print(f"Average: {grades_list.count('AVERAGE')}")
    print(f"Below Average: {grades_list.count('BELOW AVERAGE')}")
    passed = sum(1 for s in scores if s >= 0)
    print(f"Pass: {passed} | Fail: {len(scores) - passed}")
def stu():
    print('\t\t\t!!! STUDENT EXAM PORTAL !!!')
    print("Enter your Login ID and password.")
    for i in range(3): #This loop will give the protection from the outsider or imposter.
        while True:
            login = input("Enter your login ID: ") #The login ID is student.
            password = input("Enter your password: ") #The password is student123.
            if login == "student" and password == "student123":
                print("\t\t\t**** Login Successful ****")
                name = input("Enter your name: ").upper()
                roll = input("Enter your roll: ")
                inst()
                numbers()
                results()
                review()
                all_results.append({"name": name, "roll": roll, "score": result, "percentage": percentage, "grades": grades,
                     "time": exam_time})
                print("--- THE END OF THE EXAM ---")
                return 
            else :
                print("Either your login ID or password is wrong.\tTry Again!")
            break
    else:
       print("SYSTEM BLOCKED!\nYou can't go further!!!")
            # I am "The Monster".
def admin():
    print("\t\t\t!!! ECAT ADMIN PORTAL !!!")
    print("Enter your Login ID and password.")
    for i in range(3): #This loop will give the protection from the outsider or imposter.
        while True:
            login = input("Enter your login ID: ") #The login ID is ecat_admin
            password = input("Enter your password: ") #The password is ecat@2026
            if login == "ecat_admin" and password == "ecat@2026":
                print("\t\t\t**** Login Successful ****")
                print("\t\t\t=== ADMIN MENU ===")
                print("1. View All Questions\n2. Add New Questions\n3. Delete Questions\n"
                      "4. Question Bank Statistics\n5. View All Student Results\n6. View Detailed Results\n"
                      "7. Class Result Statistics\n8. Logout")
                while True:
                    a = int(input("Enter your choice: "))
                    if a == 1:
                        view_que()
                    elif a == 2:
                        add_new_que()
                    elif a == 3:
                        del_que()
                    elif a == 4:
                        que_stats()
                    elif a == 5:
                        stu_results()
                    elif a == 6:
                        detailed_result()
                    elif a == 7:
                        class_statistics()
                    elif a == 8:
                        return
                    else:
                        print("Invalid Input! Try again!!!")
            else:
                print("Either your login ID or password is wrong.\tTry Again!")
                break
    else:
        print("SYSTEM BLOCKED!.\nYou can't go further.")
        #I am "The Monster".
def main():
    while True: #Main Body
        stat = True
        acc = 0
        print("select one of the portals:\n1. Admin\n2. student\n3. Exit")
        try:
            acc = int(input("Enter 1, 2 or 3: ")) #The user should enter 1,2 or 3 for execution.
        except ValueError:
            print('Invalid choice!!!\tAccess denied...')
            stat = False
        if stat:
            if acc == 1:
                admin() #Enter into the admin portal.
            elif acc == 2:
                stu() #Enter into the student portal.
            elif acc == 3: #Exit the window.
                break
            else:
                print('Invalid choice!!!\tAccess denied...')
                #My signature: I am "The Monster".
main()