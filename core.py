import geopandas
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from cartopy.feature import ShapelyFeature
from shapely.geometry import LineString
import geocoder #Library which gets user LatLong through google API. Uses Requests and Ratelim as dependencies
import tkinter as tkk #Tkinter is heavily used in this program for the UI elements
from shapely.ops import nearest_points
import numpy as np

#----------1.0 Import Shapefiles----------#
outline = gpd.read_file('data/NIoutline/NI_outline.shp') #Outline of Northern Ireland for Reference
mclocation = gpd.read_file('data/mclocation/mclocation2.shp') #Point database of every McDonalds in Northern Ireland. Build this file for an earlier module from FHSR data.
myCRS = 'EPSG:4326'

#----------1.1 plotting shapefiles----------#
fig, ax = plt.subplots() #Defines primary plot as 'ax', allowing for multiple elements on the same plot.
ax.set_aspect('equal')
outline.plot(ax=ax, color='white', edgecolor='black')
mclocation.plot(ax=ax, marker='o', color='red', markersize=5)

#----------2.0 Primary functions----------#
#----------2.1 Find Line from User to nearest McDonalds----------#

#union McLocation for nearest point. This took about 3 days to get working alone.
def nearMC():
    pts3 = mclocation.geometry.unary_union
    #Function used to generate nearest point calculation
    def near(point, pts=pts3):
        #Shapely Nearest_points find the closest point to the User Input
        nearest = mclocation.geometry == nearest_points(point, pts)[1]
        #Returns the POSTCODE value of the nearest point, taken from the shapefile.
        print('Your Nearest McDonalds in Northern Ireland: ', mclocation[nearest].POSTCODE)
        return mclocation[nearest].POSTCODE.to_numpy()[0]
    gdf['Nearest'] = gdf.apply(lambda row: near(row.geometry), axis=1)
    for i, row in gdf.iterrows():
        nearestDF=[nearest_points(row.geometry, pts3)[0], nearest_points(row.geometry, pts3)[1]]
        #Returns Both nearest point and user point as an array
        geom = LineString(nearestDF)
        #Converts array of points to linestring, then a GeoDataFrame line
        gdfNear = geopandas.GeoDataFrame(geometry=[geom]);
    return gdfNear

#----------2.2 Importing user Location for Point----------#

#This functions obtains the users lat/long from GeoCoder as a list
#The coordinates are then called to convert into a dataframe, then a GeoDataFrame
#The Coordinates are then plotted as a blue point on the map
#The function then closes the dialogue window, and plots the map.
def userGeoLoc():
    global gdf
    g = geocoder.ip('me')
    userloc = g.latlng
    userdf = pd.DataFrame({'Longitude': userloc[1], 'Latitude':userloc[0]}, index=[0])
    gdf = gpd.GeoDataFrame(userdf, geometry=gpd.points_from_xy(userdf.Longitude, userdf.Latitude, crs=myCRS))
    gdf.plot(ax=ax, marker='o', color='blue', markersize=7)
    nearMC().plot(ax=ax, color='blue') #Fine nearest Line and Plot
    root.destroy() #Close Menus
    plt.show() #Display Map
    return gdf

#----------2.3 Taking User Submission for point---------->

#Funtion will open prompts for latitude/longitude
#Saves them as list, then plots in the same way as above.
def userManualEntry():
    window = tkk.Toplevel(root) #Opens a new menu for user inputs.
    #Nested function for registering user input and generating map
    def genMapLaLo():
        global gdf
        UserLat = EnterLat.get() #obtains user inputs from menu
        UserLong = EnterLong.get()
        float(UserLat)
        float(UserLong) #converts user input to float
        userdf = pd.DataFrame({'Longitude': UserLong, 'Latitude':UserLat}, index=[0])
        gdf = gpd.GeoDataFrame(userdf, geometry=gpd.points_from_xy(userdf.Longitude, userdf.Latitude, crs=myCRS)) #User Input converted to GeodataFrame
        gdf.plot(ax=ax, marker='o', color='blue', markersize=7) #Plot User Point
        nearMC().plot(ax=ax, color='blue') #Fine nearest Line and Plot
        plt.show() #Display Map
        root.destroy() #Close Menus

    #Code for User Entry Window
    window.title('Manual Entry')
    LatLongIntro = tkk.Label(window, text='Enter Lat/Long coordinates below')
    tkk.Label(window,text='Latitude: ').grid( column=0, row=0, )
    tkk.Label(window, text='Longitude: ').grid( column=0, row=1)
    EnterLat= tkk.Entry(window)
    EnterLat.grid(column=1, row=0)
    EnterLong= tkk.Entry(window)
    EnterLong.grid(column=1, row=1)
    submitLaLo = tkk.Button(window, text='Submit', command=genMapLaLo).grid(columnspan=2)
    window.mainloop()
    return gdf


#----------3.0 User Prompt GUI----------#
root = tkk.Tk() #Establish intro Screen
root.title('welcome')
#intro text for screen1 of dialogue tree
introText = tkk.Label(root, text='Welcome to the nearest Mcdonalds locator. You can choose to find the nearest McDonalds in Northern Ireland from your location, or enter custom Lat/Long coordinates')

#Buttons to choose between Geolocation or custom lat/long
uGLButt = tkk.Button(root, text="My Location", command=userGeoLoc)
LaLoButt = tkk.Button(root, text="Enter Lat/Long", command=userManualEntry)

introText.grid(columnspan=2)
uGLButt.grid(row=1, column=0)
LaLoButt.grid(row=1, column=1)

root.mainloop()
