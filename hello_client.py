import sys
sys.path.append('gen-py')
from hello import HelloSrv

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

trans = TSocket.TSocket("ec2-35-180-69-6.eu-west-3.compute.amazonaws.com", 4001)
trans = TTransport.TBufferedTransport(trans)
proto = TBinaryProtocol.TBinaryProtocol(trans)
client = HelloSrv.Client(proto)

trans.open()
msg = client.hello_fun(12.3455)
print("[CLIENT] recieved %s" % msg)
trans.close()

