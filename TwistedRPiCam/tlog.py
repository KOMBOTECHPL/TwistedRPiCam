# vim: set fileencoding=utf-8 ts=2 sw=2 et st=2 :
from twisted.python import log
from twisted.python import logfile
import os

class DailyLogFile(logfile.DailyLogFile):
  def suffix(self, tupledate):
    """Return the suffix given a (year, month, day) tuple or unixtime"""
    try:
      return "{0}_{1:0>2}_{2:0>2}".format(*tupledate)
    except:
      # try taking a float unixtime
      return "{0}_{1:0>2}_{2:0>2}".format(*self.toDate(tupledate))

def logger():
  log_filename = "log/TwistedRPiCam.log"
  log_dir, log_name = os.path.split(os.path.abspath(log_filename))
  ret = log.FileLogObserver(DailyLogFile(log_name, log_dir)).emit
  return ret

