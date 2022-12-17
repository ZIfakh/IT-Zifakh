import socket

IP = "127.0.0.1"
PORT = 9696

print(' - Нажмите T, чтобы выйти  \n - Введите значения x и y, затем операцию')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Введите x')
    a = input()

    print('Введите y')
    b = input()

    print('Операция (+, - )')
    operator = input()

    message = a +', '+b+', '+operator
    socket.sendto(message.encode('utf-8'), (IP, PORT))

    if a == 'T' or b == 'T' or operator == 'T':
        break

    data, address = socket.recvfrom(2048)
    text = data.decode('utf-8')
    print(f'Ответ {text}\n')

socket.close()