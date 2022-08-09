import PyPDF2

a = PyPDF2.PdfFileReader('Application form Amabassador programme.pdf')

str = ""

for i in range(1,10):
    str += a.getPage(i).extract_text()

with open ("text.txt", "w") as f:
    f.write(str)




