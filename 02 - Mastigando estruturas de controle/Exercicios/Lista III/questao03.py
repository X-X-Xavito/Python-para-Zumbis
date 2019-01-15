ano = 0
popA = 80000
popB = 200000

while popA < popB:
    popA = popA + (popA*0.03)
    popB = popB + (popB*0.015)
    ano = ano + 1

print(ano)
