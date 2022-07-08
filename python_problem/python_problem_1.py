# -*- coding: utf-8 -*-
num = 0

while True :
    while True :   
        try:
            cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if cnt!=1 and cnt!=2 and cnt!=3 :
                raise Exception
            break
        except ValueError :
            print('정수를 입력하세요')
        except Exception as e:
            print('1,2,3 중 하나를 입력하세요', e)

    for i in range(num, num+cnt) :
        num += 1
        print('playerA :', i+1)
        if num == 31:
            break
    if num == 31:
        print('playerB win!')
        break 

    while True :   
        try:
            cnt2 = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if cnt2!=1 and cnt2!=2 and cnt2!=3 :
                raise Exception
            break
        except ValueError :
            print('정수를 입력하세요')
        except Exception as e:
            print('1,2,3 중 하나를 입력하세요', e)
    for i in range(num, num + cnt2) :
        num += 1
        print('playerB :', i+1)
        if num == 31:
            break
    if num == 31:
        print('playerA win!')
        break 

