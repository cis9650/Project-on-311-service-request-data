class sr:
    date=''
    latitude=0
    longitude=0
 #open the 311 service requests data of mass shooting 20171001   
f = open("mass_shooting_20171001.csv")
import csv
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]#using split to 
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
#calculate the daily number of requests before and after a shooting
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata))
#draw a plot to show the trend of the number of 311 service requests by the day
import matplotlib.pyplot as plt
plt.plot(dates,datecount)
plt.show() 
#calculate the number of requests the week before and two weeks after a mass shooting
weekBefore=0
weekAfter1=0
weekAfter2=0
for i in range(22):
    if i==7:
        continue
    if i<7:
        weekBefore+=datecount[i]
    elif i<15:
        weekAfter1+=datecount[i]
    else:
        weekAfter2+=datecount[i]
print(weekBefore,weekAfter1,weekAfter2)
week=[weekBefore,weekAfter1,weekAfter2]
#find the trend of the number of 311 service requests by the week
plt.plot(week)
plt.show() 

#after read all the mass shootings, we get 'barchart' which is a list of lists.
barchart=[
[34777,33757,33477],
[35755,35379,33863],
[32436,31700,32330],
[47531,49483,48802],
[50059,47931,46231],
[54890,53380,52124],
[49512,44822,48815],
[58306,52228,50661],
[54474,61622,57023],
[41859,40166,40164]
]

import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame(barchart,index=['7/20/2012','12/14/2012','9/16/2013','6/12/2016',
'10/1/2017','11/5/2017','2/14/2018','10/27/2018','5/31/2019','8/3/2019'],
columns=pd.Index(['week1','week2','week3'],
name='Mass Shootings'))
print(df)
df.plot.bar(alpha=0.7,rot=0,legend=False) 
plt.xticks(rotation='vertical')
plt.legend(['week1','week2','week3'])
