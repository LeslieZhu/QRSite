from __future__ import absolute_import

import os
import cherrypy
from qrsite.QR import QRSite
    
__version__ = "0.0.1"

conf = {
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './static'
    }
}

def main():
    cherrypy.quickstart(QRSite(),'/',conf)

if __name__ == "__main__":
    import sys
    sys.exit(main())
