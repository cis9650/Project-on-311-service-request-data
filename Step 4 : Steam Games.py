import pandas as pd
import datetime
from datetime import timedelta
import numpy

dfgame = pd.read_csv("steam.csv")

dfgame = dfgame[["name", "release_date", "categories", "genres", "owners", "price", "steamspy_tags", "english"]]
dfgame.columns = ["Name", "Date", "Category", "Genre", "Own", "Price", "Spy", "Eng"]

dfgame = dfgame[dfgame["Eng"] == 1]
#Only 2018 data
#Complaint type = noise - residential
#Location type = residential building/house
#Descriptor = loud music and loud talking
#Resolution type = police responded
df311 = pd.read_csv("311.csv")
df311 = df311[["Created Date", "Borough"]]
df311.columns = ["Date", "Boro"]
df311 = df311[["Date", "Boro"]]

df311["Date"] = df311["Date"].str.split(' ').str[0]
df311["Date"] = df311.apply(lambda row: datetime.datetime.strptime(row["Date"], '%m/%d/%Y'), axis = 1)

start = datetime.datetime.strptime('2018-01-01', '%Y-%m-%d')

#Change date into datetime object
dfgame["Date"] = dfgame.apply(lambda row: datetime.datetime.strptime(row["Date"], '%Y-%m-%d'), axis = 1)
#Due to the dataset having a range of game owners
#Split the range into 2 numbers and grab the larger of the 2 numbers
dfgame["Own"] = dfgame["Own"].str.split('-').str[1]
dfgame["Own"] = dfgame['Own'].astype(int)
#Sort dataframe over 2010
dfgame = dfgame[dfgame["Date"] > start]
end = start

yr = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
multi = []
sale=[]
fps = []
xaxis=[]
yaxis=[]
genre = 0
gun = 0
#Break year into quarters
#Sort games by releases into specific quarters
for x in range(12):
    end = start + timedelta(days=31)
    dftemp = dfgame[(dfgame["Date"] >= start) & (dfgame["Date"] <= end)]
    dfgmax = dftemp.sort_values("Own",ascending=False).head(2)
    ind = dfgmax.index[0]
    ind2 = dfgmax.index[1]
    #Get the top 2 games in terms of sales
    if dftemp.at[ind, "Own"] == dftemp.at[ind2, "Own"]:
        xaxis.append(dftemp.at[ind, "Name"] + " , " + dftemp.at[ind2, "Name"])
    else:
        xaxis.append(dftemp.at[ind, "Name"])
    #Create a list of the top selling games by months
    #If 2 games have the same range of sales record them both
    df3temp = df311[(df311["Date"] >= start) & (df311["Date"] <= end)]
    yaxis.append(len(df3temp))
    #Get the count of 311 noise complaints in the month
    boolist = dftemp["Spy"].str.contains("Open World").tolist()
    for line in boolist:
        if line == True:
            genre += 1
    #Search for a count of games in the multiplayer category
    gunlist = dftemp["Spy"].str.contains("Battle Royale").tolist()
    for line in gunlist:
        if line == True:
            gun += 1
    #Search for a count of games considered first person shooters
    sale.append(len(dftemp))
    fps.append(gun)
    multi.append(genre)
    start = end
    genre = 0
    gun = 0

import matplotlib.pyplot as plt

plt.plot(xaxis, yaxis)
plt.xticks(rotation=90)
plt.xlabel("Games Sold the Most")
plt.ylabel("Noise Complaints by Month")
plt.title("Top Selling Games and Noise Complaints")
plt.show()

plt.plot(yr, sale)
plt.xlabel("Months")
plt.ylabel("Game Sales by Month")
plt.title("Sales Number by Month")
plt.xticks(rotation=90)
plt.show()

print ("Correlation between noise complaints and Steam game sales ", numpy.corrcoef(yaxis,sale)[0, 1])

plt.plot(yr, multi)
plt.xticks(rotation=90)
plt.xlabel("Months")
plt.ylabel("Open World Games")
plt.title("Open World Games Sales by Month")
plt.show()

print ("Correlation between noise complaints and Open World game sales", numpy.corrcoef(yaxis,multi)[0, 1])

plt.plot(yr, fps)
plt.xticks(rotation=90)
plt.xlabel("Months")
plt.ylabel("Battle Royal Games")
plt.title("Battle Royal Games Sales by Month")
plt.show()

print ("Correlation between noise complaints and Battle Royal game sales", numpy.corrcoef(yaxis,fps)[0, 1])



















