# This class represents the instance of a registered user 

from User import User
from Photo import Photo


class RegisteredUser:
    def __init__(self, userName, birthDate, userPhoto, userPlaylist, usersFavoriteVideos):
        self.userName = userName
        self.birthDate = birthDate
        self.userPhoto = userPhoto
        self.userPlaylist = userPlaylist
        self.userFavoriteVideos = usersFavoriteVideos

    def get_userName(self):
        return self.userName

    def set_userName(self, userName):
        self.userName = userName

    def get_birthDate(self):
        return self.birthDate

    def set_birthDate(self, birthDate):
        self.birthDate = birthDate

    def get_userPhoto(self):
        return self.userPhoto

    def set_userPhoto(self, userPhoto):
        self.userPhoto = userPhoto

    def get_userPlaylist(self):
        return self.userPlaylist

    def set_userPlaylist(self, userPlaylist):
        self.userPlaylist = userPlaylist

    def get_fileSize(self):
        return self.fileSize

    def set_usersFavoriteVideos(self, usersFavoriteVideos):
        self.userFavoriteVideos = usersFavoriteVideos



    def createPlaylist():
        pass

    def addVideoToFavorits(video):
        pass

    def uploadUserPhoto(photo):
        pass

    def addVideoToPlaylist(video, playlist):
        pass