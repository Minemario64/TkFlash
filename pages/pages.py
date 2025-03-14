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

    def change_menu_colors(menu):
        menu.configure(background='#292929', foreground='white', activebackground="#393939", activeforeground="white")

        for index in range(menu.index('end')):
            menu.entryconfig(index, background='#292929', foreground='white', activebackground="#393939", activeforeground="white")

    label = ttk.Label(self.root, text="Select Flashcard Pack", style='TLabel').pack(pady=10)
    spacer_1 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=20)
    menu = OptionMenu(self.root, menu_var, *menu_options, command=export_menu)
    menu.config(bg="#191919", fg="#FFF", borderwidth=0, highlightthickness=0, activebackground="#292929", activeforeground="#FFF")
    menu.pack(pady=10)
    menu.bind("<Map>", lambda event: change_menu_colors(event.widget.nametowidget(event.widget['menu'])))
    spacer_2 = ttk.Label(self.root, text="|", foreground="#191919").pack(pady=10)

    buttonStyle = ttk.Style()
    buttonStyle.configure('SButton.TButton', foreground="black", background="#191919")

    start_button = ttk.Button(self.root, text="Start A Training Session", command=lambda: start_questions(self=self), style='SButton.TButton')
    start_button.pack(pady=20)

def SingleQuestionResults(self, timerResults : SpeedrunTimer, results : list):
    if results[0] == "Correct":
        bg = "#00DF51"
    elif results[0] == "Incorrect":
        bg = "#D8002A"
        fg = "#FFC9C9"
    self.root.config(background=bg)
    loadfont("Lemon Fruit.otf")
    textStyle = ttk.Style()
    textStyle.configure("ParaText.TLabel", font=('Lemon Fruit', 40), foreground="white", background=bg)


    resultLabel = ttk.Label(self.root, text=f"\n{results[0]}", style="ParaText.TLabel")
    resultLabel.pack(pady=5)
    if results[0] == "Incorrect":
        answerStyle = ttk.Style()
        answerStyle.configure("Answer.TLabel", font=('Lemon Fruit', 20), foreground=fg, background=bg)

        answerLabel = ttk.Label(self.root, text=results[1], style="Answer.TLabel")
        answerLabel.pack(pady=0)

        actualLabel = Label(self.root, text=results[2], font=("Lemon Fruit", 32), fg="#FFEFEF", bg=bg)
        actualLabel.pack(pady=20)

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
            print(ShuffledAnswers[var.get()])
            if ShuffledAnswers[var.get()] == questionManager.answers[0]:
                self.change_pages("SingleQuestionResults", questionTimer, ["Correct", ShuffledAnswers[var.get()], questionManager.answers[0]])
            else:
                self.change_pages("SingleQuestionResults", questionTimer, ["Incorrect", ShuffledAnswers[var.get()], questionManager.answers[0]])

        for answer in range(0, len(ShuffledAnswers)):
            MCAnswers[f"a{{answer}}"] = Radiobutton(self.root, text=ShuffledAnswers[answer], background="#191919", fg="white", variable=MCAnswers["var"], value=answer, command=lambda: MCAnswerSubmission(MCAnswers["var"]))
            MCAnswers[f"a{{answer}}"].pack(pady=10)
        print(MCAnswers)
        questionTimer = SpeedrunTimer("mins:secs", "normal")
        questionTimer.start()