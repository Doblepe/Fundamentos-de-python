from time import sleep, perf_counter
from threading import Thread, current_thread, Semaphore
def task():
    sleep(1)


start = perf_counter()
# task()
# task()
# task()
# task()
finish = perf_counter()

print(f"Tiempo total serie {finish-start: 0.2f} segundos")



start = perf_counter()

#inializar hilos
new_th1 = Thread(target=task)
new_th2 = Thread(target=task)
new_th3 = Thread(target=task)
new_th4 = Thread(target=task)

#lanzar hilos
new_th1.start()
new_th2.start()
new_th3.start()
new_th4.start()

finish = perf_counter()

print(f"Tiempo total paralelo 1 {finish-start: 0.2f} segundos")


start = perf_counter()

#inializar hilos
new_th1 = Thread(target=task)
new_th2 = Thread(target=task)
new_th3 = Thread(target=task)
new_th4 = Thread(target=task)

#lanzar hilos
new_th1.start()
new_th2.start()
new_th3.start()
new_th4.start()

#esperar hilos
new_th1.join()
new_th2.join()
new_th3.join()
new_th4.join()


finish = perf_counter()

print(f"Tiempo total paralelo 2 {finish-start: 0.2f} segundos")


start = perf_counter()

def task(id):
    print(f"Entrando la hebra {id}")
    print(current_thread().getName())
    sleep(1)

hebras = []

for n in range(0,10):
    t = Thread(target=task,args=(n,),name="th_"+str(n))
    hebras.append(t)
    t.start()

for t in hebras:
    t.join()


finish = perf_counter()

print(f"Tiempo total paralelo 2 {finish-start: 0.2f} segundos")



#semaforos

semaforo = Semaphore(1)

def region_critica(id):
    #with semaforo:
    global x
    x = x + id
    print(f"el hilo {id} vale {x}")
    x = 1


x = 1

for n in range(0,10):
    t = Thread(target=region_critica,args=(n,),name="th_"+str(n)).start()
