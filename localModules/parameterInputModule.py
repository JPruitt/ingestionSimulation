import tkinter as tk
from tkinter import *
from tkinter import ttk

def getParamValues(*args):

    workDaysPerYear()
    enterStartingConditions()

    paramValues = paramDict
    return paramValues

def workDaysPerYear():
    #Variables with values set in this module that are required elsewhere
    global daysPerYear, timeWindow
    '''
    Currently estimates the number of available work days per year
    '''
    daysPerYear = 365
    daysPerYear = daysPerYear - 104 # Weekends
    daysPerYear = daysPerYear - 12 # Federal Holidays
    timeWindow = daysPerYear

def parameterEntry(*args):
    '''
    This function reads input values (or the predetermined delaults) from GUI and converts them to
    values usable by the simulation. 
    '''
    try:
        #Variables with values set in this modulae that are required elsewhere
        global paramDict

        #Initailize list to pass variable values
        paramDict = []

        simFileName = simFileNameEntry.get(); paramDict.append(simFileName)
        nservers = float(nserversEntry.get()); paramDict.append(nservers)

        coMinutes = float(coTimeEntry.get()); paramDict.append(coMinutes)
        coServerTime = (1/((1/coMinutes)*(60/1)*(8/1))); paramDict.append(coServerTime)
        filesCo = float(iatCoEntry.get()); paramDict.append(filesCo)
        if filesCo > 0:
            iatCo = 1/((filesCo*12)/daysPerYear); paramDict.append(iatCo)
        else:
            iatCo = 0; paramDict.append(iatCo)

        dkMinutes = float(dkTimeEntry.get()); paramDict.append(dkMinutes)
        dkServerTime = (1/((1/dkMinutes)*(60/1)*(8/1))); paramDict.append(dkServerTime)
        filesDk = float(iatDkEntry.get()); paramDict.append(filesDk)
        if filesDk > 0:
            iatDk = 1/((filesDk*12)/daysPerYear); paramDict.append(iatDk)
        else:
            iatDk = 0; paramDict.append(iatDk)

        maMinutes = float(maTimeEntry.get()); paramDict.append(maMinutes)
        maServerTime = (1/((1/maMinutes)*(60/1)*(8/1))); paramDict.append(maServerTime)
        filesMa = float(iatMaEntry.get()); paramDict.append(filesMa)
        if filesMa > 0:
            iatMa = 1/((filesMa*12)/daysPerYear); paramDict.append(iatMa)
        else:
            iatMa = 0; paramDict.append(iatMa)

        njMinutes = float(njTimeEntry.get()); paramDict.append(njMinutes)
        njServerTime = (1/((1/njMinutes)*(60/1)*(8/1))); paramDict.append(njServerTime)
        filesNj = float(iatNjEntry.get()); paramDict.append(filesNj)
        if filesNj > 0:
            iatNj = 1/((filesNj*12)/daysPerYear); paramDict.append(iatNj)
        else:
            iatNj = 0; paramDict.append(iatNj)

        rdMinutes = float(rdTimeEntry.get()); paramDict.append(rdMinutes)
        rdServerTime = (1/((1/rdMinutes)*(60/1)*(8/1))); paramDict.append(rdServerTime)
        filesRd = float(iatRdEntry.get()); paramDict.append(filesRd)
        if filesRd > 0:
            iatRd = 1/((filesRd*12)/daysPerYear); paramDict.append(iatRd)
        else:
            iatRd = 0; paramDict.append(iatRd)

        svMinutes = float(svTimeEntry.get()); paramDict.append(svMinutes)
        svServerTime = (1/((1/svMinutes)*(60/1)*(8/1))); paramDict.append(svServerTime)
        filesSv = float(iatSvEntry.get()); paramDict.append(filesSv)
        if filesSv > 0:
            iatSv = 1/((filesSv*12)/daysPerYear); paramDict.append(iatSv)
        else:
            iatSv = 0; paramDict.append(iatSv)

        tgMinutes = float(tgTimeEntry.get()); paramDict.append(tgMinutes)
        tgServerTime = (1/((1/tgMinutes)*(60/1)*(8/1))); paramDict.append(tgServerTime)
        filesTg = float(iatTgEntry.get()); paramDict.append(filesTg)
        if filesTg > 0:
            iatTg = 1/((filesTg*12)/daysPerYear); paramDict.append(iatTg)
        else:
            iatTg = 0; paramDict.append(iatTg)

        wtMinutes = float(wtTimeEntry.get()); paramDict.append(wtMinutes)
        wtServerTime = (1/((1/wtMinutes)*(60/1)*(8/1))); paramDict.append(wtServerTime)
        filesWt = float(iatWtEntry.get()); paramDict.append(filesWt)
        if filesWt > 0:
            iatWt = 1/((filesWt*12)/daysPerYear); paramDict.append(iatWt)
            meanWt = float(meanWtEntry.get()); paramDict.append(meanWt)
            devWt = float(devWtEntry.get()); paramDict.append(devWt)
        else:
            iatWt = 0; paramDict.append(iatWt)
            meanWt = 0; paramDict.append(meanWt)
            devWt = 0; paramDict.append(devWt)

        # New file types - not currently processed
        nameAa = nameAaEntry.get(); paramDict.append(nameAa)
        aaMinutes = float(aaTimeEntry.get()); paramDict.append(aaMinutes)
        aaServerTime = (1/((1/aaMinutes)*(60/1)*(8/1))); paramDict.append(aaServerTime)
        filesAa = float(iatAaEntry.get()); paramDict.append(filesAa)
        if filesAa > 0:
            iatAa = 1/((filesAa*12)/daysPerYear); paramDict.append(iatAa)
        else:
            iatAa = 0; paramDict.append(iatAa)

        nameTi = nameTiEntry.get(); paramDict.append(nameTi)
        tiMinutes = float(tiTimeEntry.get()); paramDict.append(tiMinutes)
        tiServerTime = (1/((1/tiMinutes)*(60/1)*(8/1))); paramDict.append(tiServerTime)
        filesTi = float(iatTiEntry.get()); paramDict.append(filesTi)
        if filesTi >0:
            iatTi = 1/((filesTi*12)/daysPerYear); paramDict.append(iatTi)
        else:
            iatTi = 0; paramDict.append(iatTi)

        nameMe = nameMeEntry.get(); paramDict.append(nameMe)
        meMinutes = float(meTimeEntry.get()); paramDict.append(meMinutes)
        meServerTime = (1/((1/meMinutes)*(60/1)*(8/1))); paramDict.append(meServerTime)
        filesMe = float(iatMeEntry.get()); paramDict.append(filesMe)     
        if filesMe > 0:
            iatMe = 1/((filesMe*12)/daysPerYear); paramDict.append(iatMe)
        else:
            iatMe = 0; paramDict.append(iatMe)

        nameFs = nameFsEntry.get(); paramDict.append(nameFs)
        fsMinutes = float(fsTimeEntry.get()); paramDict.append(fsMinutes)
        fsServerTime = (1/((1/fsMinutes)*(60/1)*(8/1))); paramDict.append(fsServerTime)
        filesFs = float(iatFsEntry.get()); paramDict.append(filesFs)
        if filesFs >0:
            iatFs = 1/((filesFs*12)/daysPerYear); paramDict.append(iatFs)
        else:
            iatFs = 0; paramDict.append(iatFs)

        timeWindowYears = float(timeWindowEntry.get()); paramDict.append(timeWindowYears)
        paramDict.append(daysPerYear)
        timeWindow = timeWindowYears*daysPerYear; paramDict.append(timeWindow)
        lowProb = float(lowPriorityEntry.get()); paramDict.append(lowProb)
        medProb = float(medPriorityEntry.get()); paramDict.append(medProb)
        highProb = float(highPriorityEntry.get()); paramDict.append(highProb)
        vHighProb = float(vHighPriorityEntry.get()); paramDict.append(vHighProb)
        dkTransferTime = float(dkTransferEntry.get()); paramDict.append(dkTransferTime)
    except ValueError:
        pass

    return paramDict        

def enterStartingConditions():
    #Variables with values set in this module that are required elsewhere
    global timeWindowEntry, devWtEntry, meanWtEntry, iatCoEntry, iatDkEntry, iatMaEntry, fileGrowthEntry, sensorGrowthEntry
    global iatRdEntry, iatSvEntry, iatTgEntry, iatWtEntry, nserversEntry, coTimeEntry, dkTimeEntry, aaTimeEntry, ingestEfficiencyEntry
    global maTimeEntry, njTimeEntry, rdTimeEntry, svTimeEntry, tgTimeEntry, wtTimeEntry, fsTimeEntry, tiTimeEntry, meTimeEntry
    global iatAaEntry, iatTiEntry, iatNjEntry, nameAaEntry, nameTiEntry, iatMeEntry, iatFsEntry, dkTransferEntry
    global nameMeEntry, nameFsEntry, simFileNameEntry, lowPriorityEntry, medPriorityEntry, highPriorityEntry, vHighPriorityEntry
    '''
    This function draws the input GUI that contains the instructions, editable default values for
    simulation parameters and goals, a submit button to confirm changes and a
    button to begin the simulation which closes the GUI window, and passes all required values to 
    the simulation engine.
    '''
    #Open Root
    root = Tk()

    # Initialize window settings
    root.title("Capabilities Development Data Ingestion Simulation - Parameter Entry")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    #Initialize local variable 'i' to be used to make inserting or removing data entry item easier
    i = 1
    
    #Instruction for parameter form
    tk.Label(mainframe, text = "Data Entry Instructions", font=("Arial Black", 20)).grid(row=i, column=1, columnspan = 7, sticky = N); i+=1
    tk.Label(mainframe, text = "1. Adjust parameter values from default values as desired.").grid(row=i, column=3, columnspan = 2, sticky = W)
    ttk.Button(mainframe, text="Submit Parameter Entries", command=parameterEntry).grid(row=i, column=6, sticky = W); i+=1
    tk.Label(mainframe, text = "2. Click the <<Submit Parameter Entries>> button.").grid(row=i, column=3, columnspan = 2, sticky = W); i+=1
    tk.Label(mainframe, text = "3. Click the <<Begin Simulation>> button.").grid(row=i, column=3, columnspan = 2, sticky = W)
    ttk.Button(mainframe, text="Begin Simulation", command=root.destroy).grid(row=i, column=6, sticky = W); i+=1  
    tk.Label(mainframe, text = "").grid(row=i, column=2, columnspan = 2, sticky = W); i+=1
    
    #Personnel available for data ingestion
    nserversEntry = StringVar()
    nserversEntry = ttk.Entry(mainframe, width=7, textvariable=nserversEntry)
    nserversEntry.insert(0, "3")
    nserversEntry.grid(row=i, column=2, sticky=(W, E))
    ttk.Label(mainframe, text="Number of FTE used to ingest data.").grid(row=i, column=3, sticky=W, padx=5, pady=5)

    #fileName 
    simFileNameEntry = StringVar()
    simFileNameEntry = ttk.Entry(mainframe, width=7, textvariable=simFileNameEntry)
    simFileNameEntry.insert(0, "testFile")
    simFileNameEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="File name prefix.").grid(row=i, column=5, sticky=W, padx=5, pady=5)

    #Enclave transfer time
    dkTransferEntry = StringVar()
    dkTransferEntry = ttk.Entry(mainframe, width=7, textvariable=dkTransferEntry)
    dkTransferEntry.insert(0, "1")
    dkTransferEntry.grid(row=i, column=6, sticky=(W,E))
    ttk.Label(mainframe, text="SIPR to NIPR transfer time (work days).").grid(row=i, column=7, sticky=W, padx=5, pady=5); i+=1

    #Years can be represented as a decimal number (fractions of years)
    timeWindowEntry = StringVar()
    timeWindowEntry = ttk.Entry(mainframe, width=7, textvariable=timeWindowEntry)
    timeWindowEntry.insert(0, "1")
    timeWindowEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Years to simulate.").grid(row=i, column=3, sticky=W, padx=5, pady=5); i+=1

    tk.Label(mainframe, text = "").grid(row=i, column=2, columnspan = 2, sticky = W); i+=1
    tk.Label(mainframe, text = "Data File Priority Distribution", font=("Arial Black", 10)).grid(row=i, column=3, columnspan = 2, sticky = W); i+=1
    #data file priority proportions
    lowPriorityEntry = StringVar()
    lowPriorityEntry = ttk.Entry(mainframe, width=7, textvariable=lowPriorityEntry)
    lowPriorityEntry.insert(0, "0.1")
    lowPriorityEntry.grid(row=i, column=2, sticky=(W, E))
    ttk.Label(mainframe, text="Low Priority(%).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    medPriorityEntry = StringVar()
    medPriorityEntry = ttk.Entry(mainframe, width=7, textvariable=medPriorityEntry)
    medPriorityEntry.insert(0, "67.4")
    medPriorityEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Medium Priority(%).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1
    highPriorityEntry = StringVar()
    highPriorityEntry = ttk.Entry(mainframe, width=7, textvariable=highPriorityEntry)
    highPriorityEntry.insert(0, "30")
    highPriorityEntry.grid(row=i, column=2, sticky=(W, E))
    ttk.Label(mainframe, text="Low Priority(%).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    vHighPriorityEntry = StringVar()
    vHighPriorityEntry = ttk.Entry(mainframe, width=7, textvariable=vHighPriorityEntry)
    vHighPriorityEntry.insert(0, "2.5")
    vHighPriorityEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Medium Priority(%).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1
    #Space
    tk.Label(mainframe, text = "").grid(row=i, column=2, columnspan = 2, sticky = W); i+=1

    # AVG files (by type) per month is used to estimate inter-arrival times
    tk.Label(mainframe, text = "Core Sensors", font=("Arial Black", 10)).grid(row=i, column=3, columnspan = 2, sticky = W); i+=1
    # Potential new file types that we do not currently process/accept
    iatCoEntry = StringVar()
    iatCoEntry = ttk.Entry(mainframe, width=7, textvariable=iatCoEntry)
    iatCoEntry.insert(0, "14")
    iatCoEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average number Corian files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    coTimeEntry = StringVar()
    coTimeEntry = ttk.Entry(mainframe, width=7, textvariable=coTimeEntry)
    coTimeEntry.insert(0, "60")
    coTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average Corian processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatDkEntry = StringVar()
    iatDkEntry = ttk.Entry(mainframe, width=7, textvariable=iatDkEntry)
    iatDkEntry.insert(0, "3")
    iatDkEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average Drake files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    dkTimeEntry = StringVar()
    dkTimeEntry = ttk.Entry(mainframe, width=7, textvariable=dkTimeEntry)
    dkTimeEntry.insert(0, "60")
    dkTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average Drake processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatMaEntry = StringVar()
    iatMaEntry = ttk.Entry(mainframe, width=7, textvariable=iatMaEntry)
    iatMaEntry.insert(0, "1")
    iatMaEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average L-Madis files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    maTimeEntry = StringVar()
    maTimeEntry = ttk.Entry(mainframe, width=7, textvariable=maTimeEntry)
    maTimeEntry.insert(0, "60")
    maTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average L-Madis processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatNjEntry = StringVar()
    iatNjEntry = ttk.Entry(mainframe, width=7, textvariable=iatNjEntry)
    iatNjEntry.insert(0, "101")
    iatNjEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average Ninja files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    njTimeEntry = StringVar()
    njTimeEntry = ttk.Entry(mainframe, width=7, textvariable=njTimeEntry)
    njTimeEntry.insert(0, "60")
    njTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average Ninja processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatRdEntry = StringVar()
    iatRdEntry = ttk.Entry(mainframe, width=7, textvariable=iatRdEntry)
    iatRdEntry.insert(0, "1")
    iatRdEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average RD-SUADS files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    rdTimeEntry = StringVar()
    rdTimeEntry = ttk.Entry(mainframe, width=7, textvariable=rdTimeEntry)
    rdTimeEntry.insert(0, "60")
    rdTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average RD-SUADS processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatSvEntry = StringVar()
    iatSvEntry = ttk.Entry(mainframe, width=7, textvariable=iatSvEntry)
    iatSvEntry.insert(0, "2")
    iatSvEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average Skyview files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    svTimeEntry = StringVar()
    svTimeEntry = ttk.Entry(mainframe, width=7, textvariable=svTimeEntry)
    svTimeEntry.insert(0, "30")
    svTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average Skyview processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatTgEntry = StringVar()
    iatTgEntry = ttk.Entry(mainframe, width=7, textvariable=iatTgEntry)
    iatTgEntry.insert(0, "1")
    iatTgEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average TGS files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    tgTimeEntry = StringVar()
    tgTimeEntry = ttk.Entry(mainframe, width=7, textvariable=tgTimeEntry)
    tgTimeEntry.insert(0, "30")
    tgTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average TGS processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1

    iatWtEntry = StringVar()
    iatWtEntry = ttk.Entry(mainframe, width=7, textvariable=iatWtEntry)
    iatWtEntry.insert(0, "130")
    iatWtEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average Windtalker files per month.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    wtTimeEntry = StringVar()
    wtTimeEntry = ttk.Entry(mainframe, width=7, textvariable=wtTimeEntry)
    wtTimeEntry.insert(0, "10")
    wtTimeEntry.grid(row=i, column=4, sticky=(W, E))
    ttk.Label(mainframe, text="Average Windtalker processing time (minutes).").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1
    
    # Collect windtalker weekly batch size parameters (all windtalker files arrive o/a Mondays)
    meanWtEntry = StringVar()
    meanWtEntry = ttk.Entry(mainframe, width=7, textvariable=meanWtEntry)
    meanWtEntry.insert(0, "27.33")
    meanWtEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Average weekly Windtalker batch size.").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    devWtEntry = StringVar()
    devWtEntry = ttk.Entry(mainframe, width=7, textvariable=devWtEntry)
    devWtEntry.insert(0, "6.74")
    devWtEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="Standard deviation of weekly Windtalker batch size.").grid(row=i, column=5, sticky=W, padx=5, pady=5); i+=1
    
    tk.Label(mainframe, text = "").grid(row=i, column=2, columnspan = 2, sticky = W); i+=1
    tk.Label(mainframe, text = "Potential New Sensors", font=("Arial Black", 10)).grid(row=i, column=3, columnspan = 2, sticky = W); i+=1
    # Potential new file types that we do not currently process/accept
    nameAaEntry = StringVar()
    nameAaEntry = ttk.Entry(mainframe, width=7, textvariable=nameAaEntry)
    nameAaEntry.insert(0, "AA")
    nameAaEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Two-letter code for new file type one (if applicable).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    iatAaEntry = StringVar()
    iatAaEntry = ttk.Entry(mainframe, width=7, textvariable=iatAaEntry)
    iatAaEntry.insert(0, "0")
    iatAaEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="Average files per month.").grid(row=i, column=5, sticky=W, padx=5, pady=5)
    aaTimeEntry = StringVar()
    aaTimeEntry = ttk.Entry(mainframe, width=7, textvariable=aaTimeEntry)
    aaTimeEntry.insert(0, "90")
    aaTimeEntry.grid(row=i, column=6, sticky=(W, E))
    ttk.Label(mainframe, text="Average processing time (minutes).").grid(row=i, column=7, sticky=W, padx=5, pady=5); i+=1
    nameTiEntry = StringVar()
    nameTiEntry = ttk.Entry(mainframe, width=7, textvariable=nameTiEntry)
    nameTiEntry.insert(0, "TI")
    nameTiEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Two-letter code for new file type two (if applicable).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    iatTiEntry = StringVar()
    iatTiEntry = ttk.Entry(mainframe, width=7, textvariable=iatTiEntry)
    iatTiEntry.insert(0, "0")
    iatTiEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="Average files per month.").grid(row=i, column=5, sticky=W, padx=5, pady=5)
    tiTimeEntry = StringVar()
    tiTimeEntry = ttk.Entry(mainframe, width=7, textvariable=tiTimeEntry)
    tiTimeEntry.insert(0, "120")
    tiTimeEntry.grid(row=i, column=6, sticky=(W, E))
    ttk.Label(mainframe, text="Average processing time (minutes).").grid(row=i, column=7, sticky=W, padx=5, pady=5); i+=1
    nameMeEntry = StringVar()
    nameMeEntry = ttk.Entry(mainframe, width=7, textvariable=nameAaEntry)
    nameMeEntry.insert(0, "ME")
    nameMeEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Two-letter code for new file type one (if applicable).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    iatMeEntry = StringVar()
    iatMeEntry = ttk.Entry(mainframe, width=7, textvariable=iatMeEntry)
    iatMeEntry.insert(0, "0")
    iatMeEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="Average files per month.").grid(row=i, column=5, sticky=W, padx=5, pady=5)
    meTimeEntry = StringVar()
    meTimeEntry = ttk.Entry(mainframe, width=7, textvariable=meTimeEntry)
    meTimeEntry.insert(0, "120")
    meTimeEntry.grid(row=i, column=6, sticky=(W, E))
    ttk.Label(mainframe, text="Average processing time (minutes).").grid(row=i, column=7, sticky=W, padx=5, pady=5); i+=1
    nameFsEntry = StringVar()
    nameFsEntry = ttk.Entry(mainframe, width=7, textvariable=nameTiEntry)
    nameFsEntry.insert(0, "FS")
    nameFsEntry.grid(row=i, column=2, sticky=(W,E))
    ttk.Label(mainframe, text="Two-letter code for new file type two (if applicable).").grid(row=i, column=3, sticky=W, padx=5, pady=5)
    iatFsEntry = StringVar()
    iatFsEntry = ttk.Entry(mainframe, width=7, textvariable=iatFsEntry)
    iatFsEntry.insert(0, "0")
    iatFsEntry.grid(row=i, column=4, sticky=(W,E))
    ttk.Label(mainframe, text="Average files per month.").grid(row=i, column=5, sticky=W, padx=5, pady=5)
    fsTimeEntry = StringVar()
    fsTimeEntry = ttk.Entry(mainframe, width=7, textvariable=fsTimeEntry)
    fsTimeEntry.insert(0, "120")
    fsTimeEntry.grid(row=i, column=6, sticky=(W, E))
    ttk.Label(mainframe, text="Average processing time (minutes).").grid(row=i, column=7, sticky=W, padx=5, pady=5); i+=1
    #Space
    tk.Label(mainframe, text = "").grid(row=i, column=2, columnspan = 2, sticky = W); i+=1
   
    root.bind("<Return>", parameterEntry())
    root.mainloop()

if __name__ == "__main__":
    getParamValues()
