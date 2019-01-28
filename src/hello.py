
# prints hello

import utils

@utils.benchmark
def say_hi():
	print("hello Dior")

@utils.benchmark
def say_bye():
        print("bye git!")


if __name__ == "__main__":
	say_hi()
	say_bye()

# hello this is a change

