import time, paramiko, os, vlc

time.sleep(1)

print('ok')
ssh0 = paramiko.SSHClient()
ssh0.load_system_host_keys()
ssh0.connect(hostname="192.168.8.106", username="feth", password="fiada")

ssh1 = paramiko.SSHClient()
ssh1.load_system_host_keys()
ssh1.connect(hostname="192.168.8.107", username="feth", password="fiada")

instance = vlc.Instance("--aout=alsa --embedded-video --no-audio --fullscreen --no-osd")
player=instance.media_player_new()
video=instance.media_new("Desktop/ff/fedh_fiada1.mp4")
player.set_media(video)
player.set_fullscreen(True)

count = 0

while count < 5:
    player.play()
    (stdin, stdout, stderr) = ssh0.exec_command("omxplayer -o local --no-osd Desktop/ff/fedh_fiada2.mp4")
    (stdin, stdout, stderr) = ssh1.exec_command("omxplayer -o local --no-osd Desktop/ff/fedh_fiada3.mp4")
    time.sleep(10)
    player.stop()
    (stdin, stdout, stderr) = ssh0.exec_command("killall omxplayer.bin")
    (stdin, stdout, stderr) = ssh1.exec_command("killall omxplayer.bin")
    count = count+1