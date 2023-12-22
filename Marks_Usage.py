import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Creates graph comparing each changes in academic performance and frequency of usage"""

# method creates graph based on given faculty data
def makeUsagesCharts(dummies, usage):

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title('Distribution of Respondents Who ' + usage + ' Use ChatGPT \nand Changes in Their Academic Performances\n')
    labels = ['Significantly\nDecreased', 'Somewhat\nDecreased', 'Neither Increased\nor Decreased', 'Somewhat\nIncreased', 'Significantly\nIncreased']
    colours = ['#fb8072','#fbd462', '#bc80bd','#ccebc5','#8dd3c7']
    #     colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada', '#fccde5', '#8dd4c7']

    # removes lists with 0 data counts
    for index, item in enumerate(dummies):
        if item == 0:
            dummies.pop(index)
            labels.pop(index)
            colours.pop(index)

    plt.pie(dummies, colors=colours, labels=labels, autopct='%1.0f%%',pctdistance=0.45, startangle=160);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()

df = pd.read_csv('ChatGPT Survey.csv')   # reads file

often = [0]*5
sometimes = [0]*5
rarely = [0]*5

for frequency, improvement in zip(df['Have you experimented with ChatGPT before?'], df['My academic performance and productivity has improved significantly by using ChatGPT. Skip question if not applicable.']):
    if 'often' in frequency:
        if improvement == 1:  # decreased
            often[0] += 1
        elif improvement == 2:
            often[1] += 1
        elif improvement == 3:
            often[2] += 1
        elif improvement == 4:
            often[3] += 1
        elif improvement == 5:  # increased
            often[4] += 1

    if 'sometimes' in frequency:
        if improvement == 1:
            sometimes[0] += 1
        elif improvement == 2:
            sometimes[1] += 1
        elif improvement == 3:
            sometimes[2] += 1
        elif improvement == 4:
            sometimes[3] += 1
        elif improvement == 5:
            sometimes[4] += 1

    if 'rarely' in frequency:
        if improvement == 1:
            rarely[0] += 1
        elif improvement == 2:
            rarely[1] += 1
        elif improvement == 3:
            rarely[2] += 1
        elif improvement == 4:
            rarely[3] += 1
        elif improvement == 5:
            rarely[4] += 1

# Creates graph by calling chart method and providing data and name
data = [often, sometimes, rarely]
title = ['Often', 'Sometimes', 'Rarely']

for i in range(3):
    makeUsagesCharts(data[i], title[i])
