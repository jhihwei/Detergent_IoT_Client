import subprocess
import os
from dotenv import load_dotenv

class Player2:
    def __init__(self):
        load_dotenv(dotenv_path="/home/pi/Detergent_IoT_Client/")
        self._PLAYER = str(os.getenv('PLAYER'))
        self.system_path = os.path.dirname(os.path.abspath(__file__))
        self.videos_path = os.path.join(
            self.system_path, "..", "player", "test_videos")
        print(self._PLAYER)

    def play(self):
        files = os.listdir(self.videos_path)
        for f in files:
            f = f'{self.videos_path}/{f}'
            if self._PLAYER == "vlc":
                subprocess.run(["vlc", "--fullscreen", f])
            else:
                subprocess.run(["omxplayer", "-o", "hdmi", f])


if __name__ == '__main__':
    player2 = Player2()
    while True:
        player2.play()
