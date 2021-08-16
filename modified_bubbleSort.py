#you can specify the dict for which alphabeth you use.

letters_dict ={" ":30,"A": 0, "B": 1, "C": 2, "Ç": 3, "D": 4, "E": 5, "F": 6, "G": 7, "Ğ": 8, "H": 9, "I": 10, "İ": 11,"J": 12, "K": 13,
               "L": 14, "M": 15, "N": 16, "O": 17, "Ö": 18, "P": 19, "R": 20, "S": 21, "Ş": 22,"T": 23, "U": 24, "Ü": 25, "V": 26, "Y":27,"Z":28}
voc_list=["merhaba","aslan","leylek","kalem","kale","askı","aşı","cereyan","bilgisayar","birim","futbol","futsal","fenerbahçe","ağlak"]
def modified_BubbleSort(liste,letters_dict):

    for i in range(len(liste)-1):
        for j in range(0,len(liste)-i-1):
            liste[j]=liste[j].upper()
            liste[j+1] = liste[j+1].upper()


            if len(liste[j])<=len(liste[j+1]):
                for l_index in range(len(liste[j])):
                    if letters_dict[liste[j][l_index]]> letters_dict[liste[j+1][l_index]]:
                        liste[j + 1], liste[j] = liste[j], liste[j + 1]
                        break
                    elif letters_dict[liste[j][l_index]] == letters_dict[liste[j+1][l_index]]:
                        continue
                    else:
                        break


            else:
                for l_index2 in range(len(liste[j+1])):
                    if letters_dict[liste[j][l_index2]]> letters_dict[liste[j+1][l_index2]]:
                        liste[j + 1], liste[j] = liste[j], liste[j + 1]
                        break
                    elif letters_dict[liste[j][l_index2]] == letters_dict[liste[j+1][l_index2]]:
                        continue
                    else:
                        break
    print(liste)
