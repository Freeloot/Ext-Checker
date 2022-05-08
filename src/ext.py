import sys, pathlib, os

def main(fpath):
	if os.path.isfile(fpath):
		file_ext = pathlib.Path(fpath).suffix 
		print(file_ext)
	else:
		exit()

if __name__ == '__main__': main(sys.argv[1])