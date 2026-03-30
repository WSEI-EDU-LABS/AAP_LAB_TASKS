import requests
import time
import concurrent.futures

def fetch_cat_fact(dummy=None):
    url = "https://catfact.ninja/fact"
    fakt = requests.get(url).json().get("fact")

    return fakt

def multithreading():
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        wyniki = executor.map(fetch_cat_fact, [None]*20)
        diff = end - start
        
    for fakt in wyniki:
        print(fakt)

    end = time.time()
    

    print(diff)

def sequence():
    start = time.time()

    for i in range(20):
        print(fetch_cat_fact())

    end = time.time()
    diff = end - start
    print(diff)

def main():
    sequence()

if __name__ == "__main__":
    main()
    


    