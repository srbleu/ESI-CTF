import threading
import logging
import hashlib
from datetime import datetime
from datetime import timedelta
import time


class ManagingConnections(threading.Thread, object):

    def __init__(self, connection, address, ts_init_conn):
        threading.Thread.__init__(self)
        self.conn = connection
        self.addr = address
        self.init_ts = ts_init_conn

    def run(self):
        # to be overriden
        pass


class Echo(ManagingConnections):
    chall = "ECHO"

    def run(self):

        with self.conn:
            logging.debug("New connection from %s ...", self.addr)
            self.conn.sendall("Hey dude! I'm the server, tell me what you want ...\n".encode('utf8'))

            while True:
                # Waiting for client data
                data = self.conn.recv(1024)
                logging.debug("Received %s from %s", data, self.addr)
                if not data:
                    break
                # Send request echo to the client
                self.conn.sendall(data)


class Einstein(ManagingConnections):

    chall = "EINSTEIN"

    EINSTEIN_HINT = "Una persona que nunca ha cometido un error"
    TO_FLAG = "nunca intenta nada nuevo"
    CHALL_TIMEOUT = 5  # in seconds

    def run(self):

        with self.conn:
            logging.debug("Chall %s - New connection from %s ...", self.chall, self.addr)
            hint_msg = "Completa la frase: {0} ".format(self.EINSTEIN_HINT).encode()
            self.conn.sendall(hint_msg)

            while True:
                # Waiting for client data
                data = self.conn.recv(1024)
                logging.debug("Chall %s - Received %s from %s", self.chall, data, self.addr)

                # Current timestamp
                current_ts = datetime.now()

                diff = (current_ts - self.init_ts)
                if diff <= timedelta(seconds=self.CHALL_TIMEOUT):
                    if data.decode() == self.TO_FLAG:
                        self.conn.sendall("Enhorabuena! Aqui tienes tu flag: flag{flagtastico}\n".encode())
                        logging.debug("Chall %s - Ending connection %s from %s", self.chall, data, self.addr)
                        break

                    else:
                        self.conn.sendall("Ohh! Has fallado! Corre e intentalo de nuevo\n".encode())
                else:
                    too_slow = "Demasiado lento! Has tardado en responder {0} s".format(diff.seconds).encode()
                    self.conn.sendall(too_slow)
                    logging.debug("Chall %s - Ending connection from %s", self.chall, self.addr)
                    self.conn.close()
                    break

                # updating ts
                current_ts = datetime.now()

