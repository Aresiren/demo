#_*_coding:utf-8_*_

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import simplejson
import random
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

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

        data = simplejson.loads(self.data_string)
        with open("test123456.json", "w") as outfile:
            simplejson.dump(data, outfile)
        print "{}".format(data)
        f = open("for_presen.py")
        self.wfile.write(f.read())
        return


def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


print '开始。。'
run()
#if __name__ == "__main__":
#    from sys import argv

#if len(argv) == 2:
#    run(port=int(argv[1]))
#else:
#    #执行默认的httpServer,端口：8080
#    run()