from PIL import Image
from turtle import *

#loads in new image
image = Image.open('SmallTreeBoa.jpg')

#gets width and height of image
width, height = image.size

#list of pixel RGB values
pixelValues = list(image.getdata())

#create a new list to hold string colors
colorsOfPicture = []

#determines what color pixel is closest to
for rgb in pixelValues:
    if rgb[0] < 200 and rgb[1] < 200 and rgb[2] > 200:
        colorsOfPicture.append("blue")
    elif rgb[0] > 200 and rgb[1] < 200 and rgb[2] < 200:
        colorsOfPicture.append("red")
    else:
        colorsOfPicture.append("green")

dookie = Turtle()
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
setworldcoordinates(0,0,width*10,height*10)
tracer(0,0)
num = 0
dookie.speed(0)
for i in list(colorsOfPicture):
    dookieAngle = 90
    xPos,yPos = dookie.pos()
    dookie.color(i)
    fillcolor(i)
    dookie.begin_fill()
    for i in range(5):
        dookie.forward(5)
        dookie.setheading(dookieAngle)
        dookieAngle += 90
    num += 1
    #this allows for different rows
    #rather than a straight line
    if num % width == 0:
        dookie.up()
        xPos +=4.5
        dookie.goto(xPos,-.01)
        dookie.pendown()
    #gives update every 5000 pixels drawn
    if num % 5000 == 0:
        update()
    dookie.end_fill()
update()

done()
