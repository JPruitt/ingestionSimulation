# Python libraries
from fpdf import FPDF
import os

# Local Libraries
from helperFunctions import get_current_date

pageWidth = 210
pageHeight = 297

filePathPrefix = "./capDevDataIngestSim"
#filePathPrefix = "."

reportDate = get_current_date() 

def getFileName(fileName):
   global filePrefix
   filePrefix = fileName+"_"
   create_analytics_report(reportDate, fileName+".pdf")

def createTitle(day, pdf, i):
    pdf.image(filePathPrefix+"/reportResources/dtraHeader.png", 0, 0, pageWidth)
    pdf.set_font('Arial', 'B', 14)  
    pdf.cell(0, 5, "Capabilities Development Data Ingestion", 0, 1, "C", False)
    pdf.cell(0, 5, "Process Model", 0, 1, "C", False)
    pdf.ln(2)
    pdf.set_font('Arial', 'I', 10) 
    pdf.cell(0, 5, "Simulation Report", 0, 1, "C", False)
    pdf.ln(12)
    pdf.set_font('Arial', '', 8)
    pdf.cell(0, 4, "Produced on: "+f'{day}', 0, 1, "R", False)

def createHeader(day, pdf, i):
    pdf.set_font('Arial', '', 8)  
    pdf.cell(0, 5, "Capabilities Development Data Ingestion Process Model - Simulation Report", 0, 0, "L", False)
    pdf.cell(0, 4, "Page "f'{i}', 0, 1, "R", False)

def create_analytics_report(day=reportDate, filename="testReport.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)

    ''' First Page '''
    i = 1
    pdf.add_page()
    createTitle(day, pdf, i)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    ''' Second Page '''
    i+=1
    pdf.add_page()
    createHeader(day, pdf, i)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    ''' Third Page '''
    pdf.add_page()
    createHeader(day, pdf, i)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    ''' Fourth Page '''
    pdf.add_page()
    createHeader(day, pdf, i)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    pdf.output(filePathPrefix+"/reports/"+filename, "F")

if __name__ == '__main__':
    fileName = "testFile"
    getFileName(fileName)
