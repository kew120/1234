def get_fixed_price(p):
    return p*100/(100-c)

c = int(input('할인율은? '))
a = int(input('A 상품의 할인된 가격은? '))
b = int(input('B 상품의 할인된 가격은? '))
print('A 상품의 정가는', int(get_fixed_price(a)), '원')
print('B 상품의 정가는', int(get_fixed_price(b)), '원')
