#!/usr/bin/env python3

import time, paramiko, os, vlc
import RPi.GPIO as GPIO

time.sleep(1)
    

ssh0 = paramiko.SSHClient()
ssh0.load_system_host_keys()
ssh0.connect(hostname="192.168.8.106", username="feth", password="fiada")

ssh1 = paramiko.SSHClient()
ssh1.load_system_host_keys()
ssh1.connect(hostname="192.168.8.107", username="feth", password="fiada")

ssh2 = paramiko.SSHClient()
ssh2.load_system_host_keys()
ssh2.connect(hostname="192.168.8.108", username="feth", password="fiada")

'''instance = vlc.Instance("--aout=alsa --embedded-video --no-audio --fullscreen --no-osd")
player=instance.media_player_new()
video=instance.media_new("Desktop/ff/fedh_fiada1.mp4")
player.set_media(video)
player.set_fullscreen(True)'''

button_pin = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback(channel):
    print("button pushed")
    play_movies()
    #shutdown_all()

GPIO.add_event_detect(10, GPIO.RISING,callback=button_callback, bouncetime=200)

button_press = False


def play_movies():
    count = 0
    while count<5:
        #player.play()
        (stdin, stdout, stderr) = ssh0.exec_command("omxplayer -o local --no-osd Desktop/ff/fedh_fiada2.mp4")
        (stdin, stdout, stderr) = ssh1.exec_command("omxplayer -o local --no-osd Desktop/ff/fedh_fiada3.mp4")
        (stdin, stdout, stderr) = ssh2.exec_command("omxplayer -o local --no-osd Desktop/ff/fedh_fiada1.mp4")
        time.sleep(10)
        #player.stop()
        (stdin, stdout, stderr) = ssh0.exec_command("killall omxplayer.bin")
        (stdin, stdout, stderr) = ssh1.exec_command("killall omxplayer.bin")
        (stdin, stdout, stderr) = ssh2.exec_command("killall omxplayer.bin")
        count = count+1
        print("count")
    GPIO.cleanup()
        
def shutdown_all():
    (stdin, stdout, stderr) = ssh0.exec_command("sudo shutdown now")
    (stdin, stdout, stderr) = ssh1.exec_command("sudo shutdown now")
    time.sleep(5)


while True:
    print('running')
    time.sleep(1)
    #GPIO.cleanup()

