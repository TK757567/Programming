def dec(check):
    username = ""
    password = ""
    char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for j, enc in enumerate(check):
        for i in char:
            for x in char:
                if (j + (j + 1) * (ord(x) + ord(i)) - ord(i)) == enc:
                    username += i
                    password += x
                    c = 1
                    break
            if c == 1:
                c = 0
                break
    return username,password






check=[103,340,511,724,1044,969,1365,1631,1648,1980,2237,2684,2669,2974,2092,2449]

username,password=dec(check)

print(f'User:{username}\nPass:{password}')
