def jumlahkan(*listAngka):
    total = 0
    for angka in listAngka:
        total += angka
    return total

total = jumlahkan(10, 10)

print(total)
