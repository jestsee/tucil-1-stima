#Nama       :   Jesica
#NIM        :   13519011
#Kelas      :   01
#Nama file  :   cryp3.py
#Deskripsi  :   Cryptarithmetic Solver - Tucil 1 Strategi Algortima IF2211

import re
import time
solved = False

def readWords(x,y):
    with open(x,'r') as f:
        for line in f:
            y += filter(None, re.split(r'\W|\d', line))

def solve(huruf, angka, visited, words):
    
    global solved
    ''' BASIS '''
    if len(set) == len(angka):
        
        map = {} #dictionary
        
        for letter, val in zip(huruf,angka): 
            map[letter] = val

        for i in range(len(words)):
            if map[words[i][0]] == 0: 
            # menangani kasus ketika huruf pertama setiap kata bernilai 0
                return
        solve.counter += 1

        #inisialisasi
        wordi = [0 for i in range (len(words))]
        for i in range(len(words)):
            wordi[i] = ""

        for i in range(len(words)):
            for c in words[i]: 
                wordi[i] += str(map[c]) 
        
        sum = 0
        for i in range(len(wordi)-1): 
            sum = sum + int(wordi[i]) 

        if sum == int(wordi[len(wordi)-1]): 
            cetak(words)
            cetakangka(wordi)
            print("\n")
            print(solve.counter,"total tes sampai ditemukan solusi ini")
            solved = True
        return

    ''' REKURENS '''
    for i in range(10): 
        if not visited[i]: 
            visited[i] = True
            angka.append(i)
            solve(huruf, angka, visited, words) 
            angka.pop() 
            visited[i] = False   
             
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

#DIASUMSIKAN INPUT DALAM BENTUK UPPERCASE SEMUA
################## INPUT ######################
directory = '..\\test\\'
namafile = input("Masukkan nama file : ")
WordList = []

readWords(directory+namafile,WordList)

result = WordList[len(WordList)-1]
WordList.pop()
wordcomp = WordList

start_time = time.perf_counter()
if len(result) > (maxx(wordcomp)+1): 
    print("\nTidak ada solusi")
else:
    set = []
    for i in range(len(wordcomp)):
        for char in wordcomp[i]:
            if char not in set:
                set.append(char)
    
    for c in result:
        if c not in set:
            set.append(c)

    if len(set) > 10:
        print("\nJumlah huruf melebihi 10 buah")
        exit()
    
    print("Solusi:")

    wordcomp.append(result)
    solve.counter = 0
    solve(set, [], [False for _ in range(10)], wordcomp)

    if not solved:
        print("\nTidak ada solusi")

    print("Total waktu yang dibutuhkan",time.perf_counter() - start_time, "detik")