# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:17:29 2019

@author: mengy
"""
import pandas as pd
df1 = pd.read_csv('daily_aqi_by_county_2018.csv')
df1=df1[["State Name","county Name","Date","AQI","Category"]]
df1=df1[df1["State Name"]=="New York"]
df1=df1[(df1["county Name"]=="Queens")|(df1["county Name"]=="Bronx")|(df1["county Name"]=="New York")|(df1["county Name"]=="Kings")|(df1["county Name"]=="Richmond")]
df1["Date"]=df1["Date"].astype('datetime64')
df1 = df1.set_index('Date')
AQI2018data=df1.resample('D').mean().reset_index()

def Cat(x):
    if x<50:
        return "Good"
    elif x>50 and x<=100:
        return "moderate"
    elif x>100 and x<=150:
        return "Unhealthy for Sensitive Groups"
    elif x>150 and x<=200:
        return "Unhealthy"
    elif x>200 and x<=300:
        return "Very Unhealthy"
    else:
        return "Hazardous"
    
AQI2018data["Category"]=AQI2018data.AQI.apply(Cat)

df311_20180101 = pd.read_csv("311_Service_Requests_20180101.csv")
df311_20180101 = df311_20180101[["Created Date", "Complaint Type"]]
df311_20180101['date2'] = df311_20180101['Created Date'].astype('datetime64')

df311_20180521 = pd.read_csv("311_Service_Requests_from_20180521.csv")
df311_20180521 = df311_20180521[["Created Date", "Complaint Type"]]
df311_20180521['date2'] = df311_20180521['Created Date'].astype('datetime64')

df311_20181003 = pd.read_csv("311_Service_Requests_from_20181003.csv")
df311_20181003 = df311_20181003[["Created Date", "Complaint Type"]]
df311_20181003['date2'] = df311_20181003['Created Date'].astype('datetime64')


df311_2018 = pd.concat([df311_20180101,df311_20180521,df311_20181003], ignore_index = True)

df311_2018 = df311_2018.set_index("date2")
df311_2018 = df311_2018.resample('D').count().reset_index()


df311_2018 = df311_2018[["date2", "Created Date"]]
df311_2018.columns = ["Date", "Number of Incidence"]
df311_2018=df311_2018[["Number of Incidence"]]


data = pd.concat([AQI2018data,df311_2018], axis=1)




from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
X = data["AQI"].values.reshape(-1, 1)  
Y = data["Number of Incidence"].values.reshape(-1, 1)  
linear_regressor = LinearRegression()  
linear_regressor.fit(X, Y) 
Y_pred = linear_regressor.predict(X) 
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.title("AQI vs. Number of Daily 311 Service Request Cases for 2018")
plt.xlabel("AQI")
plt.ylabel("Number of Incidence")

plt.show()
import seaborn as sns
sns.set(style="whitegrid")
ax = sns.boxplot(x="Category", y="Number of Incidence", data=data).set_title('Boxplot')



