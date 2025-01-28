# Python libraries
from fpdf import FPDF
import os

# Local Libraries
from helperFunctions import get_current_date, askSimulation


pageWidth = 210
pageHeight = 297

filePathPrefix = "./capDevDataIngestSim"
#filePathPrefix = "."

reportDate = get_current_date() 

def getFileName(fileName, fileValues, queueStats):
        global outPutFile, sysStats, aaStats, coStats, dkStats, fsStats, maStats, meStats, njStats
        global rdStats, svStats, tgStats, tiStats, wtStats, filePrefix, iatValues, j

        filePrefix = fileName+"_"
        iatValues = fileValues

        j=0
        sysStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        aaStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        coStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        dkStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        fsStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        maStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        meStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        njStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        rdStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        svStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        tgStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        tiStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3
        wtStats = queueStats[j]+queueStats[j+1]+queueStats[j+2]; j+=3

        outPutFile = str(fileName)+".pdf"
        create_analytics_report(filePrefix, iatValues, outPutFile, reportDate)

def createTitle(day, pdf):
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

def createHeader(pdf):
        pdf.set_font('Arial', '', 8)  
        pdf.cell(0, 5, "Capabilities Development Data Ingestion Process Model - Simulation Report", 0, 0, "L", False)
        pdf.cell(0, 4, "Page "f'{pdf.page_no()}', 0, 1, "R", False)

def create_analytics_report(filePrefix, iatValues, outPutFile, day=reportDate):
        global pdf
        pdf = FPDF() # A4 (210 by 297 mm)

        ''' Title Page '''
        pdf.add_page()
        createTitle(day, pdf)

        ''' Introduction '''
        pdf.set_font('Arial', "B", 10)
        pdf.ln(5)
        pdf.cell(0, 5, "Purpose")
        pdf.ln(8)
        pdf.set_font('Arial', "", 10)
        pdf.multi_cell(pageWidth-20, 4, txt = "     Develop a Capabilities Development data ingestion process model with accompanying mathematical and visual simulation. Parameter values for arrival and processing are editable to enable what-if analysis, identify points of risk associated with unacceptable data processing wait times.")
        pdf.ln(11)
        pdf.set_font('Arial', "B", 10)
        pdf.cell(0, 5, "Contraints, Limitations & Assuptions")
        pdf.set_font('Arial', "", 10)
        pdf.ln(8)
        pdf.multi_cell(pageWidth-20, 4, 
                        txt = "Constraints:\n  -  Time limited to end of calendar year 2024.\n  -  Software limited to that available on DTRA NLAN, SLAN and UNET.\n  -  The file simStart.py must be run in a debugger enabled Visual Studio Code installation, or from a local installation of python IDLE.")
        pdf.ln(5)
        pdf.multi_cell(pageWidth-20, 4, 
                        txt = "Limitations:\n  -  Parameter value estimations are based on the data available and can be refined as more accurate data is generated.")
        pdf.ln(5)
        pdf.multi_cell(pageWidth-20, 4, 
                        txt = "Assumptions:\n  -  Steady state simulation based on a mean of 250 files ingested per calendar month.\n  -  Windtalker files arrive on Mondays with normally distributed batch sizes.\n  -  All other file types arrive based on exponentially distributed interarrival times based on the mean files received per calendar month.\n  -  Default parameter values assume three FTEs dedicated to data ingestion of 6 FTEs available.")
        pdf.ln(20)

        ''' Second Page '''
        pdf.add_page()
        j=0
        createHeader(pdf)
        #System Time in Queue Statistics
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"Length_of_Stay_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #System Queue Length Statistics
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Stair.png", 10, 70, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Hist.png", pageWidth/3+5, 70, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"System_Queue_Length_Box.png", 2*(pageWidth/3), 70, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(110)
        # System statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")

        pdf.ln(20)
        
        if iatValues[0] > 0:
                j+=1
                addAaPage(pdf)
        if iatValues[1] > 0:
                j+=1
                addCoPage(pdf)
        if iatValues[2] > 0:
                j+=1
                addDkPage(pdf)
        if iatValues[3] > 0:
                j+=1
                addFsPage(pdf)
        if iatValues[4] > 0:
                j+=1
                addMaPage(pdf)
        if iatValues[5] > 0:
                j+=1
                addMePage(pdf)
        if iatValues[6] > 0:
                j+=1
                addNjPage(pdf)
        if iatValues[7] > 0:
                j+=1
                addRdPage(pdf)
        if iatValues[8] > 0:
                j+=1
                addSvPage(pdf)
        if iatValues[9] > 0:
                j+=1
                addTgPage(pdf)
        if iatValues[10] > 0:
                j+=1
                addTiPage(pdf)
        if iatValues[11] > 0:
                j+=1
                addWtPage(pdf)

        ''' Last Page '''
        pdf.add_page()
        createHeader(pdf)
        pdf.set_font('Arial', "", 10)
        pdf.ln(20)
        pdf.cell(0, 5, "Appendix A - Parameters for This Simulation Run")
        pdf.ln(8)

        ''' File Output '''
        pdf.output(filePathPrefix+"/reports/"+outPutFile, "F")

''' Additional Pages, as Required '''
def addAaPage(pdf):
        ''' AA Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"AA_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addCoPage(pdf):
        ''' CO Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"CO_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)
        
        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addDkPage(pdf):
        ''' DK Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"DK_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addFsPage(pdf):
        ''' FS Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"FS_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addMaPage(pdf):
        ''' MA Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"MA_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addMePage(pdf):
        ''' ME Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"ME_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addNjPage(pdf):
        ''' NJ Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"NJ_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addRdPage(pdf):
        ''' RD Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"RD_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addSvPage(pdf):
        ''' SV Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"SV_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addTgPage(pdf):
        ''' TG Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TG_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addTiPage(pdf):
        ''' TI Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"TI_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

def addWtPage(pdf):
        ''' WT Page '''
        pdf.add_page()
        createHeader(pdf)

        pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Stair.png", 10, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Hist.png", pageWidth/3+5, 20, pageWidth/3-10)
        pdf.image(filePathPrefix+"/plots/"+filePrefix+"WT_Queue_length_Box.png", 2*(pageWidth/3), 20, pageWidth/3-10)

        #Files per Month Plot
        pdf.image(filePathPrefix+"/plots/"+"SYS_Stay_Box_Files_per_Month.png", ((pageWidth/3+5)+(2*(pageWidth/3)))/2, 135, pageWidth/3-10)

        pdf.ln(60)
        # Statistics data table
        i = 0
        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "File Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Total Files:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Min File per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Files per Month:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Queue Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Queue Length:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1; pdf.ln(5)

        pdf.set_font('Arial', "BU", 8)
        pdf.cell(43, h = 5, txt = "Stay Statistics", ln = 1, align = "R")
        pdf.set_font('Arial', "", 8)
        pdf.cell(33, h = 3, txt = "Min Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Max Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Median Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Mean Stay (Days):", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R"); i+=1
        pdf.cell(33, h = 3, txt = "Standard Deviation:", ln = 0, align = "R"); pdf.cell(10, h = 3, txt = f"{sysStats[i]:10.2f}", ln = 1, align = "R")
        pdf.ln(20)

''' Re-Start Script '''

askSimulation()

if __name__ == '__main__':
        fileName = "testFile"
        iatValues = [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1]
        test = "testing"
        getFileName(fileName, iatValues, test)