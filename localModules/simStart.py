# local imports
from parameterInputModule import getParamValues
from animationModule import setParameterValues

# The simStart module is the 'wrapper' for all simulation elements

'''
Go to parameter input module, run GUI to confirm parameter values, and return a list with all of the 
parameter values included in the following order:
nservers, filesServerTime, serverTime, filesCo, iatCo, filesDk, iatDk, filesMA, iatMa, filesNj,
iatNj, filesRd, iatRd, filesSv, iatSv, filesTg, iatTg, filesWt, iatWt, meanWt, devWy, nameAa,
filesAa, iatAa, nameTi, filesTi, iatTi, nameMe, filesMe, iatMe, nameFs, filesFs, iatFs timeWindowYears, 
daysPerYear, timeWindow
'''
paramValues = []
paramValues = getParamValues()
setParameterValues(paramValues)





