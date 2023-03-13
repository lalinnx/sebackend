
import docx2txt
from io import BytesIO


class readDoc:
    def __init__(self, file, fileType):
        self.file = file
        self.fileType = fileType

    def getText(self):
        result = ""
        try:
            if (self.fileType == "docx"):
                print("this is docx")
                text = docx2txt.process(BytesIO(self.file.read()))
                print(text)
                for x in text.split("\n"):
                    if x != "":
                        result = result+x

            elif (self.fileType == "doc"):
                print("this is doc")
            elif (self.fileType == "pdf"):
                print("this is pdf")
            return result
        except Exception as e:
            return "These're somethings wrong with "+str(e)
