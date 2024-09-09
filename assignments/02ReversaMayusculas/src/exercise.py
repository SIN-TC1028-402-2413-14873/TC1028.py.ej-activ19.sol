def main():
    s = input(">>>")

    sr=''
    s = s.upper()

    for i in range(len(s)-1,-1,-1):
        sr = sr + s[i]

    print(sr)

if __name__=='__main__':
    main()
