#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import

import cherrypy
import qrcode
import os
from qrsite import utils
from cherrypy.lib.static import serve_file

class QRSite(object):
    @cherrypy.expose
    def index(self):
        print "Content-type: text/html"
        print
        return utils.homepage()

    @cherrypy.expose
    def uploadFile(self,uploadFile):
        if 'file' in dir(uploadFile):
            reqFile = uploadFile.file
            all_data = bytearray()

            while True:
                data = reqFile.read(8192)
                if not data:
                    break
                
                all_data += data
                
            saved_file=open('static/qrcode.png', 'wb')
            saved_file.write(all_data)
            saved_file.close()
        else:
            return "请上传文件!"

    @cherrypy.expose
    def upload(self,uploadFile):
        if 'file' in dir(uploadFile):
            self.uploadFile(uploadFile)
            return self.decode("static/qrcode.png")
        else:
            return "解析失败!"

    @cherrypy.expose
    def download(self, qrtext):
        if qrtext.strip() != "":
            outFile = self.encode(qrtext)
            if(os.path.exists(outFile)):
                return serve_file(os.path.abspath(outFile))
            else:
                return "File " +outFile+ " not found"
        else:
            return "请输入用于生成二维码的内容."

    @cherrypy.expose
    def run(self,**parameters):
        print "Content-type: text/html"
        print

        encode = parameters.get("encode",None)
        decode = parameters.get("decode",None)
        qrtext = parameters.get("qrtext","")
        uploadFile = parameters.get("uploadFile","")
        
        if encode and qrtext.strip() != "":
            return "<center><p><img src=\"%s\"/></p></center>" % self.encode(qrtext)
        elif decode and 'file' in dir(uploadFile) and uploadFile.file != None:
            self.uploadFile(uploadFile)
            return '<center><textarea id="qrtext" name="qrtext" style="width: 640px; height: 250px">%s</textarea></center>' % self.decode("static/qrcode.png")
        else:
            return "<p>请输入内容!</p>"

    @cherrypy.expose        
    def encode(self,qrtext):
        filename = "static/qrcode.png"
            
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(qrtext)
        qr.make(fit=True)
        
        img = qr.make_image()
        img.save(filename)
        
        return filename

    @cherrypy.expose
    def decode(self,imgfile):
        import zbar
        from PIL import Image
        
        scanner = zbar.ImageScanner()
        scanner.parse_config("enable")
        
        pil = Image.open(imgfile).convert('L')
        width, height = pil.size
        raw = pil.tostring()
        
        image = zbar.Image(width, height, 'Y800', raw)
        scanner.scan(image)
        
        data = ''
        for symbol in image:
            data += symbol.data
            
        del(image)

        if data:
            return data
        else:
            return "解析失败!\n确定上传的是二维码图片吗?!"
        

if __name__ == "__main__":
    import sys
    sys.exit(cherrypy.quickstart(QRSite()))
