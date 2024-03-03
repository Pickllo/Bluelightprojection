import cv2
import numpy as np
import math
import random

# BLue
color1 = (255, 0, 0)
# Black
color2 = (0, 0, 0)
def generate_random_inputs():
    num_stripes = random.randint(1, 20)
    num_squares = random.randint(1, 20)
    direction = random.randint(-1, 1)
    speedpercent = random.randint(1, 100)
    while direction == 0:
        direction = random.randint(-1, 1)

    return num_stripes, num_squares, direction, speedpercent

def Hstripes(width, height, num_stripes, color1, color2, speedpercent,direction):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    stripe_height = height // num_stripes
    speed1 = int(10+(1-speedpercent / 100) * (250-10))
    speed2 = int(direction*((speedpercent/100)*10))

    for i in range(num_stripes):
        color = color1 if i % 2 == 0 else color2
        image[i * stripe_height:  (i+1) * stripe_height, :, :] = color

    while True:
        image = np.roll(image, shift=speed2, axis=0)
        cv2.imshow("Moving Vertical Stripes", image)
        key = cv2.waitKey(speed1)  # Adjust the delay time between frames (in milliseconds)
        if key != -1:
            break

    cv2.destroyAllWindows()

def Vstripes(width, height, num_stripes, color1, color2, speedpercent,direction):
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    # Calculate the width of each stripe
    stripe_width = width // num_stripes
    speed = int(10+(1-speedpercent / 100) * (250-10))
    speed2 = int(direction*((speedpercent/100)*10))

    for i in range(num_stripes):
        color = color1 if i % 2 == 0 else color2
        image[:, i * stripe_width : (i + 1) * stripe_width, :] = color

    while True:
        image = np.roll(image, shift=speed2 , axis=1)
        cv2.imshow("Moving Vertical Stripes", image)
        key = cv2.waitKey(speed)  # Adjust the delay time between frames (in milliseconds)

        if key != -1:
            break

    cv2.destroyAllWindows()

# def checkerboard(width, height, num_squares, color1, color2):
#     image = np.ones((height, width, 3), dtype=np.uint8) * 255
#
#     # Calculate the width and height of each square
#     square_width = width // num_squares
#     square_height = height // num_squares
#
#     # Draw the checkerboard pattern
#     for i in range(num_squares):
#         for j in range(num_squares):
#             # Calculate the starting and ending coordinates of each square
#             start_x = j * square_width
#             end_x = (j + 1) * square_width
#             start_y = i * square_height
#             end_y = (i + 1) * square_height
#
#             # Draw the square with the specified color
#             color = color1 if (i + j) % 2 == 0 else color2
#             image[start_y:end_y, start_x:end_x, :] = color
#
#     cv2.imshow("Checkerboard Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# def Dstripes(width, height, num_stripes, slope, color1, color2):
#     image = np.ones((height, width, 3), dtype=np.uint8) * 0
#
#     # Calculate the thickness to make the diagonal stripes seamless
#     thickness = max(width, height) // num_stripes
#
#     # Calculate the length of the diagonal line to fill the entire image
#     diagonal_length = int(math.sqrt(width ** 2 + height ** 2))
#
#     # Calculate the angle of the diagonal lines
#     angle_rad = math.atan(slope)
#
#     # Draw the diagonal stripes
#     for i in range(num_stripes):
#         # Calculate the starting and ending points of each diagonal stripe
#         start_point = (0, i * height // num_stripes)
#         # Calculate the x-coordinate of the ending point based on the diagonal length
#         end_x = diagonal_length
#         # Calculate the y-coordinate of the ending point based on the width and slope
#         end_y = i * height // num_stripes + int(diagonal_length * slope * math.tan(angle_rad))
#         end_point = (end_x, end_y)
#
#         # Determine the color based on the stripe index
#         color = color1 if i % 2 == 0 else color2
#
#         # Draw the diagonal stripe
#         cv2.line(image, start_point, end_point, color, thickness=thickness)
#
#     cv2.imshow("Diagonal Striped Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# def spiral(width, height, num_turns, color1):
#     image = np.ones((height, width, 3), dtype=np.uint8) * 0
#
#     # Center coordinates
#     center_x, center_y = width // 2, height // 2
#
#     # Maximum radius to cover the entire image
#     max_radius = min(width, height) // 2
#
#     # Number of points to draw for the spiral
#     num_points = 2000
#
#     # Draw the spiral
#     for i in range(num_points):
#         angle = num_turns * 2 * math.pi * i / num_points
#         radius = i * max_radius / num_points
#
#         # Calculate the coordinates of the point on the spiral
#         x = int(center_x + radius * math.cos(angle))
#         y = int(center_y + radius * math.sin(angle))
#
#         # Draw the point on the image
#         cv2.circle(image, (x, y), 1, color1, -1)
#
#     cv2.imshow("Spiral Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# def radial_gradient(width, height, color1, color2):
#     image = np.ones((height, width, 3), dtype=np.uint8) * 255
#
#     # Center coordinates
#     center_x, center_y = width // 2, height // 2
#
#     # Generate radial gradient with color interpolation
#     for y in range(height):
#         for x in range(width):
#             distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
#             intensity = int(255 * distance / max(center_x, center_y))
#
#             # Interpolate between color1 and color2 based on intensity
#             color = tuple(np.clip(int(c1 + (c2 - c1) * intensity / 255), 0, 255) for c1, c2 in zip(color1, color2))
#             image[y, x] = color
#
#     cv2.imshow("Radial Gradient Image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Example usage:
# for all
width = int(input("Enter the width of the image: "))
height = int(input("Enter the height of the image: "))
randomizer = input("Do you want to randomize the patterns (Y/N)?").upper()

if randomizer == "Y":
    num_stripes, num_squares, direction, speedpercent = generate_random_inputs()
    Hstripes(width, height, num_stripes, color1, color2, speedpercent, direction)
    num_stripes, num_squares, direction, speedpercent = generate_random_inputs()
    Vstripes(width, height, num_stripes, color1, color2, speedpercent, direction)
    # checkerboard(width, height, num_squares, color1, color2)
    # num_stripes, num_squares, slope, num_turns = generate_random_inputs()
    # Dstripes(width, height, num_stripes, slope, color1, color2)
    # spiral(width, height, num_turns, color1)
    # # radial_gradient(width, height, color1, color2)
else:
    # for stripes
    num_stripes = int(input("Enter the number of stripes: "))
    speedpercent = int(input("Enter the speed percentage: "))
    direction = int(input("1 or -1: "))
    # for checkerboard
    # num_squares = int(input("Enter the number of squares per row/column: "))
    # #for diagonal stripe
    # slope = float(input("Enter the slope of the lines (e.g., 0.5 for a 45-degree angle): "))
    # # for spiral
    # num_turns = float(input("Enter the number of turns for the spiral: "))
    Hstripes(width, height, num_stripes, color1, color2, speedpercent, direction)
    Vstripes(width, height, num_stripes, color1, color2, speedpercent, direction)
    # checkerboard(width, height, num_squares, color1, color2)
    # Dstripes(width, height, num_stripes, slope, color1, color2)
    # spiral(width, height, num_turns, color1)
    # radial_gradient(width, height, color1, color2)
