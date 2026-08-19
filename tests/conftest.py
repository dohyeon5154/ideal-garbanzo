import pytest
from src.cart import Cart


@pytest.fixture(scope="function")
def cart():
    print("\n\t\t[준비] 새 장바구니")
    c = Cart()
    yield c  # 테스트 함수에 생성된 Cart 인스턴스(c) 전달
    print("\t\t[정리] 장바구니 비움")
    c.items.clear()  # 테스트 종료 후 실행되는 뒷정리(Teardown)

