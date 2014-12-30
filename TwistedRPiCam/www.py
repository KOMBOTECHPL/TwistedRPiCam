# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
from twisted.internet import reactor
from twisted.application import internet, service
from twisted.web import static, server, resource

class CamPhoto(resource.Resource):
  def __init__(self, cam):
    ret = resource.Resource.__init__(self)
    self.isLeaf = True
    self.cam = cam
    return ret

  def render_POST(self, request):
    request.setHeader("Connection","close")
    #request.setHeader("Connection","Keep-Alive")
    request.setHeader("Content-type","image/jpeg")
    request.setResponseCode(200)
    #print "TwistedRPiCam CamPhoto"
    return self.cam.photo

  def render_GET(self, request):
    return self.render_POST(request)

