# EGM722Assignment
 - Introduction
The nearestMC tool is a program which locates the nearest McDonalds in Northern Ireland relative to the user prescribed Latitude Longitude Coordinates.
The user has the choice of having the program use their own coordinates through the use of Geocoder APIs, or to enter a customised Latitude/Longitude coordinate.
Once the user coordinate is determined, a straight line is drawn between the user point and the nearest McDonalds, and is displayed on a Map.
The GitHub Repository for this Assignment can be found at https://github.com/MothmanIE/EGM722Assignment .

Setup
 - Prerequisites
In order to setup this application, the user must first install Git, found at https://git-scm.com/.
Additionally, it is strongly recommended the user install Conda and the Anaconda navigator GUI, in order to create the environment in which to run the program.
Getting Started
Once Git and Anaconda are installed, the GitHub repository must be cloned. This can be done through the GitHub desktop application, or through the console using Git Bash.

 - GitHub Desktop:
From the Applications Main page, select File > Clone Repository > URL. In the URL input box, enter the link to the repository: https://github.com/MothmanIE/EGM722Assignment. 

 - Git Bash (Windows):
Use the Windows Key and search Git Bash. Clicking this will open a command prompt. Enter:
Git clone https://github.com/MothmanIE/EGM722Assignment
After entering the command, the repository should be downloaded, and a confirmation message should appear in the console shortly.

 - Setting up the Environment:
In the Anaconda navigator, select Environments > Import and navigate to the location of the cloned repository in order to select the environment.yml file, which contains the necessary extensions.
With the repository and environment set up, it is recommended to open the core.py file using an IDE such as PyCharm.

 - Dependencies
-GeoPandas
-MatPlotLib
-GeoCoder
-Cartopy

 - Data Files:
The provides shapefiles are an outline of Northern Ireland obtained from Ordinance Survey Northern Ireland (https://www.nidirect.gov.uk/campaigns/ordnance-survey-of-northern-ireland), and a Shapefile which contains a point database of  every McDonalds in Northern Ireland and their postcode. This data was adapted from publicly available data provided by the Food Standards Agency (FHRS) at https://ratings.food.gov.uk/. 
The functions in this application could conceivably work with any Point Based shapefile with minor modifications, however at present it is designed for the McLocations shapefile.
Running the Application
Once the application is open in the user IDE, press the Run button and Tkinter GUI should appear prompting the user to take further action
