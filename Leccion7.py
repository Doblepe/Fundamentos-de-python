from threading import Thread
from time import sleep, perf_counter
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

# def print_num(thread, num):
#     print('printing nums:')
#     for i in range(1,  num +1):
#         print("Thread", thread, ":",i) 
# try:
#     Thread.start( print_num, (1,9))
#     Thread.start( print_num, (1,3))
# except:
#     print("Error")