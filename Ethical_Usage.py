import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Creates graph comparing how ethical respondents think ChatGPT is and their frequency of usage"""

# method creates graph based on given faculty data
def makeUsagesCharts(dummies, usage):

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title('Respondents Who ' + usage + ' Use ChatGPT \nand Agreement with Statement:\n"ChatGPT Should be Considered an Ethical Tool."\n')
    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fb8072','#fbd462', '#bc80bd','#ccebc5','#8dd3c7']

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
never = [0]*5

for frequency, ethical in zip(df['Have you experimented with ChatGPT before?'], df['ChatGPT should be considered as an ethical tool/resource for students and professors.']):
    if 'often' in frequency:
        if ethical == 1:  # not ethical
            often[0] += 1
        elif ethical == 2:
            often[1] += 1
        elif ethical == 3:
            often[2] += 1
        elif ethical == 4:
            often[3] += 1
        elif ethical == 5:  # ethical
            often[4] += 1

    if 'sometimes' in frequency:
        if ethical == 1:
            sometimes[0] += 1
        elif ethical == 2:
            sometimes[1] += 1
        elif ethical == 3:
            sometimes[2] += 1
        elif ethical == 4:
            sometimes[3] += 1
        elif ethical == 5:
            sometimes[4] += 1

    if 'rarely' in frequency:
        if ethical == 1:
            rarely[0] += 1
        elif ethical == 2:
            rarely[1] += 1
        elif ethical == 3:
            rarely[2] += 1
        elif ethical == 4:
            rarely[3] += 1
        elif ethical == 5:
            rarely[4] += 1

    if 'No' in frequency:
        if ethical == 1:
            never[0] += 1
        elif ethical == 2:
            never[1] += 1
        elif ethical == 3:
            never[2] += 1
        elif ethical == 4:
            never[3] += 1
        elif ethical == 5:
            never[4] += 1

# Creates graph by calling chart method and providing data and name
data = [often, sometimes, rarely, never]
title = ['Often', 'Sometimes', 'Rarely', 'Don\'t']

for i in range(4):
    makeUsagesCharts(data[i], title[i])
