
while True:
    Number = input('What number are you thinking?  ')
    if len(Number) > 0:
        Number = int(Number)
        if Number % 2 == 0:
            print('That is s an Even  number! Have another?')
        else:
            print('That is s an odd   number! Have another?')
        continue
    else:
        print('Please  Enter Correct Number ')
    continue
