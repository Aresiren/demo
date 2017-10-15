#_*_coding:utf-8_*_

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
#import simplejson
import random
import sys
import os
reload(sys) 
sys.setdefaultencoding('utf8')
# sys.path.append(str(os.getcwd()).split(r'\test')[0])
sys.path.append(os.path.pardir)

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
#        self.send_header('charset', 'UTF-8')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("douban2.txt", "r")#douban.txt  index.html
        self.wfile.write(f.read().decode('utf-8'))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

#        data = simplejson.loads(self.data_string)
#        with open("test123456.json", "w") as outfile:
#            simplejson.dump(data, outfile)
#        print "{}".format(data)
        f = open("douban1.txt")
        self.wfile.write(f.read())
        return


def runMy(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()



# runMy()
if __name__ == "__main__":
    print 'server开始。。'
    # 1.底层server
    # runMy()
    # 2.应用Flask，web.py等
    from myFlaskApp import app as application
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8080, application)
    print('web app running:localhost:8080')
    httpd.serve_forever()

#if __name__ == "__main__":
#    from sys import argv

#if len(argv) == 2:
#    run(port=int(argv[1]))
#else:
#    #执行默认的httpServer,端口：8080
#    run()