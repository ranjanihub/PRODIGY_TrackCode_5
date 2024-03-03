#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
accidents_data = pd.read_csv(r"C:\Users\TRINITY ELE\Downloads\Crash_Reporting_-_Drivers_Data.csv")

# Exploratory Data Analysis (EDA)
# Visualize distribution of accidents by speed limit
plt.figure(figsize=(10, 6))
if 'Speed Limit' in accidents_data.columns:
    sns.countplot(x='Speed Limit', data=accidents_data)
    plt.title('Distribution of Accidents by Speed Limit')
    plt.xlabel('Speed Limit')
    plt.ylabel('Number of Accidents')
    plt.show()
else:
    print("Column 'Speed Limit' not found in the dataset.")

# Visualize accident hotspots using a heatmap based on speed limit
plt.figure(figsize=(10, 8))
if 'Speed Limit' in accidents_data.columns and 'Latitude' in accidents_data.columns and 'Longitude' in accidents_data.columns:
    accidents_data['Speed Limit'] = accidents_data['Speed Limit'].astype(int)
    accidents_data = accidents_data.groupby(['Latitude', 'Longitude', 'Speed Limit']).size().reset_index(name='Accident Count')
    sns.scatterplot(x='Longitude', y='Latitude', data=accidents_data, hue='Speed Limit', size='Accident Count', sizes=(20, 200), palette='viridis', legend='brief')
    plt.title('Accident Hotspots by Speed Limit')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
else:
    print("Columns 'Speed Limit', 'Latitude', or 'Longitude' not found in the dataset.")


# In[ ]:




