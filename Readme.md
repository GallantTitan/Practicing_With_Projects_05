# 📝 CLI Quiz App in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)

A **command-line quiz application** in Python that allows users to **create quizzes, take quizzes, track results, and save them in JSON format**.
Built using **Object-Oriented Programming (OOP)** and Python’s built-in **JSON module**.

---

## ✨ Features

| Feature               | Description                                                     |
| --------------------- | --------------------------------------------------------------- |
| ✅ Create Quiz         | Add multiple-choice questions (MCQs) dynamically                |
| ✅ Take Quiz           | Students can attempt quizzes and get scores automatically       |
| ✅ Track Wrong Answers | Stores wrong answers per student roll number                    |
| ✅ Check Results       | Retrieve individual student marks                               |
| ✅ Save to JSON        | Export all student data and wrong answers to `quiz_result.json` |
| ✅ Interactive CLI     | Easy-to-use command-line interface                              |

---

## 🛠 Requirements

* Python 3.x
* No external libraries (uses only built-in `json` module)

---

## 🚀 How to Use

1. Clone the repository:

```bash
git clone GallantTitan/Practicing_With_Projects_05
cd Practicing_With_Projects_05
```

2. Run the application:

```bash
python 14_quiz_app_cli.py
```

3. Choose from the menu:

```
1️⃣ Create Quiz
2️⃣ Take Quiz
3️⃣ Check Result
4️⃣ Check Wrong Answers
5️⃣ Save File To JSON
6️⃣ Exit
```

4. Follow prompts to:

   * Enter questions, options, and correct answers
   * Take quizzes by entering **name** and **roll number**
   * Check individual results or wrong answers
   * Save all results to a **JSON file**

---

## 🗂 Example JSON Output

```json
{
    "Student 1": {
        "name": "Alice",
        "roll_no": "f23",
        "marks": 2,
        "wrong_answers": {
            "What is Python?": "Programming Language"
        }
    },
    "Student 2": {
        "name": "Bob",
        "roll_no": "f24",
        "marks": 3,
        "wrong_answers": "No data found."
    }
}
```

---

## 🧩 How It Works

* **`Quiz` class** handles:

  * Questions, correct answers, and user answers
  * Tracking wrong answers per student roll number
* **CLI menu** allows creating quizzes, taking quizzes, and checking results
* **Data storage**:

  * Keeps all student info and wrong answers
  * Exports to JSON for permanent storage

---

## 🔮 Future Improvements

* ⏱ Add a timer for each question
* 🎯 Support multiple quizzes at once
* 🔢 Add difficulty levels for questions
* 🗄 Store quizzes and student data permanently in a database

---

## 👨‍💻 Author

**Khubayb Saleem**

---

## ⭐ Note

This project is part of my learning journey toward becoming a **Software Engineer** and **AI Developer**.

---
