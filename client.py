# coding: utf-8
import sys
from socketIO_client import SocketIO, BaseNamespace
import time
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

_socketIO = SocketIO('https://www.dutbit.com/', port=443, verify=False)

_client = _socketIO.define(BaseNamespace, '/zigbee')


def send(channl: str, message):
    _client.emit(channl, {
        'message': message, 'timestamp': time.time()})


def recv(channl: str, callback: object):
    _client.on(channl, callback)


def wait():
    _socketIO.wait()
