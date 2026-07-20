import time

score = 0

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A. class", "B. function", "C. def", "D. lambda"],
        "answer": "C"
    },
    {
        "question": "3. Which operator is used for multiplication?",
        "options": ["A. +", "B. -", "C. *", "D. /"],
        "answer": "C"
    }
]

print("------MCQ QUIZ GAME------")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    print("you have 15 seconds to answer...")

    start = time.time()
    print("Start Time:", time.ctime(start))

    start = time.time()
    ans = input("Enter your answer (A/B/C/D): ").upper()

    end = time.time()
    print("End Time:", time.ctime(end))

    taken = end - start
    print("Time Taken:", round(taken, 2), "seconds")


    if end - start > 15 :
        print("Time Over....")
    elif ans == q["answer"] :
        print("Correct")
        score += 1

    else:
        print("Wrong! Correct Answer is", q["answer"])

print("\n------ RESULT ------")
print("Your Score:", score, "/", len(questions))    