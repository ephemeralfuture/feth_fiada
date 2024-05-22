import vlc, time

instance = vlc.Instance("DISPLAY=:0 --aout=alsa --embedded-video --no-audio --fullscreen --no-osd")
player=instance.media_player_new()
video=instance.media_new("Desktop/ff/fedh_fiada2.mp4")
player.set_media(video)
player.set_fullscreen(True)

player.play()
time.sleep(10)
player.stop()