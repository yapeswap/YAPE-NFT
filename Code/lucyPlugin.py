#!/usr/bin/env python

import random
import numpy
from gimpfu import *

ceil = 474
hatCeil = 14
gradCeil = 29

monkies = []

elements = [True, False]
hatWeight = [0.1, 0.9]
fangsWeight = [0.2, 0.8]
hatWeight = [0.05, 0.95]

def monkeyGen(id):

    patNum = random.sample(range(ceil), 4)
    accNum = random.sample(range(hatCeil), 3)
    gradNum = random.randint(0, gradCeil)

    newMonkey = (id+1, 
                patNum[0],
                patNum[1],
                patNum[2],
                patNum[3],
                gradNum,
                accNum[0],
                accNum[1],
                accNum[2],
                numpy.random.choice(elements, p=hatWeight),
                numpy.random.choice(elements, p=fangsWeight),
                numpy.random.choice(elements, p=hatWeight)
                )

    if newMonkey not in monkies:
        monkies.append(newMonkey)
    else:
        monkeyGen(id-1)

def lucyGen(monkey):
    ident = str(monkey[0])

    coinPattern = "pat"+str(monkey[1])+".png"
    hairPattern = "pat"+str(monkey[2])+".png"
    faceEarsPattern = "pat"+str(monkey[3])+".png"
    eyesMouthPattern = "pat"+str(monkey[4])+".png"

    canePattern = "grad"+str(monkey[5])+".png"
    hatOuterPattern = "hat"+str(monkey[6])+".png"
    hatOuterStarPattern = "hat"+str(monkey[7])+".png"
    hatInnerStarPattern = "hat"+str(monkey[8])+".png"

    hatAcc = monkey[9]
    fangsAcc = monkey[10]
    caneAcc = monkey[11]


    image = pdb.gimp_file_load("/home/notes/Programming/yape-nft/Images/lucy.xcf", "lucy.xcf")


    image.active_layer = image.layers[10]
    drawable = image.active_layer

    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[8])
    pdb.gimp_context_set_pattern(coinPattern)
    pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

    image.active_layer = image.layers[9]
    drawable = image.active_layer
    pdb.gimp_context_set_pattern(hairPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[7])
    pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

    image.active_layer = image.layers[8]
    drawable = image.active_layer
    pdb.gimp_context_set_pattern(faceEarsPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[6])
    pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

    image.active_layer = image.layers[7]
    drawable = image.active_layer
    pdb.gimp_context_set_pattern(eyesMouthPattern)
    pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[5])
    pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

    #Hat outer needs to be the drawing layer because the area is cut out 
    #Just stack vectored fills lol
    if(hatAcc):
        image.active_layer = image.layers[4]
        drawable = image.active_layer
        image.layers[3].visible = True
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[3])
        pdb.gimp_context_set_pattern(hatOuterPattern)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
        
        #HatLines
        image.active_layer = image.layers[4]
        image.layers[3].visible = True
        drawable = image.active_layer

        image.active_layer = image.layers[4]
        drawable = image.active_layer
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[2])
        pdb.gimp_context_set_pattern(faceEarsPattern)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[4]
        drawable = image.active_layer
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[1])
        pdb.gimp_context_set_pattern(eyesMouthPattern)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

    else:
        image.layers[4].visible = False
        image.layers[3].visible = False
        

    #SET CANE TO VISIBLE FILL TO CANEGRAD VECTOR
    #FILL LAYER 2
    #MAKE LAYER 1 VISIBLE
    #EVERTHING IS PROBABLY OFFSET
    if(caneAcc):
        image.layers[1].visible = True
        image.active_layer = image.layers[2]

        drawable = image.active_layer
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[0])
        pdb.gimp_context_set_pattern(canePattern)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
    else:
        image.layers[1].visible = False



    image.active_layer = image.layers[0]
    drawable = image.active_layer

    if(fangsAcc):
        image.layers[0].visible = True
    else:
        image.layers[0].visible = False

    image.active_layer = image.layers[0]
    drawable = image.active_layer

    image.add_layer(pdb.gimp_layer_new_from_visible(image, image, "vis"))

    image.active_layer = image.layers[0]
    drawable = image.active_layer

    pdb.file_png_save(image, drawable, "/home/notes/Programming/yape-nft/Test/"+ident+".png", ident+".png", 0, 0, 0, 0, 0, 1, 1)


def lucyPlugin(timg, tdrawable):
    for i in range(1,100):
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
