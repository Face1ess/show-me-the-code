#!/usr/bin/python
import Image, ImageDraw, ImageFont, ImageFilter
import random

def generateVerifyImage(verPicPath):
    width = 60 * 4
    height = 60
    vImage = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('/Library/Fonts/Microsoft/Arial.ttf',36)
    draw = ImageDraw.Draw(vImage)
    randSeed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    ranChar = random.sample(randSeed,4)
    
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill = randColor())
    
    for i in range(4):
        draw.text((60*i+20,10),ranChar[i],font=font, fill=randCharColor())
    
    vImage = vImage.filter(ImageFilter.BLUR)
    if verPicPath[-1] != '/':
       verPicPath = verPicPath+'/'
    vImage.save(verPicPath+'code.jpg','jpeg')

def randColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def randCharColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

if __name__ == '__main__':
    generateVerifyImage('/Users/penggarfield/Desktop')

