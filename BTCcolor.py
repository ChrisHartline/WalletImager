import random
from PIL import Image, ImageDraw

def visualize_address(address, grid_size):
    base58_colors = {}
    for char in set(address):
        base58_colors[char] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    cell_size = 20
    image_size = (grid_size[0] * cell_size, grid_size[1] * cell_size)
    
    image = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(image)
    
    for i, char in enumerate(address):
        row = i // grid_size[1]
        col = i % grid_size[1]
        x1, y1 = col * cell_size, row * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        draw.rectangle((x1, y1, x2, y2), fill=base58_colors[char])
    
    image.save('wallet_address_visualization4.png')

# Example usage
#address = '14  .... QAnQa'
address = 'bc '

#'1HtBYZ3poESWg5csdrz5CXpgqNtjzBH3J8'
#'1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2' 
grid_size = (5, 7)
visualize_address(address, grid_size)