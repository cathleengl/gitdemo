# utils for gitflowdemo

def benchmark(func):
	''' Standard benchmark decorator. '''

	from time import clock

	def wrapper(*args, **kwargs):
		t = clock()
		res = func(*args, **kwargs)
		print("function: ", func.__name__, "benchmark: ", clock()-t, "s")
		return res

	return wrapper


