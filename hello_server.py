import sys
sys.path.append('gen-py')
from hello import HelloSrv

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloHandler:
    def hello_fun(self, numero):
        print("[SERVER] Handling client request")
        return "Hello from server {}".format(numero)

handler = HelloHandler()
proc = HelloSrv.Processor(handler)

trans_svr = TSocket.TServerSocket(port=4001)
trans_fac = TTransport.TBufferedTransportFactory()
proto_fac = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(proc, trans_svr, trans_fac, proto_fac)
server.serve()

