# QRSite

建立一个生成/解析二维码图片的站点


# 功能

- 提供内容，生成包含内容的二维码图片

  ```
  $ wget localhost:8080/download?qrtext="hello,world." -O qrcode.png
  ```
  
- 上传二维码图片，解析包含的内容

  ```
  $ curl  -F "uploadFile=@/Desktop/test.png"  localhost:8080/upload > qrtext.txt
  ```


# 文档

参考目录 `docs/`

# 注意

`zbar` 在OS X上需要安装打了补丁 http://launchpadlibrarian.net/134768014/zbar_0.10+doc-7build3_0.10+doc-8.diff.gz 的源码.
