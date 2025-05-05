from lib.generating.create_file import *
from lib.constants import *
import os
from tkinter import filedialog

VERSION = open(os.path.join(".", "lib", "VERSION"), "r").read().strip()

def generate(name: str, ingredients: str, titles: str, steps: list, img_b64: dict, css: str) -> None:
    directory = filedialog.asksaveasfilename()
    if directory.split(".")[-1]!= "html" or directory.split(".")[-1]!= "htm":
        file_name = directory + ".html"
    if os.path.exists(file_name):
        count = 1
        while os.path.exists(file_name):
            count += 1
            file_name = directory + str(count) + ".html"
    if css == "":
        file = open(file_name, "wb")
        file.write(build_html(name, ingredients, titles, steps, img_b64, build_css(preset=1)).encode('utf-8'))
        file.close()
    else:
        file = open(file_name, "wb")
        file.write(build_html(name, ingredients, titles, steps, img_b64, css).encode('utf-8'))
        file.close()


def writeSaveFile(file: open, name: str, ingredients: str, titles: list, steps: list, css: str, img_b64: dict) -> None:
    file.write(bytes(VERSION, 'utf-8'))
    file.write(bytes('\n', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    file.write(bytes(name.replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    file.write(bytes(ingredients.replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    if len(titles) > 0:
        for i in titles:
            file.write(bytes('{', 'utf-8'))
            file.write(bytes(i.replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
            file.write(bytes('}', 'utf-8'))
    else:
        file.write(bytes('None', 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    if len(steps) > 0:
        for i in steps:
            file.write(bytes('{', 'utf-8'))
            file.write(bytes(i.replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
            file.write(bytes('}', 'utf-8'))
    else:
        file.write(bytes('None', 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    if css != "":
        file.write(bytes(css.replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
    else:
        file.write(bytes('None', 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.write(bytes('<', 'utf-8'))
    if len(img_b64) > 0:
        keys = list(img_b64.keys())
        for i in keys:
            file.write(bytes('{', 'utf-8'))
            file.write(bytes(str(i).replace('&', '&&').replace('<', '&lt;').replace('>', '&gt;').replace('\"', '&quot;').replace("'", '&apos;').replace('{', '&brace;').replace('}', '&brack;').replace('\n', '&n;').replace('\r', '&r;'), 'utf-8'))
            file.write(bytes(':', 'utf-8'))
            if isinstance(img_b64[i][0], str):
                file.write(bytes(img_b64[i][0], 'utf-8'))
            else:
                file.write(img_b64[i][0])
            file.write(bytes('.', 'utf-8'))

            if isinstance(img_b64[i][-1], str):
                file.write(bytes(img_b64[i][-1], 'utf-8'))
            else:
                file.write(img_b64[i][-1])
            file.write(bytes('}', 'utf-8'))
    else:
        file.write(bytes('None', 'utf-8'))
    file.write(bytes('>', 'utf-8'))
    file.close()