def uniq(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)): 
            if(str[i] == str[j]):
                return False
    return True


def validity(x,y):
    if(x.isalpha()&y.isalpha()):
        if((len(a)<26)&(len(b)<26)):
           if(uniq(a)&uniq(b)):
               return True
           else:
                print("Please Do not repeat")
        else:
            print("Please Do not repeat")
    else:
        print("Only Alphabets please")
    return False


raw_a=input("Alphabets in room 1:- ")
raw_b=input("Alphabets in room 2:- ")
a=raw_a.replace(" ","")
b=raw_b.replace(" ","")
if(validity(a,b)==True):
    res = [x for x in a + b if x not in a or x not in b]
    print(res)
