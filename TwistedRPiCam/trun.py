# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
#from twisted.internet import epollreactor
#epollreactor.install()

from twisted.internet import reactor
from twisted.application import internet, service
from twisted.web import static, server, resource
from TwistedRPiCam.cam import Cam
from TwistedRPiCam.www import CamPhoto

import os
DIR = os.path.join(os.path.dirname(__file__), "www")
#print "DIR", DIR

def run():
  application = service.Application('TwistedRPiCam')
  sc = service.IServiceCollection(application)

  cam = Cam()
  reactor.callLater(2, cam.run)
  root = static.File(DIR)
  root.putChild('cam.jpeg', CamPhoto(cam))
  site = server.Site(root)

  i = internet.TCPServer(8080, site)
  i.setServiceParent(sc)
  return application

