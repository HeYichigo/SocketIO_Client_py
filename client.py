# coding: utf-8
import sys
from socketIO_client import SocketIO, BaseNamespace
import time
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

socketIO = SocketIO('https://www.xxx.com/', port=443, verify=False)

zigbee = socketIO.define(BaseNamespace, '/zigbee')


def send(message):
    zigbee.emit('collection_channl', {
                'message': message, 'timestamp': time.time()})
