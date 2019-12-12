# NYC 311 Service Requests Analysis

Group Project Overview for CIS9650.
Group Members: Mengyan Huang, Jinxi Huang, Kay Jiang, Sunny Liu, Xinli Hou

## Problem Statement
We would like to analyze the patterns of Non-emergency Service Requests (SR). Another goal is to discover external triggers or affecting factors to NYC residents’ complaints, such as weather, politics, gaming, shooting incidents, and other social events. We aim to provide helpful recommendations to improve work efficiency of government agencies and enhance NYC citizens satisfaction, and insights to future complaints prediction and management. 

## Datasets Used
1. **[311 Service Requests Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)**

	This is our main dataset - 311 Service Requests in NYC from 2010 to present. We undertake exploratory analysis on this dataset to find out the **peak hours** of non-emergency requests, and the **most common complaint issues**.
Based on this 311 SR dataset, we explore 4 other areas in order to find out external factors with significant impact. Below are the details of our directions.

2. **[Air Quality Data](https://aqs.epa.gov/aqsweb/airdata/download_files.html)**

	First we try to find out the connection between the air quality and the complaint volume.  By clicking the hyperlink Air Quality Data, in the the title line of this section, you can find the datafile for 2018 daily air quality index (AQI). This datafiles is then read in with only "State Name","County Name", "Date", "AQI", and "Category". Next, we filter rows with its "County Name" only Bronx, Queens, New York(Mahanttan), Richmond(Staten Island), Kings(Brooklyn). Their AQI is then averaged for a typical day. Then, based on the averaged AQI, we have assigned a new column with its category rank from "Good","Moderate",..., to "Hazardous". To find a possible correlation between daily AQI and number of daily 311 service request, we first do a scattered plot and then a fitted line, which results in a fairly flat trendline. And then,we do boxplots with the 6 AQI categories and its corresponding daily 311 service requests. The plot also shows no significant difference in number of daily 311 service requests for different AQI categories.

3. **[Mass Shooting](https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/ )**

	Next we would like to see if a mass shooting incident will trigger an increase in complaints.

4. **[Game Releases](https://www.kaggle.com/nikdavis/steam-store-games)**

	Meanwhile, we want to find out the relationship between steam game releases and the complaint rates.

5. **[President Popularity](https://www.kaggle.com/vkat72293/presidential-approval-ratings)**

	Finally we look at the big picture by exploring the correlation between the complaint volume and the approval rate of the current president. 


## Our Discovery

We consolidated our findings in a deck and have presented it via [Google Slides](https://docs.google.com/presentation/d/1en7uFHJYv60zOgmxJKyNdhBjIxUAko3qAfyzLncFQOc/edit?usp=sharing).
