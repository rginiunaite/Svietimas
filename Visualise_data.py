import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('../Mokiniu_skaicius.xlsx', index_col=0)
df = df[0:8]  # only language variables

dfT = df.transpose()

labels = ['2017/2018', '2018/2019', '2019/2020', '2020/2021', '2021/2022', '2022/2023']

width = 0.5  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

df = dfT

# plot a Stacked Bar Chart using matplotlib
dfT.plot(
    x='Metai',
    kind='barh',
    stacked=True,
    title='Mokinių skaičius',
    mark_right=True)

df_total = df["Lietuvių"] + df["Rusų"] + df["Lenkų"] + df['Baltarusių'] + df['Anglų'] + df['Prancūzų'] + df['Kita']
df_rel = df[df.columns[1:4]].div(df_total, 0) * 100 # specify how many values to show
df_relall = df[df.columns[1:]].div(df_total, 0) * 100 # define all

for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n],
                                         df[n], df_rel[n])):
        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%',
                 va='center', ha='center')

# ax.set_title('Scores by group and gender')
plt.tight_layout()
plt.show()

for i in range(6, 7):

    plt.rcParams.update({'font.family': 'Times New Roman'})

    plt.rcParams.update({'font.size': 12})

    ## now pie chart for the number of students in different years

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labelscountries = 'Lietuvių', 'Rusų', 'Lenkų', 'Baltarusių', 'Anglų', 'Prancūzų', 'Kita'
    sizes = df_relall.iloc[6,:]
    explode = (0, 0, 0, 0.25, 0.25, 0.25, 0.25)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labelscountries, explode=explode)  # , autopct='%1.1f%%')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.title('x= ' + str(x) + ', y = ' + str(y))
    if i == 1:
        str = '2017/2018'
    if i == 2:
        str = '2018/2019'
    if i == 3:
        str = '2019/2020'
    if i == 4:
        str = '2020/2021'
    if i == 5:
        str = '2021/2022'
    if i == 6:
        str = '2022/2023'

    ax1.set_title('Mokinių skaičius ' + str)

    percentages = sizes / sum(sizes) * 100
    # use a list comprehension to update the labels
    labels = [f'{l}, {s:0.1f}%' for l, s in zip(labelscountries, percentages)]
    plt.legend(bbox_to_anchor=(0.75, 1.1), loc='upper left', labels=labels)  # bbox_to_anchor=(0.85, 1)
    plt.show()


