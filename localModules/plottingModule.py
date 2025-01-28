import salabim as sim
import matplotlib.pyplot as plt
import numpy as np
import random
import os

filePath = "./capDevDataIngestSim/plots/"
#filePath = "./plots/"

def systemScatterPlot(fileQueueX, fileQueueY, plotXlabel, plotYlabel, plotTitle, plotColor, simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xlabel(plotXlabel, color = "whitesmoke")
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")
    ax.scatter(fileQueueX, fileQueueY, color = plotColor)
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()

def systemHistPlot(fileQueue, plotXlabel, plotYlabel, plotTitle, plotColor, simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xlabel(plotXlabel, color = "whitesmoke")
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")
    ax.hist(fileQueue, color = plotColor, density = True, histtype="stepfilled",
            align = "left")
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()

def systemBoxPlot(fileQueue, plotYlabel, plotTitle, plotColor, simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xticks([0,1])
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")

    # Get quartile values
    q1, median, q3 = np.percentile(fileQueue, [25, 50, 75])

    # Annotate the quartile values
    ax.text(1.1, q1, f"Q1: {q1:.2f}", color = plotColor)
    ax.text(1.1, median, f"Median: {median:.2f}", color = plotColor)
    ax.text(1.1, q3, f"Q3: {q3:.2f}", color = plotColor)    
    
    ax.boxplot(fileQueue, patch_artist=True, manage_ticks=True,
                showfliers=True, notch=False, positions = [1],
                flierprops={"color":plotColor},
                medianprops={"color":"black"},
                boxprops={"facecolor":plotColor, "edgecolor":plotColor},
                whiskerprops={"color":plotColor},
                capprops={"color":plotColor}
                )
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()

def systemStairPlot(fileQueue, plotXlabel, plotYlabel, plotTitle, plotColor, simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xlabel(plotXlabel, color = "whitesmoke")
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")
    ax.stairs(fileQueue, color = plotColor)
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()

def systemLinePlot(fileQueue, plotXlabel, plotYlabel, plotTitle, plotColor, simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xlabel(plotXlabel, color = "whitesmoke")
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")
    ax.plot(fileQueue, color = plotColor)
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()

def systemMultiLinePlot(fileQueue, plotXlabel, plotYlabel, plotTitle, plotColor,simFileName):
    fig, ax = plt.subplots(facecolor = "gray")
    ax.set_facecolor("silver")
    ax.set_xlabel(plotXlabel, color = "whitesmoke")
    ax.set_ylabel(plotYlabel, color = "whitesmoke")
    ax.set_title(plotTitle, color = "snow")
    j = len(plotColor)
    for i in range (0,j):
        ax.plot(fileQueue[[i]], color = plotColor[i])
    ax.tick_params(labelcolor = "white")
    plt.savefig(filePath+"/"+simFileName+"_"+plotTitle+".png")
    plt.close()



if __name__ == "__main__":
    simFileName = "testPlots"
    
    fileQueueX = [random.randint(1,100) for _ in range(10)] 
    fileQueueY = [random.randint(1,100) for _ in range(10)]
    systemScatterPlot(fileQueueX, fileQueueY, "Time", "Files", "Random Numbers_Scatter", "red", simFileName)
    plt.show()

    fileQueue = [random.randint(1,100) for _ in range(10)] 
    systemHistPlot(fileQueue, "Time", "Files", "Random Numbers_Hist", "red", simFileName)
    plt.show()
    
    fileQueueData = [np.random.rand(50) * 100] 
    flierHigh = [np.random.rand(10) * 100 + 100]
    flierLow = [np.random.rand(10) * -100]
    fileQueue = fileQueueData + flierHigh + flierLow
    systemBoxPlot(fileQueueData, "Files", "Random Numbers_Box", "red", simFileName)    
    plt.show()

    fileQueue = [random.randint(1,100) for _ in range(10)] 
    systemStairPlot(fileQueue, "Time", "Files", "Random Numbers_Stair", "red", simFileName)
    plt.show()
    
    fileQueue = [random.randint(1,100) for _ in range(10)] 
    systemLinePlot(fileQueue, "Time", "Files", "Random Numbers_Line", "red", simFileName)
    plt.show()
