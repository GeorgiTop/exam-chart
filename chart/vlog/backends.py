from embed_video.backends import VideoBackend


class CustomBackend(VideoBackend):
    template_name = 'embed_video/embed_code.html'
