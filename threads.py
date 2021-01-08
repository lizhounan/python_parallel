import threading
import concurrent.futures
import time

start = time.perf_counter()

def do_something(sec):
	print(f'sleep {sec} sec')
	time.sleep(sec)
	return f'done sleeping {sec} secs'


# threads = []
# for _ in range(10):
# 	t = threading.Thread(target=do_something, args=[_])
# 	t.start()
# 	threads.append(t)

# for t in threads:
# 	t.join()


with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(do_something, 1)   # f1 is a future object, which can tell us the function results or something else; automatically joni!
	f2 = executor.submit(do_something, 1)
	# when call the result(), it will wait until the thread finish
	print(f1.result())
	print(f2.result())

	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(do_something, sec) for sec in secs]

	# also we can use the map method, thos will directly return the results
	# results = executor.map(do_something, secs)

	# this will follow the order that those threads completed
	for f in concurrent.futures.as_completed(results):
		print(f.result())

	# this will follow the order that the threads starts
	# for res in results:
	# 	print(res.result())




finish = time.perf_counter()

print(f'{finish - start} seconds')