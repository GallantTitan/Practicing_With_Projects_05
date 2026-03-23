import json
    
class Quiz():
    def __init__(self, q_m_a):
        self.q_m_a = q_m_a
        self.mcqs = None
        self.ans = None
        self.u_ans = None
        self.false = 0
        self.wrong = {}
        self.wrong_with_roll = {}
        self.str_w_q = []
        self.option_map = {}
        
        
    def quiz(self, roll_no):
        question = self.q_m_a.keys()
        print(list(question)[0])
        for mcqs_ans in self.q_m_a.values():
            for m, a in mcqs_ans.items():
                self.mcqs = m
                self.ans = a
        print(f"a): {self.mcqs[0]}\t\tb): {self.mcqs[1]}\nc): {self.mcqs[2]}\t\td): {self.mcqs[3]}")
        self.option_map = {"a": self.mcqs[0], 
                           "b" : self.mcqs[1], 
                           "c": self.mcqs[2], 
                           "d" : self.mcqs[3]}
        self.u_ans = input("Your answer(a/b/c/d): ").lower()
        selected_answer = self.option_map.get(self.u_ans, None)

        if (selected_answer!=self.ans):
            self.str_w_q = list(question)[0]
            w = {self.str_w_q : self.ans}      
            if roll_no not in self.wrong_with_roll:
                self.wrong_with_roll[roll_no] = {}
            self.wrong_with_roll[roll_no].update(w)

        if selected_answer == self.ans:
            return 1
        else:
            return 0 
        
    def wrong_answers(self, r_no):
        if (r_no not in self.wrong_with_roll):
            return "No data found."
        i = 1
        for q, a in self.wrong_with_roll[r_no].items():
            print(f"Question {i}: {q}")
            print(f"Correct Answer: {a}.")
            i += 1
    
    @staticmethod
    def store_to_json(a_s_i, a_q):  
        all_stu_info = {}
        for i, s_info in enumerate(a_s_i):
            s_stu = {}
            name = (s_info[0])
            roll_no = (s_info[1])
            marks = (s_info[2])
            w_a = {}
            for q_obj in a_q:
                if roll_no in q_obj.wrong_with_roll:
                    w_a.update(q_obj.wrong_with_roll[roll_no])
            if not w_a:
                w_a = "No data found."

            s_stu[f"Student {i+1}"] = {"name" : name, "roll_no" : roll_no, "marks" : marks, "wrong_answers" : w_a}
            all_stu_info.update(s_stu)

        return all_stu_info

# main code

all_questions = []
all_student_info = []

choices = """\n1. Create Quiz
2. Take Quiz
3. Check Result
4. Check Wrong Answers
5. Save File To JSON
6. Exit"""

while True: 
    try:
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
                        option = input(f"MCQ {i+1}: ")
                        mcqs.append(option)
                    answer = input("Answer: ")
                    q_m_a = {question:{tuple(mcqs):answer}}
                    Q_M_A = Quiz(q_m_a)
                    all_questions.append(Q_M_A)
            case 2:
                marks = 0
                s_name = input("Your Name: ")
                s_roll_no = input("Your Roll No: ")
                student_info = [s_name, s_roll_no]
                for i, question in enumerate(all_questions):
                    print(f"\nQuestion {i+1}: ",end="")
                    marks += question.quiz(s_roll_no)
                student_info.append(marks)
                all_student_info.append(student_info)
            case 3:
                check_roll_no = input("Roll No: ")
                for n_r_m_i in all_student_info:
                    if check_roll_no==n_r_m_i[1]:
                        print(f"Name: {n_r_m_i[0]}\t\tRoll NO: {n_r_m_i[1]}")
                        print(f"You Got {n_r_m_i[2]} marks.")
                        break
                else:
                    print("Student not present.")
            case 4:
                check_roll_no = input("Roll No: ")
                print("")
                for s_s_w_a in all_questions:
                    s_s_w_a.wrong_answers(check_roll_no)
            case 5:
                j_file = Quiz.store_to_json(all_student_info, all_questions)
                with open("quiz_result.json", "w") as f:
                    json.dump(j_file, f, indent=4)
            case 6:
                break
    except ValueError:
        print("Please input correct data...")
        continue



