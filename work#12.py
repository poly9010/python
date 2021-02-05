def inputPoly(): #다항식을 입력하는 함수
    a=int(input('지수:'))
    b=int(input('계수:'))
    num=[]
    p=[]
    while a>=0:
        num.append(a)
        k=num.count(a)
        if k==1:
            t=[]
            t.append(a)
            t.append(b)
            p.append(t)
            a=int(input('지수:'))
            b=int(input('계수:'))
        else:
            print(' 같은 지수 값을 가지는 원소가 있습니다.')
            a = int(input('지수:'))
            b = int(input('계수:'))
    p.sort()
    p.reverse()
    return p


def printPoly(p): #다항식을 표현하는 리스트 p를 다항식 형태로 출력하는 함수
    num1=[]
    num2=[]
    a=0
    b=1
    k=0
    for i in range(0,len(p)):
        num1.append(p[i][a])
        num2.append(p[i][b])
    for i in range(0,len(p)):
        if num2[i]>1 or num2[i]<0:
            if num1[i]>1:
                print(num2[i],end='')
                print('x^',end='')
                print(num1[i],end='')
            elif num1[i]==0:
                print(num2[i],end='')
            elif num1[i]==1:
                print(num2[i],end='')
                print('x',end='')

        else:
            if num2[i]==1:
                if num1[i]>1:
                    print('x^',end='')
                    print(num1[i],end='')
                elif num1[i]==1:
                    print('x')
                elif num1[i]==0:
                    print(num2[i],end='')
        if i!=len(p)-1:
            if num2[k+1]>0:
                print('+',end='')
                k+=1
            else:k+=1
    print('')
def evalPoly(p, x): #x의 값을 입력하면 다항식을 계산한 결과를 반환하는 함수
    a = 0
    b = 1
    s = 1
    t = 0
    for i in range(len(p)):
        j = 1
        while j <= p[i][a]:
            s *= x
            j += 1
        s *= p[i][b]
        t += s
        s = 1
    return t


def addPoly(A, B): #두 개의 다항식 A와 B를 더한 결과를 반환하는 함수
    a=0
    b=1
    i=0
    c=[]
    if len(A)!=len(B):
        t=[0,0]
        while len(A)>len(B):
            B.append(t)
        while len(A)<len(B):
            A.append(t)

    while i<=len(A)-1:
        j=0
        while j<=len(B)-1:
            d=[]
            e=[]
            if A[i][a]==B[j][a]:
                d.append(A[i][a])
                d.append(A[i][b]+B[j][b])
                c.append(d)
                i+=1
                j+=1
            else:
                if A[i][a]>B[j][a]:
                    d.append(A[i][a])
                    d.append(A[i][b])
                    c.append(d)
                    e.append(B[j][a])
                    e.append(B[j][b])
                    c.append(e)
                    i+=1
                    j+=1
                else:
                    d.append(B[j][a])
                    d.append(B[j][b])
                    c.append(d)
                    e.append(A[i][a])
                    e.append(A[i][b])
                    c.append(e)
                    i+=1
                    j+=1
        i+=1
    i=0
    while i<=len(c)-1:
        j=len(c)-1
        while i<j:
            if c[i][a]==c[j][a]:
                c[i][b]=c[i][b]+c[j][b]
                c.pop(j)
                j-=1
            else:j-=1
        i+=1
    while i<=len(c)-1:
        j=len(c)-1
        while i<j:
            if c[i][a]==c[j][a]:
                c[i][b]=c[i][b]+c[j][b]
                c.pop(j)
                j-=1
            else:j-=1
        i+=1
    return c


def multiplyPoly(A,B): #두 개의 다항식 A와 B를 곱한 결과를 반환하는 함수
    b=1
    i=0
    a=0
    c=[]
    while i<=len(A)-1:
        j=0
        while j<=len(B)-1:
            d=[]
            d.append(A[i][a]+B[j][a])
            d.append(A[i][b]*B[j][b])
            c.append(d)
            j+=1
        i+=1
    i=0
    while i<=len(c)-1:
        j=len(c)-1
        while i<j:
            if c[i][a]==c[j][a]:
                c[i][b]=c[i][b]+c[j][b]
                c.pop(j)
                j-=1
            else:j-=1
        i+=1
    c.sort()
    c.reverse()
    return c

# 메인 함수 #
m = 1
P = []
while m != 9:
    print('1. 다항식 입력')
    print('2. 다항식 출력')
    print('3. 다항식 계산')
    print('4. 다항식 덧셈')
    print('5. 다항식 곱셈')
    m = int(input('메뉴 선택 (종료시는 9) : '))
    if m == 1:
        print('다항식 입력 선택\n')
        P = inputPoly()
    elif m == 2:
        print('다항식 출력 선택\n')
        print('다항식 P')
        printPoly(P)
    elif m == 3:
        print('다항식 계산 선택\n')
        printPoly(P)
        x = int(input('X = '))
        result = evalPoly(P, x)
        print('계산 결과 : ', result)
    elif m == 4:
        print('다항식 덧셈 선택\n')
        A = inputPoly()
        print('')
        B = inputPoly()
        print('다항식 A')
        printPoly(A)
        print('다항식 B')
        printPoly(B)
        C = addPoly(A, B)
        print('A+B')
        printPoly(C)
    elif m == 5:
        print('다항식 곱셈 선택\n')
        A = inputPoly()
        print('')
        B = inputPoly()
        print('다항식 A')
        printPoly(A)
        print('다항식 B')
        printPoly(B)
        C = multiplyPoly(A, B)
        print('A*B')
        printPoly(C)
    else:
        if m != 9:
            print('메뉴 선택 오류\n')
