from PyPDF2 import PdfMerger

list_of_pdf = ["AGAAAAAAAAAIN","NEWPDFYEAAAAAHHHH.pdf"]
PdfMerger()
for pdf in list_of_pdf:
    PdfMerger().append(pdf)
PdfMerger().write("HAHAHHAHAHA")
PdfMerger().close()