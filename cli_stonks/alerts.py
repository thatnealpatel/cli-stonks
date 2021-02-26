import os

bell = 'assets/bell.mp3'
scifi = 'assets/scifi_alarm.mp3'
os.system('mpg123 -q ' + bell)
os.system('mpg123 -q ' + scifi)