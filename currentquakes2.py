import matplotlib.pyplot as plt


import matplotlib.image as mpimg
image = mpimg.imread("long_and_lat.png")
plt.imshow(image)
plt.show()

plt.axis("off")
plt.imshow(image)
plt.show()

#import cv2
#image = cv2.imread("long_and_lat.png")
plt.axis("off")
plt.imshow(image)
plt.show()

plt.axis("off")
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

plt.ylim (-150,150)
plt.xlim (-60,80)

plt.clf ()
Quakes = open("currentQuakes.txt")
#FullData = Quakes.read()
#print (FullData)

ColumnNames = Quakes.readline()
print (ColumnNames)

#Empty Lists
latitude = []
longitude = []

for line in Quakes:
   line = line.split(',')
   #print(line[0])
   latitude.append(float(line[2]))
   longitude.append(float(line[1]))


plt.scatter(longitude, latitude, label = "earthquake")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.suptitle("Demographic and Intensity of Earthquakes in 2017 Based on Hemisphere")
plt.show()