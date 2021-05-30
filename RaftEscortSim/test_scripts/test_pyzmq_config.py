import zmq
from zmq import socket
context=zmq.Context()
socket=context.socket(zmq.REP)
