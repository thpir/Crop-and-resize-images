import glob
from PIL import Image

# Store the path where your list of files are stored
# folPath = r'C:\Users\tpirmez\Documents\SOFTWARE\DOC\Python\resizeImg\resources'
folPath = r'resources'

# Initialize a counter
counter = 0

# Use the glob library to generate a list of filepaths of each file stored in the folder defined in folPath
# And iterate through every file
for filePath in glob.glob("{0}\*.jpg".format(folPath)):
    # print the filepath
    print(filePath)

    # Open the image and find original width and height
    image = Image.open(filePath)
    width = image.size[0]
    height = image.size[1]

    # Determine the aspect ratio of the original image
    aspect = width / float(height)

    # Define the desired aspect ratio
    ideal_width = 800
    ideal_height = 600
    ideal_aspect = ideal_width / float(ideal_height)

    if aspect > ideal_aspect:
        # Then crop the left and right edges
        new_width = int(ideal_aspect * height)
        offset = (width - new_width) / 2
        resize = (offset, 0, width - offset, height)
    else:
        # Then crop the top and NOT the bottom
        new_height = int(width / ideal_aspect)
        offset = height - new_height
        resize = (0, offset, width, height)

    # Info: Antialiasing is a technique used in digital imaging to reduce the visual defects that occur when high-resolution images are presented in a lower resolution.
    image_resized = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)

    # Save the new image in the output folder
    # image_resized.save(r'C:\Users\tpirmez\Documents\SOFTWARE\DOC\Python\resizeImg\resources\output\resized' + str(counter) + '.jpg') 
    image_resized.save(r'resources\output\resized' + str(counter) + '.jpg')

    # Update the counter
    counter += 1   


