def calculateNumber(*listNumber):
    total = 0
    for number in listNumber:
        total += number
    print(f"List {listNumber} - Hasil : {total}")


calculateNumber(10)
calculateNumber(10, 20)


def sayHelloAndCalculateNumber(name, *listNumber):
    total = 0
    for number in listNumber:
        total += number
    print(f"Helo {name} ini hasil angka mu : {total}")

sayHelloAndCalculateNumber("Abed", 10, 20)