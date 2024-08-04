

def getIntUser(str_: str, rang1, rang2) -> int:
    while True:
        try:
            value = int(input(str_))
            if value < rang1 or value > rang2:
                print(f"Digite um número entre {rang1} e {rang2}")
                continue
            return value
        except ValueError:
            print("Digite um número inteiro")
