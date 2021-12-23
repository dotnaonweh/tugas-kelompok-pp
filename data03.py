def baca_data03():
	file = open('data03.txt','r')
	read = file.read()
	file.close()
	return read

def main():
	list_data = []
	file = baca_data03()
	data = list(map(int, file.split()))
	list_data.extend(data)
	print(list_data)
	print('Tipe data :',type(list_data))
main()