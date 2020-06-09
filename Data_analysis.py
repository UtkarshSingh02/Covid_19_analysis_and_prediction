import pandas as pd
import numpy as np
importmatplotlib as plt

Data = pd.read_csv('covid.csv')
df = pd.DataFrame(Data)
df.head()

ax = plt.gca()
df.plot(x ='date', y='totalconfirmed', kind = 'line', color='Red', ax = ax)
df.plot(x ='date', y='totaldeceased', kind = 'line', color='Blue', ax = ax)
df.plot(x ='date', y='totalrecovered', kind = 'line', color='Black', ax = ax)
plt.show()

ax= plt.gca()
df.plot(x ='date', y='dailyconfirmed', kind = 'line', color='Pink', ax = ax)
df.plot(x ='date', y='dailydeceased', kind = 'line', color='Brown', ax = ax)
df.plot(x ='date', y='dailyrecovered', kind = 'line', color='Green', ax = ax)
plt.show()

import pandas as pd
data_2 = pd.read_csv('patients_data.csv')
data_2.head()

df.groupby(['gender']).sum().plot(kind='pie', subplots=True, shadow = True,startangle=90,
figsize=(15,10), autopct='%1.1f%%')
#the above piece is used to generate a pie chart.

df.groupby(['type_of_transmission']).sum().plot(kind='pie', subplots=True, shadow = True,startangle=90,
figsize=(15,10), autopct='%1.1f%%')

import pandas as pd
data_4 = pd.read_csv('IndividualDetails.csv')
data_4.head()
ax= plt.gca()
df.plot(x ='date', y='agebracket', kind = 'line', color='Pink', ax = ax)
df.plot(x ='date', y='currstatus', kind = 'line', color='Brown', ax = ax)
plt.show()

plt.plot( 'updatetimestamp', 'totalsamplestested', data=df2, marker='', color='Yellow', linewidth=2, linestyle='dashed', label="totaltested")
plt.plot( 'updatetimestamp', 'totalindividualstested', data=df2, marker='', color='olive', linewidth=2)
plt.plot( 'updatetimestamp', 'totalpositivecases', data=df2, marker='', color='red', linewidth=2, linestyle='dashed', label="positive_cases")
plt.legend()


