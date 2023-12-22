import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

# reads survey data
df = pd.read_csv("ChatGPT Survey.csv")


def get_ages():
    """Creates pie chart of ages of respondents"""

    # Splits respondents' choices
    ages = df['What is your age?'].str.get_dummies(sep=';')

    # Sums the dummy variables for a count for each choice
    total_counts = ages.sum()

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title('Ages of Respondents ')
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69']
    ax1.pie(total_counts, labels=total_counts.index, colors=colours, autopct='%1.0f%%',pctdistance=0.5, startangle=0);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_genders():
    """Creates pie chart of gender identities of respondents"""

    # Splits respondents' choices
    gender = df['Which best describes your gender identity?'].str.get_dummies(sep=';')

    # Sums the dummy variables for a count for each choice
    total_counts = gender.sum()

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title('Gender Distribution of Respondents ')
    colours = ['#fdb462','#b3de69','#80b1d3']
    ax1.pie(total_counts, labels=total_counts.index, colors=colours, autopct='%1.0f%%',pctdistance=0.5, startangle=10);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_ethnicities():
    """Creates pie chart for distribution of ethnicities"""

    # Splits respondents' choices
    ethnicities = df['Which best describes your ethnicity? Check all that apply.'].str.get_dummies(sep=';')

    # Sums the dummy variables for a count for each choice
    total_counts = ethnicities.sum()

    # Prints counts for each option
    print(total_counts)

    # Creates graph
    fig1, ax1 = plt.subplots(figsize=(7,5))

    plt.title('Ethnicities of Respondents\n')
    colours = ['#bebada','#fb8072', '#ffffb3', '#8dd3c7','#bc80bd','#fdb462','#b3de69','#fccde5','#80b1d3']
    ax1.pie(total_counts, colors=colours, autopct='%1.0f%%',pctdistance=0.8, startangle=90);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout(rect=[-0.35,0,1,1])

    ax1.legend(loc='upper right', labels=total_counts.index, bbox_to_anchor=(1.01, 1))
    ax1


    plt.show()


def get_academic_roles():
    """Creates pie chart for distribution of role in academia"""

    answers = [0]*5

    # Groups similar 'other' choice responses into groups
    for role in zip(df['What is your role in academia? If you are a graduate student and a teaching assistant, please pick teaching assistant.']):
        if 'Undergrad' in str(role):
            answers[0] += 1

        if 'Graduate' in str(role) or 'Master' in str(role):
            answers[1] += 1

        if 'Teaching' in str(role):
            answers[2] += 1

        if 'Professor' in str(role):
            answers[3] += 1

        if 'Chang' in str(role) or 'Continu' in str(role):
            answers[4] += 1

    # Prints counts for each option
    print(answers)

    # Creates graph

    labels = ['Undergraduate\nStudent', 'Graduate\nStudent', 'Teaching\nAssistant', 'Professor', 'Certificate\nProgram\Student']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    fig1, ax1 = plt.subplots()

    plt.title('Distribution of Respondents\' Roles in Academia')
    labels = ['Undergraduate\nStudent', 'Graduate\nStudent', 'Teaching\nAssistant', 'Professor', 'Certificate\nProgram']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    plt.pie(answers, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.5, startangle=50);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_faculties():
    """Creates pie chart for faculty distribution"""

    answers = [0]*9

    for faculty in zip(df['Which faculty is your degree related to? Check all that apply.']):
        if 'Arts' in str(faculty):
            answers[0] += 1

        if 'Business' in str(faculty):
            answers[1] += 1

        if 'Community Service'in str(faculty):
            answers[2] += 1

        if 'Education' in str(faculty):
            answers[3] += 1

        if 'Engineering/Architectural Science' in str(faculty):
            answers[4] += 1

        if 'Humanities' in str(faculty):
            answers[5] += 1

        if 'Law' in str(faculty):
            answers[6] += 1

        if 'Medicine/Health' in str(faculty):
            answers[7] += 1

        if 'Science/Mathematics' in str(faculty) or 'Computer Science' in str(faculty):
            answers[8] += 1

    # Prints counts for each option
    print(answers)

    # Creates graph
    fig1, ax1 = plt.subplots(figsize=(7, 6))

    plt.title('Faculties of Respondents ')
    labels = ['Arts', 'Business', 'Community\nService', 'Education', 'Engineering/Architecture', 'Humanities', 'Law', 'Medicine/\nHealth', 'Science/\nMathematics']
    colours = ['#fb8072','#b3de69', '#8dd3c7', '#ffffb3', '#fccde5', '#80b1d3', '#bc80bd', '#fdb462', '#bebada',]
    plt.pie(answers, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.5, startangle=150);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_usage_frequency():
    """Creates pie chart for distribution of respondents who used ChatGPT and frequency of usage"""

    # Splits respondents' choices
    dummies = df['Have you experimented with ChatGPT before?'].str.get_dummies(sep=';')

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Prints counts of each option
    print(total_counts)

    # Creates graph
    fig1, ax1 = plt.subplots()

    labels = ['Does Not\nUse', 'Rarely Uses', 'Often Uses', 'Sometimes Uses']
    plt.title('Distribution of Respondents\' Frequency of ChatGPT Use\n')
    colours = ['#fb8072','#ccebc5','#b3de69', '#8dd3c7']
    plt.pie(total_counts, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.45, startangle=100);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_reason_for_use():
    """Creates bar graph breaking down why respondents use ChatGPT"""

    answers = [0]*6

    # Removes answers from those who haven't used ChatGPT and counts relevant responses
    for uses in zip(df['Why do you use ChatGPT? Skip question if not applicable. ']):
        if 'Provides concise answers' in str(uses):
            answers[0] += 1
        if 'Source of inspiration for tasks' in str(uses):
            answers[1] += 1
        if 'Reduces time needed to do task by hand' in str(uses):
            answers[2] += 1
        if 'Saves time researching' in str(uses):
            answers[3] += 1
        if 'Improves skills (ex. coding, writing)' in str(uses):
            answers[4] += 1
        if 'Entertainment' in str(uses) or 'Explore' in str(uses) or 'fun' in str(uses) or 'just' in str(uses):
            answers[5] += 1

    # Prints counts for each option
    print(answers)

    # Creates graph
    plt.figure(figsize=(11,9))

    labels = ['Provides Concise\nAnswers', 'Source of\nInspiration for\nTasks', 'Reduces Time\nNeeded to do \nTasks By Hand', 'Saves Time\nResearching', 'Improves Skills', 'Other']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada', '#fccde5']

    plt.bar(labels, answers, color=colours, width=0.7, align='center' )
    plt.xlabel('\nReasons for Use')
    plt.ylabel('Number of Respondents')
    plt.title('Respondents\' Uses of ChatGPT\n')

    plt.show()


def get_concerns():
    """Creates bar graph representing respondents concerns over ChatGPT"""

    answers = [0]*5

    # Splits multi-select answers and counts them
    for uses in zip(df['What are your concerns regarding ChatGPT?']):
        if 'Plagiarism and cheating' in str(uses):
            answers[0] += 1
        if 'Decreases problem solving & critical thinking skills' in str(uses):
            answers[1] += 1
        if 'Inaccurate information' in str(uses):
            answers[2] += 1
        if 'Impact on career opportunities (e.g. replacing teachers, programmers…)' in str(uses):
            answers[3] += 1
        if 'No major concerns' in str(uses):
            answers[4] += 1

    # Prints counts of options
    print(answers)

    # Creates graph
    plt.figure(figsize=(9,9))

    labels = ['Plagiarism and\nCheating', 'Decreases Problem \nSolving & Critical \nThinking Skills', 'Inaccurate\nInformation', 'Impact on Career\nOpportunities', 'No Major\nConcerns']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    plt.bar(labels, answers, color=colours, width=0.7, align='center')
    plt.xlabel('\nConcerns')
    plt.ylabel('Number of Respondents')
    plt.title('Respondents\' Concerns About ChatGPT\n')

    plt.show()


def get_reliability():
    """Creates bar graph representing how reliable respondents beleive CHatGPT is"""

    # Splits respondents' choices
    data = df['I find ChatGPT to be reliable and accurate.']
    dummies = pd.get_dummies(data)

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Creates graph
    plt.figure(figsize = (7, 6))

    labels = ['Strongly \nDisagree', 'Somewhat \nDiagree', 'Neither Agree \nor DIsagree', 'Somewhat \nAgree', 'Strongly \nAgree']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    plt.title('How Strongly Respondents Agree or Disagree With Statement: \n"I Find ChatGPT to be Reliable and Accurate." ')
    plt.bar(labels, total_counts, color=colours)
    plt.xlabel('Level of Agreement')
    plt.ylabel('Number of Respondents')

    plt.show()


def get_academic_performance_changes():
    """Creates bar graph of the respondents' changes in their academic performance"""

    # Splits respondents' choices
    dummies = pd.get_dummies(df['My academic performance and productivity has improved significantly by using ChatGPT. Skip question if not applicable.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Creates graph
    plt.figure(figsize = (7, 8))

    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"My academic performance and productivity has improved \nsignificantly by using ChatGPT."\n')
    plt.bar(labels, total_counts, color=colours, edgecolor = 'black')
    plt.xlabel('\nLevel of Agreement')
    plt.ylabel('Number of Respondents')

    plt.show()


def get_future_students_impact():
    """Creates pie chart of respondents opinions of the impact of future students' academic abilities"""

    # Splits respondents' choices
    dummies = pd.get_dummies(df['ChatGPT will have a positive impact on the academic abilities of students in the future.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Prints counts of options
    print(total_counts)

    # Creates graph
    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    fig1, ax1 = plt.subplots()

    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fb8072','#fbd462', '#bc80bd','#ccebc5','#8dd3c7']
    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"ChatGPT Will Have a Positive Impact on the Academic Abilities \nof Students in the Future."\n')

    plt.pie(total_counts, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.45, startangle=100);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_if_plagarism():
    """Creates pie chart showing whether respondents think ChatGPT is a form of plagarism"""

    # Splits respondents' choices
    dummies = pd.get_dummies(df['Using ChatGPT is a form of plagiarism.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Prints counts of each option
    print(total_counts)

    # Creates graph
    fig1, ax1 = plt.subplots()

    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fb8072','#fbd462','#bc80bd','#ccebc5', '#8dd3c7']
    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"Using ChatGPT is a form of plagiarism."\n')

    plt.pie(total_counts, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.45, startangle=100);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_if_ethical():
    """Creates bar graph showing whether respondents think ChatGPT is an ethical tool"""
    # Splits respondents' choices
    dummies = pd.get_dummies(df['ChatGPT should be considered as an ethical tool/resource for students and professors.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Creates graph
    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada']

    plt.figure(figsize = (7, 8))

    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"ChatGPT should be considered as an ethical \ntool/resource for students and professors."\n')
    plt.bar(labels, total_counts, color=colours, edgecolor = 'black')
    plt.xlabel('\nLevel of Agreement')
    plt.ylabel('Number of Respondents')

    plt.show()


def get_makes_students_lazy():
    """Creates pie chart showing whether respondents think ChatGPT makes students lazy"""

    # Splits respondents' choices
    dummies = pd.get_dummies(df['Regular use of ChatGPT can make students lazy.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Pritns counts for options
    print(total_counts)

    # Creates graph
    fig1, ax1 = plt.subplots()

    labels = ['Strongly\nAgree', 'Somewhat\nAgree', 'Neither Agree\nor Disagree', 'Somewhat\nDisagree', 'Strongly\nDisagree']
    colours = ['#8dd3c7','#ccebc5', '#bc80bd','#fbd462','#fb8072']
    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"Regular Use of ChatGPT Can Make Students Lazy."\n')

    plt.pie(total_counts, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.45, startangle=100);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_if_banned():
    """Creates pie chart showing whether respondents think ChatGPT should be banned in schools"""

    # Splits respondents' choices
    dummies = pd.get_dummies(df['Post-secondary institutions should ban the use of ChatGPT.'])

    # Sums the dummy variables for a count for each choice
    total_counts = dummies.sum()

    # Prints counts of options
    print(total_counts)

    # Creates graph
    fig1, ax1 = plt.subplots()

    labels = ['Strongly\nDisagree', 'Somewhat\nDisagree', 'Neither Agree\nor Disagree', 'Somewhat\nAgree', 'Strongly\nAgree']
    colours = ['#fb8072','#fbd462','#bc80bd','#ccebc5', '#8dd3c7']
    plt.title('How Strongly Respondents Agree or Disagree With Statement:\n"Post-Secondary Snstitutions Should Ban the Use of ChatGPT."\n')

    plt.pie(total_counts, labels=labels, colors=colours, autopct='%1.0f%%',pctdistance=0.45, startangle=100);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


def get_postsecondary_allowed():
    """Creates bar graph showing in what areas respondents think ChatGPT should be allowed"""

    answers = [0]*7

    # Splits and sorts respondents choices
    for uses in zip(df['In what areas should post-secondary institutions allow and regulate the use of ChatGPT by students? Check all that apply.']):
        if 'Homework' in str(uses):
            answers[0] += 1
        if 'Learning material' in str(uses):
            answers[1] += 1
        if 'Research' in str(uses):
            answers[2] += 1
        if 'Creativity' in str(uses):
            answers[3] += 1
        if 'Communication' in str(uses):
            answers[4] += 1
        if 'Writing' in str(uses):
            answers[5] += 1
        if 'Should not' in str(uses):
            answers[6] += 1

    # Prints counts of options
    print(answers)

    # Creates graph
    plt.figure(figsize=(11,8))

    labels = ['Homework/\nAssignments', 'Learning\nConcepts', 'Research', 'Creativity', 'Communication', 'Writing', 'Should Not\nBe Used']
    colours = ['#fdb462','#80b1d3','#fb8072','#b3de69', '#bebada', '#fccde5', '#8dd4c7']

    plt.bar(labels, answers, color=colours, width=0.7, align='center')
    plt.xlabel('Areas to Be Allowed')
    plt.ylabel('Number of Respondents')
    plt.title('Areas Respondents Think that Post-Secondary Institutions\nShould Allow and Regulate the Use of ChatGPT\n')

    plt.show()


def get_if_reccomend():
    """Creates pie chart for distribution of whether respondents would recommend ChatGPT"""

    # Splits respondents' choices
    recommendations = df['Would you recommend ChatGPT to others?'].str.get_dummies(sep=';')

    # Sums the dummy variables for a count for each choice
    total_counts = recommendations.sum()

    # Creates graph
    fig1, ax1 = plt.subplots()

    plt.title('Distribution of Whether Respondents Would Reccomend ChatGPT')
    colours = ['#fb8072','#80b1d3','#b3de69']
    ax1.pie(total_counts, labels=total_counts.index, colors=colours, autopct='%1.0f%%',pctdistance=0.5, startangle=0);

    centre_circle = plt.Circle((0,0),0.6,fc='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    # main contains method call for graphs of all survey questions
    # uncomment call to view graph

    # independent variable questions
     get_ages()
    # get_genders()
    # get_ethnicities()
    # get_academic_roles()
    # get_faculties()

    # dependent variable questions
    # get_usage_frequency()
    # get_reason_for_use()
    # get_concerns()
    # get_reliability()
    # get_academic_performance_changes()
    # get_future_students_impact()
    # get_if_plagarism()
    # get_if_ethical()
    # get_makes_students_lazy()
    # get_if_banned()
    # get_postsecondary_allowed()
    # get_if_reccomend()
