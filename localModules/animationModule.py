#Global Packages
import salabim as sim
import os

# Local Modules
from plottingModule import systemHistPlot, systemBoxPlot, systemStairPlot
from pdfGeneratingModule import getFileName
from helperFunctions import csvExport, formatFileData, formatStayData, createFileDataMaster, createStayDataMaster, createFilesStats
from helperFunctions import createQueueStats, createStayStats, showErrorWindow

# Get values from parameter input module
def setParameterValues(paramDict):
    global nservers, filesCo, iatCo, filesDk, iatDk, filesMa, iatMa, filesNj, iatNj, filesRd, iatRd, filesSv, iatSv, filesTg, iatTg
    global filesWt, iatWt, meanWt, devWt, nameAa, filesAa, iatAa, nameTi, filesTi, iatTi, nameMe, filesMe, iatMe, nameFs, filesFs, iatFs
    global timeWindowYears, daysPerYear, timeWindow, simFileName, lowProb, medProb, highProb, vHighProb, dkTransferTime
    global coServerTime, coMinutes, dkServerTime, dkMinutes, maServerTime, maMinutes, njServerTime, njMinutes, rdServerTime, rdMinutes, svServerTime, svMinutes
    global tgServerTime, tgMinutes, wtServerTime, wtMinutes, aaServerTime, aaMinutes, tiServerTime, tiMinutes, meServerTime, meMinutes, fsServerTime, fsMinutes
    
    paramValues = paramDict
    i=0

    simFileName = paramValues[i]; i+=1
    nservers = float(paramValues[i]); i+=1
    coMinutes = float(paramValues[i]); i+=1
    coServerTime = float(paramValues[i]); i+=1
    filesCo = float(paramValues[i]); i+=1
    iatCo = float(paramValues[i]); i+=1
    dkMinutes = float(paramValues[i]); i+=1
    dkServerTime = float(paramValues[i]); i+=1
    filesDk = float(paramValues[i]); i+=1
    iatDk = float(paramValues[i]); i+=1
    maMinutes = float(paramValues[i]); i+=1
    maServerTime = float(paramValues[i]); i+=1
    filesMa = float(paramValues[i]); i+=1
    iatMa = float(paramValues[i]); i+=1
    njMinutes = float(paramValues[i]); i+=1
    njServerTime = float(paramValues[i]); i+=1
    filesNj = float(paramValues[i]); i+=1
    iatNj = float(paramValues[i]); i+=1
    rdMinutes = float(paramValues[i]); i+=1
    rdServerTime = float(paramValues[i]); i+=1
    filesRd = float(paramValues[i]); i+=1
    iatRd = float(paramValues[i]); i+=1
    svMinutes = float(paramValues[i]); i+=1
    svServerTime = float(paramValues[i]); i+=1
    filesSv = float(paramValues[i]); i+=1
    iatSv = float(paramValues[i]); i+=1
    tgMinutes = float(paramValues[i]); i+=1
    tgServerTime = float(paramValues[i]); i+=1
    filesTg = float(paramValues[i]); i+=1
    iatTg = float(paramValues[i]); i+=1
    wtMinutes = float(paramValues[i]); i+=1
    wtServerTime = float(paramValues[i]); i+=1
    filesWt = float(paramValues[i]); i+=1
    iatWt = float(paramValues[i]); i+=1
    meanWt = float(paramValues[i]); i+=1
    devWt = float(paramValues[i]); i+=1
    nameAa = paramValues[i]; i+=1
    aaMinutes = float(paramValues[i]); i+=1
    aaServerTime = float(paramValues[i]); i+=1
    filesAa = float(paramValues[i]); i+=1
    iatAa = float(paramValues[i]); i+=1
    nameTi = paramValues[i]; i+=1
    tiMinutes = float(paramValues[i]); i+=1
    tiServerTime = float(paramValues[i]); i+=1
    filesTi = float(paramValues[i]); i+=1
    iatTi = float(paramValues[i]); i+=1
    nameMe = paramValues[i]; i+=1
    meMinutes = float(paramValues[i]); i+=1
    meServerTime = float(paramValues[i]); i+=1
    filesMe = float(paramValues[i]); i+=1
    iatMe = float(paramValues[i]); i+=1
    nameFs = paramValues[i]; i+=1
    fsMinutes = float(paramValues[i]); i+=1
    fsServerTime = float(paramValues[i]); i+=1
    filesFs = float(paramValues[i]); i+=1
    iatFs = float(paramValues[i]); i+=1
    timeWindowYears = float(paramValues[i]); i+=1
    daysPerYear = float(paramValues[i]); i+=1
    timeWindow = float(paramValues[i]); i+=1
    lowProb = float(paramValues[i]); i+=1
    medProb = float(paramValues[i]); i+=1
    highProb = float(paramValues[i]); i+=1
    vHighProb = float(paramValues[i]); i+=1
    dkTransferTime = float(paramValues[i]); i+=1

    runSimulation()

def do_animation():
    simHeight = 1150
    simWidth = 1500
    xMonitor = 50
    yMonitor = 900
    
    videoFilePath = "./capDevDataIngestSim/video/"
    # videoFilePath = "./video/"

    # set global animation parameters    
    env.animation_parameters(
        animate = True,
        speed=4, 
        background_color="30%gray",
        height = simHeight,
        width = simWidth, 
        title = "CapDev Data Ingestion Process Model",
        video = videoFilePath + simFileName + "capDevSim.avi"
    )   

    '''
    animate file queue and data processor activity; file queue populates to the left from the 
    bottom-right corner with no queue length maximum, processor activity populates up from the 
    bottom-right corner with a length maximum defined by nservers.
    '''

    # Labels for queue animation
    sim.AnimateText(text="Data Processors", fontsize = 10, x=975, y=25, text_anchor="n")
    sim.AnimateText(text="<-- Waiting Data Files", fontsize = 10, x=850, y=25, text_anchor="n")
    sim.AnimateText(text="Priority (%)", fontsize = 10, x=975, y=665, text_anchor="n")

    # Queue  animation
    sim.AnimateQueue(servers.requesters(), x=1250, y=75, title="", direction="w")
    sim.AnimateQueue(servers.claimers(), x=1400, y=75, direction="n", title="")

    def animateMonitor(j):
        global monitorType, monitorColor
        # creates 14 animated monitors from lists of monitor attribute values

        monitorType = [system.length_of_stay, system.length, sysCo.length,
            sysDk.length, sysMa.length, sysNj.length, sysAa.length,
            sysMe.length, sysRd.length, sysSv.length, sysTg.length,
            sysWt.length, sysTi.length, sysFs.length]
        
        xOffset = [0, 0, 0, 0, 0, 0, 0, 0, 675, 675, 675, 675, 675, 675]
        
        yOffset = [-25, -125, -250, -350, -450, -550, -650, -750, -250, -350, -450, -550, -650, -750]
        
        wOffset = [-200, -200, -875, -875, -875, -875, -875, -875, -875, -875, -875, -875, 
            -875, -875]
        
        vScale = [10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        
        monitorColor = ["white", "white", "red", "yellow", "blue", "orange", "tomato", "goldenrod",
            "green", "purple", "peru", "teal", "yellowgreen", "violet"]

        monitorTitle = ["Time in data file queue.  Mean ={:10.2f}   Days", "Number of data files in the queue.  Mean ={:10.2f}   Files", 
            "Number of Corian (CO) files in the queue. Mean ={:10.2f}   Files", "Number of Drake (DK) files in the queue. Mean ={:10.2f}   Files", 
            "Number of L-Madis (MA) files in the queue. Mean ={:10.2f}   Files", "Number of Ninja (NJ) files in the queue. Mean ={:10.2f}   Files",
            "Number of "+nameAa+" files in the queue. Mean ={:10.2f}   Files", "Number of "+nameMe+" files in the queue. Mean ={:10.2f}   Files",
            "Number of RD-SUADS (RD) files in the queue. Mean ={:10.2f}   Files", "Number of Skyview (SV) files in the queue. Mean ={:10.2f}   Files",
            "Number of TGS (TG) files in the queue. Mean ={:10.2f}   Files", "Number of Windtalker (WT) files in the queue. Mean ={:10.2f}   Files",
            "Number of "+nameTi+" files in the queue. Mean ={:10.2f}   Files", "Number of "+nameFs+" files in the queue. Mean ={:10.2f}   Files"]
      
        sim.AnimateMonitor(
            monitorType[j],
            linewidth= 2,
            x = xMonitor + xOffset[j],
            y = yMonitor + yOffset[j],
            height=75,
            width=env.width() + wOffset[j],
            linecolor=monitorColor[j],
            horizontal_scale=10,
            vertical_scale=vScale[j],
            title=lambda: monitorTitle[j].format(monitorType[j].mean()),
        )

    # aggregate simulation monitors; time in the queue of files, and number of files in the queue
    # ... and separate monitors for each file type; number of files in the queue

    for i in range (0,14):
        animateMonitor(i)

    global nserversLast, filesCoLast, coMinutesLast, filesDkLast, dkMinutesLast, filesMaLast, maMinutesLast, filesNjLast, njMinutesLast, filesRdLast, rdMinutesLast
    global filesSvLast, svMinutesLast, filesTgLast, tgMinutesLast, filesWtLast, wtMinutesLast, devWtLast, meanWtLast, filesAaLast, aaMinutesLast
    global filesMeLast, meMinutesLast, filesTiLast, tiMinutesLast, filesFsLast, fsMinutesLast, timeWindowYearsLast
    global lowProbLast, medProbLast, highProbLast, vHighProbLast, dkTansferTimeLast

    xSlider = 50
    ySlider = -47.5

    def setFilesAa(val):
        global filesAaLast
        global filesAa
        global iatAa
        filesAa = float(val)
        if filesAa != filesAaLast:
            filesAaLast = filesAa
            iatAa = 1/((filesAa*12)/daysPerYear)

    def setFilesMe(val):
        global filesMeLast
        global filesMe
        global iatMe
        filesMe = float(val)
        if filesMe != filesMeLast:
            filesMeLast = filesMe
            iatMe = 1/((filesMe*12)/daysPerYear)

    def setFilesTi(val):
        global filesTiLast
        global filesTi
        global iatTi
        filesTi = float(val)
        if filesTi != filesTiLast:
            filesTiLast = filesTi
            iatTi = 1/((filesTi*12)/daysPerYear)

    def setFilesFs(val):
        global filesFsLast
        global filesFs
        global iatFs
        filesFs = float(val)
        if filesFs != filesFsLast:
            filesFsLast = filesFs
            iatFs = 1/((filesFs*12)/daysPerYear)

    def setNservers(val):
        global nserversLast
        global nservers
        nservers = float(val)
        if nservers != nserversLast:
            nserversLast = nservers

    def setCoServerTime(val):
        global coMinutesLast, coMinutes, coServerTime
        coMinutes = float(val)
        if coMinutes != coMinutesLast:
            coMinutesLast = coMinutes
            coServerTime = (1/((1/coMinutes)*(60/1)*(8/1)))*nservers

    def setTimeWindowYears(val):
        global timeWindowYearsLast
        global timeWindowYears
        global timeWindow
        global daysPerYear
        timeWindowYears = float(val)
        if timeWindowYears != timeWindowYearsLast:
            timeWindowYearsLast = timeWindowYears
            timeWindow = timeWindowYears*daysPerYear

    def setFilesCo(val):
        global filesCoLast
        global filesCo
        global iatCo
        filesCo = float(val)
        if filesCo != filesCoLast:
            filesCoLast = filesCo
            iatCo = 1/((filesCo*12)/daysPerYear)

    def setDevWt(val):
        global devWtLast
        global devWt
        devWt = float(val)
        if devWt != devWtLast:
            devWtLast = devWt

    def setMeanWt(val):
        global meanWtLast
        global meanWt
        meanWt = float(val)
        if meanWt != meanWtLast:
            meanWtLast = meanWt

    def setFilesWt(val):
        global filesWtLast
        global filesWt
        global iatWt
        filesWt = float(val)
        if filesWt != filesWtLast:
            filesWtLast = filesWt
            iatWt = 1/((filesWt*12)/daysPerYear)

    def setFilesTg(val):
        global filesTgLast
        global filesTg
        global iatTg
        filesTg = float(val)
        if filesTg != filesTgLast:
            filesTgLast = filesTg
            iatTg = 1/((filesTg*12)/daysPerYear)

    def setFilesSv(val):
        global filesSvLast
        global filesSv
        global iatSv
        filesSv = float(val)
        if filesSv != filesSvLast:
            filesSvLast = filesSv
            iatSv = 1/((filesSv*12)/daysPerYear)

    def setFilesRd(val):
        global filesRdLast
        global filesRd
        global iatRd
        filesRd = float(val)
        if filesRd != filesRdLast:
            filesRdLast = filesRd
            iatRd = 1/((filesRd*12)/daysPerYear)

    def setFilesNj(val):
        global filesNjLast
        global filesNj
        global iatNj
        filesNj = float(val)
        if filesNj != filesNjLast:
            filesNjLast = filesNj
            iatNj = 1/((filesNj*12)/daysPerYear)

    def setFilesMa(val):
        global filesMaLast
        global filesMa
        global iatMa
        filesMa = float(val)
        if filesMa != filesMaLast:
            filesMaLast = filesMa
            iatMa = 1/((filesMa*12)/daysPerYear)

    def setFilesDk(val):
        global filesDkLast
        global filesDk
        global iatDk
        filesDk = float(val)
        if filesDk != filesDkLast:
            filesDkLast = filesDk
            iatDk = 1/((filesDk*12)/daysPerYear)

    def setFilesCo(val):
        global filesCoLast
        global filesCo
        global iatCo
        filesCo = float(val)
        if filesCo != filesCoLast:
            filesCoLast = filesCo
            iatCo = 1/((filesCo*12)/daysPerYear)

    def setDkServerTime(val):
        global dkMinutesLast, dkMinutes, dkServerTime
        dkMinutes = float(val)
        if dkMinutes != dkMinutesLast:
            dkMinutesLast = dkMinutes
            dkServerTime = (1/((1/dkMinutes)*(60/1)*(8/1)))

    def setMaServerTime(val):
        global maMinutesLast, maMinutes, maServerTime
        maMinutes = float(val)
        if maMinutes != maMinutesLast:
            maMinutesLast = maMinutes
            maServerTime = (1/((1/maMinutes)*(60/1)*(8/1)))

    def setNjServerTime(val):
        global njMinutesLast, njMinutes, njServerTime
        njMinutes = float(val)
        if njMinutes != njMinutesLast:
            njMinutesLast = njMinutes
            njServerTime = (1/((1/njMinutes)*(60/1)*(8/1)))

    def setAaServerTime(val):
        global aaMinutesLast, aaMinutes, aaServerTime
        aaMinutes = float(val)
        if aaMinutes != aaMinutesLast:
            aaMinutesLast = aaMinutes
            aaServerTime = (1/((1/aaMinutes)*(60/1)*(8/1)))

    def setMeServerTime(val):
        global meMinutesLast, meMinutes, meServerTime
        meMinutes = float(val)
        if meMinutes != meMinutesLast:
            meMinutesLast = meMinutes
            meServerTime = (1/((1/meMinutes)*(60/1)*(8/1)))

    def setRdServerTime(val):
        global rdMinutesLast, rdMinutes, rdServerTime
        rdMinutes = float(val)
        if rdMinutes != rdMinutesLast:
            rdMinutesLast = rdMinutes
            rdServerTime = (1/((1/rdMinutes)*(60/1)*(8/1)))

    def setSvServerTime(val):
        global svMinutesLast, svMinutes, svServerTime
        svMinutes = float(val)
        if svMinutes != svMinutesLast:
            svMinutesLast = svMinutes
            svServerTime = (1/((1/svMinutes)*(60/1)*(8/1)))

    def setTgServerTime(val):
        global tgMinutesLast, tgMinutes, tgServerTime
        tgMinutes = float(val)
        if tgMinutes != tgMinutesLast:
            tgMinutesLast = tgMinutes
            tgServerTime = (1/((1/tgMinutes)*(60/1)*(8/1)))

    def setWtServerTime(val):
        global wtMinutesLast, wtMinutes, wtServerTime
        wtMinutes = float(val)
        if wtMinutes != wtMinutesLast:
            wtMinutesLast = wtMinutes
            wtServerTime = (1/((1/wtMinutes)*(60/1)*(8/1)))

    def setTiServerTime(val):
        global tiMinutesLast, tiMinutes, tiServerTime
        tiMinutes = float(val)
        if tiMinutes != tiMinutesLast:
            tiMinutesLast = tiMinutes
            tiServerTime = (1/((1/tiMinutes)*(60/1)*(8/1)))

    def setFsServerTime(val):
        global fsMinutesLast, fsMinutes, fsServerTime
        fsMinutes = float(val)
        if fsMinutes != fsMinutesLast:
            fsMinutesLast = fsMinutes
            fsServerTime = (1/((1/fsMinutes)*(60/1)*(8/1)))

    def setLowProb(val):
        global lowProb, lowProbLast
        lowProb = float(val)
        if lowProb != lowProbLast:
            lowProbLast = lowProb

    def setMedProb(val):
        global medProb, medProbLast
        medProb = float(val)
        if medProb != medProbLast:
            medProbLast = medProb

    def setHighProb(val):
        global highProb, highProbLast
        highProb = float(val)
        if highProb != highProbLast:
            highProbLast = highProb

    def setVHighProb(val):
        global vHighProb, vHighProbLast
        vHighProb = float(val)
        if vHighProb != vHighProbLast:
            vHighProbLast = vHighProb

    def setDkTrans(val):
        global dkTransferTime, dkTansferTimeLast
        dkTransferTime = float(val)
        if dkTransferTime != dkTansferTimeLast:
            dkTansferTimeLast = dkTransferTime

    # Slider attribute values
    sliderLabels = ["Proc. FTE", "CO Minutes", "DK Minutes", "MA Minutes", "NJ Minutes", f"{nameAa} Minutes", f"{nameMe} Minutes", 
                    "RD Minutes", "SV Minutes", "TG Minutes", "WT Minutes", f"{nameTi} Minutes", f"{nameFs} Minutes", "Sim Years", 
                    "CO Files", "DK Files", "MA Files", "NJ Files", f"{nameAa} Files", f"{nameMe} Files", "RD Files", "SV Files", 
                    "TG Files", "WT Files", "WT Avg", "WT Dev", f"{nameTi} Files", f"{nameFs} Files", "Low", "Medium", "High", 
                    "Very High", "SIPR Xfer"]
    
    sliderXvalue = [0, 100, 170, 240, 310, 380, 450,
                    520, 590, 660, 755, 920, 990, 1225,
                    100, 170, 240, 310, 380, 450, 520, 590, 
                    660, 755, 825, 825, 920, 990, 1350, 1350, 
                    1350, 1350, 1350]
    
    sliderYvalue = [25, 25, 25, 25, 25, 25, 25, 
                    25, 25, 25, 25, 25, 25, 25, 
                    -35, -35, -35, -35, -35, -35, -35, -35, 
                    -35, -35, 25, -35, -35, -35, -145, -205, 
                    -255, -325, -445]
    
    sliderVar = [nservers, coMinutes, dkMinutes, maMinutes, njMinutes, aaMinutes, meMinutes, 
                rdMinutes, svMinutes, tgMinutes, wtMinutes, tiMinutes, fsMinutes, timeWindowYears, 
                filesCo, filesDk, filesMa, filesNj, filesAa, filesMe, filesRd, filesSv, 
                filesTg, filesWt, meanWt, devWt, filesTi, filesFs, lowProb, medProb,
                highProb, vHighProb, dkTransferTime]
            
    sliderRes = [0.25, 5, 5, 5, 5, 5, 5, 
                5, 5, 5, 5, 5, 5, 1/12, 
                1, 1, 1, 1, 1, 1, 1, 1, 
                1, 1, 1, 0.25, 1, 1, 0.1, 0.1,
                0.1, 0.1, 0.1]
    
    sliderMin = [1, 5, 5, 5, 5, 5, 5, 
                5, 5, 5, 5, 5, 5, 1/12, 
                0, 0, 0, 0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0]
    
    sliderMax = [8, 900, 900, 900, 900, 900, 900, 
                900, 900, 900, 900, 900, 900, 10, 
                900, 900, 900, 900, 900, 900, 900, 900, 
                900, 900, 900, 900, 900, 900, 100, 100,
                100, 100, 10]
    
    sliderAction = [setNservers, setCoServerTime, setDkServerTime, setMaServerTime, setNjServerTime, setAaServerTime, setMeServerTime, 
                    setRdServerTime, setSvServerTime, setTgServerTime, setWtServerTime, setTiServerTime, setFsServerTime, setTimeWindowYears, 
                    setFilesCo, setFilesDk, setFilesMa, setFilesNj, setFilesAa, setFilesMe, setFilesRd, setFilesSv, 
                    setFilesTg, setFilesWt, setMeanWt, setDevWt, setFilesTi, setFilesFs, setLowProb, setMedProb,
                    setHighProb, setVHighProb, setDkTrans]   

    nserversLast = nservers
    coMinutesLast = coMinutes
    filesCoLast = filesCo
    dkMinutesLast = dkMinutes
    filesDkLast = filesDk
    maMinutesLast = maMinutes
    filesMaLast = filesMa
    njMinutesLast = njMinutes
    filesNjLast = filesNj
    aaMinutesLast = aaMinutes
    filesAaLast = filesAa
    meMinutesLast = meMinutes
    filesMeLast = filesMe
    rdMinutesLast = rdMinutes
    filesRdLast = filesRd
    svMinutesLast = svMinutes
    filesSvLast = filesSv
    tgMinutesLast = tgMinutes
    filesTgLast = filesTg
    wtMinutesLast = wtMinutes
    filesWtLast = filesWt
    tiMinutesLast = tiMinutes
    filesTiLast = filesTi
    fsMinutesLast = fsMinutes
    filesFsLast = filesFs
    timeWindowYearsLast = timeWindowYears
    meanWtLast = meanWt
    devWtLast = devWt
    lowProbLast = lowProb
    medProbLast = medProb
    highProbLast = highProb
    vHighProbLast = vHighProb
    dkTansferTimeLast = dkTransferTime

    # Sliders to display and/or change parameter values and restart the simulation
    for i in range (0, 33):
        sim.AnimateSlider(
            x=xSlider+sliderXvalue[i],
            y=ySlider+sliderYvalue[i],
            width=60,
            height=20,
            fontsize=10,
            vmin=sliderMin[i],
            vmax=sliderMax[i],
            resolution=sliderRes[i],
            v=sliderVar[i],
            label=sliderLabels[i],
            action=sliderAction[i],
            xy_anchor="nw"
        )

    # Button to restart simulation if parameter values are changed
    if lowProb+medProb+highProb+vHighProb == 100:
        sim.AnimateButton(
                x=xSlider+1225,
                y=ySlider-85,
                width=175,
                fontsize=20,
                fillcolor="20%gray",
                color="snow",
                text="Restart Simulation",
                action=runSimulation,
                xy_anchor="nw"
        )
    else:
        showErrorWindow("Probabilities must add to 100%")
'''
Generates files for the queue by filetype if (and only if) the file type's inter-arrival time (iat) is
greater than zero.  iat = 0 represents file types not being processed for the current simulation
'''

def dataFileGenerator():
    global qCo, qDk, qMa, qNj, qRd, qSv, qTg, qWt, qAa, qTi, qMe, qFs, filePriority
    filePriority = sim.Pdf((4, 3, 2, 1), (lowProb, medProb, highProb, vHighProb))

    if iatCo != 0: 
        qCo = sim.ComponentGenerator(dataFile, i = 0, id = "red", name= "CO", iat = sim.Exponential(iatCo).sample)
    if iatDk != 0: 
        qDk = sim.ComponentGenerator(dataFile, i = 1, id = "yellow", name="DK", iat = sim.Exponential(iatDk).sample)
    if iatMa != 0: 
        qMa = sim.ComponentGenerator(dataFile, i = 2, id = "blue", name="MA", iat = sim.Exponential(iatMa).sample)
    if iatNj != 0: 
        qNj = sim.ComponentGenerator(dataFile, i = 3, id = "orange", name="NJ", iat = sim.Exponential(iatNj).sample)
    if iatRd != 0: 
        qRd = sim.ComponentGenerator(dataFile, i = 4, id = "green", name="RD", iat = sim.Exponential(iatRd).sample)
    if iatSv != 0: 
        qSv = sim.ComponentGenerator(dataFile, i = 5, id = "purple", name="SV", iat = sim.Exponential(iatSv).sample)
    if iatTg != 0: 
        qTg = sim.ComponentGenerator(dataFile, i = 6, id = "peru", name="TG", iat = sim.Exponential(iatTg).sample)
    if iatWt != 0: 
        #for loop to add WT batch arrival behavior
        for i in range (1, int(sim.Normal(meanWt, devWt).bounded_sample(lowerbound=0))): 
            qWt = sim.ComponentGenerator(dataFile, i = 7, id = "teal", name="WT", iat = sim.IntUniform(5, 5).sample)
    if iatAa != 0: 
        qAa = sim.ComponentGenerator(dataFile, i = 8, id = "tomato", name="AA", iat = sim.Exponential(iatAa).sample)
    if iatTi != 0: 
        qTi = sim.ComponentGenerator(dataFile, i = 9, id = "goldenrod", name="TI", iat = sim.Exponential(iatTi).sample)
    if iatMe != 0: 
        qMe = sim.ComponentGenerator(dataFile, i = 10, id = "yellowgreen", name="ME", iat = sim.Exponential(iatMe).sample)
    if iatFs != 0: 
        qFs = sim.ComponentGenerator(dataFile, i = 11, id = "violet", name="FS", iat = sim.Exponential(iatFs).sample)


class dataFile(sim.Component): 
    def setup(self, i, id):
        self.i=i
        self.id = id
        self.fileRequest = fileRequest[i]
        self.serverTime = serverTime[i]
        self.fileQueue = fileQueue[i]
        self.filePriority = filePriority.sample()

    def animation_objects(self):
        if id == 'text':
            ao0 = sim.AnimateText(text=self.name(), textcolor='fg', text_anchor='nw')
            return 0, 16, ao0
        else:
            ao0 = sim.AnimateRectangle((0, 0, 30, 30),
                text=self.name(), fillcolor=self.id, textcolor='black', fontsize=10, arg=self)
            return 40, 40, ao0
   
    def process(self):
        # File hold process (130i and No New Data)
        holdP = sim.Pdf(("Yes", "No"), (1.2, 98.8)).sample()
        if holdP == "Yes":
            rHold = sim.Normal(81, 10.25).bounded_sample(0) # mean = 90 Calendar days; Std Dev = 10.25 Calendar days
            if rHold <= 10: # Files held for more than ten days are counted as no new data (queue renege)
                self.hold(rHold)
            else:
                self.leave()
        
        # Drake file hold process (SIPR -> NIPR)
        if self.name() == "DK":
            self.hold(sim.Normal(1, .5).bounded_sample(0))
        
        # Enter queues system and request an analyst for data ingestion
        self.enter(system)
        self.enter(self.fileQueue)
        self.request(servers)    
        self.request(self.fileRequest)     
       
        # Ingest data
        self.hold(sim.Exponential(self.serverTime).sample())
        self.release(self.fileRequest)
        self.leave()

def runSimulation():
    global env, system, fileRequest, serverTime, fileQueue, noNewData
    global servers, fileCo, fileDk, fileMa, fileNj, fileRd, fileSv
    global fileTg, fileWt, fileAa, fileTi, fileMe, fileFs
    global sysCo, sysDk, sysMa, sysNj, sysRd, sysSv, sysTg, sysWt, sysAa, sysTi, sysMe, sysFs

    env = sim.Environment(time_unit = "days")
    system = sim.Queue(name = "system")
    sysCo = sim.Queue(name = "sysCo")
    sysDk = sim.Queue(name = "sysDk")
    sysMa = sim.Queue(name = "sysMa")
    sysNj = sim.Queue(name = "sysNj")
    sysRd = sim.Queue(name = "sysRd")
    sysSv = sim.Queue(name = "sysSv")
    sysTg = sim.Queue(name = "sysTg")
    sysWt = sim.Queue(name = "sysWt")
    sysAa = sim.Queue(name = "sysAa")
    sysTi = sim.Queue(name = "sysTi")
    sysMe = sim.Queue(name = "sysMe")
    sysFs = sim.Queue(name = "sysFs")

    servers = sim.Resource(name="servers", capacity=nservers, preemptive=True)
    fileCo = sim.Resource(name = "fileCo", capacity = sim.inf)
    fileDk = sim.Resource(name = "fileDk", capacity = sim.inf)
    fileMa = sim.Resource(name = "fileMa", capacity = sim.inf)
    fileNj = sim.Resource(name = "fileNj", capacity = sim.inf)
    fileRd = sim.Resource(name = "fileRd", capacity = sim.inf)
    fileSv = sim.Resource(name = "fileSv", capacity = sim.inf)
    fileTg = sim.Resource(name = "fileTg", capacity = sim.inf)
    fileWt = sim.Resource(name = "fileWt", capacity = sim.inf)
    fileAa = sim.Resource(name = "fileAa", capacity = sim.inf)
    fileTi = sim.Resource(name = "fileTi", capacity = sim.inf)
    fileMe = sim.Resource(name = "fileMe", capacity = sim.inf)
    fileFs = sim.Resource(name = "fileFs", capacity = sim.inf)

    dataFileGenerator()

    fileRequest = [fileCo, fileDk, fileMa, fileNj, fileRd, fileSv, fileTg, fileWt, fileAa, 
        fileTi, fileMe, fileFs]
    
    fileQueue = [sysCo, sysDk, sysMa, sysNj, sysRd, sysSv, sysTg, sysWt, sysAa, sysTi, sysMe, sysFs]
    
    serverTime = [coServerTime, dkServerTime, maServerTime, njServerTime, rdServerTime, svServerTime, tgServerTime,
                  wtServerTime, aaServerTime, tiServerTime, meServerTime, fsServerTime]

    do_animation()

    env.run(till=timeWindow)

    # Generate data plots
    plotXlabel = ["Length of Time in the Queue (Days)", "Queue Length", "CO-Queue Length", "DK-Queue Length",
        "MA-Queue Length", "NJ-Queue Length", "AA-Queue Length", "ME-Queue Length", "RD-Queue Length",
        "SV-Queue Length", "TG-Queue Length", "WT-Queue Length", "TI-Queue Length", "FS-Queue Length"]

    fileNamePrefix = ["Length_of_Stay_", "System_Queue_Length_", "CO_Queue_length_", 
        "DK_Queue_length_", "MA_Queue_length_", "NJ_Queue_length_", "AA_Queue_length_",
        "ME_Queue_length_", "RD_Queue_length_", "SV_Queue_length_", "TG_Queue_length_", 
        "WT_Queue_length_", "TI_Queue_length_",  "FS_Queue_length_"]

    fileNameSuffix = ["Hist", "Box", "Stair"]

    for i in range(0,len(monitorColor)):       
        sysLen = []; sysLen = monitorType[i].tx(); sysLen = [float(e) for e in sysLen[1]]
        j = 0
        systemHistPlot(sysLen, plotXlabel[i], "Number of Days", fileNamePrefix[i]+fileNameSuffix[j], monitorColor[i], simFileName); j=+1
        systemBoxPlot(sysLen, plotXlabel[i], fileNamePrefix[i]+fileNameSuffix[j], monitorColor[i], simFileName); j+=1
        systemStairPlot(sysLen, "Files Over Time", plotXlabel[i], fileNamePrefix[i]+fileNameSuffix[j], monitorColor[i], simFileName); j+=1

    # Generate data files (.csv)
    fileList = ["SYS_Files", "CO_Files", "DK_Files", "MA_Files", "NJ_Files", "AA_Files", "ME_Files", "RD_Files",
                "SV_Files", "TG_Files", "WT_Files", "TI_Files", "FS_Files"]
    
    stayList = ["SYS_Stay", "CO_Stay", "DK_Stay", "MA_Stay", "NJ_Stay", "AA_Stay", "ME_Stay", "RD_Stay", 
                "SV_Stay", "TG_Stay", "WT_Stay", "TI_Stay", "FS_Stay"]

    fileMonitorList = [system.length, sysCo.length, sysDk.length, sysMa.length, sysNj.length, sysAa.length, sysMe.length, sysRd.length, 
                       sysSv.length, sysTg.length, sysWt.length, sysTi.length, sysFs.length]
    
    stayMonitorList = [system.length_of_stay, sysCo.length_of_stay, sysDk.length_of_stay, sysMa.length_of_stay, 
                       sysNj.length_of_stay, sysAa.length_of_stay, sysMe.length_of_stay, sysRd.length_of_stay, sysSv.length_of_stay, 
                       sysTg.length_of_stay, sysWt.length_of_stay, sysTi.length_of_stay, sysFs.length_of_stay]

    for i in range(0, len(fileList)):
        sysLen = fileMonitorList[i].tx()
        csvExport(fileList[i], sysLen)
        formatFileData(fileList[i]+".csv")

    for i in range(0, len(stayList)):
        sysLen = stayMonitorList[i].tx()
        csvExport(stayList[i], sysLen)
        formatStayData(stayList[i]+".csv")

    createFileDataMaster(fileList)
    createStayDataMaster(stayList)

    env.video_close()

    # Generate report tables
    iatValues = [iatAa, iatCo, iatDk, iatFs, iatMa, iatMe, iatNj, iatRd, iatSv, iatTg, iatTi, iatWt]
    boxColorList = ["white", "tomato", "red", "yellow", "violet", "blue", "goldenrod", "orange", "green", "purple", "peru", "yellowgreen", "teal"]

    queueStats = []
    k = 0
    sysFile = createFilesStats("SYS_Stay", timeWindow, boxColorList[k]); queueStats.append(sysFile); k+=1
    sysQueue = createQueueStats("SYS_Files"); queueStats.append(sysQueue)
    sysStay = createStayStats("SYS_Stay"); queueStats.append(sysStay)

    aaFile = createFilesStats("AA_Stay", timeWindow, boxColorList[k]); queueStats.append(aaFile); k+=1
    aaQueue = createQueueStats("AA_Files"); queueStats.append(aaQueue)
    aaStay = createStayStats("AA_Stay"); queueStats.append(aaStay)

    coFile = createFilesStats("CO_Stay", timeWindow, boxColorList[k]); queueStats.append(coFile); k+=1
    coQueue = createQueueStats("CO_Files"); queueStats.append(coQueue)
    coStay = createStayStats("CO_Stay"); queueStats.append(coStay)

    dkFile = createFilesStats("DK_Stay", timeWindow, boxColorList[k]); queueStats.append(dkFile); k+=1
    dkQueue = createQueueStats("DK_Files"); queueStats.append(dkQueue)
    dkStay = createStayStats("DK_Stay"); queueStats.append(dkStay)

    fsFile = createFilesStats("FS_Stay", timeWindow, boxColorList[k]); queueStats.append(fsFile); k+=1
    fsQueue = createQueueStats("FS_Files"); queueStats.append(fsQueue)
    fsStay = createStayStats("FS_Stay"); queueStats.append(fsStay)

    maFile = createFilesStats("MA_Stay", timeWindow, boxColorList[k]); queueStats.append(maFile); k+=1
    maQueue = createQueueStats("MA_Files"); queueStats.append(maQueue)
    maStay = createStayStats("MA_Stay"); queueStats.append(maStay)
    
    meFile = createFilesStats("ME_Stay", timeWindow, boxColorList[k]); queueStats.append(meFile); k+=1
    meQueue = createQueueStats("ME_Files"); queueStats.append(meQueue)
    meStay = createStayStats("ME_Stay"); queueStats.append(meStay)

    njFile = createFilesStats("NJ_Stay", timeWindow, boxColorList[k]); queueStats.append(njFile); k+=1
    njQueue = createQueueStats("NJ_Files"); queueStats.append(njQueue)
    njStay = createStayStats("NJ_Stay"); queueStats.append(njStay)

    rdFile = createFilesStats("RD_Stay", timeWindow, boxColorList[k]); queueStats.append(rdFile); k+=1
    rdQueue = createQueueStats("RD_Files"); queueStats.append(rdQueue)
    rdStay = createStayStats("RD_Stay"); queueStats.append(rdStay)

    svFile = createFilesStats("SV_Stay", timeWindow, boxColorList[k]); queueStats.append(svFile); k+=1
    svQueue = createQueueStats("SV_Files"); queueStats.append(svQueue)
    svStay = createStayStats("SV_Stay"); queueStats.append(svStay)

    tgFile = createFilesStats("TG_Stay", timeWindow, boxColorList[k]); queueStats.append(tgFile); k+=1
    tgQueue = createQueueStats("TG_Files"); queueStats.append(tgQueue)
    tgStay = createStayStats("TG_Stay"); queueStats.append(tgStay)

    tiFile = createFilesStats("TI_Stay", timeWindow, boxColorList[k]); queueStats.append(tiFile); k+=1
    tiQueue = createQueueStats("TI_Files"); queueStats.append(tiQueue)
    tiStay = createStayStats("TI_Stay"); queueStats.append(tiStay)

    wtFile = createFilesStats("WT_Stay", timeWindow, boxColorList[k]); queueStats.append(wtFile); k+=1
    wtQueue = createQueueStats("WT_Files"); queueStats.append(wtQueue)
    wtStay = createStayStats("WT_Stay"); queueStats.append(wtStay)

    simEndValues = []
    simEndValues.append(simFileName)
    simEndValues.append(nservers)
    simEndValues.append(coMinutes)
    simEndValues.append(filesCo)
    simEndValues.append(iatCo)
    simEndValues.append(dkMinutes)
    simEndValues.append(filesDk)
    simEndValues.append(iatDk)
    simEndValues.append(maMinutes)
    simEndValues.append(filesMa)
    simEndValues.append(iatMa)
    simEndValues.append(njMinutes)
    simEndValues.append(filesNj)
    simEndValues.append(iatNj)
    simEndValues.append(rdMinutes)
    simEndValues.append(filesRd)
    simEndValues.append(iatRd)
    simEndValues.append(svMinutes)
    simEndValues.append(filesSv)
    simEndValues.append(iatSv)
    simEndValues.append(tgMinutes)
    simEndValues.append(filesTg)
    simEndValues.append(iatTg)
    simEndValues.append(wtMinutes)
    simEndValues.append(filesWt)
    simEndValues.append(iatWt)
    simEndValues.append(meanWt)
    simEndValues.append(devWt)
    simEndValues.append(nameAa)
    simEndValues.append(aaMinutes)
    simEndValues.append(filesAa)
    simEndValues.append(iatAa)
    simEndValues.append(nameTi)
    simEndValues.append(tiMinutes)
    simEndValues.append(filesTi)
    simEndValues.append(iatTi)
    simEndValues.append(nameMe)
    simEndValues.append(meMinutes)
    simEndValues.append(filesMe)
    simEndValues.append(iatMe)
    simEndValues.append(nameFs)
    simEndValues.append(fsMinutes)
    simEndValues.append(filesFs)
    simEndValues.append(iatFs)
    simEndValues.append(timeWindowYears)
    simEndValues.append(timeWindow)

    getFileName(simFileName, iatValues, queueStats, simEndValues)

if __name__ == "__main__":   
    # Declare parameter variables
    daysPerYear = 365
    daysPerYear = daysPerYear - 104 # Weekends
    daysPerYear = daysPerYear - 12 # Federal Holidays
    timeWindow = daysPerYear
    timeWindowYears = 1
    timeWindow = 22

    simFileName = "testFile"
    nservers = 3
    coMinutes = 60
    coServerTime = (1/((1/coMinutes)*(60/1)*(8/1)))
    filesCo = 14
    iatCo = 1/((filesCo*12)/daysPerYear)
    dkMinutes = 540
    dkServerTime = (1/((1/dkMinutes)*(60/1)*(8/1)))
    filesDk = 3
    iatDk = 1/((filesDk*12)/daysPerYear)
    maMinutes = 60
    maServerTime = (1/((1/maMinutes)*(60/1)*(8/1)))
    filesMa = 1
    iatMa = 1/((filesMa*12)/daysPerYear)
    njMinutes = 60
    njServerTime = (1/((1/njMinutes)*(60/1)*(8/1)))
    filesNj = 101
    iatNj = 1/((filesNj*12)/daysPerYear)
    rdMinutes = 60
    rdServerTime = (1/((1/rdMinutes)*(60/1)*(8/1)))
    filesRd = 1
    iatRd = 1/((filesRd*12)/daysPerYear)
    svMinutes = 30
    svServerTime = (1/((1/svMinutes)*(60/1)*(8/1)))
    filesSv = 2
    iatSv = 1/((filesSv*12)/daysPerYear)
    tgMinutes = 30
    tgServerTime = (1/((1/tgMinutes)*(60/1)*(8/1)))
    filesTg = 1
    iatTg = 1/((filesTg*12)/daysPerYear)
    wtMinutes = 10
    wtServerTime = (1/((1/wtMinutes)*(60/1)*(8/1)))
    filesWt = 130
    iatWt = 1/((filesWt*12)/daysPerYear)
    meanWt = 30
    devWt = 20.1
    nameAa = "AA"
    aaMinutes = 90
    aaServerTime = (1/((1/aaMinutes)*(60/1)*(8/1)))
    filesAa = 0
    iatAa = 0
    nameTi = "TI"
    tiMinutes = 120
    tiServerTime = (1/((1/tiMinutes)*(60/1)*(8/1)))
    filesTi = 0
    iatTi = 0
    nameMe = "ME"
    meMinutes = 120
    meServerTime = (1/((1/meMinutes)*(60/1)*(8/1)))
    filesMe = 0
    iatMe = 0
    nameFs = "FS"
    fsMinutes = 120
    fsServerTime = (1/((1/fsMinutes)*(60/1)*(8/1)))
    filesFs = 0
    iatFs = 0
    lowProb = 0.1
    medProb = 67.4
    highProb = 30.0
    vHighProb = 2.5
    dkTransferTime = 1


    runSimulation()
