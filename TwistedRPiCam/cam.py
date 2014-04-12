# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
import time
import picamera
import io
import traceback
from twisted.internet.threads import deferToThread
from twisted.internet import reactor, defer

class Cam(object):
  def __init__(self):
    self.photo = "EMPTY"
    self.end = False

  @defer.inlineCallbacks
  def close(self):
    self.end = True
    d = defer.Deferred()
    reactor.callLater(3, d.callback, 1)
    print "CAM: closing..."
    yield d
    print "CAM: closed"
    return

  @defer.inlineCallbacks
  def run(self):
    reactor.addSystemEventTrigger("before", "shutdown", self.close)
    try:
      print "CAM: initializing..."
      self.camera = camera = yield deferToThread(picamera.PiCamera)
      #camera.resolution = (2592, 1944)
      camera.resolution = (1920, 1080)
      print "CAM: capturing..."
      while not self.end:
        stream = io.BytesIO()
        yield deferToThread(camera.capture, stream, "jpeg", resize=(640,480))
        self.photo = stream.getvalue()
        stream.close()
    except Exception, e:
      print "CAM: EXCEPTION: "+str(e)+"|| "+str(traceback.format_exc())

