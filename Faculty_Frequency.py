import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Creates graph comparing each faculty and frequency of usage"""

# method creates graph based on given faculty data
def makeUsagesCharts(dummies, faculty):
    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title(faculty + ' Faculty Members\' \nFrequency of Using ChatGPT\n')
    labels = ['Often Uses\nChatGPT', 'Sometimes\nUses ChatGPT', 'Rarely Uses\nChatGPT', 'Never Used\nChatGPT']
    colours = ['#b3de69','#8dd3c7','#ccebc5','#fb8072']

    # removes lists with 0 data counts
    for index, item in enumerate(dummies):
        if item == 0:
            dummies.pop(index)
            labels.pop(index)
            colours.pop(index)

    plt.pie(dummies, colors=colours, labels=labels, autopct='%1.0f%%',pctdistance=0.45, startangle=110);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()

df = pd.read_csv('ChatGPT Survey.csv')   # reads file

arts = [0]*4
business = [0]*4
community_service = [0]*4
education = [0]*4
engineering = [0]*4
humanities = [0]*4
law = [0]*4
medicine = [0]*4
science = [0]*4

for faculty, usage in zip(df['Which faculty is your degree related to? Check all that apply.'], df['Have you experimented with ChatGPT before?']):
    if 'Arts' in faculty:
        if usage == 'Yes, often.':
            arts[0] += 1
        elif usage == 'Yes, sometimes.':
            arts[1] += 1
        elif usage == 'Yes, but rarely.':
            arts[2] += 1
        else:
            arts[3] + 1

    if 'Business' in faculty:
        if usage == 'Yes, often.':
            business[0] += 1
        elif usage == 'Yes, sometimes.':
            business[1] += 1
        elif usage == 'Yes, but rarely.':
            business[2] += 1
        else:
            business[3] += 1

    if 'Community Service'in faculty:
        if usage == 'Yes, often.':
            community_service[0] += 1
        elif usage == 'Yes, sometimes.':
            community_service[1] += 1
        elif usage == 'Yes, but rarely.':
            community_service[2] += 1
        else:
            community_service[3] += 1

    if 'Education' in faculty:
        if usage == 'Yes, often.':
            education[0] += 1
        elif usage == 'Yes, sometimes.':
            education[1] += 1
        elif usage == 'Yes, but rarely.':
            education[2] += 1
        else:
            education[3] += 1

    if 'Engineering/Architectural Science' in faculty:
        if usage == 'Yes, often.':
            engineering[0] += 1
        elif usage == 'Yes, sometimes.':
            engineering[1] += 1
        elif usage == 'Yes, but rarely.':
            engineering[2] += 1
        else:
            engineering[3] += 1

    if 'Humanities' in faculty:
        if usage == 'Yes, often.':
            humanities[0] += 1
        elif usage == 'Yes, sometimes.':
            humanities[1] += 1
        elif usage == 'Yes, but rarely.':
            humanities[2] += 1
        else:
            humanities[3] += 1

    if 'Law' in faculty:
        if usage == 'Yes, often.':
            law[0] += 1
        elif usage == 'Yes, sometimes.':
            law[1] += 1
        elif usage == 'Yes, but rarely.':
            law[2] += 1
        else:
            law[3] += 1

    if 'Medicine/Health' in faculty:
        if usage == 'Yes, often.':
            medicine[0] += 1
        elif usage == 'Yes, sometimes.':
            medicine[1] += 1
        elif usage == 'Yes, but rarely.':
            medicine[2] += 1
        else:
            medicine[3] += 1

    if 'Science/Mathematics' in faculty or 'Computer Science' in faculty:
        if usage == 'Yes, often.':
            science[0] += 1
        elif usage == 'Yes, sometimes.':
            science[1] += 1
        elif usage == 'Yes, but rarely.':
            science[2] += 1
        else: # no
            science[3] += 1


# Creates graph by calling chart method and providing faculty data and name
faculties = ['Arts', 'Business', 'Community Service', 'Education', 'Engineering & Architecture', 'Humanities', 'Law', 'Medicine & Health', 'Science & Mathematics']
data = [arts, business, community_service, education, engineering, humanities, law, medicine, science]

for i in range(len(faculties)):
   makeUsagesCharts(data[i], faculties[i])
