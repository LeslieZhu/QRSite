from __future__ import absolute_import

import os
import cherrypy
from qrsite.QR import QRSite
    
__version__ = "0.0.1"

def main():
    thisdir = os.path.dirname(os.path.dirname(__file__))
    print thisdir
    cherrypy.quickstart(QRSite(),'/',config=os.path.join(thisdir, 'qrsite.conf'))

if __name__ == "__main__":
    import sys
    sys.exit(main())
