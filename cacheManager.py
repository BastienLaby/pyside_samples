# -*- coding: utf-8 -*-

# @package cacheManager
# created on 28/10/2015 by bastien.laby

import time
import os
import shutil
from PySide import QtCore, QtGui


def copyFile(src, dst, buffer_size=10485760, perserveFileDate=True):
    '''
    Copies a file to a new location. Much faster performance than Apache Commons due to use of larger buffer
    @param src:    Source File
    @param dst:    Destination File (not file path)
    @param buffer_size:    Buffer size to use during copy
    @param perserveFileDate:    Preserve the original file date
    '''
    #    Check to make sure destination directory exists. If it doesn't create the directory
    dstParent, dstFileName = os.path.split(dst)
    if(not(os.path.exists(dstParent))):
        os.makedirs.(dstParent)

    #    Optimize the buffer for small files
    buffer_size = min(buffer_size, os.path.getsize(src))
    if(buffer_size == 0):
        buffer_size = 1024

    if shutil._samefile(src, dst):
        raise shutil.Error("`%s` and `%s` are the same file" % (src, dst))
    for fn in [src, dst]:
        try:
            st = os.stat(fn)
        except OSError:
            # File most likely does not exist
            pass
        else:
            # XXX What about other special files? (sockets, devices...)
            if shutil.stat.S_ISFIFO(st.st_mode):
                raise shutil.SpecialFileError("`%s` is a named pipe" % fn)
    # with open(src, 'rb') as fsrc:
    #     with open(dst, 'wb') as fdst:
    #         shutil.copyfileobj(fsrc, fdst, buffer_size)
    fsrc = open(src, 'rb')
    try:
        fdst = open(dst, 'wb')
        try:
            shutil.copyfileobj(fsrc, fdst, buffer_size)
        finally:
            fdst.close()
    finally:
        fsrc.close()

    if(perserveFileDate):
        shutil.copystat(src, dst)

class ImageCacher(QtCore.QThread):
    imgAdded = QtCore.Signal(str, int)
    finishLoading = QtCore.Signal()

    def __init__(self, parent):
        QtCore.QThread.__init__(self)

        self.parent = parent
        self.ttPlayer = self.parent.ttPlayer
        self.state = "waiting"

        self.refreshRate = 0.1  # second
        self.oldTime = time.time()

    def run(self):
        while self.parent.loadList:
            self.cacheImage()
        self.finishLoading
        print "cacher thread stoped"


    def cacheImage(self):
        imgPath = self.parent.loadList.pop(0)
        if imgPath and os.path.isfile(imgPath):
            newPath = imgPath.replace("/mnt/", self.parent.localDir)
            copyFile(imgPath, newPath)
            modTime = os.path.getmtime(newPath)
            self.parent.bdd.newFrame(imgPath, modTime)
            self.imgAdded.emit(imgPath, modTime)



class CacheManager(QtGui.QProgressDialog):
    def __init__(self, localDir="/tmp/ttPlayer/cache/"):
        QtGui.QProgressDialog.__init__(self)

        self.ttPlayer = TTPlayer()

        self.nbThreads = 4
        self.runningThreads = 0
        self.threads = []

        self.loadList = []
        self.loadingCounter = 0

        self.localDir = localDir
        self.currentFrame = 0

        self.canceled.connect(self.finish)
        self.setWindowModality(QtCore.Qt.WindowModal)

        print "INITIALISATION OF CACHER THREADS FINISHED !!"

    def manageImageCache(self):
        if self.ttPlayer.episodeLoaded:
            self.show()
            self.bdd = self.ttPlayer.episodeCacheBdd
            for versionName in self.ttPlayer.episode.versions:
                currentVersion = self.ttPlayer.episode.versions[versionName]
                for frame in xrange(self.ttPlayer.episode.visibleRange):
                    framePath = currentVersion.getFramePath(frame)
                    self.loadList.append(framePath)
        self.setMaximum(len(self.loadList))
        self.startCachingImg()

    def updateProgress(self, path, timestamp):
        self.currentFrame += 1
        self.setValue(self.currentFrame)

    def finish(self):
        self.loadList = []
        self.bdd.commit(force=True)
        self.hide()

    def startCachingImg(self):
        while self.runningThreads < self.nbThreads:
            newThread = ImageCacher(self)
            newThread.imgAdded.connect(self.updateProgress)
            newThread.finishLoading.connect(self.finish)
            self.threads.append(newThread)
            newThread.start()
            self.runningThreads += 1


class ImageManager():
    def __init__(self):
        self.images = []
        for f in os.listdir("E:/Bastien/OBK/render/101/101-024/"):
            filepath = "E:/Bastien/OBK/render/101/101-024/" + f
            if os.path.isfile(filepath):
                self.images.append(filepath)

    def loadFrame(self):
        
