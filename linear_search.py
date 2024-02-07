def find_number(arr, query):
    if len(arr)==0:
        return -1
    for i in range(0,len(arr)-1):
        if arr[i]==query:
            return i

    return -1

print("found number: ",find_number([], 7))