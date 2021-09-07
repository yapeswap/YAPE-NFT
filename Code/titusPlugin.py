#!/usr/bin/env python

import random
import numpy
import json
from gimpfu import *

#  ___    ___ ________  ________  _______   ________  ___       __   ________  ________   
# |\  \  /  /|\   __  \|\   __  \|\  ___ \ |\   ____\|\  \     |\  \|\   __  \|\   __  \  
# \ \  \/  / | \  \|\  \ \  \|\  \ \   __/|\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ 
#  \ \    / / \ \   __  \ \   ____\ \  \_|/_\ \_____  \ \  \  __\ \  \ \   __  \ \   ____\
#   \/  /  /   \ \  \ \  \ \  \___|\ \  \_|\ \|____|\  \ \  \|\__\_\  \ \  \ \  \ \  \___|
# __/  / /      \ \__\ \__\ \__\    \ \_______\____\_\  \ \____________\ \__\ \__\ \__\   
#|\___/ /        \|__|\|__|\|__|     \|_______|\_________\|____________|\|__|\|__|\|__|   
#\|___|/                                      \|_________|                                

#Todo

#Tend to zen garden.

#Will run gas cost tests to make sure
#Finish Analytics File

ceil = 474
hatCeil = 14
gradCeil = 29

elements = [True, False]

#Lord forgive me for I have sinned
hatTable = [(True, False, False),(False, True, False),(False, False, True)]
hatAssist = [0, 1, 2]
hatChoice = [0.15, 0.25, 0.6,]

hatWeight = [0.1, 0.9]
shadesWeight = [0.1, 0.9]
caneWeight = [0.1, 0.9]
fangsWeight = [0.1, 0.9]

patNames = []
hatNames = []
gradNames = []

#Make it to where you can only have one of cmdr durag or cans then make it pick randomly between the three
class Monkey():
    def __init__(self, ident, coinPat, hairPat, faceEarsPat, eyeMouthPat, canePat, cmdrOuterPat, cmdrOuterStarPat, cmdrInnerStarPat, duragPat, cansInnerPat, cansOuterPat, shadesPat):
    
        self.ident = ident
        self.name = ""
        self.coinNum = coinPat
        self.hairNum = hairPat
        self.faceEarsNum = faceEarsPat
        self.eyeMouthNum = eyeMouthPat
        self.hatAcc = numpy.random.choice(elements, p=hatWeight)
        self.cmdrAcc = False
        self.duragAcc = False
        self.cansAcc = False

        self.shadesAcc = numpy.random.choice(elements, p=shadesWeight)
        self.caneAcc = numpy.random.choice(elements, p=caneWeight)
        self.fangsAcc = numpy.random.choice(elements, p=fangsWeight)

        #METADATA: Numbers of Accessories, to be mapped to names and given rarity. 
        self.cmdrOuterNum = cmdrOuterPat
        self.cmdrOuterStarNum = cmdrOuterStarPat
        self.cmdrInnerStarNum = cmdrInnerStarPat
        self.duragNum = duragPat
        self.cansOuterNum = cansOuterPat
        self.cansInnerNum = cansInnerPat
        self.shadesNum = shadesPat
        self.caneNum = canePat

        #Translated to Names Later
        self.coinPat = "pat"+str(coinPat)+".png"
        self.hairPat = "pat"+str(hairPat)+".png"
        self.faceEarsPat = "pat"+str(faceEarsPat)+".png"
        self.cansOuterPat = "pat"+str(cansOuterPat)+".png"
        self.cansInnerPat = "pat"+str(cansInnerPat)+".png"

        #Also Translated to names. 
        self.cmdrOuterPat = "hat"+str(cmdrOuterPat)+".png"
        self.cmdrOuterStarPat = "hat"+str(cmdrOuterStarPat)+".png"
        self.cmdrInnerStarPat = "hat"+str(cmdrInnerStarPat)+".png"
        self.duragPat = "hat"+str(duragPat)+".png"

        #Canes and Shades can be the same, see gradNum
        self.shadesPat = "grad"+str(shadesPat)+".png"
        self.canePat = "grad"+str(canePat)+".png"
        self.eyeMouthPat = "grad"+str(eyeMouthPat)+".png"

        self.whatHat = ""
        if(self.hatAcc == True or self.shadesAcc == True or self.caneAcc == True or self.fangsAcc == True):
            self.hasAcc = True
        else:
            self.hasAcc = False 


def analytics(monkies):
    accessoryCount = 0
    hatsCount = 0
    shadesCount = 0
    fangsCount = 0
    caneCount = 0

    pats = []
    hats = []
    grad = []

    for x in range(ceil):
        pats.append((x, 0))
    for x in range(hatCeil):
        hats.append((x, 0))
    for x in range(gradCeil):
        grad.append((x, 0))

    for x in monkies
        if x.hasAcc:
            accessoryCount += 1
        if x.shadesAcc:
            shadesCount += 1
        if x.fangsAcc:
            fangsCount += 1
        if x.caneAcc:
            caneCount += 1
        pats.append(x.coinPat, x.hairpat, x.faceEarsPat, x.cansOuterPat, x.cansInnerPat)
        hats.append(x.cmdrOuterPat, x.cmdrOuterStarPat, x.cmdrInnerStarPat, x.duragPat)
        grad.append(x.shadesPat, x.canePat, x.eyeMouthPat)



    def hatValidate(self):
        #pick one of the three to make true at random
        if(self.hatAcc):
            choice = numpy.random.choice(hatAssist, p=hatChoice)
            self.cmdrAcc = hatTable[choice][0]
            self.duragAcc = hatTable[choice][1]
            self.cansAcc = hatTable[choice][2]
            if cmdrAcc:
                self.whatHat = "Commander"
            if ragAcc:
                self.whatHat = "Rag"
            if cansAcc:
                self.whatHat = "Cans"

    def setSelfName(self, n):
        self.name = n


def monkeyGen(ident):

    patNum = random.sample(range(ceil), 6)
    accNum = random.sample(range(hatCeil), 4)
    gradNum = random.randint(0, gradCeil)

    #Need to generate a lot more numbers, need some ceilings and some more patterns, also need to ensure none of the numbers match for 

    newMonkey = Monkey(
                    ident,
                    patNum[0],
                    patNum[1],
                    patNum[2],
                    gradNum,
                    gradNum,
                    accNum[0],
                    accNum[1],
                    accNum[2],
                    accNum[3],
                    patNum[4],
                    patNum[5],
                    gradNum
                    )

    return newMonkey
