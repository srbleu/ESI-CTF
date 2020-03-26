#!/usr/bin/env python3

import socket
from core.connection import Echo
from core.connection import Einstein

import logging

from logging.handlers import RotatingFileHandler

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter('%(asctime)s %(levelname)s - %(threadName)s - mod: %(module)s, method: %(funcName)s, msg: %(message)s')

fhall = RotatingFileHandler("server_debug.log", maxBytes=0, backupCount=0) # NO rotation, neither by size, nor by number of files
fhall.setFormatter(format)
fhall.setLevel(logging.DEBUG)

fherror = RotatingFileHandler("server_error.log", maxBytes=0, backupCount=0) # NO rotation, neither by size, nor by number of files
fherror.setFormatter(format)
fherror.setLevel(logging.ERROR)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

log.addHandler(fhall)
log.addHandler(fherror)
log.addHandler(ch)

logging.info("Starting server ... ")


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen() # Should I define the number of queued requests?
        while True:
            logging.debug('Waiting for connections ...')
            conn, addr = s.accept()
            # A new thread is launched to manage a single client connection
            mc = Einstein(conn, addr)
            mc.start()
            logging.debug("Thread launched for %s request", addr)

if __name__ == "__main__":
   main()