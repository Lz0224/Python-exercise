f = open('file5', 'w+')

f.write('p')

f.seek(1024*1024*3)

f.write('a')
