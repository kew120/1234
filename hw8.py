def buy(d):
    print('\n[구입]')
    a=input('상품명? ')
    if a=='': return False
    b=int(input('수량은? '))
    d[a]=b
    print(f'장바구니에 {a} {b}개가 담겼습니다.')

def show(d):
    print('\n>>> 장바구니 보기:',d)

def find(d):
    print('\n[검색]')
    a=input('장바구니에서 확인하고자 하는 상품은? ')
    if a in d:
        print(f'{a}은(는) {d[a]}개 담겨 있습니다.')
    else:
        print(f'장바구니에 {a}은(는) 없습니다.')
    
shopping_bag={}
while True:
    if buy(shopping_bag)==False:
        break
show(shopping_bag)
find(shopping_bag)
