def Mergesort(liste):

    def Merge(leftList,rightList):
        lengthLeft=len(leftList)
        lenghtRight=len(rightList)
        k=0
        i=0
        j=0
        while i<lengthLeft and j<lenghtRight:
            if  leftList[i]<=rightList[j]:
                liste[k]=leftList[i]
                i+=1
            else:
                liste[k]=rightList[j]
                j+=1
            k+=1


        while i< lengthLeft:
            liste[k]=leftList[i]
            i+=1
            k+=1
        while j< lengthLeft:
            liste[k]=rightList[j]
            j+=1
            k+=1


    if len(liste)>1:
        midIndex=math.floor(len(liste)/2)
        leftList=liste[0:midIndex]
        rightList=liste[midIndex:]

        Mergesort(leftList)
        Mergesort(rightList)
        Merge(leftList,rightList)

