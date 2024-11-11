from ast import arg
from tkinter import *
from PIL import ImageTk,Image
from questions.questionManager import *
from questions.timeManager import *
from tkinter import ttk
from getfile import *
from fontLoader import *

def start_questions(self):
    test = Question(type="MC", dbColumnList=["id", "Spanish", "English", "class_id"], dbCallList=[1, 2], db="translates.db", dbTable="translates", class_id=0)
    test.create_question()
    self.change_pages("QuestionPage", test)

def cardselect(self):
    loadfont("Lemon Fruit.otf")
    h1style = ttk.Style()
    h1style.configure('TLabel', font=('Lemon Fruit', 32), foreground="white", background="#191919")

    menu_var = StringVar(value="Select a Flashcard Pack")
    menu_options = ["PS - Element Orders", "ESP - Verbs"]

    def export_menu(menu_var):
        print(menu_var)

    label = ttk.Label(self.root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=20)
    menu = OptionMenu(self.root, menu_var, *menu_options, command=export_menu).pack(pady=10)
    spacer_2 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=10)

    start_button = ttk.Button(self.root, text="Start A Training Session", command=lambda: start_questions(self=self)).pack()

def SingleQuestionResults(self, timerResults : SpeedrunTimer, results : dict):
    self.root.config(background="#00E100")
    loadfont("Sweety Rasty.otf")
    textStyle = ttk.Style()
    textStyle.configure("paraText", font=('Lemon Fruit', 20), foreground="white", background="#00E100")

    resultLabel = ttk.Label(self.root, text="Test", style="paraText")
    resultLabel.pack(pady=30, fill=X)

def QuestionPage(self, questionManager : Question):
    loadfont("Lemon Fruit.otf")
    questionStyle = ttk.Style()
    questionStyle.configure('TLabel', font=('Lemon Fruit', 28), foreground="white", background="#191919")

    question = ttk.Label(self.root, text=questionManager.question, style='TLabel').pack(pady=10)
    if questionManager.type == "Multiple Choice":
        mcFrame = ttk.Frame(self.root)
        mcFrame.pack(pady=50, padx=20)
        MCAnswers = {}
        MCAnswers["var"] = IntVar(name="MCvar.INT")
        ShuffledAnswers = sample(questionManager.answers, len(questionManager.answers))

        def MCAnswerSubmission(var : IntVar):
            questionTimer.stop()
            time = questionTimer.get_time(3, "")
            if ShuffledAnswers[var.get()] == questionManager.answers[0]:
                self.change_pages("SingleQuestionResults", questionTimer, f"Correct")
            else:
                self.change_pages("SingleQuestionResults", questionTimer, f"Incorrect")

        for answer in range(0, len(ShuffledAnswers)):
            MCAnswers[f"a{{answer}}"] = Radiobutton(self.root, text=questionManager.answers[answer], background="#191919", fg="white", variable=MCAnswers["var"], value=answer, command=lambda: MCAnswerSubmission(MCAnswers["var"]))
            MCAnswers[f"a{{answer}}"].pack(pady=10)
        print(MCAnswers)
        questionTimer = SpeedrunTimer("mins:secs", "normal")
        questionTimer.start()