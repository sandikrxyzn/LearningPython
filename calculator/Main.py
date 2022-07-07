# Kalkulator Sederhana Menggunkan python

# fungsi perjumlahan (+)
def add(x, y):
    return x + y

# fungsi pengurangan (-)
def subtract(x, y):
    return x - y

# fungsi Perkalian (x *)
def multiply(x, y):
    return x * y

# fungsi pembagian(/)
def divide(x, y): 
    return x / y

# Menu Operasi 
print('Pilih Operasi')
print('1.jumlah')
print('2.Pengurangan')
print('3.Perkalian')
print('4.Pembagian')

# Meminta Input Dari User
pilih = input('Masukan pilihan (1/2/3/4) : ')

num1 = int(input('Masukan Bilangan Pertama : '))
num2 = int(input('Masukan Bilangan Kedua   : '))

if pilih == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif pilih == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif pilih == '3':
    print(num1, "x", num2, "=", multiply(num1,num2))

elif pilih == '4':
    print(num1, "-", num2, "=", divide(num1,num2))

# Apabila User MEnginput Tidak Sesuai Maka Akn Menampilkan Ini!!!

else :
    print("Maaf Input Tidak Di Kenal :)")
