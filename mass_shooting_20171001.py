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