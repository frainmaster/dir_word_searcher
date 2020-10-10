import os

def readfile(path, i):
	with open(path + '/' + i, 'r') as file:
		k = [ii if 'c' in option else ii.lower() for ii in keyword]
		for a, lines in enumerate(file):
			l = lines if 'c' in option else lines.lower()
			if len(keyword) > 1 and 'm' in option:
				if all(ii in l for ii in k):
					if 'j' in option:
						print('file: {}'.format((path+'/'+i).replace(oriPath, '')))
						break
					print('file: {}, line: {}'.format((path+'/'+i).replace(oriPath, ''), a+1))
			else:
				if any(j in l for j in k):
					k = [j for j in k if j not in l]
				if len(k) == 0:
					print('file: {}, line: {}'.format((path+'/'+i).replace(oriPath, ''), a+1))
					break

def cdfolder(path):
	try:
		for i in os.listdir(path):
			if 'f' in option:
				if any(j.lower() in i.lower() for j in keyword):
					print('path: ' + i)
			try:
				if os.path.isfile(path + '/' + i):
					readfile(path, i)
				else:
					cdfolder(path + '/' + i)
			except UnicodeDecodeError:
				if 'b' in option:
					print('Problem reading {} or it is a binary file'.format((path+'/'+i).replace(oriPath, '')))
				pass
	except OSError:
		print('path not found. please insert a proper path. Type "S" to start again.')
		path = input()
		oriPath = path
		if path.lower() == 's':
			pass
		else:
			cdfolder(path)

if __name__ == '__main__':
	while True:
		keyword = []
		option = ''
		print('\nkeyword to search:')
		i = input()
		while i != '' or len(keyword) == 0:
			if i != '':
				keyword.append(i)
			print('insert more keywords')
			i = input()

		print('input a path:')
		path = input()
		while path == '':
			print('please insert a proper path')
			path = input()
		oriPath = path

		print('additional actions (type the key, combine as single string):')
		print('- (C) case sensitive')
		print('- (B) show if binary files')
		print('- (J) just show the files involved, no line number')
		print('- (F) include search for file/dir names')
		if len(keyword) > 1:
			print('- (M) search multiple keywords in a single line')
		print('Press enter if not applicable')
		option = input().lower()

		cdfolder(path)
