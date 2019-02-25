import socket

IP = "localhost"

s = socket.socket()
s.connect((IP, 3825))

while True:
    c = input("Rock, Paper, or Scissors, or q to quit? [r, p, s]").lower()[0]
    if c=="q":
        break
    s.send(c.encode())
    won = s.recv(1024).decode()[0]
    print("You won!" if won=="w" else "Draw!" if won=="d" else "You lost!")

s.close()
