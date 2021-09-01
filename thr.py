from time import sleep, time


def foo(num):
    sleep(2)
    print(num)

############################

# start = time()
# for i in range(10):
#     foo(i)
# print(f'Done in: {time() - start}')

############################

# import threading
#
# start = time()
# print('start')
# t1 = threading.Thread(target=foo, args=(0,))
# t2 = threading.Thread(target=foo, args=(1,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print(f'Done in: {time() - start}')

############################

# import threading
#
# start = time()
# print('start')
# threads = []
# for i in range(10):
#     t = threading.Thread(target=foo, args=(i,))
#     t.start()
#     threads.append(t)
#
# threads[-1].join()
# print(f'Done in: {time() - start}')

############################

# import threading
# import requests
# import os
# import uuid
# # url = 'https://www.thispersondoesnotexist.com/'
# url = 'https://loremflickr.com/320/240/dog'
#
#
# def get_res():
#     return requests.get(url).content
#
#
# def get_res2(*args):
#     print(threading.current_thread())
#     response = requests.get(url, stream=True)
#     if response.status_code == 200:
#         name = response.url.split('/')[-1]
#         path = os.path.join(os.getcwd(), 'tmp', name)
#         with open(path, 'wb') as f:
#             for chunk in response:
#                 f.write(chunk)


# start = time()
# print('start')
# threads = []
# print(threading.current_thread())
# for _ in range(10):
#     # get_res()
#     # get_res2()
#     t = threading.Thread(target=get_res2)
#     t.start()
#     threads.append(t)
#     ####################
#
# threads[-1].join()


# from multiprocessing.pool import ThreadPool
#
# start = time()
# with ThreadPool(10) as pool:
#     pool.map(get_res2, range(20))
# for i in range(100):
#     pool.apply(get_res2)
#
# pool.join()
#
# print(f'Done in: {time() - start}')


#############################


import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n > 0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Done in:', end - start)
#
#
# t1 = Thread(target=countdown, args=(COUNT//2,))
# t2 = Thread(target=countdown, args=(COUNT//2,))
#
# start = time.time()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time.time()
#
# print('Done in:', end - start)
#
# from multiprocessing import Process
# from time import time
# start = time()
# print('start')
# p1 = Process(target=countdown, args=(COUNT//2,))
# p2 = Process(target=countdown, args=(COUNT//2,))
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
# print(f'Done in: {time() - start}')
#
#
# import asyncio
# import aiohttp
# import os
#
# async def fetch_content(url, session):
#     async with session.get(url, allow_redirects=True) as response:
#         data = await response.read()
#         name = str(response.url).split('/')[-1]
#         path = os.path.join(os.getcwd(), 'tmp', name)
#         with open(path, 'wb') as f:
#             f.write(data)
#         return data
#
#
# async def main():
#     tasks = []
#
#     async with aiohttp.ClientSession() as session:
#         for i in range(100):
#             task = asyncio.create_task(fetch_content(url, session))
#             tasks.append(task)
#
#         return await asyncio.gather(*tasks)
#
# asyncio.run(main())
#
# import requests
# url = 'https://speed.hetzner.de/10GB.bin'
# # response = requests.get(url)
# local_filename = url.split('/')[-1]
# with requests.get(url, stream=True) as r:
#     r.raise_for_status()
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=8192):
#             if chunk: # filter out keep-alive new chunks
#                 f.write(chunk)
