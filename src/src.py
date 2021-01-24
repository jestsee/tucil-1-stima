#Nama       :   Jesica
#NIM        :   13519011
#Kelas      :   01
#Nama file  :   cryp1.py
#Deskripsi  :   Cryptarithmetic Solver - Tucil 1 Strategi Algortima IF2211

import re
import time
solved = False

def readWords(x,y):
    with open(x,'r') as f:
        for line in f:
            # Append to y
            y += filter(None, re.split(r'\W|\d', line))

def solve(huruf, values, visited, words,count=0):
    global solved #kalo mau akses variabel global DAN modif variabel tsb
    ''' BASIS '''
    if len(set) == len(values):
        map = {} #dictionary??? mungkin kayak {(2,'TWO')} - merepresentasikan bahwa TWO memiliki nilai 2 // Mungkin nanti mau dibikin array of tuple
        
        ''' 
        isi dictionary {'S': 5, 'O': 2, 'J': 0} 
        cara akses : map['S'] (udah nyoba) 
        '''
        
        for letter, val in zip(huruf,values): #zip tuh dia hasilnya mengisi map {}, kayak si {(2,'TWO')}
            map[letter] = val #map[huruf] = angka
            ''' 
            misal huruf = 'BAKSO' value = 12345
            maka setelah dilakukan proses diatas hasilnya adalah 
            {'S': '4', 'O': '5', 'J': 0, 'B': '1', 'A': '2', 'K': '3'}
            '''
        for i in range(len(words)):
            if map[words[i][0]] == 0: #gabisa huruf awalnya bernilai 0
            # mengakses huruf awal kata pertama, huruf awal kata kedua dan huruf awal kata ketiga
                return
        #print(map)
        #inisialisasi
        wordi = [0 for i in range (len(words))]
        for i in range(len(words)):
            wordi[i] = ""

        for i in range(len(words)):
            for c in words[i]: #untuk setiap karakter di kata pertama
                wordi[i] += str(map[c]) #angka yang merepresentasikan suatu huruf dikonversi menjadi string kemudian dimasukkan ke word 1. cth : 1 2 3 di jadiin string angka 123
        
        sum = 0
        for i in range(len(wordi)-1): #wordi yang terakhir adalah res
            sum = sum + int(wordi[i]) 

        if sum == int(wordi[len(wordi)-1]): #lalu dikonversi kembali menjadi integer
            #print("{} + {} = {}\t{}".format(word1, word2, res, map)) #buat ngeprint
            #print(map)
            cetak(words)
            cetakangka(wordi)
            print(count,"total tes sampai ditemukan solusinya")
            solved = True
        return

    ''' REKURENS '''
    for i in range(10): 
        #count = count + 1
        if not visited[i]: #jika visited[i] masih false, artinya belum pernah di-visit
            
            visited[i] = True #dibikin true
            #count = count + 1
            values.append(i) # nilai i nya dimasukkin ke array values
            
            solve(huruf, values, visited, words, count+1) #rekursif dia bakal append ke values terus sampe len values = len huruf
            
            '''
            nanti kalo len nya udah sama dia bakal ngecek hasil operasinya bener ato engga, 
            kalo bener solved jadi true namun kalo salah solved tetep false dan proses dilakukan kembali
            '''
            values.pop() #lawannya append, alias dibuang dari belakang
            
            visited[i] = False    
            #count = count + 1
        
def maxx(arrayofwords): #mencari jumlah karakter maksimal dari array of kata
    maxnya = len(arrayofwords[0]) # indeks dimulai dari 0
    for i in range (1,len(arrayofwords)):
        if(maxnya <= len(arrayofwords[i])):
            maxnya = len(arrayofwords[i])
    return maxnya

def cetak(arrayofwords): #array of words include result
    ''' 
    menghasilkan output
      SEND
      MORE
    +-----
     MONEY
    '''
    print("\n")
    blank = " "
    selisih = 0
    for i in range(len(arrayofwords)-1):
        selisih = len(result) - len(arrayofwords[i])
        preview = (blank * selisih) + arrayofwords[i]
        print(preview)
    divider = (len(result) * "-") + "+"
    print(divider)
    print(result)
    
def cetakangka(arrayofwords): #array of words include result
    ''' 
    menghasilkan output
      SEND
      MORE
    +-----
     MONEY
    '''
    print("\n")
    blank = " "
    selisih = 0
    for i in range(len(arrayofwords)-1):
        selisih = len(result) - len(arrayofwords[i])
        preview = (blank * selisih) + arrayofwords[i]
        print(preview)
    divider = (len(result) * "-") + "+"
    print(divider)
    print(arrayofwords[len(arrayofwords)-1])    



print("\nCRYPTARITHMETIC PUZZLE SOLVER")
# DIASUMSIKAN INPUT DALAM BENTUK UPPERCASE SEMUA
################## INPUT ######################
'''
n = int(input("Banyak operan : "))
wordcomp=[0 for i in range(n)]
for i in range(n):
    wordcomp[i] = input("Masukkan kata ke - {} : ".format(i+1))
#print(wordcomp)

#word1 = input("Enter WORD1: ")
#word2 = input("Enter WORD2: ")

result = input("Enter RESULT: ")
'''
namafile = input("Masukkan nama file : ")
WordList = []

readWords(namafile,WordList)

result = WordList[len(WordList)-1]
WordList.pop()
wordcomp = WordList

start_time = time.perf_counter()
if len(result) > (maxx(wordcomp)+1): 
    print("\n0 Solutions!") #untuk menangani kasus di bawah
    '''
       AKI
      AKMU+
      ----
    HAHAHA (result hanya boleh berselisih maksimal 1 banyaknya dengan word1 ataupun word2)
    '''
else:
    set = [] #set berisi semua huruf yang ada (tidak ada perulangan huruf)
    #jika huruf belum ada di array maka huruf tersebut dimasukkan ke array

    for i in range(len(wordcomp)):
        for char in wordcomp[i]:
            if char not in set:
                set.append(char)
    
    for c in result:
        if c not in set:
            set.append(c)

    #huruf di dalam set tidak boleh melebihi 10 buah
    if len(set) > 10:
        print("\nNo solutions!")
        exit()
    
    print("Solutions:")

    wordcomp.append(result)
    #print(wordcomp)
    solve(set, [], [False for _ in range(10)], wordcomp)

    if not solved:
        print("\n0 solutions!")

    print(time.perf_counter() - start_time, "seconds")