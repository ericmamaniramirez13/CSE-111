import tkinter as tk
import random
import math


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)
    draw(canvas, 0, 0, width-1, height-1, 100)
    root.mainloop()
    

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    sun_feft = scene_left +50
    sun_top = scene_top +50
    lines = 10
    draw_sun(canvas, sun_feft, sun_top, lines)
    draw_clouds(canvas)
    draw_grass(canvas, scene_right, scene_bottom)
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 50
    tree_top = scene_top + 240
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_walls(canvas)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, left, top, right, bottom):
    canvas.create_rectangle(left, top, right, bottom, fill="turquoise1")
def draw_sun(canvas, x, y, lines):
    canvas.create_oval(x, y, x+100, y+100, fill="gold", width=False)
    lines = 10
    for i in range (lines):
        angle = (2*math.pi/lines)*i
        ray_x = 100 + math.cos(angle)*100
        ray_y = 100 + math.sin(angle)*100
        canvas.create_line(100,100,ray_x,ray_y, fill="gold", width=3)
def draw_clouds(canvas):
    canvas.create_oval(150, 100, 350, 150, fill="floralWhite" )
    canvas.create_oval(350, 0, 600, 50, fill="floralWhite")
    canvas.create_oval(550, 50, 750, 100, fill="floralWhite")
def draw_grass(canvas, right, bottom):
    canvas.create_rectangle(0, 300, right, bottom, fill="forestGreen")
def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height
    for i in range (0,8):
        # Draw the trunk of the pine tree.
        canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")
        # Draw the crown (also called skirt) of the pine tree.
        canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")
        trunk_left+=100
        trunk_right+=100
        peak_x+=100
        skirt_right+=100
        skirt_left+=100
def draw_walls(canvas):
    x=0
    z=50
    top=25
    for i in range(0,10):    
        canvas.create_polygon(x,400,top,350,z,400,z,500,x,500, fill="tan4")
        if i ==4:
            x+=200
            z+=200
            top+=200
        x+=55
        z+=55
        top+=55

def draw(canvas, left, top, right, bottom, grid_space):
    for i in range(top, bottom, grid_space):
        canvas.create_line(left, i, right, i)
    for i in range(left, right, grid_space):
        canvas.create_line(i, top, i, bottom)
# Call the main function so that
# this program will start executing.
main()