#!/usr/bin/env python

import math
import random
from gimpfu import *

coinCeil = 530
headCeil = 530
faceEarsCeil = 530
eyesMouthCeil = 530
accessoryCeil = 20

monkies = []

def monkeyGen(id):
    newMonkey = (id+1, 
                random.randint(0,coinCeil), 
                random.randint(0,headCeil), 
                random.randint(0,faceEarsCeil),
                random.randint(0,eyesMouthCeil))
                #[10 if x == 0 else 1 for x in range(accessoryCeil)])[0])
    
    if newMonkey not in monkies:
        monkies.append(newMonkey)

def lucyGen(timg, tdrawable, monkey):
    ident = str(monkey[0])
    coinPattern = "pat"+monkey[1]
    hairPattern = "pat"+monkey[2]
    faceEarPattern = "pat"+monkey[3]
    eyesMouthPattern = "pat"+monkey[4]

    image = pdb.gimp_file_load("/home/notes/Programming/YAPE-NFT/Images/newape.xcf", "newape.xcf")
    image.active_layer = image.layers[5]
    drawable = image.active_layer

    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[4])
    #pdb.gimp_context_set_pattern('Granite #1')
    pdb.gimp_context_set_pattern(coinPattern)
    pdb.gimp_edit_bucket_fill(drawable,2,LAYER_MODE_NORMAL_LEGACY,75,0,FALSE,0,0)


    image.active_layer = image.layers[4]
    drawable = image.active_layer
    pdb.gimp_context_set_pattern('Marble #1')
    pdb.gimp_context_set_pattern(hairPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[3])
    pdb.gimp_edit_bucket_fill(drawable,2,LAYER_MODE_NORMAL_LEGACY,75,0,FALSE,0,0)


    image.active_layer = image.layers[3]
    drawable = image.active_layer
    #pdb.gimp_context_set_pattern('Parque #1')
    pdb.gimp_context_set_pattern(faceEarsPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[2])
    pdb.gimp_edit_bucket_fill(drawable,2,LAYER_MODE_NORMAL_LEGACY,75,0,FALSE,0,0)

    image.active_layer = image.layers[2]
    drawable = image.active_layer
    #pdb.gimp_context_set_pattern('Wood #1')
    pdb.gimp_context_set_pattern(eyesMouthPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[1])
    pdb.gimp_edit_bucket_fill(drawable,2,LAYER_MODE_NORMAL_LEGACY,75,0,FALSE,0,0)

    image.active_layer = image.layers[0]
    drawable = image.active_layer

    #pdb.file_png_save(image, drawable, "/home/notes/Programming/YAPE-NFT/Test/"+id+".png", id+".png", 0, 0, 0, 0, 0, 1, 1)
    print("FirstCall")
    print(image.layers)

    image.add_layer(pdb.gimp_layer_new_from_visible(image, image, "vis"))
    
    print(image.layers)

    image.active_layer = image.layers[0]
    drawable = image.active_layer

    pdb.file_png_save(image, drawable, "/home/notes/Programming/YAPE-NFT/Test/"+ident+".png", ident+".png", 0, 0, 0, 0, 0, 1, 1)

    #pdb.gimp_plugin_menu_register(procedure_name, menu_path)

def lucyPlugin(timg, tdrawable):
    for i in range(5,10):
        monkeyGen(i)

    for monkey in monkies:
        lucyGen(monkey)


register(
    "lucyPlugin",
    "Generates test lucy",
    "Generates test lucy",
    "0xSumna",
    "0xSumna",
    "2021",
    "<Image>/Filters/Artistic/Lucy",
    "",
    [],
    [],
    lucyPlugin)


main()

