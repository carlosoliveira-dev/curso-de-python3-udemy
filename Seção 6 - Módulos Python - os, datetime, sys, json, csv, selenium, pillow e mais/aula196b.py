from threading import Thread
from time import sleep


def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()

while t1.is_alive():
    print('Esperando a Thread.')
    sleep(2)

print('Thread acabou!')
