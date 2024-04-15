def sliding_window(elements, windowSize):
    if len(elements) <= windowSize:
        print(elements)
    else:
        for i in range(len(elements)- windowSize + 1):
            print("len(elements):",len(elements),windowSize + 1)
            print("index:",i)
            print("i ans windowSize+i:",i,windowSize+i)
            print("len(elements) ans windowSize+1:",len(elements)-windowSize+1)

            print(elements[i:i+windowSize])

lst = [1,2,3,4,5,6,7,8] 
sliding_window(lst,3)