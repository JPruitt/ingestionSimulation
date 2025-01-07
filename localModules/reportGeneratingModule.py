# Python libraries
from fpdf import FPDF
import os

# Local Libraries
from helperFunctions import get_current_date

pageWidth = 210
pageHeight = 297

reportDate = get_current_date() 

def createTitle(day, pdf, i):
    pdf.set_font('Arial', 'B', 14)  
    pdf.cell(0, 5, "Capabilities Development Data Ingestion", 0, 1, "C", False)
    pdf.cell(0, 5, "Process Model", 0, 1, "C", False)
    pdf.ln(2)
    pdf.set_font('Arial', 'I', 10) 
    pdf.cell(0, 5, "Simulation Report", 0, 1, "C", False)
    pdf.ln(10)
    pdf.set_font('Arial', '', 8)
    pdf.cell(0, 4, "Produced on: "+f'{day}', 0, 1, "R", False)
    pdf.cell(0, 4, "Page "f'{i}', 0, 1, "R", False)

def create_analytics_report(day=reportDate, filename="testReport.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)

    ''' First Page '''
    i = 1
    pdf.add_page()
    pdf.image("./capDevDataIngestSim/reportResources/dtraHeader.png", 0, 0, pageWidth)
    createTitle(day, pdf, i)

    pdf.image("./capDevDataIngestSim/plots/Length_of_Stay_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/Length_of_Stay_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/Length_of_Stay_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/System_Queue_Length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/System_Queue_Length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/System_Queue_Length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    ''' Second Page '''
    i+=1
    pdf.add_page()
    createTitle(day, pdf, i)

    pdf.image("./capDevDataIngestSim/plots/AA_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/AA_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/AA_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/CO_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/CO_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/CO_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/DK_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/DK_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/DK_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/FS_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/FS_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/FS_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    ''' Third Page '''
    pdf.add_page()

    pdf.image("./capDevDataIngestSim/plots/MA_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/MA_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/MA_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/ME_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/ME_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/ME_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/NJ_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/NJ_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/NJ_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/RD_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/RD_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/RD_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    ''' Fourth Page '''
    pdf.add_page()

    pdf.image("./capDevDataIngestSim/plots/SV_Queue_length_Stair.png", 10, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/SV_Queue_length_Hist.png", pageWidth/3+5, 50, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/SV_Queue_length_Box.png", 2*(pageWidth/3), 50, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/TG_Queue_length_Stair.png", 10, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/TG_Queue_length_Hist.png", pageWidth/3+5, 100, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/TG_Queue_length_Box.png", 2*(pageWidth/3), 100, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/TI_Queue_length_Stair.png", 10, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/TI_Queue_length_Hist.png", pageWidth/3+5, 150, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/TI_Queue_length_Box.png", 2*(pageWidth/3), 150, pageWidth/3-10)

    pdf.image("./capDevDataIngestSim/plots/WT_Queue_length_Stair.png", 10, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/WT_Queue_length_Hist.png", pageWidth/3+5, 200, pageWidth/3-10)
    pdf.image("./capDevDataIngestSim/plots/WT_Queue_length_Box.png", 2*(pageWidth/3), 200, pageWidth/3-10)

    pdf.output("./capDevDataIngestSim/reports/"+filename, "F")

if __name__ == '__main__':
  
  create_analytics_report(reportDate)
