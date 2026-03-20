import random

class Questions_MCQs_Answers:
    def __init__(self, q_m_a, total):
        self.q_m_a = q_m_a
        self.total = total
        self.mcqs = None
        self.ans = None
        self.u_ans = None
        self.correct = 0
        self.false = 0


class Quiz(Questions_MCQs_Answers):
    def quiz(self):
        print(list(self.q_m_a.keys())[0])
        for mcqs_ans in self.q_m_a.values():
            for m, a in mcqs_ans.items():
                self.mcqs = m
                self.ans = a
        print(f"a): {self.mcqs[0]}\t\tb): {self.mcqs[1]}\nc): {self.mcqs[2]}\t\td): {self.mcqs[3]}")
        self.u_ans = input("Your answer: ")
        if (self.u_ans==self.ans):
            self.correct += 1
        else:
            self.false += 1


class Student_Result(Quiz):

    def check_marks(self):
        global marks 
        marks = 14
        
    def wrong_questions(self):
        if (self.u_ans!=self.ans):
            print(f"Question: {list(self.q_m_a.keys())[0]}")
            print(f"Correct Answer: {self.ans}.")
        






#case 1:

all_questions = []
all_student_info = []

choices = """\n1. Create Quiz
2. Take Quiz
3. Check Result
6. Exit"""

while True: 
    user_choice = int(input(f"{choices}\nYour Choice: "))
    print()
    match user_choice:
        case 1:
            que_no = int(input("How many questions you wanna add: "))
            print(f"\nPlease input your Data for {que_no} Quetions...")
            for x in range(que_no):
                question = input(f"Question {x+1}: ")
                mcqs = []
                for i in range(4):
                    x = input(f"MCQ {i+1}: ")
                    mcqs.append(x)
                answer = input("Answer: ")
                q_m_a = {question:{tuple(mcqs):answer}}
                Q_M_A = Quiz(q_m_a, que_no)
                all_questions.append(Q_M_A)
        case 2:
            s_name = input("Your Name: ")
            s_roll_no = input("Your Roll No: ")
            test_unique_id = random.randint(1111,9999)
            student_info = [s_name, s_roll_no]
            for i, question in enumerate(all_questions):
                print(f"\nQuestion {i+1}: ",end="")
                question.quiz()
        case 3:
            print(f"You Got {marks} marks.")
            if marks!=que_no:
                print("Wrong Answers...")
                for i, question in enumerate(all_questions):
                    question.wrong_questions()
                    

        case 6:
            break




