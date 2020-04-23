import subprocess
import os


class Player2:
    def __init__(self):
        self.system_path = os.path.dirname(os.path.abspath(__file__))
        self.videos_path = os.path.join(
            self.system_path, "..", "player", "test_videos")
        print()

    def play(self):
        files = os.listdir(self.videos_path)
        for f in files:
            f = f'{self.videos_path}/{f}'
            subprocess.run(["omxplayer", "-o", "hdmi", f])


if __name__ == '__main__':
    player2 = Player2()
    while True:
        player2.play()
