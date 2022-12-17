import socket
import operator

history = []
operators = {
            "+": operator.add,
            "-": operator.sub,
            }

IP = "127.0.0.1"
PORT = 9696

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((IP, PORT))

print('Сервер запущен {}'.format(socket.getsockname()))

while True:
    messageBytes, address = socket.recvfrom(2048)
    messageString = messageBytes.decode('utf-8')
    print('Получили информацию от {} : {}'.format(address, messageString))

    messageString = messageString.split(", ")
    a = messageString[0]
    b = messageString[1]
    operator = messageString[2]

    if a == 'T' or b == 'T' or operator == 'T':
        break

    result = operators[operator](int(a), int(b))
    history_result = (a, b, operator, result)
    history.append(history_result)

    socket.sendto(str(result).encode(), address)

socket.close()
print(history)
