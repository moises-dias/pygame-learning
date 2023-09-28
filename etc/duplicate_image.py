# from PIL import Image

# # Open the original image
# original_image = Image.open("assets/player.jpg")

# # Create a new 800x1600 image with RGBA mode
# new_image = Image.new("RGBA", (800, 1600))

# # Paste the original image onto the top half
# new_image.paste(original_image, (0, 0))

# # Create a black and white version of the original image
# bw_image = original_image.convert("L")

# # Apply the alpha channel from the original image to the black and white version
# bw_image.putalpha(original_image.getchannel("A"))

# # Paste the black and white image onto the bottom half
# new_image.paste(bw_image, (0, 800), bw_image)

# # Save the resulting image
# new_image.save("resulting_image.png")

# # Optionally, display the image
# new_image.show()

from PIL import Image

# Open the original image
original_image = Image.open("assets/player.jpg")

# Create a new 800x1600 image with RGBA mode
new_image = Image.new("RGBA", (800, 1600))

# Paste the original image onto the top half
new_image.paste(original_image, (0, 0))

# Create a black image of the same size as the original image
black_image = Image.new("RGBA", original_image.size, (0, 0, 0, 255))

# Apply the alpha channel from the original image to the black image
black_image.putalpha(original_image.getchannel("A"))

# Paste the black image onto the bottom half
new_image.paste(black_image, (0, 800), black_image)

# Save the resulting image
new_image.save("resulting_image.png")

# Optionally, display the image
new_image.show()
