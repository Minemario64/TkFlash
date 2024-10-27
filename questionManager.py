from random import *
from customErrors import *

class Question:

    types = [["MC", "Multiple Choice", "mc", "multiple choice"], ["typed", "Typed", "Open Ended", "OE", "oe", "open ended"]]
    modes = ["Multiple Choice", "Typed"]

    def __init__(self, type : str, dbColumnList : list[str], dbCallList : list[int]):
        for mode in range(0, len(self.types)):
            print(mode)
            if type in self.types[mode]:
                self.type = self.modes[mode]
                print(self.type)
                break
            else:
                raise TkFlashError("question error", "Not a valid type")

test = Question(type="MC", dbColumnList=["id", "Spanish", "English", "class_id"], dbCallList=[1, 2])
