import os

def readfile(path, i):
	with open(path + '\\' + i, 'r') as file:
		for a, lines in enumerate(file):
			k, l = [i.lower() for i in keyword], lines.lower()
			if 'c' in option:
				k, l = [i for i in keyword], lines
			kk = [i for i in k]
			if 'm' in option:
				if all(i in l for i in k):
					if 'j' in option:
						print('file: {}'.format((path+'\\'+i).replace(oriPath, '')))
						break
					print('file: {}, line: {}'.format((path+'\\'+i).replace(oriPath, ''), a+1))
			elif 'n' in option:
				if any(i in l for i in k):
					kk = [i for i in kk if i not in l]
				if len(kk) == 0:
					print('file: {}'.format((path+'\\'+i).replace(oriPath, '')))
					break

def cdfolder(path):
	for i in os.listdir(path):
		if 'f' in option:
			if any(j in i for j in keyword):
				print(path + '\\' + i)
		try:
			if os.path.isfile(path + '\\' + i):
				readfile(path, i)
			else:
				cdfolder(path + '\\' + i)
		except UnicodeDecodeError:
			if 'b' in option:
				print('Problem reading {} or it is a binary file'.format((path+'\\'+i).replace(oriPath, '')))
			pass

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
			print('- (N) search multiple keywords within the document')
		print('Press enter if not applicable')
		option = input().lower()

		cdfolder(path)
