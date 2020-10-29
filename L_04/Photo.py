#This class represents the instance of a photo 

class Photo:
  def __init__(self, fileSize, fileName, photoWidth, photoHeight):
      self.fileSize = fileSize
      self.fileName = fileName
      self.photoWidth = photoWidth
      self.photoHeight = photoHeight

    def get_fileSize(self):
        return self.fileSize

    def set_fileSize(self, fileSize):
        self.fileSize = fileSize

    def get_fileName(self):
        return self.fileName

    def set_fileName(self, fileName):
        self.fileName = fileName

    def get_photoWidth(self):
        return self.photoWidth

    def set_photoWidth(self, photoWidth):
        self.photoWidth = photoWidth

    def get_photoHeight(self):
        return self.photoHeight

    def set_photoHeight(self, photoHeight):
        self.photoHeight = photoHeight