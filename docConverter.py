### Testing


import docx2txt as doc
import pypandoc as py

docFileName = 'Adavantech_Matthew Williams_IT TSS.docx'

output = py.convert_file(docFilename, 'plain', outputfile="somefile.txt")
assert output == ""