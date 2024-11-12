from jsonImport import *
import re

class Theme:

    def __init__(self, filepath : str):
        self.filepath = filepath
        self.rawJson = importFromJSON(filepath)
        self.parseTheme()

    def parseTheme(self):
        if self.rawJson["Main_bgColor"] or self.rawJson["Main_backgroundColor"]:
            hex_pattern = re.compile(r"^#([0-9A-Fa-f]{3}){1,2}$")
            if hex_pattern.match(self.rawJson["Main_bgColor"]) or hex_pattern.match(self.rawJson["Main_backgroundColor"]):
                self.bg = self.rawJson["Main_bgColor"] or self.rawJson["Main_backgroundColor"]
                print(f"{self.bg} is now official.")
            else:
                print(f"{self.bg} is not a hex value.")

        if self.rawJson["Main_fgColor"] or self.rawJson["Main_foregroundColor"]:
            hex_pattern = re.compile(r"^#([0-9A-Fa-f]{3}){1,2}$")
            if hex_pattern.match(self.rawJson["Main_fgColor"]) or hex_pattern.match(self.rawJson["Main_foregroundColor"]):
                self.fg = self.rawJson["Main_fgColor"] or self.rawJson["Main_foregroundColor"]
                print(f"{self.fg} is now official.")
            else:
                print(f"{self.fg} is not a hex value.")

        if self.rawJson["fontStyles"]:
            fontStyles = []
            for key in self.rawJson["fontStyles"]:
                fontStyles.append(key)
            if len(fontStyles) == 0:
                print("Warning : You have nothing in the key 'fontStyles', this will decrease your performance")
            self.fontStyles = {}
            for style in fontStyles:
                self.fontStyles[style] = {}

                if self.rawJson["fontStyles"][style]["fontpath"]:
                    self.fontStyles[style]["fontpath"] = self.rawJson["fontStyles"][style]["fontpath"]
                    print(f"({self.fontStyles[style]["fontpath"]} : fontpath) is now official.")

                if self.rawJson["fontStyles"][style]["fontName"]:
                    self.fontStyles[style]["fontName"] = self.rawJson["fontStyles"][style]["fontName"]
                    print(f"({self.fontStyles[style]["fontName"]} : fontName) is now official.")

                if self.rawJson["fontStyles"][style]["fontSize"]:
                    self.fontStyles[style]["fontSize"] = self.rawJson["fontStyles"][style]["fontSize"]
                    print(f"({self.fontStyles[style]["fontSize"]} : fontSize) is now official.")

test = Theme("test.json")