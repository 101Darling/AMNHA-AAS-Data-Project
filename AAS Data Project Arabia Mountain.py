# File: AAS Data Project Arabia Mountain.py
# Author: Darling Ngoh
# Contact: darlingngoh@gmail.com
# Date:1/08/24

"""
Prog Description(DANC AAS Data Project):
    An ongoing project to visualize and monitor the water/stream chemical testing data given Arabia Mountain's
    Adopt A Stream project. This may serve to further equip volunteers and staff, likewise fostering community
    engagement with user-friendly monitoring visualisation given local water ecosystems.
    Hosted by the Davidson-Arabia Nature Center Ranger Shaundon and data scientist Darling.

    Our quality of life is directly related to the quality of the rivers,streams and wetlands around us.
    Regular monitoring and tracking provides baseline information about the health...
    of our local streams and other water bodies.

    Guiding questions/Goals:
        - Keep track of the continuous chemical test data for adopt a stream volunteer sessions.
        - Available parameters {Group_ID, Group_name, SIte_ID, Site_Name, Event_ID, Event_Date, Time_Spent,
        ... DraftIndicator, Air_Temp, Water_Temp, PH, DissolvedOxygen, DO_Saturation, Conductivity}
        - Identify anomalies with set notifications for call to action
        - Ensure user-friendly functionality, easy to understand data with insightful summaries

    ETL (Extract, Transform, Load):
    Pandas for data extraction, transformation, and analysis in-memory.
    Storing cleaned and processed data in an SQLite database for persistent storage.
    This combination is useful when the benefits of both in-memory manipulation and persistent storage is needed.

PROJECT PARAMETERS:
1) General data outputs:
To briefly recap, there are 6 parameters we are dealing with: Air & Water temp; pH, Conductivity, Dissolved Oxygen (DO);
 & E. Coli. I would like the outputs to be visualized in the following way…

    -Air & Water Temp on the same graph
    -pH & Conductivity on the same graph
    -DO as its own graph
    -E. Coli as its own graph

2) Graph Design
I would like to tweak the graph design as well if this is possible to do. See below:

    - use a Line Graph versus a bar graph for cleaner look
    - y-axis labels so that they show just the Month & Year. From a graph standpoint, the month is all we care about.

    -We mentioned that, for most of the values, there is a threshold which if crossed would mean that a stream is
    impaired. Whenever this threshold is crossed, would you be able to represent that point as a “Star” or some other
    “Symbol” on the line graph? Those thresholds are listed below:

        - Air Temp: No threshold
        - Water Temp: >32.2°C is bad (red zone)
        - Conductivity: No threshold
        - DO: <4 mg/L is bad (red zone)
        - pH has a middle zone: We want our data to fall between 6-8.5. If is is above or below that zone, it is bad.
        - E. Coli: >1000 is bad

3) Dream Goal
Ideally, I’d like most of the key insights from the water quality data to be obtained from the 1st page of the report.
    - Overview report should resemble a chart with months and parameters, the chart can be color-coded to reflect "good"
    or "bad" health for that month and given parameter

"""
#import csv
import csv
# import pandas for data analysis and exploration
import pandas as pd

# import sqlite for persistent data storage
#import sqlite3

# import matplotlib for data visualisations
import matplotlib.pyplot as plt

#import numpy as np

data_list = []

# convert spreadsheet data to list without heading and summary given first 8 rows in spreadsheet
with open('Hillside Commons Stream Data.csv', 'r') as csvfile:
    file_reader = csv.reader(csvfile, delimiter=',')

    # skip the first 8 rows using next() method
    for i in range(8):
        next(csvfile)

    row_num = 1
    for row in file_reader:
        data_list.append(row)
        row_num += 1

# create a new csv and write the rows within list
with open('Sorted AAS CSV.csv', 'w+') as sorted_csvfile:
    # initalize writing to csv file
    csv_writer = csv.writer(sorted_csvfile)

    # writing multiple rows from list
    csv_writer.writerows(data_list)

    csv.reader(sorted_csvfile)
    file_reader = csv.reader(sorted_csvfile, delimiter=',')


# initialize csv file into pandas dataframe for sorting and exploration
# specify the file path and columns to be selected
relevant_param = ['SIte_ID', 'Site_Name', 'Event_Date', 'Air_Temp', 'Water_Temp', 'PH', 'DissolvedOxygen',
                  'DO_Saturation', 'Conductivity',]
pd_file_name = 'Sorted AAS CSV.csv'
raw_data = pd.read_csv(pd_file_name, usecols=relevant_param)
# clean up dataframe by removing rows/records with no value
AAS_Info = raw_data.dropna()

raw_ecoli_data = pd.read_csv(pd_file_name,usecols=['Event_Date','ThreeMEcoli'])
AAS_Info_Ecoli = raw_ecoli_data.dropna()


#remove timestamp from dates and insert updated dates
updated_dates = []
for i in AAS_Info["Event_Date"]:
    new = i.split()
    updated_dates.append(new[0])
AAS_Info.loc[:, "Event_Date"] = updated_dates

#remove timestamp from E.Coli dates and insert updated dates
dates_ecoli = []
for i in AAS_Info_Ecoli["Event_Date"]:
    new = i.split()
    dates_ecoli.append(new[0])
AAS_Info_Ecoli.loc[:, "Event_Date"] = dates_ecoli


# def global variables for reporting title formatting
global city
global county
global watershedname
global sitename


city = ' City: Grayson'
county = ' County: Gwinnett'
watershedname = ' Upper Ocmulgee River Watershed'
sitename = AAS_Info['Site_Name'][0]

def viz_data_air_and_water():
    """
    :returns: the visualization for air and water temp
    Threshholds to keep in mind:
    - Air Temp: No threshold
    - Water Temp: >32.2°C is bad (red zone)
    """
    site_name = AAS_Info['Site_Name'][0]
    event_date = AAS_Info['Event_Date']
    air_temp = AAS_Info['Air_Temp']
    water_temp = AAS_Info['Water_Temp']
    air_temp_F = []
    water_temp_F = []
    normal_temp = []

    # change temp from C to  F conversion
    for c in air_temp:
        air_temp_F.append(int(c * (9/5) + 32))
    for c in water_temp:
        water_temp_F.append(int(c * (9/5) + 32))
        normal_temp.append(int(32.2 * (9/5) + 32))


    plt.title('(*Air & Water Temp*)\n'
              f'{site_name},{city},{county},{watershedname}', size=15)
    # info text
    '''info_text = (f'Program Name: Arabia Mt AAS Reports\n'
                 f'Algorithm author: Darling Ngoh\n'
                 f'Contact: darlingngoh@gmail.com\n'
                 f'TESTING LOCATION: {site_name}')'''
    #plt.text(62, 96, info_text, color='red', size=9, ha='right')

# Show ‘Air_Temp’ and ‘Water_Temp’ over time (line graph)

    # label x and y axis
    plt.xlabel('Date', size=12)
    # make labels horizontal given rotation param, rotation for vertical and pad for spacing
    plt.ylabel('AIR & \nWATER TEMPERATURE \n(F)', rotation=0, ha='left', labelpad=120, size=12)

    #plot values
    plt.plot(event_date, air_temp_F, label='Air Temp', color='Orange')
    plt.plot(event_date, water_temp_F, label='Water Temp', color='Blue')
    plt.plot(event_date, normal_temp, label="Water Temp Threshold - *temps above 89 is bad (red zone)", color='Red')

    # add value labels on top of the bars
    for num, val in enumerate(air_temp_F):
        plt.text(num, val + 0.5, str(val), ha='right', va='bottom', size=7)
    for num, val in enumerate(water_temp_F):
        plt.text(num, val + 0.5, str(val), ha='left', va='bottom', size=7)

    # set date output format
    plt.xticks(event_date, rotation=70)
    # set grid lines for visual threshold monitoring
    plt.grid(axis='y')
    # ensure legend is present
    plt.legend()
    plt.show()


def viz_data_ph_and_conductivity():
    """
    Returns: pH & Conductivity on the same graph
    param/thresholds:
     - Conductivity: No threshold
     - pH has a middle zone: We want our data to fall between 6-8.5. If is above or below that zone, it is bad.

    """
    # initialize arrays for plotting
    site_name = AAS_Info['Site_Name'][0]
    event_date = AAS_Info['Event_Date']
    conductivity = AAS_Info['Conductivity']
    ph = AAS_Info['PH']
    low_zone_ph = []
    high_zone_ph = []

    # set low and high parameters for ph threshold
    for param in ph:
        low_zone_ph.append(6)
        high_zone_ph.append(8.5)

    plt.title('(*pH *)\n'f'{site_name},{city},{county},{watershedname}', size=15)

    # label x and y axis
    plt.xlabel('Date', size=12)
    # make labels horizontal given rotation param, rotation for vertical and pad for spacing
    plt.ylabel('PH', rotation=0, ha='left', labelpad=120, size=12)

    # plot values
    plt.plot(event_date,ph,label='PH',color='blue')
    #plt.plot(event_date,conductivity,label='Conductivity',color='green')
    plt.plot(event_date,low_zone_ph,label='Low-zone PH threshold',color='red')
    plt.plot(event_date, high_zone_ph, label='High-zone PH threshold',color='red')

    # set date output format
    plt.xticks(event_date, rotation=70)

    # ensure legend is present
    plt.legend()
    # add gridlines for easier readability
    plt.grid()

    plt.show()


    # plot conductivity
    plt.title('(*Conductivity*)\n'f'{site_name},{city},{county},{watershedname}', size=15)

    # label x and y axis
    plt.xlabel('Date', size=12)
    # make labels horizontal given rotation param, rotation for vertical and pad for spacing
    plt.ylabel('Conductivity', rotation=0, ha='left', labelpad=120, size=12)

    # plot values
    plt.plot(event_date,conductivity,label='Conductivity',color='green')

    # set date output format
    plt.xticks(event_date, rotation=70)

    # ensure legend is present
    plt.legend()
    # add gridlines for easier readability
    plt.grid()

    plt.show()


# visualize do on its own graph
def viz_data_do():
    # Param to keep in mind- DO: <4 mg/L is bad

    # initialize arrays for plotting
    site_name = AAS_Info['Site_Name'][0]
    event_date = AAS_Info['Event_Date']
    DO = AAS_Info['DissolvedOxygen']
    low_do = []

    for param in DO:
        low_do.append(4)


    plt.title('(*Dissolved Oxygen (DO)*)\n'
              f'{site_name},{city},{county},{watershedname}', size=15)

    # label x and y axis
    plt.xlabel('Date', size=12)
    # make labels horizontal given rotation param, rotation for vertical and pad for spacing
    plt.ylabel('Dissolved Oxygen\n (mg/L)', rotation=0, ha='left', labelpad=120, size=12)

    # plot values
    plt.plot(event_date,DO,label='Dissolved Oxygen',color='blue')
    plt.plot(event_date,low_do,label='Anything <4 mg/L is bad',color='red')


    # set date output format
    plt.xticks(event_date, rotation=70)

    # ensure legend is present
    plt.legend()
    # add gridlines for easier readability
    plt.grid()

    plt.show()


# visualize E.coli on it's own graph
def viz_data_ecoli():
    # param to keep in mind: E. Coli: >1000 is bad

    # initialize arrays for plotting
    site_name = AAS_Info['Site_Name'][0]
    event_date = AAS_Info_Ecoli['Event_Date']
    ecoli = AAS_Info_Ecoli['ThreeMEcoli']
    high_ecoli_warning = []

    for param in ecoli:
        high_ecoli_warning.append(1000)

    plt.title('(*Three M Ecoli*)\n'
              f'{site_name},{city},{county},{watershedname}', size=15)

    # label x and y axis
    plt.xlabel('Date', size=12)
    # make labels horizontal given rotation param, rotation for vertical and pad for spacing
    plt.ylabel('Ecoli', rotation=0, ha='left', labelpad=120, size=12)

    # plot values
    plt.plot(event_date, ecoli, label='E. Coli', color='green')
    plt.plot(event_date, high_ecoli_warning, label='Anything >1000 is bad', color='red')

    # set date output format
    plt.xticks(event_date, rotation=70)

    # ensure legend is present
    plt.legend()
    # add gridlines for easier readability
    plt.grid()

    plt.show()

def RunReport():
    viz_data_air_and_water()
    viz_data_ph_and_conductivity()
    viz_data_do()
    viz_data_ecoli()

RunReport()

# Define thresholds
thresholds = {
    'Air_Temp': None,  # No threshold
    'Water_Temp': 32.2,
    'Conductivity': None,  # No threshold
    'PH': (6, 8.5),
    'DissolvedOxygen': 4,
    'ThreeMEcoli': 1000
}
# Merge E.Coli data into the main dataset
AAS_Info = AAS_Info.merge(AAS_Info_Ecoli, on='Event_Date', how='left')

# Convert Event_Date to datetime for better handling
AAS_Info['Event_Date'] = pd.to_datetime(AAS_Info['Event_Date'], errors='coerce')

# Filter data to include only records from 1/1/2023 onward
filter_date = pd.to_datetime('2023-1-1')
AAS_Info = AAS_Info[AAS_Info['Event_Date'] >= filter_date]

# Extract month and year for easier grouping
AAS_Info['Month'] = AAS_Info['Event_Date'].dt.month
AAS_Info['Year'] = AAS_Info['Event_Date'].dt.year

# Prepare data for visualization
parameters = ['Air_Temp', 'Water_Temp', 'Conductivity', 'PH', 'DissolvedOxygen', 'ThreeMEcoli']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
table_data = []

for parameter in parameters:
    row = [parameter] + [''] * 12  # Initialize row with parameter name and 12 empty cells
    for month in range(1, 13):  # Loop over each month
        monthly_data = AAS_Info[AAS_Info['Month'] == month][parameter]
        if not monthly_data.empty:
            value = monthly_data.values[0]  # Assuming one reading per month
            row[month] = value  # Insert value (for debugging purposes, you can leave this out if you don't want to display the value)
    table_data.append(row)

# Plot the table
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')

# Create the table
table = ax.table(cellText=table_data, colLabels=['Parameter'] + months, cellLoc='center', loc='center')

# Apply color coding
for i, parameter in enumerate(parameters):
    for j in range(1, 13):
        cell = table[(i + 1, j)]
        value = table_data[i][j]
        if value != '':  # If there's a value to check
            if parameter == 'PH':
                if thresholds[parameter][0] <= value <= thresholds[parameter][1]:
                    color = 'green'
                else:
                    color = 'red'
            elif parameter == 'DissolvedOxygen':
                color = 'green' if value >= thresholds[parameter] else 'red'
            elif parameter == 'Water_Temp':
                color = 'green' if value <= thresholds[parameter] else 'red'
            elif parameter == 'ThreeMEcoli':
                color = 'green' if value <= thresholds[parameter] else 'red'
            else:
                color = 'green'  # For parameters with no threshold
            cell.set_facecolor(color)
        else:
            cell.set_facecolor('white')  # If no value, leave it white

# Set font size and maintain the parameter names
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 3.6)

plt.title(f'Water Quality Overview Report 2023\n {sitename},{city},{county},{watershedname}', size=15)

plt.show()
