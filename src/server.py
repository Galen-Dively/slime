import socket
from _thread import *
from player import Player
import pickle
import json

class Server:
    def __init__(self):
        # get server connfigs
        with open("server_config.json") as f:
            self.server_config = json.loads(f)

        self.server = self.server_config["Host"]
        self.port = self.server_config["Port"]

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.bind((self.server, self.port))

        self.s.listen(2)
        print("Waiting for a connection, Server Started")


    self.players = [Player(1), Player(2)]
    self.bullets = []

    def threaded_client(conn, player):

        conn.send(pickle.dumps(players[player]))
        reply = ""
        while True:
            try:
                data = pickle.loads(conn.recv(2048))
                players[player] = data

                if not data:
                    print("Disconnected")
                    break
                else:
                    if player == 1:
                        reply = players[0]
                    else:
                        reply = players[1]

                    print("Received: ", data)
                    print("Sending : ", reply)

                conn.sendall(pickle.dumps(reply))
            except:
                break

        print("Lost connection")
        conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
