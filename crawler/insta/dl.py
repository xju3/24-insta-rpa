import yt_dlp

from common.config import yt_options
from common.env import Environment
from db.opus_manager import OpusManager, OpusStatus
from publisher.xhs.cmd import list_dir_files

env = Environment()

def dl_insta_video(code, path):
    options = yt_options(f'{path}')
    with yt_dlp.YoutubeDL(options) as ydl:
        url = env.config.insta_opus_url(code)
        ydl.download([url])

class InstaDownloader:

    def __init__(self):
        self.opus_manager = OpusManager()

    def download(self):
        opus_list = self.opus_manager.get_pending_items(5)
        for opus in opus_list:
            self.opus_manager.set_opus_status(opus.code, OpusStatus.downloaded)
            code = opus.code
            path = f'{env.config.opus_dir}/{code}'
            try:
                dl_insta_video(code, path=path)
            except Exception as e:
                self.opus_manager.set_opus_status(opus.code, OpusStatus.err)
                env.logger.error(e)