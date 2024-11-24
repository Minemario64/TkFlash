from random import *
from customerrors import *
from getfile import *

class Question:

    types = [["MC", "Multiple Choice", "mc", "multiple choice"], ["typed", "Typed", "Open Ended", "OE", "oe", "open ended"]]
    modes = ["Multiple Choice", "Typed"]

    def __init__(self, type : str, dbColumnList : list[str], dbCallList : list[int], db : str, dbTable : str, class_id : int):
        self.dbColumnList = dbColumnList
        self.db = db
        self.class_id = class_id
        self.dbTable = dbTable
        self.dbCallList = dbCallList
        for mode in range(0, len(self.types)):
            if type in self.types[mode]:
                self.type = self.modes[mode]
                break
            else:
                raise TkFlashError("question error", "Not a valid type")

    def create_question(self):
        query = tkflash_query_db(self.db, dbTable=self.dbTable, dbColumnList=self.dbColumnList, dbCallList=self.dbCallList, allColumns=False, class_id=self.class_id)
        choice = randint(0, len(query) - 1)
        choices = []
        for i in range(0, len(query)):
            choices.append(i)
        self.question = query[choice][0]
        if self.type == "Multiple Choice":
            numOfAnswers = randint(2, 4)
            self.answers = [query[choice][1]]
            choices.remove(choice)
            for _ in range(1, numOfAnswers):
                while not choice in choices:
                    choice = randint(0, len(query) - 1)
                choices.remove(choice)
                self.answers.append(query[choice][1])