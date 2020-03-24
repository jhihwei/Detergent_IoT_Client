from flask_api import FlaskAPI
import pafy
import vlc
from gevent.pywsgi import WSGIServer
import os

app = FlaskAPI(__name__)

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

# Define VLC player
player = instance.media_list_player_new()
# Loop Playlist
player.set_playback_mode(vlc.PlaybackMode.loop)
# Current Path
system_path = os.path.abspath(os.getcwd())
@app.route("/play")
def play():
    test_videos_path = system_path+'test_videos'
    files = os.listdir(test_videos_path)
    media_list = instance.media_list_new()
    for f in files:
        media = instance.media_new(f'{test_videos_path}{f}')
        media_list.add_media(media)

    player.set_media_list(media_list)
    player.play()

    return str(media_list.count()) + " Video has been added to list"


@app.route("/stop")
def stop():
    player.stop()
    return "stop"


if __name__ == '__main__':
    # app.run(debug=True, host='localhost')
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
