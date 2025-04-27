rint("Nama:haidul mahfud  Nim : 24241130")

inputUser = int(input("masukan angka yang bernilai kurang dari 24 atau lebih besar dari 33:"))

#+++++24-------------
#memeriksa angka kurang dari 24
iskurangdari = (inputUser <24)

#memeriksa angka lebih dari 33
islebihdari = (inputUser >30)

final = iskurangdari or islebihdari
print("angka yang anda masukan :",final)