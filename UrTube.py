from user import User
from time import sleep

from video import Video


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
            else:
                print('Not identified user')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, word: str):
        videos = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                videos.append(video.title)
        return videos

    def watch_video(self, video_title: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        if self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        for VideoObject in self.videos:
            if VideoObject.title == video_title:
                for second in range(1, VideoObject.duration + 1):
                    print(second, end=' ', flush=True)
                    sleep(1)
                print('Конец видео')
                return

