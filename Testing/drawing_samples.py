"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
02/08/2022
"""
from tkinter.messagebox import YES
import arcade

#Open an Arcade window with (Width, Height, "Window_name")
arcade.open_window(600, 600, "Test")

#Set background color of window (can use RGB)
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

#DRAWING START...
arcade.start_render()


#GRASS
arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.csscolor.DARK_GREEN)

#SUN
def sun():
    arcade.draw_circle_filled(70, 470, 30, arcade.csscolor.YELLOW)
    arcade.draw_line(70, 530, 70, 410, arcade.csscolor.YELLOW, 3) #Top to Bottom
    arcade.draw_line(10, 470, 130, 470, arcade.csscolor.YELLOW, 3) #Left to Right
    arcade.draw_line(30, 435, 105, 508, arcade.csscolor.YELLOW, 3)
    arcade.draw_line(30, 508, 105, 435, arcade.csscolor.YELLOW, 3)

def clouds():
    arcade.draw_ellipse_filled(50, 470, 45, 30, arcade.csscolor.PAPAYA_WHIP)

clouds()

#DRAWING STOPS...
arcade.finish_render()

#Keep the window up until user closes.
arcade.run()

