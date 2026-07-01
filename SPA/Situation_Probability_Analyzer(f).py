p_store = []
probable = []
def ins():
    print("It is easy to use, You just need to tell the following things:\n\t\t1. Describe your current situation."
          "\n\t\t2. Describe the relevant past situation."
          "\n\t\t3. how many possibilities do you think can occur for the specific future situation?"
          "\n\t\t4. Describe the possibilities for the future one by one in the shadow of current and the past conditions. (keep it in mind,"
          "to predict the best possibility, you must know that current and the past actions are closely related to the near upcoming future and"
          " the future is directly affected by the current actions. A subtle change in decision or even in mood can change the whole scenario."
          "you must know to connect the two things in mind)"
          "\n\t\t5. After describing the future possibilities you foresee, You must rate them one by one out 10."
          "Then you will get to know the probability % of the given scenarios."
          "\nFor Example: \nPossibility no.1: I think Pakistan will win the match.\nProbability out of 10: 7")
def current():
    while True:
        cur = input("Describe the current situation in 200 words or less :\n")
        if len(cur.split()) > 200:
            print("The words exceeded the limit.")
            print("TRY AGAIN!")
        else:
            return cur
def past():
    while True:
        pst = input("Describe the relevant past situation in 200 words or less :\n")
        if len(pst.split()) > 200:
            print("The words exceeded the limit.")
            print("TRY AGAIN!")
        else:
            return pst
def possibility():
    for i in range(1, int(input("How many possibilities you foresee: ")) + 1):
        while True:
            p = input(f"Describe the Possibility no.{i}: ")
            if len(p.split()) > 100:
                print("The words exceeded the limit.")
                print("TRY AGAIN!")
            else:
                p_store.append(p)
                break
def probability():
    ratings = []
    x = 1
    y = 1
    for j in p_store:
        rate = int(input(f"Rate the Possibility no.{x}:\n\t\t\t\t{j} out of 10: "))
        print("Got it!")
        ratings.append(rate)
        x += 1
    total = sum(ratings)
    for k in range(len(p_store)):
        prob = (ratings[k] / total) * 100
        probable.append(prob)
        print(f"The probability % of {y}:\n====={p_store[k]}====: {probable[k]:.2f} %")
        y += 1
    max_prob = max(probable)
    max_index = probable.index(max_prob)
    print(f"{p_store[max_index]} with {max_prob:.2f}% probability has the highest possibility to happen.")
    print(f'{name}! You must believe on the "{p_store[max_index]}" possibility.')
def store(name, crnt, pasat, p_store, probable):
    filename = f"SPA_{name}.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Name: {name}\n")
        f.write(f"Current Situation: {crnt}\n")
        f.write(f"Past Situation: {pasat}\n")
        f.write("\nPossibilities & Probabilities:\n")
        for i in range(len(p_store)):
            f.write(f"  {i+1}. {p_store[i]} — {probable[i]:.2f}%\n")
        max_prob = max(probable)
        max_index = probable.index(max_prob)
        f.write(f"\nMost Probable: {p_store[max_index]} ({max_prob:.2f}%)\n")
        f.write("=" * 50 + "\n\n")
    print(f"Results saved to {filename}")
def take():
    print("Analyzing the Scenarios...")
    print("Analyzing completed!")
    print(f"So the overall scenario is:\nThe present:\t{crnt}")
    print(f"The past situation is:\t{pasat}")
    print("The Process is starting...")

while True:
    print("=== Welcome to The Situation Probability Analyzer ===")
    name = input("What is your name ? ")
    print(f"Hello dear {name}!\nSo {name} here you can check the best probability of the situations based on your thoughts, current and the "
        f"past conditions")
    a = input("Do you want to play ?(Type Yes or no): ").upper()
    if a == "YES":
        p_store.clear()
        probable.clear()
        print("===== THE INSTRUCTIONS TO FOLLOW =====")
        ins()
        print("===== THE PRESENT SITUATION ANALYZER =====")
        crnt = current()
        print("===== THE PAST SITUATION ANALYZER =====")
        pasat = past()
        take()
        print("===== THE PROCESS START =====")
        print("===== GIVE THE HONEST DESCRIPTION FOR YOUR OWN CONVENIENCE =====")
        possibility()
        print("===== NOW GIVE THE MOST RELEVANT AND CONFIDENT RATINGS FOR EACH POSSIBILITY =====")
        probability()
        store(name, crnt, pasat, p_store, probable)
        print("WARNING:\n\t\tThe app dont predict anything. It is pure calculations made on your provided information.")
        print(f"THANK YOU {name}!!!")
    elif a == "NO":
        print("Goodbye!")
        break
    else :
        print("Error! Wrong Input!")