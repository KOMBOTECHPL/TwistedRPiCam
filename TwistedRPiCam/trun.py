# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
#from twisted.internet import epollreactor
#epollreactor.install()

from twisted.internet import reactor, ssl
from twisted.application import internet, service
from twisted.web import static, server, resource
from TwistedRPiCam.cam import Cam
from TwistedRPiCam.www import CamPhoto
from twisted.web.guard import HTTPAuthSessionWrapper, BasicCredentialFactory, DigestCredentialFactory
from twisted.cred import portal, checkers, credentials
from zope.interface import implements


import os
DIR = os.path.join(os.path.dirname(__file__), "www")
#print "DIR", DIR
ssl_key = '/etc/ssl/certs/ssl-cert-snakeoil.pem'
ssl_crt = '/etc/ssl/private/ssl-cert-snakeoil.key'
passwd_file = 'passwd'

def run():
  application = service.Application('TwistedRPiCam')
  sc = service.IServiceCollection(application)

  cam = Cam()
  reactor.callLater(2, cam.run)
  root = static.File(DIR)
  root.putChild('cam.jpeg', CamPhoto(cam))

  if os.path.isfile(passwd_file):
    checker = checkers.FilePasswordDB(passwd_file)
    credentialFactory = BasicCredentialFactory("TwistedRPiCam")
    root_realm = HttpPasswordRealm(root)
    p = portal.Portal(root_realm, [checker])
    sec_root = HTTPAuthSessionWrapper(p, [credentialFactory])
  else: 
    print "No password file! Authentication is NOT enabled!"
    sec_root = root

  site = server.Site(sec_root)

  i = internet.TCPServer(8080, site)
  i.setServiceParent(sc)

  if os.path.isfile(ssl_crt) and os.path.isfile(ssl_key):
    i = internet.SSLServer(8443, site, ssl.DefaultOpenSSLContextFactory(ssl_crt, ssl_key))
    i.setServiceParent(sc)
  else:
    print "No SSL cert/key found! SSL is NOT started!"

  return application

class HttpPasswordRealm(object):
  implements(portal.IRealm)

  def __init__(self, res):
    self.res = res

  def requestAvatar(self, user, mind, *interfaces):
    if resource.IResource in interfaces:
      return (resource.IResource, self.res, lambda: None)
    raise NotImplementedError()
