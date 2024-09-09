def main():
    s1 = input("Cadena 1:")
    s2 = input("Cadena 2:")

    if len(s1)==len(s2):
        print(s1)
        print(s2)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)

if __name__=='__main__':
    main()
