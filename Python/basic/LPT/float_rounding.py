if __name__ == '__main__':

    list(map(lambda x: print(f"round(float({x})) : {round(float(x))}\n"), ('1.2', '-1.2', '1.5', '-1.5', '2.5', '-2.5', '3.5', '-3.5', '4.5', '-4.5')))

    list(map(lambda x: print(f"round(float({x})) : {round(float(x), 1)}\n"), ('0.12', '-0.12', '0.15', '-0.15', '0.25', '-0.25', '0.35', '-0.35', '0.45', '-0.45')))
