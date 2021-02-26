import os

bell = 'assets/bell.mp3'
scifi = 'assets/scifi_alarm.mp3'
airraid = 'assets/air_raid.mp3'
os.system('mpg123 -q ' + bell)
os.system('mpg123 -q ' + scifi)
os.system('mpg123 -q ' + airraid)