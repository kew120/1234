print('[구입]')
shopping_bag={}
while True:
    item=input('상품명? ')
    if item=='': break
    a=int(input('수량은? '))
    shopping_bag[item]=a
    print(f'장바구니에 {item} {a}개가 담겼습니다.')
    print()
print()
print(f'>>> 장바구니 보기: {shopping_bag}')
print()
print('[검색]')
b=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{b}은(는) {shopping_bag[b]}개 담겨 있습니다.')
