from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

pdf_files = ['pdf_files/fluturas.pdf']

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("merged_1_page.pdf")
merger.close