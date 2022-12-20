#menghitung nilai average

list = []
total = 0

n = int(input("Masukkan banyaknya data: "))

for a in range(n):
    nilai = float(input("Masukkan nilai ke-{} : ".format(a+1))) 
    list.append(nilai) #append() = menambahkan nilai setelah list/ array dari belakang


print("\nHasil nilai total adalah : {}".format(sum(list))) #format() = untuk mengukur format berupa string ke layar monitor 

print("Hasil rata-rata adalah : {}".format(sum(list)/n))
 

