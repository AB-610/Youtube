from os import kill
from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
import csv
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from seaborn import set_palette
from seaborn.palettes import color_palette

# from seaborn.rcmod import axes_style

filename = "enter name and location for file to be saved as"
data = pd.read_csv(filename)


images = []
with open(filename, "r") as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        images.append(row[5])
del images[0]
path = "path of the location to save the file"
n = 1

"""
path='path of the location to save the file'
n=1
for url in images:
    
    img=f"{path}"+"%d.jpg" %n
    urllib.request.urlretrieve(
    url,
    img)
    print("Image %d saved",n)
    n=n+1
"""

paths = []
for url in images:
    img = f"{path}" + "%d.jpg" % n
    paths.append(img)
    n = n + 1
sns.set_style("darkgrid")
sns.set(rc={"axes.facecolor": "#1d1d1d", "figure.facecolor": "#1d1d1d"})
plt.axes(color="r")
sns.scatterplot(data=data, x="No.", y="views", hue="(likes/views)%", marker="D")
plt.xlabel("Videos")
sns.lineplot(data=data, x="No.", y="meanviews", palette=("black"))
plt.ylabel("Views in millions")
plt.margins(0.02)
plt.show()
