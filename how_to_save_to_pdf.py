#For PDF
# from reportlab.pdfgen import canvas 
# from reportlab.pdfbase.ttfonts import TTFont 
# from reportlab.pdfbase import pdfmetrics 
# from reportlab.lib import colors 

# # https://www.geeksforgeeks.org/creating-pdf-documents-with-python/
# # https://code-maven.com/create-multipage-pdf-file-in-python
# fileName = 'sample.pdf'
# documentTitle = 'sample'
# title = 'Stocks Summary'
# # creating a pdf object 
# pdf = canvas.Canvas(fileName) 
  
# # setting the title of the document 
# pdf.setTitle(documentTitle) 
  
# # registering a external font in python 
# # pdfmetrics.registerFont( 
# #     TTFont('abc', 'SakBunderan.ttf') 
# # ) 
  
# # creating the title by setting it's font  
# # and putting it on the canvas 
# pdf.setFont('Courier', 36) 
# pdf.drawCentredString(300, 800, title) 
  
# # creating the subtitle by setting it's font,  
# # colour and putting it on the canvas 
# # pdf.setFillColorRGB(0, 0, 255) 
# # pdf.setFont("Courier-Bold", 24) 
# # pdf.drawCentredString(290, 720, subTitle) 
  
# # drawing a line 
# # pdf.line(30, 710, 550, 710) 
  
# # creating a multiline text using  
# # textline and for loop 
# beginTextX = 30
# beginTextY = 770
# fontSize = 12
# text = pdf.beginText(beginTextX, beginTextY) 
# text.setFont("Courier", fontSize) 
# color = None
# counter = 0
# for key, value in symbols_curr_vs_last_perc_sorted.items():
#     color = colors.red if value < 0 else colors.green 
#     text.setFillColor(color)
#     text.textLine(f"{key} -> {value}")
#     counter += 1
#     if counter % 48 == 0:
#         pdf.drawText(text)
#         pdf.showPage()
#         text = pdf.beginText(beginTextX, beginTextY)
#         text.setFont("Courier", fontSize) 

# text.setFillColor(colors.black)
# text.textLine("sybomls_curr_price_failed")
# text.textLine(','.join(sybomls_curr_price_failed))
# text.textLine("sybomls_last_price_failed")
# text.textLine(','.join(sybomls_last_price_failed))
# pdf.drawText(text) 
  
# # drawing a image at the  
# # specified (x.y) position 
# # pdf.drawInlineImage(image, 130, 400) 
  
# # saving the pdf 
# pdf.save() 