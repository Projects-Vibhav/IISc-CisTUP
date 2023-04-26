#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import time

df = pd.read_csv('bike_data_new.csv')
df.head(100)
print(len(df))


# In[ ]:


def calc_time(df,index):
    start_date = df['started_at'][index].split(' ') 
    end_date = df['ended_at'][index].split(' ')
    
    start_hour = int(start_date[1].split(':')[0])
    start_min = int(start_date[1].split(':')[1])
    end_hour = int(end_date[1].split(':')[0])
    end_min = int(end_date[1].split(':')[1])
    
    return (end_hour - start_hour)*60 + (end_min) -  (start_min)   
    
    
    

# Saving the original contents of the dataframe before dropping as it may be of use in the future
df_1 = df

def funct_1(df):
    
    
    
    minimum_time = calc_time(df,0)
    maximum_time = calc_time(df,0)
    
   
    for i in range(len(df)):
        
         # Dropping the rows where the start and end time is the same
        if (df['started_at'][i]==df['ended_at'][i]):
            df = df.drop(index = i)
            
        # Finding the minimum and maximum trip times simultaneously while traversing
        else:
            if (calc_time(df,i)>maximum_time):
                maximum_time = calc_time(df,i)
            if (calc_time(df,i)<minimum_time):
                temp = i
                minimum_time = calc_time(df,i)
    
    # Resetting the indices after the required columns have been dropped in order to make for easier traversal          
    df = df.reset_index(drop=True) 
   
   
    # Counting the number if trips having the minimum time (calculated to be 1 minute)
    count_min = 0
    for i in range(len(df)):
        if (calc_time(df,i)==minimum_time):
            count_min += 1
    
    # Counting the number of circular trips, and finding the percentage
    c_trips = 0
    for i in range(len(df)):
        if df['start_lat'][i]==df['end_lat'][i] and df['start_lng'][i]==df['end_lng'][i]:
            c_trips+=1
    c_trips_percent = (c_trips/len(df))*100
    
    print("Maximum duration of the trip :", maximum_time,"minutes")
    print("Minimum duration of the trip :", minimum_time,"minutes")
    print("Total trips that had duration as minimum duration :", count_min,"trips")
    print("Percentage of circular trips:", c_trips_percent, "%")
        
        
    
    
    
# Calculating the run time of the function using the time module in Python            
s_time = time.time()            
funct_1(df)
e_time = time.time()
print("Runtime of the function : ",e_time - s_time,"seconds")
    
        
    


# In[ ]:


df_2 = df_1
for i in range(len(df_1)):
    # Extracting only the hour from the 'started_at' column
    start_hour = int(df_1['started_at'][i].split(' ')[1].split(':')[0]) 
    
    # The times are in 24 hour format so the hour should be between 6 and 18, 18 not included. So we filter out the hours outside this range
    if (start_hour<6 or start_hour>=18):
        df_1 = df_1.drop(index = i)

# Performing the reset operation again    
df_1 = df_1.reset_index(drop=True)

pairs = 0
p = []
# for i in range(len(df_1)-1):
#     for j in range(i+1,len(df_1)):
#         if(df_1['start_lat'][i]==df_1['end_lat'][j] and df_1['start_lng'][i]==df_1['end_lng'][j] and df_1['ended_at'][i]<df_1['started_at'][j]):
#                 pairs+=1
#                 l = []
#                 l.append(df_1['trip_id'][i])
#                 l.append(df_1['trip_id'][j])
#                 p.append(l)
                
print(p)
                
        

        
        
        
    


# In[ ]:




