class QuizApp:
    def __init__(self):
        self.questions = [
            {
                "question": "Who is known as the 'God of Cricket'?",
                "options": ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Brian Lara"],
                "answer": "Sachin Tendulkar"
            },
            {
                "question": "Which country won the first-ever Cricket World Cup in 1975?",
                "options": ["Australia", "India", "West Indies", "England"],
                "answer": "West Indies"
            },
            {
                "question": "What is the highest individual score in an ODI cricket match?",
                "options": ["183", "200", "264", "235"],
                "answer": "264"
            },
            {
                "question": "Who has the most Test wickets in cricket history?",
                "options": ["Shane Warne", "Anil Kumble", "James Anderson", "Muttiah Muralitharan"],
                "answer": "Muttiah Muralitharan"
            },
            {
                "question": "In which year did India win its first Cricket World Cup?",
                "options": ["1983", "2007", "2011", "1975"],
                "answer": "1983"
            },
            {
                "question": "Which cricketer is nicknamed 'The Wall'?",
                "options": ["Rahul Dravid", "Sourav Ganguly", "VVS Laxman", "MS Dhoni"],
                "answer": "Rahul Dravid"
            },
            {
                "question": "Who hit the first six of the 2011 Cricket World Cup final?",
                "options": ["MS Dhoni", "Gautam Gambhir", "Virat Kohli", "Yuvraj Singh"],
                "answer": "MS Dhoni"
            },
            {
                "question": "Which bowler has the best bowling figures in a single innings in Test cricket?",
                "options": ["Jim Laker", "Anil Kumble", "Shane Warne", "Dale Steyn"],
                "answer": "Jim Laker"
            },
            {
                "question": "What is the term used for scoring 100 runs in cricket?",
                "options": ["Century", "Half-century", "Double century", "Triple century"],
                "answer": "Century"
            },
            {
                "question": "Who was the captain of the Indian team when they won the 2007 ICC World Twenty20?",
                "options": ["MS Dhoni", "Sourav Ganguly", "Rahul Dravid", "Virat Kohli"],
                "answer": "MS Dhoni"
            }
        ]
        self.score = 0

    def display_question(self, question_data):
        print("\n" + question_data["question"])
        for i, option in enumerate(question_data["options"], 1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the number): ")
        return user_answer

    def check_answer(self, user_answer, correct_answer, options):
        try:
            user_choice = options[int(user_answer) - 1]
            if user_choice == correct_answer:
                print("Correct!")
                return True
            else:
                print(f"Wrong! The correct answer is: {correct_answer}")
                return False
        except (ValueError, IndexError):
            print("Invalid input! Please enter a valid number.")
            return False

    def run_quiz(self):
        print("Welcome to the Cricket Quiz Application!")
        for question_data in self.questions:
            user_answer = self.display_question(question_data)
            if self.check_answer(user_answer, question_data["answer"], question_data["options"]):
                self.score += 1
            print(f"Your current score: {self.score}/{len(self.questions)}")

        print("\nQuiz Completed!")
        print(f"Your final score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You got all the answers correct!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You did well.")
        else:
            print("Better luck next time!")

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.run_quiz()