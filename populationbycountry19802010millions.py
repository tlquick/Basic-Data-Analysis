import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FileName = 'populationbycountry19802010millions.csv'
df = pd.read_csv(FileName, na_values=["NA", "--"])
df.set_index("Country", inplace=True)

# describe & head
print(df.describe())
print(df.head())

# remove nulls
# print(df.isnull().sum())
# 1.delete
df.dropna(inplace=True)
# 2.replace
# df.fillna(0, inplace=True)

# convert string to numeric
# only to found there are no strings

# drop unused columns
df = df.loc[['Australia', 'China']]
df = df[["1980", "1990", "2000", "2010"]]
# Create an average column using python
df['Average'] = df.mean(axis=1)
# Plot 2 graphs – a multiple bar for 1980, 2010 & Average and a line plot for 1980-2010
XBar = [1980, 2010, "Average"]
XLine = [1980, 1990, 2000, 2010]
YBarAustralia = []
YBarChina = []
YLineAustralia = []
YLineChina = []
for Year in XBar:
    YBarAustralia.append(df.loc['Australia'][str(Year)])
    YBarChina.append(df.loc['China'][str(Year)])
for Year in XLine:
    YLineAustralia.append(df.loc['Australia'][str(Year)])
    YLineChina.append(df.loc['China'][str(Year)])
Fig, (Ax1, Ax2) = plt.subplots(1, 2, sharey=True)
Fig.set_figheight(6)
Fig.set_figwidth(13)

# a multiple bar for 1980, 2010 & Average
XBarAxis = np.arange(len(XBar))
p1 = Ax1.bar(XBarAxis - 0.3, YBarAustralia, width=0.2, label="Australia")
p2 = Ax1.bar(XBarAxis + 0.3, YBarChina, width=0.2, label="China")
Ax1.bar_label(p1, label_type="edge")
Ax1.bar_label(p2, label_type="edge")
Ax1.set_ylabel('Population(million)')
Ax1.set_xlabel('Year')
Ax1.set_title('Population of Australia & China')
Ax1.set_xticks(XBarAxis, XBar)
Ax1.legend()

# a line plot for 1980-2010
Ax2.plot(XLine, YLineAustralia, label="Australia")
Ax2.plot(XLine, YLineChina, label="China")
Ax2.set_ylabel('Population(million)')
Ax2.set_xlabel('Year')
Ax2.set_title('Population of Australia & China')
Ax2.legend()
for x, y in zip(XLine, YLineAustralia):
    Ax2.annotate(y, (x, y))
for x, y in zip(XLine, YLineChina):
    Ax2.annotate(y, (x, y))
plt.show()