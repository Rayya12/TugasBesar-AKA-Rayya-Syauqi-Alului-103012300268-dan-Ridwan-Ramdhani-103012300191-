def convertRecursive(angka : int):
    assert angka >= 0

    if angka == 0:
        return "0"
    elif angka == 1:
        return "1"
    else:
        return convertRecursive(angka//2) + str(angka%2)
    

def convertIterative(angka: int) -> str:
    assert angka >= 0

    biner = ""
    while (angka > 0):
        if angka % 2 == 0:
            biner = "0" + biner
        else:
            biner = "1" +  biner
        angka =  angka//2
    return biner
