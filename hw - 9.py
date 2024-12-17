#1.

def merge_string(word1, word2):
    merge = []
    i = 0
    j = 0
    while i < len(word1) and j < len(word2):
        merge.append(word1[i])   #[i = 0, j = 0] #merge =[]
        merge.append(word2[j])   #word1[0] = a #word2[0] = p
                                 ##merge = [a,p]
        i += 1
        j += 1
    merge += word1[i:]
    merge += word2[j:]
    return ''.join(merge)

word1 = input("Enter word 1:")
word2 = input("Enter word 2:")
result = merge_string(word1, word2)
print(result)



#2.
def Flowers(flowerbed,n):
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i]== 0 and flowerbed [i - 1] == 0 and flowerbed[i + 1]== 0:
            flowerbed[i] = 1
            count += 1
            if count >= n:
                return True
            return False
print(Flowers([1,0,0,0,1],1))
print(Flowers([1,0,0,0,1],2))








            
