from threading import Thread
def task():
        print("Ejecutando task")

new_th1 = Thread(target=task)
new_th2 = Thread(target=task)
new_th3 = Thread(target=task)
new_th4 = Thread(target=task)

new_th1.start()
new_th2.start()
new_th3.start()
new_th4.start()
