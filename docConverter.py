#### Working Converter

import docx2txt as doc # pip install aspose-words
import pypandoc as py # pip install aspose-words
import aspose.words as aw # pip install aspose-words


# Run this code: 
# Takes a Word Document passed in
# Converts into .txt file as desired name
# Saves txt file into same directory 
def convertDoc(wordDoc):
    doc = aw.Document(wordDoc)
    doc.save("ResumeOutput.txt")
    
convertDoc('ResumeDocs\Matthew_Williams.docx')
convertDoc('ResumeDocs\Andrew_Chang.docx')  ### This function call replaces ResumeOutput that holds Matthew's content