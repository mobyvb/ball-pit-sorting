import vlc
import time
import random

air_raid = vlc.MediaPlayer("air-raid-siren.ogg")
test_over = vlc.MediaPlayer("the-test-is-over.mp3")
min_time = 30 * 60
max_time = 60 * 60
sort_time = 5 * 60

print "starting"

while(True):
    wait_time = random.randrange(min_time, max_time)
    print "waiting for " + str(wait_time) + " seconds"
    time.sleep(wait_time)
    print "start sorting"
    air_raid.stop()
    air_raid.play()
    time.sleep(sort_time)
    print "stop sorting"
    test_over.stop()
    test_over.play()
