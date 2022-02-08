"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
02/08/2022
"""
import arcade

#Open an Arcade window with (Width, Height, "Window_name")
arcade.open_window(600, 600, "Test")

#Set background color of window (can use RGB)
arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

arcade.start_render()

arcade.finish_render()

#Keep the window up until user closes.
arcade.run()

