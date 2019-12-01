import pandas as pd

# use 2016-2017 data

# Deal with president rating 
president = pd.read_csv("approval_polls.csv")
president = president[(president["President"] == "Trump") | (president["President"] == "Obama")]


president.dtypes
president['date2'] = president['Date'].astype('datetime64')


p_monthly = president.set_index("date2")
p_monthly = p_monthly.resample('M').mean()
p_1617 = p_monthly.loc["2016-1-1" : "2017-12-31"]
del p_1617["Days"]

presidents_1617 = p_1617.reset_index()
presidents_1617["President"] = "Obama"
presidents_1617.iloc[12:24]["President"] = "Trump"

presidents_1617 = presidents_1617[["President", "date2", "Approve", "Disapprove"]]
presidents_1617.columns = ["President", "Month", "Approve Rate", "Disapprove Rate"]
presidents_1617.to_csv("president_monthly_1617.csv", sep = ",")
#print(presidents_1617)




# Deal with 911
df911 = pd.read_csv("911_2016-2017.csv")
df911 = df911[["Creation Date", "Borough", "Incident Type"]]
df911['date2'] = df911['Creation Date'].astype('datetime64')

df911_monthly = df911.set_index("date2")
df911_monthly = df911_monthly.resample('M').count().reset_index()
df911_monthly = df911_monthly [["date2", "Creation Date"]]
df911_monthly.columns = ["Month", "Number of Incidence"]
monthly_incidences = df911_monthly[["Number of Incidence"]]

#print(df911_monthly)



# Create a new dataframe combining 911 and presidents' rating
rating_911_1617 = pd.concat([presidents_1617, monthly_incidences], axis = 1)
#print(rating_911_1617)


# discover the relationship between president's rating and 911 incidents



import matplotlib.pyplot as plt
plt.plot(rating_911_1617[["Month"]], rating_911_1617[["Number of Incidence"]], color = "blue", label = "911")
plt.plot(rating_911_1617[["Month"]], rating_911_1617[["Approve Rate"]], color = "red", label = "rating")
plt.legend()
plt.xlabel('Month')
plt.ylabel('Number of incidence')
plt.show()

correlation = rating_911_1617.corr(method='pearson')
print(correlation)
























