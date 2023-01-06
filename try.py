def AskAS():
    ft = int(input("first term:"))
    cd = int(input("common difference:"))
    nt = int(input("number of the term:"))
    print("first term:",ft,"\tcommon difference:",cd,"\tnumber of the term:",nt)
    return (ft, cd , nt)

def DisplayAS(a,d,T):
    print("the arithmetic sequence: ", end='')
    for i in range(T-1):
        print(a, end=', ')
        a = a + d
    print(a)
    return

def SumAS(a,d,T):
    sumAS = 0
    for i in range(T):
        sumAS = sumAS + a
        a = a + d
    #print("the sum: ",sumAS)
    return sumAS

def ProAS(a,d,T):
    ProAS = 1
    for i in range(T):
        ProAS = ProAS * a
        a = a + d
    #print("the pro: ",ProAS)
    return ProAS

def AskOper(a, d, T):
    mode_in = input("please choose i ii iii:")
    if mode_in == 'i':
        print("the sum: ", SumAS(a,d,T))
    if mode_in == 'ii':
        print("the pro: ", ProAS(a,d,T))
    if mode_in == 'iii':
        print("the sum and pro", SumAS(a,d,T), ProAS(a,d,T))


def main():
    a, d, T = AskAS()
    DisplayAS(a, d, T)
    AskOper(a, d, T)



main()