import os

def readfile(path, i):
	with open(path + '\\' + i, 'r') as file:
		for a, lines in enumerate(file):
			k, l = keyword.lower(), lines.lower()
			if 'c' in option:
				k, l = keyword, lines
			if k in l:
				print('file: {}, line: {}'.format((path+'\\'+i).replace(oriPath, ''), a+1))

def cdfolder(path):
	for i in os.listdir(path):
		try:
			if os.path.isfile(path + '\\' + i):
				readfile(path, i)
			else:
				cdfolder(path + '\\' + i)
		except UnicodeDecodeError:
			if 's' in option:
				print('Problem reading {} or it is a binary file'.format((path+'\\'+i).replace(oriPath, '')))
			pass

if __name__ == '__main__':
	while True:
		print('keyword to search:')
		keyword = input()

		print('input a path:')
		path = input()
		oriPath = path

		print('additional actions (type the key, combine as single string):')
		print('- (C) case sensitive')
		print('- (S) show if binary files')
		print('Ignore if not applicable')
		option = input().lower()

		cdfolder(path)