#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

#aesthetics
#plt.style.use('bmh')

#Dataframe variable for reading file
df = pd.read_csv('counts.csv')

#data sorting
df['receivetimeAEST'] = pd.to_datetime(df['receivetimeAEST'])
df.sort_values('receivetimeAEST', inplace=True)

#date formatting
date_format = mdates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)

#Specify axis
x = df['receivetimeAEST']
y = df['counts']

#Line Graph
plt.xlabel('receivetimeAEST', fontsize = 18)
plt.ylabel('counts', fontsize = 18)

#plt.scatter(x, y)
plt.plot_date(x, y, linestyle='solid')
plt.gcf().autofmt_xdate()

#Display graph
plt.show()
