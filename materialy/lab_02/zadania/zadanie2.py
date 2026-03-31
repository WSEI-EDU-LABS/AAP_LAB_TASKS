import queue
import threading
import time

def producent(q_parzyste, q_nieparzyste):
    for i in range(1, 101):
        if i % 2 == 0:
            q_parzyste.put(i)
        else:
            q_nieparzyste.put(i)
    pass
    print("Producent zakończył generowanie liczb.")

def consument(que, consument_name):
    while True:
        liczba = que.get()
        if liczba == None:
            break
        
        print(f"{consument_name} pobrał liczbę {liczba}")
        que.task_done()
        if liczba == 100:
            break

def main():
    czas = time.time()
    q_parzyste = queue.Queue()
    q_nieparzyste = queue.Queue()
    
    producent_thread = threading.Thread(target=producent, args=(q_parzyste, q_nieparzyste))

    consument1_thread = threading.Thread(target=consument, args=(q_parzyste, "Konsument parzysty"))    
    consument2_thread = threading.Thread(target=consument, args=(q_nieparzyste, "Konsument Nieparzysty"))    

    producent_thread.start()
    consument1_thread.start()
    consument2_thread.start()
    
    producent_thread.join()
    q_parzyste.put(None)
    q_nieparzyste.put(None)
    consument1_thread.join()
    consument2_thread.join()

    print(time.time() - czas)


if __name__ == "__main__":
    main()