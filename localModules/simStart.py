import tkinter as tk
from tkinter import *
from tkinter import ttk

# local imports
from parameterInputModule import getParamValues
from animationModule import setParameterValues

# The simStart module is the 'wrapper' for all simulation elements

'''
Go to parameter input module, run GUI to confirm parameter values, and return a list with all of the 
parameter values.

Send parameter list to animation module and begin simulation.
'''


paramValues = []
paramValues = getParamValues()
setParameterValues(paramValues)



