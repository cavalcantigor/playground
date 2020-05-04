def convert(number):
    try:
        n = int(number)
        raindrop = ""
        if n % 3 == 0:
            raindrop += "Pling"
        if n % 5 == 0:
            raindrop += "Plang"
        if n % 7 == 0:
            raindrop += "Plong" 
        if raindrop:
            return raindrop
        else:
            return str(number)
    except Exception:
        raise Exception('Cannot convert number parameter as integer.')