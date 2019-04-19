##
# This program will process an image and add color filter to establish a "sunset effect" by increase the level of red by 30%
#

from ezgraphics import GraphicsWindow, GraphicsImage

# input image file
filename = "input image/Golden Bridge.gif"    #input directory
origImage = GraphicsImage(filename)
win = GraphicsWindow()
canvas = win.canvas()
imageWidth = origImage.width()
imageHeight = origImage.height()

# define new image dimensions
newImage = GraphicsImage(imageWidth, imageHeight)

# output the size of image
print(imageWidth)
print(imageHeight)

# edit the image
for row in range(imageHeight):
    for col in range(imageWidth):
        red = origImage.getRed(row, col)
        newRed = int(red * 1.3)
        # if the red exceed the RGB range, it will set to the maximum
        if newRed > 255:
            newRed = 255
        green = origImage.getGreen(row, col)
        blue = origImage.getBlue(row, col)
        # set the colors of the image
        newImage.setPixel(row, col, newRed, green, blue)

# display image
canvas.drawImage(origImage)
canvas.drawImage(newImage)
win.wait()

# output image file
newImage.save("Golden Bridge Sunset.gif")