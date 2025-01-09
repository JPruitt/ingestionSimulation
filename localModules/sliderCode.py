# Functions to capture and reassign parameter values from sliders
# Updating slider values restarts animation
def setFilesMe(val):
    global filesMeLast
    global filesMe
    filesMe = float(val)
    if filesMe != filesMeLast:
        filesMeLast = filesMe

def setFilesFs(val):
    global filesFsLast
    global filesFs
    filesFs = float(val)
    if filesFs != filesFsLast:
        filesFsLast = filesFs

def setFilesAa(val):
    global filesAaLast
    global filesAa
    filesAa = float(val)
    if filesAa != filesAaLast:
        filesAaLast = filesAa

def setFilesTi(val):
    global filesTiLast
    global filesTi
    filesTi = float(val)
    if filesTi != filesTiLast:
        filesTiLast = filesTi

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

def setTimeWindowYears(val):
    global timeWindowYearsLast
    global timeWindowYears
    global timeWindow
    global daysPerYear
    timeWindowYears = float(val)
    if timeWindowYears != timeWindowYearsLast:
        timeWindowYearsLast = timeWindowYears
        timeWindow = timeWindowYears*daysPerYear

def setFilesServerTime(val):
    global filesServerTimeLast
    global filesServerTime
    global serverTime
    filesServerTime = float(val)
    if filesServerTime != filesServerTimeLast:
        filesServerTimeLast = filesServerTime
        serverTime = 1/(((filesServerTime*12)/daysPerYear)/nservers)
    
def setNservers(val):
    global nserversLast
    global nservers
    nservers = float(val)
    if nservers != nserversLast:
        nserversLast = nservers
