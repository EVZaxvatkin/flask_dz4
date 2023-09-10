import requests
import time
import threading
from url import urls


def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://',
    '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time()-start_time:.2f}seconds")

threads = []
start_time = time.time()


if __name__ == '__main__':
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()