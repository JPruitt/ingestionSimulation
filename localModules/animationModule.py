#Global Packages
import salabim as sim
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt

# Local Modules
from plottingModule import systemHistPlot, systemBoxPlot, systemStairPlot, systemMultiLinePlot
from reportGeneratingModule import create_analytics_report

def setParameterValues(parameterList):
    global nservers, filesCo, iatCo, filesDk, iatDk
    global filesMa, iatMa, filesNj, iatNj, filesRd, iatRd, filesSv, iatSv, filesTg, iatTg
    global filesWt, iatWt, meanWt, devWt, nameAa, filesAa, iatAa, nameTi, filesTi, iatTi
    global nameMe, filesMe, iatMe, nameFs, filesFs, iatFs
    global timeWindowYears, daysPerYear, timeWindow, simFileName
    global coServerTime, coMinutes, dkServerTime, dkMinutes, maServerTime, maMinutes, njServerTime, njMinutes, rdServerTime, rdMinutes, svServerTime, svMinutes
    global tgServerTime, tgMinutes, wtServerTime, wtMinutes, aaServerTime, aaMinutes, tiServerTime, tiMinutes, meServerTime, meMinutes, fsServerTime, fsMinutes

    paramValues = parameterList
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

    runSimulation()

def do_animation():
    global nserversLast, filesCoLast, filesDkLast, filesMaLast, filesNjLast, filesRdLast
    global coMinutesLast, dkMinutesLast, maMinutesLast, njMinutesLast, rdMinutesLast, svMinutesLast
    global tgMinutesLast, wtMinutesLast, aaMinutesLast, tiMinutesLast, meMinutesLast, fsMinutesLast
    global filesSvLast, filesTgLast, filesWtLast, meanWtLast, devWtLast, timeWindowYearsLast
    global filesAaLast, filesTiLast, filesMeLast, filesFsLast

    xSlider = 50
    ySlider = -47.5

    simHeight = 1150
    simWidth = 1500
    xMonitor = 50
    yMonitor = 900
    
    videoFilePath = "./capDevDataIngestSim/video/"

    # set global animation parameters    
    env.animation_parameters(
        animate = True,
        speed=4, 
        background_color="30%gray",
        height = simHeight,
        width = simWidth, 
        modelname = "CapDev Data Ingestion Process Model",
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

    # Queue  animation
    env.animate_debug(True)
    sim.AnimateQueue(servers.requesters(), x=1350, y=75, title="", direction="w")
    sim.AnimateQueue(servers.claimers(), x=1450, y=75, direction="n", title="")
    

    def animateMonitor(j):

        global monitorType, monitorColor
        # creates 14 animated monitors from lists of monitor parameter values

        monitorType = [system.length_of_stay, servers.requesters().length, fileCo.requesters().length, 
            fileDk.requesters().length, fileMa.requesters().length, fileNj.requesters().length, fileAa.requesters().length,
            fileMe.requesters().length, fileRd.requesters().length, fileSv.requesters().length, fileTg.requesters().length,
            fileWt.requesters().length, fileTi.requesters().length, fileFs.requesters().length]
        
        xOffset = [0, 0, 0, 0, 0, 0, 0, 0, 675, 675, 675, 675, 675, 675]
        
        yOffset = [-50, -150, -250, -350, -450, -550, -650, -750, -250, -350, -450, -550, -650, -750]
        
        wOffset = [-200, -200, -875, -875, -875, -875, -875, -875, -875, -875, -875, -875, 
            -875, -875]
        
        monitorColor = ["white", "white", "red", "yellow", "blue", "orange", "tomato", "goldenrod",
            "green", "purple", "peru", "teal", "yellowgreen", "violet"]

        monitorTitle = ["Time in data file queue.  Mean ={:10.2f}", "Number of data files in the queue.  Mean ={:10.2f}", 
            "Number of Corian (CO) files in the queue. Mean ={:10.2f}", "Number of Duke (DK) files in the queue. Mean ={:10.2f}", 
            "Number of L-Madis (MA) files in the queue. Mean ={:10.2f}", "Number of Ninja (NJ) files in the queue. Mean ={:10.2f}",
            "Number of Aerial Armor files in the queue. Mean ={:10.2f}", "Number of Medusa files in the queue. Mean ={:10.2f}",
            "Number of RD-SUADS (RD) files in the queue. Mean ={:10.2f}", "Number of Skyview (SV) files in the queue. Mean ={:10.2f}",
            "Number of TGS (TG) files in the queue. Mean ={:10.2f}", "Number of Windtalker (WT) files in the queue. Mean ={:10.2f}",
            "Number of Titan files in the queue. Mean ={:10.2f}", "Number of FS/MLIDS files in the queue. Mean ={:10.2f}"]
      
        sim.AnimateMonitor(
            monitorType[j],
            linewidth= 2,
            x = xMonitor + xOffset[j],
            y = yMonitor + yOffset[j],
            height=75,
            width=env.width() + wOffset[j],
            linecolor=monitorColor[j],
            horizontal_scale=10,
            title=lambda: monitorTitle[j].format(monitorType[j].mean()),
        )

    # aggregate simulation monitors; time in the queue of files, and number of files in the queue
    # ... and separate monitors for each file type; number of files in the queue

    for i in range (0,14):
        animateMonitor(i)

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
            dkServerTime = (1/((1/dkMinutes)*(60/1)*(8/1)))*nservers

    def setMaServerTime(val):
        global maMinutesLast, maMinutes, maServerTime
        maMinutes = float(val)
        if maMinutes != maMinutesLast:
            maMinutesLast = maMinutes
            maServerTime = (1/((1/maMinutes)*(60/1)*(8/1)))*nservers

    def setNjServerTime(val):
        global njMinutesLast, njMinutes, njServerTime
        njMinutes = float(val)
        if njMinutes != njMinutesLast:
            njMinutesLast = njMinutes
            njServerTime = (1/((1/njMinutes)*(60/1)*(8/1)))*nservers

    def setAaServerTime(val):
        global aaMinutesLast, aaMinutes, aaServerTime
        aaMinutes = float(val)
        if aaMinutes != aaMinutesLast:
            aaMinutesLast = aaMinutes
            aaServerTime = (1/((1/aaMinutes)*(60/1)*(8/1)))*nservers

    def setMeServerTime(val):
        global meMinutesLast, meMinutes, meServerTime
        meMinutes = float(val)
        if meMinutes != meMinutesLast:
            meMinutesLast = meMinutes
            meServerTime = (1/((1/meMinutes)*(60/1)*(8/1)))*nservers

    def setRdServerTime(val):
        global rdMinutesLast, rdMinutes, rdServerTime
        rdMinutes = float(val)
        if rdMinutes != rdMinutesLast:
            rdMinutesLast = rdMinutes
            rdServerTime = (1/((1/rdMinutes)*(60/1)*(8/1)))*nservers

    def setSvServerTime(val):
        global svMinutesLast, svMinutes, svServerTime
        svMinutes = float(val)
        if svMinutes != svMinutesLast:
            svMinutesLast = svMinutes
            svServerTime = (1/((1/svMinutes)*(60/1)*(8/1)))*nservers

    def setTgServerTime(val):
        global tgMinutesLast, tgMinutes, tgServerTime
        tgMinutes = float(val)
        if tgMinutes != tgMinutesLast:
            tgMinutesLast = tgMinutes
            tgServerTime = (1/((1/tgMinutes)*(60/1)*(8/1)))*nservers

    def setWtServerTime(val):
        global wtMinutesLast, wtMinutes, wtServerTime
        wtMinutes = float(val)
        if wtMinutes != wtMinutesLast:
            wtMinutesLast = wtMinutes
            wtServerTime = (1/((1/wtMinutes)*(60/1)*(8/1)))*nservers

    def setTiServerTime(val):
        global tiMinutesLast, tiMinutes, tiServerTime
        tiMinutes = float(val)
        if tiMinutes != tiMinutesLast:
            tiMinutesLast = tiMinutes
            tiServerTime = (1/((1/tiMinutes)*(60/1)*(8/1)))*nservers

    def setFsServerTime(val):
        global fsMinutesLast, fsMinutes, fsServerTime
        fsMinutes = float(val)
        if fsMinutes != fsMinutesLast:
            fsMinutesLast = fsMinutes
            fsServerTime = (1/((1/fsMinutes)*(60/1)*(8/1)))*nservers


# Sliders to display and/or change parameter values during the simulation
    sliderLabels = ["Proc. FTE", "CO Minutes", "DK Minutes", "MA Minutes", "NJ Minutes", "AA Minutes", "ME Minutes", 
                    "RD Minutes", "SV Minutes", "TG Minutes", "WT Minutes", "TI Minutes", "FS Minutes", "Sim Years", 
                    "CO Files", "DK Files", "MA Files", "NJ Files", "AA Files", "ME Files", "RD Files", "SV Files", 
                    "TG Files", "WT Files", "WT Avg", "WT Dev", "TI Files", "FS Files"]
    sliderXvalue = [0, 100, 170, 240, 310, 380, 450,
                    520, 590, 660, 730, 870, 940, 1225,
                    100, 170, 240, 310, 380, 450, 520, 590, 
                    660, 730, 800, 800, 870, 940]
    sliderYvalue = [-25, -25, -25, -25, -25, -25, -25, 
                    -25, -25, -25, -25, -25, -25, -25, 
                    -85, -85, -85, -85, -85, -85, -85, -85, 
                    -85, -85, -25, -85, -85, -85]
    sliderVar = [nservers, coMinutes, dkMinutes, maMinutes, njMinutes, aaMinutes, meMinutes, 
                 rdMinutes, svMinutes, tgMinutes, wtMinutes, tiMinutes, fsMinutes, timeWindowYears, 
                 filesCo, filesDk, filesMa, filesNj, filesAa, filesMe, filesRd, filesSv, 
                 filesTg, filesWt, meanWt, devWt, filesTi, filesFs]
    sliderRes = [0.25, 5, 5, 5, 5, 5, 5, 
                 5, 5, 5, 5, 5, 5, 1/12, 
                 5, 2, 2, 5, 2, 2, 2, 2, 
                 2, 5, 2, 0.5, 2, 2]
    sliderMin = [1, 5, 5, 5, 5, 5, 5, 
                 5, 5, 5, 5, 5, 5, 1/12, 
                 0, 0, 0, 0, 0, 0, 0, 0, 
                 0, 0, 0, 0, 0, 0]
    sliderMax = [8, 900, 900, 900, 900, 900, 900, 
                 900, 900, 900, 900, 900, 900, 5, 
                 300, 200, 200, 200, 200, 200, 200, 200, 
                 200, 300, 200, 100, 200, 200]
    sliderAction = [setNservers, setCoServerTime, setDkServerTime, setMaServerTime, setNjServerTime, setAaServerTime, setMeServerTime, 
                    setRdServerTime, setSvServerTime, setTgServerTime, setWtServerTime, setTiServerTime, setFsServerTime, setTimeWindowYears, 
                    setFilesCo, setFilesDk, setFilesMa, setFilesNj, setFilesAa, setFilesMe, setFilesRd, setFilesSv, 
                    setFilesTg, setFilesWt, setMeanWt, setDevWt, setFilesTi, setFilesFs]   

    nserversLast = nservers
    coMinutesLast = coMinutes
    dkMinutesLast = dkMinutes
    maMinutesLast = maMinutes
    njMinutesLast = njMinutes
    rdMinutesLast = rdMinutes
    svMinutesLast = svMinutes
    tgMinutesLast = tgMinutes
    wtMinutesLast = wtMinutes
    aaMinutesLast = aaMinutes
    tiMinutesLast = tiMinutes
    meMinutesLast = meMinutes
    fsMinutesLast = fsMinutes
    timeWindowYearsLast = timeWindowYears
    filesCoLast = filesCo
    filesDkLast = filesDk
    filesMaLast = filesMa
    filesNjLast = filesNj
    filesRdLast = filesRd
    filesSvLast = filesSv
    filesTgLast = filesTg
    filesWtLast = filesWt
    meanWtLast = meanWt
    devWtLast = devWt
    filesAaLast = filesAa
    filesFsLast = filesFs
    filesMeLast = filesMe
    filesTiLast = filesTi

    for i in range (0, 28):
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

    sim.AnimateButton(
            x=xSlider+1125,
            y=ySlider-100,
            width=175,
            fontsize=20,
            fillcolor="20%gray",
            color="snow",
            text="Restart Simulation",
            action=runSimulation,
            xy_anchor="nw"
    )

'''
Generates files for the queue by filetype if (and only if) the file type's inter-arrival time (iat) is
greater than zero.  iat = 0 represents file types not being processed for the current simulation
'''
def dataFileGenerator():
    low = 4; med = 3; hi = 2; vHi = 1
    lowP = 0.1; medP = 67.4; hiP = 30; vHiP = 2.5
    filePriority = sim.Pdf((low, med, hi, vHi), (lowP, medP, hiP, vHiP))

    if iatCo != 0: qCo = sim.ComponentGenerator(dataFile, i = 0, id = "red", name= "CO,", iat = sim.Exponential(iatCo).sample); qCo.priority = filePriority
    if iatDk != 0: qDk = sim.ComponentGenerator(dataFile, i = 1, id = "yellow", name="DK,", iat = sim.Exponential(iatDk).sample); qDk.priority = filePriority
    if iatMa != 0: qMa = sim.ComponentGenerator(dataFile, i = 2, id = "blue", name="MA,", iat = sim.Exponential(iatMa).sample); qMa.priority = filePriority
    if iatNj != 0: qNj = sim.ComponentGenerator(dataFile, i = 3, id = "orange", name="NJ,", iat = sim.Exponential(iatNj).sample); qNj.priority = filePriority
    if iatRd != 0: qRd = sim.ComponentGenerator(dataFile, i = 4, id = "green", name="RD,", iat = sim.Exponential(iatRd).sample); qRd.priority = filePriority
    if iatSv != 0: qSv = sim.ComponentGenerator(dataFile, i = 5, id = "purple", name="SV,", iat = sim.Exponential(iatSv).sample); qSv.priority = filePriority
    if iatTg != 0: qTg = sim.ComponentGenerator(dataFile, i = 6, id = "peru", name="TG,", iat = sim.Exponential(iatTg).sample); qTg.priority = filePriority
    if iatWt != 0: 
        # for loopp to add WT batch arrival behavior
        for i in range (1, int(sim.Normal(meanWt, devWt).bounded_sample(lowerbound=0))): 
            qWt = sim.ComponentGenerator(dataFile, i = 7, id = "teal", name="WT,", iat = sim.IntUniform(5, 5).sample); qWt.priority = filePriority 
    if iatAa != 0: qAa = sim.ComponentGenerator(dataFile, i = 8, id = "tomato", name="AA,", iat = sim.Exponential(iatAa).sample); qAa.priority = filePriority
    if iatTi != 0: qTi = sim.ComponentGenerator(dataFile, i = 9, id = "goldenrod", name="TI,", iat = sim.Exponential(iatTi).sample); qTi.priority = filePriority
    if iatMe != 0: qMe = sim.ComponentGenerator(dataFile, i = 10, id = "yellowgreen", name="ME,", iat = sim.Exponential(iatMe).sample); qMe.priority = filePriority
    if iatFs != 0: qFs = sim.ComponentGenerator(dataFile, i = 11, id = "violet", name="FS,", iat = sim.Exponential(iatFs).sample); qFs.priority = filePriority


class dataFile(sim.Component): 
    def setup(self, i, id):
        self.id = id
        self.fileRequest = fileRequest[i]
        self.serverTime = serverTime[i]

    def animation_objects(self, id):
        return super().animation_objects(id)

    def process(self):
        self.enter(system)    

        # Hold process
        holdP = sim.Pdf(("Yes", "No"), (1.2, 98.8)).sample()
        if holdP == "Yes":
            self.leave()
            self.hold(sim.Normal(95, 14.25).sample())
            self.enter(system)
        
        self.request(servers, self.fileRequest)     
        self.hold(sim.Exponential(self.serverTime).sample())
        self.release(self.fileRequest)
        self.leave()

def runSimulation():
    global env, system, fileRequest, serverTime
    global servers, fileCo, fileDk, fileMa, fileNj, fileRd, fileSv
    global fileTg, fileWt, fileAa, fileTi, fileMe, fileFs

    env = sim.Environment(time_unit = "days")
    system = sim.Queue(name = "system")

    servers = sim.Resource(name="servers", capacity=nservers)
    fileCo = sim.Resource(name = "fileCo", capacity = 999999)
    fileDk = sim.Resource(name = "fileDk", capacity = 999999)
    fileMa = sim.Resource(name = "fileMa", capacity = 999999)
    fileNj = sim.Resource(name = "fileNj", capacity = 999999)
    fileRd = sim.Resource(name = "fileRd", capacity = 999999)
    fileSv = sim.Resource(name = "fileSv", capacity = 999999)
    fileTg = sim.Resource(name = "fileTg", capacity = 999999)
    fileWt = sim.Resource(name = "fileWt", capacity = 999999)
    fileAa = sim.Resource(name = "fileAa", capacity = 999999)
    fileTi = sim.Resource(name = "fileTi", capacity = 999999)
    fileMe = sim.Resource(name = "fileMe", capacity = 999999)
    fileFs = sim.Resource(name = "fileFs", capacity = 999999)

    dataFileGenerator()

    fileRequest = [fileCo, fileDk, fileMa, fileNj, fileRd, fileSv, fileTg, fileWt, fileAa, 
        fileTi, fileMe, fileFs]
    
    serverTime = [coServerTime, dkServerTime, maServerTime, njServerTime, rdServerTime, svServerTime, tgServerTime,
                  wtServerTime, aaServerTime, tiServerTime, meServerTime, fsServerTime]

    do_animation()

    env.run(till=timeWindow)

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

    print(fileCo)

    env.video_close()

    create_analytics_report()

if __name__ == "__main__":   
    # Declare parameter variables
    daysPerYear = 365
    daysPerYear = daysPerYear - 104 # Weekends
    daysPerYear = daysPerYear - 12 # Federal Holidays
    timeWindow = daysPerYear
    timeWindowYears = 1
    timeWindow = 50

    simFileName = "testFile"
    nservers = 2
    coMinutes = 60
    coServerTime = (1/((1/coMinutes)*(60/1)*(8/1)))*nservers
    filesCo = 12
    iatCo = 1/((filesCo*12)/daysPerYear)
    dkMinutes = 540
    dkServerTime = (1/((1/dkMinutes)*(60/1)*(8/1)))*nservers
    filesDk = 1
    iatDk = 1/((filesDk*12)/daysPerYear)
    maMinutes = 45
    maServerTime = (1/((1/maMinutes)*(60/1)*(8/1)))*nservers
    filesMa = 1
    iatMa = 1/((filesMa*12)/daysPerYear)
    njMinutes = 30
    njServerTime = (1/((1/njMinutes)*(60/1)*(8/1)))*nservers
    filesNj = 76
    iatNj = 1/((filesNj*12)/daysPerYear)
    rdMinutes = 60
    rdServerTime = (1/((1/rdMinutes)*(60/1)*(8/1)))*nservers
    filesRd = 1
    iatRd = 1/((filesRd*12)/daysPerYear)
    svMinutes = 30
    svServerTime = (1/((1/svMinutes)*(60/1)*(8/1)))*nservers
    filesSv = 4
    iatSv = 1/((filesSv*12)/daysPerYear)
    tgMinutes = 60
    tgServerTime = (1/((1/tgMinutes)*(60/1)*(8/1)))*nservers
    filesTg = 1
    iatTg = 1/((filesTg*12)/daysPerYear)
    wtMinutes = 10
    wtServerTime = (1/((1/wtMinutes)*(60/1)*(8/1)))*nservers
    filesWt = 129
    iatWt = 1/((filesWt*12)/daysPerYear)
    meanWt = 30
    devWt = 20.1
    nameAa = "AA"
    aaMinutes = 90
    aaServerTime = (1/((1/aaMinutes)*(60/1)*(8/1)))*nservers
    filesAa = 0
    iatAa = 0
    nameTi = "TI"
    tiMinutes = 120
    tiServerTime = (1/((1/tiMinutes)*(60/1)*(8/1)))*nservers
    filesTi = 0
    iatTi = 0
    nameMe = "ME"
    meMinutes = 120
    meServerTime = (1/((1/meMinutes)*(60/1)*(8/1)))*nservers
    filesMe = 0
    iatMe = 0
    nameFs = "FS"
    fsMinutes = 120
    fsServerTime = (1/((1/fsMinutes)*(60/1)*(8/1)))*nservers
    filesFs = 0
    iatFs = 0

    runSimulation()
