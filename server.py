import socket

s = socket.socket()
s.bind(("", 3825))
s.listen(10)

c1, a1 = s.accept()
c2, a2 = s.accept()

#[11, 13, 17] # Rock, Paper, Scissors (P1)
#[23, 29, 31] # Rock, Paper, Scissors (P2)
GAME_STATE = {11*23: 0, 11*29: 2, 11*31: 1,
        13*23: 1, 13*29: 0, 13*31: 2,
        17*23: 2, 17*29: 1, 17*31: 0}

while True:
    try:
        m1 = c1.recv(1024).decode().strip()
        m2 = c2.recv(1024).decode().strip()
        m1s = {"r": 11, "p": 13, "s": 17}[m1]
        m2s = {"r": 23, "p": 29, "s": 31}[m2]
    except:
        print("A client exited. ")
        break
    if GAME_STATE[m1s*m2s] == 0:
        c1.send(b"d")
        c2.send(b"d")
    elif GAME_STATE[m1s*m2s] == 1:
        c1.send(b"w")
        c2.send(b"l")
    else:
        c1.send(b"l")
        c2.send(b"w")

c1.close()
c2.close()
s.close()
