from http.server import BaseHTTPRequestHandler,HTTPServer
from common.variable import GetVariable as gv
from multiprocessing import Process
import subprocess
from common import basePickle

pid = 0
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        d_result = {}
        find_devices="devices"
        req = self.path.split('&')
        if req[0].find(find_devices) > 0:
            d_result["devices"] = req[0].split("=")[1]
        d_result["log"] = req[1].split("=")[1]
        basePickle.write_pickle(d_result, gv.CRASH_LOG_PATH)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(b"Hello World !") #发送信息给客户端
        print("do_GET")
def open_web_server():
    server = HTTPServer((gv.HOST, gv.PORT), myHandler)
    print('Started httpserver on port ', gv.PORT)
    server.serve_forever()
if __name__=="__main__":
    p = Process(target=open_web_server, args=())
    p.start()
    # subprocess.Popen("taskkill /F /T /PID " + str(p.pid), shell=True)
    print("kkk")



