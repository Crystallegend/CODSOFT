from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkCheckBox, set_appearance_mode
import tkinter as tk

questions = [
    {"question": "What is the process by which plants convert sunlight into energy?", "choices": ["Osmosis", "Cellular Respiration", "Diffusion", "Photosynthesis"], "correct_answer": 3},
    {"question": "What are the three primary colors of light?", "choices": ["Red, Green, Blue", "Red, White, Brown", "Blue, Grey, Black", "Yellow, Green, Orange"], "correct_answer": 0},
    {"question": "What is the theory that explains the origin of the universe?", "choices": ["Steady State Theory", "Black Hole Theory", "Big Bang Theory", "Pulsating Universe Theory"], "correct_answer": 2},
    {"question": "What historical event is marked by the fall of the Berlin Wall?", "choices": ["World War I", "The Cold War", "World War II", "The French Revolution"], "correct_answer": 1},
    {"question": "Which month has the fewest number of days?", "choices": ["January", "February", "March", "April"], "correct_answer": 1},
    {"question": "Who wrote the famous novel 'Pride and Prejudice'?", "choices": ["Jane Austen", "Charles Dickens", "William Shakespeare", "Charlotte Brontë"], "correct_answer": 0},
    {"question": "If you see a stop sign at an intersection, what should you do?", "choices": ["Continue at the same speed", "Speed up", "Slow Down", "Completely Stop"], "correct_answer": 2},
    {"question": "If you flip a fair coin, what is the probability of getting heads?", "choices": ["0%", "25%", "50%", "75%"], "correct_answer": 2},
    {"question": "A group of sheep is called a flock. What is a group of cows called?", "choices": ["Pack", "Colony", "School", "Herd"], "correct_answer": 3},
    {"question": "The opposite of 'hot' is...", "choices": ["Warm", "Cold", "Lukewarm", "Tepid"], "correct_answer": 1}
]
current_question = 0
score = 0

class QuizApp(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Quiz App")
        self.master.geometry("600x300")

        self.init_ui()

    def init_ui(self):
        self.welcome_label = CTkLabel(master=self, text="Welcome to the Quiz App!\n\nRead the rules carefully before starting:\n- Select all the correct answers for each question.\n- Click 'Next' to proceed to the next question.\n\nAre you ready to begin?", justify=tk.LEFT)
        self.welcome_label.pack(pady=20)

        self.start_button = CTkButton(master=self, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.welcome_label.destroy()
        self.start_button.destroy()

        self.question_label = CTkLabel(master=self, text=f"Question {current_question + 1}/{len(questions)}:")
        self.question_label.pack(pady=10)

        self.display_question()

    def display_question(self):
        self.answer_vars = []
        self.answer_buttons = []

        current_question_data = questions[current_question]
        self.question_label.configure(text=f"Question {current_question + 1}/{len(questions)}: {current_question_data['question']}")

        for i, choice in enumerate(current_question_data["choices"]):
            answer_var = tk.BooleanVar(value=False)
            self.answer_vars.append(answer_var)
            answer_button = CTkCheckBox(master=self, text=choice, variable=answer_var)
            answer_button.pack()
            self.answer_buttons.append(answer_button)

        self.next_button = CTkButton(master=self, text="Next", command=self.check_answer)
        self.next_button.pack(pady=10)

    def check_answer(self):
        global current_question, score

        if sum(1 for value in self.answer_vars if value.get()) != 1:
            self.show_message("Please select only one box")
            return

        selected_answer = 0
        for i, answer_var in enumerate(self.answer_vars):
            if answer_var.get():
                selected_answer = i

        correct_answer = questions[current_question]["correct_answer"]

        if selected_answer == correct_answer:
            self.show_message("Correct! You got the correct answer.")
            score += 1
        else:
            correct_answer = questions[current_question]["choices"][questions[current_question]["correct_answer"]]
            self.show_message(f"Incorrect. The correct answer is: {correct_answer}.")

        for button in self.answer_buttons:
            button.destroy()
        self.next_button.destroy()

        current_question += 1
        if current_question == len(questions):
            self.show_results()
        else:
            self.display_question()

    def show_message(self, message):
        message_label = CTkLabel(master=self, text=message)
        message_label.pack(pady=10, side=tk.BOTTOM)
        message_label.after(2000, message_label.destroy)

    def show_results(self):
        self.question_label.destroy()

        self.result_label = CTkLabel(master=self, text=f"You scored {score} out of {len(questions)} questions correctly.")
        self.result_label.pack(pady=20)

        self.play_again_button = CTkButton(master=self, text="Play Again", command=self.restart_quiz)
        self.play_again_button.pack(pady=10)

    def restart_quiz(self):
        global current_question, score
        current_question = 0
        score = 0
        self.result_label.destroy()  # Remove "You scored..." label
        self.play_again_button.destroy()  # Remove "Play Again" button
        self.init_ui()  # Re-initialize UI for a new quiz

# Run the main loop
set_appearance_mode("dark")
root = CTk()
app = QuizApp(root)
app.pack(padx=10, pady=10)
root.mainloop()