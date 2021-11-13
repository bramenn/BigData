import sys

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")

        if len(line) == 10:
            edad = line[8]
            prueba = line[9]

            if prueba == "tested_positive" or prueba == "tested_negative":
                print(f"{edad} \t {prueba}")
except:
    pass
