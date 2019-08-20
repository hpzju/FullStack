def code_info(s, codings):
    codes = [hex(ord(char)) for char in s]
    print(f"origin: {s}")
    print(f"codes: {codes}")

    for coding in codings:
        print(f"encoding: {coding}")
        print(f"codes: {s.encode(coding).hex()}")


if __name__ == "__main__":
    str = 'str'
    code_info(str, ('latin-1', 'utf-8'))
