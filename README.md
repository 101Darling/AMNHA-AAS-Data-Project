# AMNHA-AAS-Data-Project
This project focuses on visualizing water stream chemical testing data to engage volunteers and the community through the Arabia Mt. Adopt A Stream program implementation.

# File: AAS Data Project Arabia Mountain.py
# Author: Darling Ngoh
# Contact: darlingngoh@gmail.com
# Date:6/08/24


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
