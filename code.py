import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

populationMean = statistics.mean(data)
populationSTD = statistics.stdev(data)

print("Population mean: ",populationMean)
print("PopulationSD: ",populationSTD)

#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.show()
#sampleSTD = statistics.stdev(dataSet)
#print("Sample Mean: ", sampleMean)
#print("Sample SD: ",sampleSTD)
#function to get mean of the given data sample

def randomSetOfMean(counter):
    dataSet = []

    for i in range(0,counter):
        randomInd = random.randint(0,len(data)-1)
        value = data[randomInd]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return(mean)

#function to plot mean of the graph
def showFig(meanList):
    df = meanList
    mean = statistics.mean(meanList)
    print("Mean of sampling distribution: ",mean)
    fig = ff.create_distplot([df],["temp"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
    fig.show()

#function to get mean of 100 data points 1000 times and plot the graphs
def setup():
    meanList = []
    for i in range(0,1000):
        mean = randomSetOfMean(36)
        meanList.append(mean)

    showFig(meanList)

setup()

def standardDeviation():
    meanList = []
    for i in range(0,1000):
        mean = randomSetOfMean(36)
        meanList.append(mean)
    
    STD = statistics.stdev(meanList)
    print("Standard Deviation of the sampleing distribution: ",STD)

standardDeviation()