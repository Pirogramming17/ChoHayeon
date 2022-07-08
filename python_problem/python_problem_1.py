# -*- coding: utf-8 -*-
import random
num = 0

while True :
    def brGame():
        while True :   
            try:
                cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                return cnt
                if cnt!=1 and cnt!=2 and cnt!=3 :
                    raise Exception
                break
            except ValueError :
                print('정수를 입력하세요')
            except Exception as e:
                print('1,2,3 중 하나를 입력하세요', e)

    cnt = brGame()
    for i in range(num, num+cnt) :
        num += 1
        print('player :', i+1)
        if num == 31:
            break
    if num == 31:
        print('computer win!')
        break 

    cnt = random.randint(1,3)
    for i in range(num, num + cnt) :
        num += 1
        print('computer :', i+1)
        if num == 31:
            break
    if num == 31:
        print('player win!')
        break 



