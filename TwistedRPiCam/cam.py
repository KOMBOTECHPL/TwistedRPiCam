# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
import time
import io
import traceback
from twisted.internet.threads import deferToThread
from twisted.internet import reactor, defer

class Cam(object):
  def __init__(self):
    self.photo = ""
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
    yield deferToThread(self.runt)

  def runt(self):
    try:
      print "CAM: initializing..."
      import picamera
      self.camera = camera = picamera.PiCamera()
      #camera.resolution = (2592, 1944)
      #camera.resolution = (1920, 1080)
      #camera.resolution = (1600, 1200)
      #camera.resolution = (800, 608)
      camera.resolution = (640, 480)
      print "CAM: capturing..."
      camera.start_preview()
      stream = io.BytesIO()
      for img in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
        self.photo = stream.getvalue()
        stream.seek(0)
        stream.truncate()
        if self.end:
          break
    except Exception, e:
      print "CAM: EXCEPTION: "+str(e)+"|| "+str(traceback.format_exc())

    stream.close()
    camera.stop_preview()
    camera.close()
