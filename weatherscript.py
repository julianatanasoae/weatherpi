#!/usr/bin/env python
#Weather Script...
#weatherscript.py
import json
import time
import datetime
import os
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
 
import Image
import ImageDraw
import ImageFont
 
os.chdir("/home/pi/Desktop/")
 
api_file = "/home/pi/weatherunderground.json"
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
width = disp.width
height = disp.height
 
font = ImageFont.load_default()
altfont24 = ImageFont.truetype('DejaVuSans.ttf', 24)
altfont20 = ImageFont.truetype('DejaVuSans.ttf', 20)
altfont18 = ImageFont.truetype('DejaVuSans.ttf', 18)
altfont14 = ImageFont.truetype('DejaVuSans.ttf', 14)
altfont10 = ImageFont.truetype('DejaVuSans.ttf', 10)
 
print "Press Ctrl+Z to exit"
 
while(True):
  now = datetime.datetime.now()
  second = now.second
  iteration = int(second/10)
  json_text = open(api_file)
  parsed_json = json.load(json_text)
  disp.begin()
  disp.clear()
  disp.display()
  image=Image.new('1',(width, height))
  draw = ImageDraw.Draw(image)
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  weather = parsed_json['current_observation']['weather']
  if iteration == 0:
    # Display 'Vremea in Magurele'
    title = 'Vremea in Magurele'
    draw.text((4,17),title,font=altfont10,fill=255)
  elif iteration == 3 or iteration == 6:
    # Display Overview
    tempc = str(parsed_json['current_observation']['temp_c'])
    draw.text((2,2),weather,font=altfont10, fill=255)
    draw.text((4,17),tempc + "C",font=altfont14, fill=255)
  elif iteration == 1 or iteration == 5:
    wind_kph = parsed_json['current_observation']['wind_kph']
    wind_dir = parsed_json['current_observation']['wind_dir']
    draw.text((2,2),weather,font=altfont10, fill=255)
    draw.text((4,17),str(wind_kph) + "kph " + wind_dir,font=altfont14, fill=255)
  elif iteration == 2:
    pressure = str(parsed_json['current_observation']['pressure_mb'])
    draw.text((2,2),"Pressure",font=altfont10,fill=255)
    draw.text((4,17),pressure + "mb",font=altfont14,fill=255)
  elif iteration == 4:
    humidity = parsed_json['current_observation']['relative_humidity']
    draw.text((2,2),"Humidity",font=altfont10, fill=255)
    draw.text((4,17),humidity, font=altfont14, fill=255)
  else:
    draw.text((2,2),"Shouldn't see this",font=font, fill=255)
  weather = parsed_json['current_observation']['weather']
  icon = parsed_json['current_observation']['icon_url']
 
  #draw.text((2,2),"iteration " + str(iteration), font=font, fill=255)
  #draw.text((2,15),line2, font=font, fill=255)
  #draw.text((2,28),line3, font=font, fill=255)
  ## draw.(weatherico)
  ## image.paste(00,255,weatherico)
  disp.image(image)
  disp.display()
  time.sleep(10)
