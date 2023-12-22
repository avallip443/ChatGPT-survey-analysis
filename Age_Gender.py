
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""Creates graph that shows distribution of age and gender of respondents"""

df = pd.read_csv('ChatGPT Survey.csv')   # reads file

# creates list for all gender options and reserves 6 spots for age categories
male_age = [0]*6
female_age = [0]*6
nonbinary_age = [0]*6
other_age = [0]*6

# iterates through gender, then age of respondents and increments their age and gender group
for gender, age in zip(df['Which best describes your gender identity?'], df['What is your age?']):
    if gender == 'Male':
        if age == '17 and under':
            male_age[0] += 1
        elif age == '18-29':
            male_age[1] += 1
        elif age == '30-39':
            male_age[2] += 1
        elif age == '40-49':
            male_age[3] += 1
        elif age == '50-59':
            male_age[4] += 1
        else:
            male_age[5] += 1

    elif gender == 'Female':
        if age == '17 and under':
            female_age[0] += 1
        elif age == '18-29':
            female_age[1] += 1
        elif age == '30-39':
            female_age[2] += 1
        elif age == '40-49':
            female_age[3] += 1
        elif age == '50-59':
            female_age[4] += 1
        else:
            female_age[5] += 1

    elif gender == 'Non-binary':
        if age == '17 and under':
            nonbinary_age[0] += 1
        elif age == '18-29':
            nonbinary_age[1] += 1
        elif age == '30-39':
            nonbinary_age[2] += 1
        elif age == '40-49':
            nonbinary_age[3] += 1
        elif age == '50-59':
            nonbinary_age[4] += 1
        else:
            nonbinary_age[5] += 1
    else:  # 'prefer not to answer'
        if age == '17 and under':
            other_age[0] += 1
        elif age == '18-29':
            other_age[1] += 1
        elif age == '30-39':
            other_age[2] += 1
        elif age == '40-49':
            other_age[3] += 1
        elif age == '50-59':
            other_age[4] += 1
        else:
            other_age[5] += 1

print(male_age, female_age)

# Creates graph
age_category = ['17 and under', '18-29', '30-39', '40-49', '50-59', '60+']
colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

width = 0.7
values = np.arange(len(age_category))
fig, axis = plt.subplots()

axis.bar(values, male_age, color=colours[1], bottom=nonbinary_age, label='Male', width=width)
axis.bar(values, female_age, color=colours[0], bottom=male_age, label='Female', width=width)
axis.bar(values, nonbinary_age, color=colours[3], label='Non-Binary', width=width)
axis.bar(values, other_age, color=colours[2], label='Prefer Not To Say', width=width)

axis.set_title('Age and Gender Distribution of Respondents')
axis.legend(loc='upper right')
axis.set_xlabel('Age Groups')
axis.set_ylabel('Number of Persons')
plt.sca(axis)
plt.xticks(values, age_category)

plt.show()
