import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from cartopy.feature import ShapelyFeature
import geocoder #Library which gets user LatLong through google API. Uses Requests and Ratelim as dependencies
import tkinter as tkk

#----------1.0 Import Shapefiles----------#
outline = gpd.read_file('data/NIoutline/NI_outline.shp') #Outline of Northern Ireland for Reference
mclocation = gpd.read_file('data/mclocation/mclocation2.shp') #Point database of every McDonalds in Northern Ireland
myCRS = 'EPSG:4326'

#----------1.1 plotting shapefiles----------#
fig, ax = plt.subplots() #Defines Subplots allowing for multiple map layers
ax.set_aspect('equal')
outline.plot(ax=ax, color='white', edgecolor='black')
mclocation.plot(ax=ax, marker='o', color='red', markersize=5)

#----------2.0 Primary functions----------#
#The intention here is to have a flow where you will be given a prompt to choose either
#Geolocation or custom Lat/Long, then the window closes and a ndew one opens with relevant prompts. Then the map generates
#based on that
def nearestMc():
    dist = {r[0]: r[1].geometry.distance(br_geom) for r in points.iterrows()}
#----------2.1 Importing user Location for Point----------#

#This functions obtains the users lat/long from GeoCoder as a list
#The coordinates are then called to convert into a dataframe, then a GeoDataFrame
#The Coordinates are then plotted as a blue point on the map
#The function then closes the dialogue window, and plots the map.
def userGeoLoc():
    g = geocoder.ip('me')
    userloc = g.latlng
    userdf = pd.DataFrame({'Longitude': userloc[1], 'Latitude':userloc[0]}, index=[0])
    gdf = gpd.GeoDataFrame(userdf, geometry=gpd.points_from_xy(userdf.Longitude, userdf.Latitude, crs=myCRS))
    gdf.plot(ax=ax, marker='o', color='blue', markersize=7)
    global root
    root.destroy()
    plt.show()
    print(nearestMc())
    return gdf

#----------2.2 Taking User Submission for point---------->
#Funtion will open prompts for latitude/longitude
#Saves them as list, then plots in the same way as above.
def userManualEntry():
    window = tkk.Toplevel(root)
    #Nested function for registering user input and generating map
    def genMapLaLo():
        UserLat = EnterLat.get()
        UserLong = EnterLong.get()
        print(UserLat)
        print(UserLong)
        float(UserLat)
        float(UserLong)
        userdf = pd.DataFrame({'Longitude': UserLong, 'Latitude':UserLat}, index=[0])
        gdf = gpd.GeoDataFrame(userdf, geometry=gpd.points_from_xy(userdf.Longitude, userdf.Latitude, crs=myCRS))
        gdf.plot(ax=ax, marker='o', color='blue', markersize=7)

        plt.show()

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
    root.destroy()
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
#----------Distance calculation----------#