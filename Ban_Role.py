import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Creates graph comparing respondents' roles in academic is and if they think ChatGPT should be banned"""

# method creates graph based on given faculty data
def makeUsagesCharts(dummies, role):

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title(role + 's\' Agreement with Statement:\n"Post-Secondary Institutions Should Ban the Use of ChatGPT."\n')
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

undergrad = [0]*5
grad = [0]*5
ta = [0]*5
prof = [0]*5
certificate = [0]*5

for role, ban in zip(df['What is your role in academia? If you are a graduate student and a teaching assistant, please pick teaching assistant.'], df['Post-secondary institutions should ban the use of ChatGPT.']):
    if 'Undergrad' in str(role):
        if ban == 1:  # ban
            undergrad[0] += 1
        elif ban == 2:
            undergrad[1] += 1
        elif ban == 3:
            undergrad[2] += 1
        elif ban == 4:
            undergrad[3] += 1
        elif ban == 5:  # not ban
            undergrad[4] += 1

    elif 'Graduate' in str(role) or 'Master' in str(role):
        if ban == 1:
            grad[0] += 1
        elif ban == 2:
            grad[1] += 1
        elif ban == 3:
            grad[2] += 1
        elif ban == 4:
            grad[3] += 1
        elif ban == 5:
            grad[4] += 1

    elif 'Teaching' in str(role):
        if ban == 1:
            ta[0] += 1
        elif ban == 2:
            ta[1] += 1
        elif ban == 3:
            ta[2] += 1
        elif ban == 4:
            ta[3] += 1
        elif ban == 5:
            ta[4] += 1

    elif 'Professor' in str(role):
        if ban == 1:
            prof[0] += 1
        elif ban == 2:
            prof[1] += 1
        elif ban == 3:
            prof[2] += 1
        elif ban == 4:
            prof[3] += 1
        elif ban == 5:
            prof[4] += 1

    elif 'Chang' in str(role) or 'Continu' in str(role):
        if ban == 1:
            certificate[0] += 1
        elif ban == 2:
            certificate[1] += 1
        elif ban == 3:
            certificate[2] += 1
        elif ban == 4:
            certificate[3] += 1
        elif ban == 5:
            certificate[4] += 1

# Creates graph by calling chart method and providing data and name
data = [undergrad, grad, ta, prof, certificate]
title = ['Undergraduate Student', 'Graduate Student', 'Teaching Assistant', 'Professor', 'Certificate Program Student']

for i in range (5):
    makeUsagesCharts(data[i], title[i])
