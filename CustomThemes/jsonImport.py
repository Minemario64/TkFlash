from json import *

def importFromJSON(filename : str) -> dict:
    with open(filename, "r") as file:
        return load(file)

def exportToJSON(dict : dict, filepath : str) -> None:
    with open(filepath, "w") as file:
        dump(dict, file)