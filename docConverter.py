#### Working Converter

import docx2txt as doc # pip install aspose-words
import pypandoc as py # pip install aspose-words
import aspose.words as aw # pip install aspose-words


# Run this code: 
# Takes a Word Document passed in
# Converts into .txt file as desired name
# Saves txt file into same directory 
doc = aw.Document("ResumeDocs\Andrew_Chang.docx")
doc.save("AndrewResume.txt")