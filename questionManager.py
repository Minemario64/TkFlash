from random import *
from customErrors import *
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
                print(self.type)
                break
            else:
                raise TkFlashError("question error", "Not a valid type")

    def create_question(self):
        query = tkflash_query_db(self.db, dbTable=self.dbTable, dbColumnList=self.dbColumnList, dbCallList=self.dbCallList, allColumns=False, class_id=self.class_id)
        print(query)
        choice = randint(0, len(query) - 1)
        self.question = query[choice][0]
        print(self.question)
        if self.type == "Multiple Choice":
            self.answers = [query[choice][1]]
        print(self.answers)

test = Question(type="MC", dbColumnList=["id", "Spanish", "English", "class_id"], dbCallList=[1, 2], db="translates.db", dbTable="translates", class_id=0)
test.create_question()
