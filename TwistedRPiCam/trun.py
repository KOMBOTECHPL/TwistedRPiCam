# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet import reactor
from twisted.application import internet, service
from twisted.web import static, server, resource
from TwistedRPiCam.www import Root
from TwistedRPiCam.cam import Cam

def run():
  application = service.Application('TwistedRPiCam')
  sc = service.IServiceCollection(application)

  cam = Cam()
  reactor.callLater(10, cam.run)
  site = server.Site(Root(cam))

  i = internet.TCPServer(8080, site)
  i.setServiceParent(sc)
  return application

