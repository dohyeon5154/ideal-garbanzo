class EmptyCartError(Exception):
    pass

class Cart:
    def __init__(self):
        self.items = []  # 장바구니에 담긴 상품들을 저장할 빈 리스트 초기화

    def add(self, name, price, qty=1):
        if price < 0:
            raise ValueError("price must be >= 0")  # 가격이 음수면 예외 발생
        self.items.append((name, price, qty))       # (상품명, 가격, 수량) 튜플 형태로 저장

    def total(self):
        if not self.items:
            raise EmptyCartError("cart is empty")  # 장바구니가 비어있으면 예외 발생
        return sum(p * q for _, p, q in self.items)  # 각 상품의 (가격 × 수량)의 총합 계산 반환