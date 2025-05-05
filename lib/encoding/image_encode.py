import base64
import lib.dynamic as d
import tempfile
import os
from lib.constants import *
import shutil
import pygame

def encode(file) -> bytes:
    output = [base64.b64encode(file.read()), bytes(file.name.split('.')[-1], 'utf-8')]
    return output  

def decode(file) -> bytes:
    output = base64.b64decode(file)
    return output         

def genTempImg() -> None:
    pass

def updateCache(img_b64: dict, cached_images: dict) -> dict:
    if not os.path.exists(TEMP_DIR):
        return reBuildCache(img_b64)
    
    keys = list(img_b64.keys())
    keys_cached = list(cached_images.keys())

    uncached = list(set(keys) - set(keys_cached))


    for k in uncached:
        filename = next(tempfile._get_candidate_names()) + '.' + str(img_b64[k][-1], 'utf-8')
        while os.path.exists(os.path.join(TEMP_DIR, filename)):
            filename = next(tempfile._get_candidate_names()) + '.' + img_b64[k][-1]
        new_file = open(os.path.join(TEMP_DIR, filename), 'wb')
        new_file.write(decode(img_b64[k][0]))
        new_file.close()
        cached_images[k] = os.path.join(TEMP_DIR, filename)

    return cached_images, updateBuildPygameImages(d.py_img_obj, cached_images)

def reBuildCache(img_b64: dict) -> dict:
    if not os.path.exists(TEMP_DIR):
        os.mkdirs(TEMP_DIR)
    else:
        shutil.rmtree(TEMP_DIR)
        os.mkdir(TEMP_DIR)
    cached_images = {}
    keys = list(img_b64.keys())
    for key in keys:
        filename = bytes(next(tempfile._get_candidate_names()), "utf-8") + bytes('.', 'utf-8') + img_b64[key][-1]
        while os.path.exists(os.path.join(TEMP_DIR, str(filename, "utf-8"))):
            filename = bytes(next(tempfile._get_candidate_names()), "utf-8") + bytes('.', 'utf-8') + img_b64[key][-1]
        new_file = open(os.path.join(TEMP_DIR, str(filename, "utf-8")), 'wb')
        new_file.write(decode(img_b64[key][0]))
        new_file.close()
        cached_images[key] = os.path.join(TEMP_DIR, str(filename, "utf-8"))
    return cached_images, reBuildPygameImages(cached_images)

def reBuildPygameImages(cached_images: dict) -> dict:
    objs = {}
    for key in cached_images.keys():
        img = pygame.image.load(cached_images[key])
        img_ratio = img.get_width() / img.get_height()
        img = pygame.transform.scale(img, (MAX_IMG_HEIGHT * img_ratio, MAX_IMG_WIDTH))


        objs[key] = img
    return objs

def updateBuildPygameImages(objs: dict, cached_images: dict) -> dict:
    undone = set(cached_images.keys()) - set(objs.keys())
    for key in undone:
        img = pygame.image.load(cached_images[key])
        img_ratio = img.get_width() / img.get_height()
        img = pygame.transform.scale(img, (int(MAX_IMG_HEIGHT * img_ratio), MAX_IMG_WIDTH))

        objs[key] = img

    return objs