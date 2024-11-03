import time
from playsound import playsound


audio_file = "./She-knows.mp3"

lyrics = [
  
  "Rest in peace to Aaliyah",
  "Rest in peace to Left Eye (Left Eye)",
  "Michael Jackson, I'll see ya",
  "Just as soon as I die (I die)",
  "",
  "Got me up so high, tryin' get a piece of that apple pie, uh",
  "I be up so high, tryin' get a piece of that apple pie",
  "Got me up so high, tryin' get a piece of that apple pie, uh",
  "I be up so high, tryin' get a piece of that apple pie"
];


def play_song_with_lyrics(audio_file, lyrics):
    
    import threading
    threading.Thread(target=playsound, args=(audio_file,)).start()

  
    for line in lyrics:
        print(line)
        time.sleep(2)  


play_song_with_lyrics(audio_file, lyrics)