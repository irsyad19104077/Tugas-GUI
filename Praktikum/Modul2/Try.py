# try..exceot
try :
    a = int(input('Masukkan Nilai a: '))
    b = int(input('Masukkan Nilai b: '))
    c = a / b
    print(f"{a} / {b} = {c}")

except ZeroDivisionError as e :
    print('Error : Tidak boleh bagi 0')

#try..except..finally
try :
    f = open('contoh.txt', 'r')
    line = f.readlines()
    for line in lines :
        print(line, end='\n')

except IOError as e :
    print('Error : File Ilang')

finally :
    if f :
        f.close()