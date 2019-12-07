import csv
import matplotlib.pyplot as plt
import pandas as pd
class sr:
    date=''
    latitude=0
    longitude=0
barchart=[]
 #open the 311 service requests data of mass shooting 20120720  
f = open("20120720.csv")
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
plt.plot(dates,datecount)
plt.xticks(rotation='vertical')
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20121214
f = open("20121214.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20130916
f = open("20130916.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20160612
f = open("20160612.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20171031
f = open("20171001.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20171105
f = open("20171105.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20180214
f = open("20180214.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20181027
f = open("20181027.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20190531
f = open("20190531.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)
#data of mass shootings happened on 20190803
f = open("20190803.csv")
readers = csv.reader(f)
next(readers)
data=[]
dates=[]
for row in readers:
    if row[1]==' ' or row[3]==' ' or row[4]==' ':
        break
    sr1=sr()
    sr1.date=row[1].split(' ')[0]
    sr1.latitude=row[3]
    sr1.longitude=row[4]
    data.append(sr1)
    if row[1].split(' ')[0] not in dates:
        dates.append(row[1].split(' ')[0])
datecount=[]
for date in dates:
    datedata=list(filter(lambda x: x.date==date,data))
    datecount.append(len(datedata)) 
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
weekdata=[weekBefore,weekAfter1,weekAfter2]
barchart.append(weekdata)

df = pd.DataFrame(barchart,index=['7/20/2012','12/14/2012','9/16/2013','6/12/2016',
'10/1/2017','11/5/2017','2/14/2018','10/27/2018','5/31/2019','8/3/2019'],
columns=pd.Index(['week1','week2','week3'],
name='Mass Shootings'))
print('\n',df)
df.plot.bar(alpha=0.7,rot=0,legend=False) 
plt.xticks(rotation='vertical')
plt.legend(['week1','week2','week3'])