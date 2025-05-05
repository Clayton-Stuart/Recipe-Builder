import os

saved, clickedOnLoop = False, False
running = True

buttons = []
dropdowns = []

page = "home"

deleted_image = False

save_path = None
name = "New Recipe"
ingredients = {}
titles = []
steps = []
css = ""
ingredients_text = """Amount of ingredient 1
Amount of ingredient 2
500 grams of Flour"""

scroll_offset_img = 0

images = {}
cached_images = {}
py_img_obj = {}

img_up_box = [0, 0, 0, 0]

file_dynamic_startup = open(os.path.join('.', 'lib', 'persistent_vars.txt'), 'r')
lines = file_dynamic_startup.readlines()

if lines[0].strip() == "True":
    dark = True
else:
    dark = False

file_dynamic_startup.close()
del file_dynamic_startup

text_box_active = False