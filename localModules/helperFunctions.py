from datetime import datetime
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
import numpy as np

from plottingModule import systemBoxPlot


def get_current_date():
    x = datetime.today()
    return x.strftime("%Y-%m-%d")

def csvExport(fileName, data):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"

    df = pd.DataFrame(data)
    df.to_csv(filePath+fileName+".csv", index = True)

def askSimulation():
    #Open Root
    root = Tk()

    # Initialize window settings
    root.title("Capabilities Development Data Ingestion Simulation")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Initialize local variable 'i' to be used to make inserting or removing data entry item easier
    i = 1

    #Instruction for parameter form
    ttk.Label(mainframe, text = "Introduction", font=("Arial", 25)).grid(row=i, column=1, sticky = N); i+=1
    ttk.Label(mainframe, text = "").grid(row=i, column=1, sticky = W); i+=1

    #Exit/BeginSim buttons
    ttk.Button(mainframe, text="Begin New Simulation", command=root.destroy).grid(row=i, column=1, sticky = W)
    ttk.Button(mainframe, text="Exit Simulation Application", command=exit()).grid(row=i, column=2, sticky = W); i+=1  

    #Space
    tk.Label(mainframe, text = "").grid(row=i, column=2, sticky = W); i+=1

    # Intro Text
    ttk.Label(mainframe, text = "This tool simulates the capabilities development data ingestion process model as a system of queued workflows.").grid(row=i, column=1, sticky = W); i+=1
    ttk.Label(mainframe, text = "The assumptions made to implement the model are detailed in the .pdf report document generated upon completion of the simulation.").grid(row=i, column=1, sticky = W); i+=1
    ttk.Label(mainframe, text = "Please choose one of the options below.").grid(row=i, column=1, sticky = W); i+=1

    #Space
    tk.Label(mainframe, text = "").grid(row=i, column=2, sticky = W); i+=1

    root.mainloop()

def formatFileData(fileName):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    fileType = fileName.split("_")[0]
    df = pd.read_csv(filePath+fileName)
    dfTransposed = df.transpose()
    dfTransposed.columns=["timeStep", "queueLength"]
    dfTransposed.insert(0, "fileEntry", dfTransposed.index, allow_duplicates=True)
    dfTransposed.insert(0, "fileType", fileType, allow_duplicates=True)
    dfTransposed.to_csv(filePath+fileName, index=False)

def formatStayData(fileName):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    fileType = fileName.split("_")[0]
    df = pd.read_csv(filePath+fileName)
    dfTransposed = df.transpose()
    dfTransposed.columns=["timeStep", "stayLength"]
    dfTransposed.insert(0, "fileNum", dfTransposed.index, allow_duplicates=True)
    dfTransposed.insert(0, "fileTypeNum", fileType+"."+dfTransposed.index, allow_duplicates=True)
    dfTransposed.to_csv(filePath+fileName, index=False)

def createFileDataMaster(fileList):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    dfCombined = pd.read_csv(filePath+fileList[1]+".csv")

    for i in range(2, len(fileList)):
        df = pd.read_csv(filePath+fileList[i]+".csv")
        dfCombined = pd.concat([dfCombined, df], ignore_index=True)

    dfCombined.to_csv(filePath+"systemFilesCombined.csv")

def createStayDataMaster(fileList):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    dfCombined = pd.read_csv(filePath+fileList[1]+".csv")
    
    for i in range(2, len(fileList)):
        df = pd.read_csv(filePath+fileList[i]+".csv")
        dfCombined = pd.concat([dfCombined, df], ignore_index=True)

    dfCombined.to_csv(filePath+"systemStayCombined.csv")

def createFilesStats(fileName, timeWindow, plotColor):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    filesStats = []
    
    df = pd.read_csv(filePath+fileName+".csv")
    df.drop(axis=0, index=[0, max(df.index)], inplace=True)

    totalFiles = len(df["fileNum"]); filesStats.append(totalFiles)

    oldMonthIndex = 1
    monthValue = 20.75
    monthFiles = []

    statMonths = np.ceil(timeWindow/monthValue)
    iMax = statMonths.astype(int)

    for i in range (0, iMax):
        monthNumber = monthValue*(i+1)
        df["diff"] = abs(df["timeStep"]-monthNumber)
        if df["diff"].empty:
            tempVal = 0; monthFiles.append(tempVal)
        else:
            monthIndex = df["diff"].idxmin()
            tempVal = float(df.iloc[oldMonthIndex:monthIndex]["fileNum"].count()); monthFiles.append(tempVal)
            oldMonthIndex = monthIndex

    minFile = pd.Series(monthFiles).min(); filesStats.append(minFile)
    maxFile = pd.Series(monthFiles).max(); filesStats.append(maxFile)
    medianFile = pd.Series(monthFiles).median(); filesStats.append(medianFile)
    meanFile = pd.Series(monthFiles).mean(); filesStats.append(meanFile)
    stdDevFile = pd.Series(monthFiles).std(); filesStats.append(stdDevFile)

    systemBoxPlot(monthFiles, "Files", "Files_per_Month", plotColor, fileName+"_Box")

    return filesStats

def createQueueStats(fileName):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    queueStats = []

    df = pd.read_csv(filePath+fileName+".csv")
    df.drop(axis=0, index=[0, 1, max(df.index)], inplace=True)
    s = pd.Series(df["queueLength"])
    minQueue = s.min(); queueStats.append(minQueue)
    maxQueue = s.max(); queueStats.append(maxQueue)
    medianQueue = s.median(); queueStats.append(medianQueue)
    meanQueue = s.mean(); queueStats.append(meanQueue)
    stdDevQueue = s.std(); queueStats.append(stdDevQueue)

    return queueStats

def createStayStats(fileName):
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
    stayStats = []

    df = pd.read_csv(filePath+fileName+".csv")
    df.drop(axis=0, index=[0, max(df.index)], inplace=True)
    s = pd.Series(df["stayLength"])
    minStay = s.min(); stayStats.append(minStay)
    maxStay = s.max(); stayStats.append(maxStay)
    medianStay = s.median(); stayStats.append(medianStay)
    meanStay = s.mean(); stayStats.append(meanStay)
    stdDevStay = s.std(); stayStats.append(stdDevStay)

    return stayStats

def createOutputTable():
    filePath = "./capDevDataIngestSim/data/"
    #filePath = "./data/"
