

def decToBin(dec):
    bin = []
    while dec > 0:
        if dec % 2 == 1:
            bin.insert(0,1)
            dec -= 1
            dec = int(dec - (dec/2))
        elif dec % 2 == 0:
            bin.insert(0,0)
            dec = dec - (dec/2)
    string = ""
    for i in bin:
        string += str(i)
    bin = int(string)
    return bin

def binToDec(bin):
    dec = 0
    bin = [int(x) for x in str(bin)]
    for i in range(len(bin)):
        digit = bin.pop()
        if digit == 1:
            dec = dec + pow(2, i)
    return dec

print(decToBin(3))
print(binToDec(11))