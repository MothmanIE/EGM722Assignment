import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from cartopy.feature import ShapelyFeature
#import cartopy.crs as ccrs
import geocoder #Library which gets user LatLong through google API. Uses Requests and Ratelim as dependencies
import tkinter as tkk

#----------Import Shapefiles----------#
outline = gpd.read_file('data/NIoutline/NI_outline.shp') #Outline of Northern Ireland for Reference
mclocation = gpd.read_file('data/mclocation/mclocation2.shp') #Point database of every McDonalds in Northern Ireland
myCRS = 'EPSG:4326'

#----------plotting shapefiles----------#
fig, ax = plt.subplots() #Defines Subplots allowing for multiple map layers
ax.set_aspect('equal')
outline.plot(ax=ax, color='white', edgecolor='black')
mclocation.plot(ax=ax, marker='o', color='red', markersize=5)

#----------User Prompt----------#
ws = tkk.Tk()
ws.title('welcome')
introText = tkk.Text(ws, height=3, width=90)
introText.pack()
introText.insert('1.0', 'Welcome to the nearest Mcdonalds locator. You can choose to find the nearest McDonalds in Northern Ireland from your location, or enter custom Lat/Long coordinates')

tkk.Button(ws, text="My Location").pack(pady=20)
tkk.Button(ws, text="Enter Lat/Long").pack(pady=20)

#----------Importing user Location for Point----------#
g = geocoder.ip('me')
userloc = g.latlng
userdf = pd.DataFrame({'Longitude': userloc[1], 'Latitude':userloc[0]}, index=[0])
gdf = gpd.GeoDataFrame(userdf, geometry=gpd.points_from_xy(userdf.Longitude, userdf.Latitude, crs=myCRS))

gdf.plot(ax=ax, marker='o', color='blue', markersize=7)

#----------Plotting Improved----------#

#The plan is for the user to be able to enter a coordinate
# and for the program to display the nearest McDonalds via a straight line
# I wonder if I could enable location acccess...

#Displays the map
plt.show()