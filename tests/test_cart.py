import logging


def test_error_is_logged(cart, caplog):
    # caplog: logging 모듈의 로그 출력을 가로채는 내장 픽스처
    with caplog.at_level(logging.ERROR):  # ERROR 레벨 이상의 로그만 캡처
        try:
            cart.total()
        except Exception:
            logging.getLogger("app").exception("빈 장바구니 결제 시도")

    assert "빈 장바구니" in caplog.text  # 로그 메시지 텍스트 검증
    assert caplog.records[0].levelname == "ERROR"  # 로그 레벨 검증