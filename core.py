import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs

outline = gpd.read_file('data/NIoutline/NI_outline.shp')
mclocation = gpd.read_file('data/mclocation/mclocation.shp')

fig, ax = plt.subplots()
ax.set_aspect('equal')
outline.plot(ax=ax, color='white', edgecolor='black')
mclocation.plot(ax=ax, marker='o', color='red', markersize=5)

plt.show();