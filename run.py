os.system ('git pull')
if __name__ == "__main__":
	try:
		__import__("chinda").Main()
	except Exception as e:
		exit(str(e))
