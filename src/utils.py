# utils for gitflowdemo

def benchmark(func):
	''' Standard benchmark decorator. '''

	from time import clock

	def wrapper(*args, **kwargs):
		t = clock()
		res = func(*args, **kwargs)
		print("Function: ", func.__name__, "time to execute: ", clock()-t, "s")
		return res

	return wrapper


