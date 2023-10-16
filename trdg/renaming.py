from PIL import Image

# Open the image file
image = Image.open(r'C:\Users\v23ASayed2\Desktop\TextRecognitionDataGenerator\trdg\out\0.jpg')

# Set the new size for the image
new_size = (320, 48)

# Resize the image
resized_image = image.resize(new_size)

# Save the resized image as a new file
resized_image.save('resized_image.jpg')