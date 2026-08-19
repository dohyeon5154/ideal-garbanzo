
def test_charge_called_with_amount(mocker):
    # 1. 대상 함수를 가짜(Mock) 객체로 교체 (패치 경로는 사용되는 곳 기준)
    fake = mocker.patch("src.payment.requests.post")

    # 2. 가짜 객체가 반환할 응답 구조 모조(Mocking)
    fake.return_value.json.return_value = {"status": "ok"}
    from src.payment import charge

    # 3. 실제 함수 호출 및 반환값 검증
    assert charge(12000) == {"status": "ok"}

    # 4. 가짜 객체가 호출된 횟수 및 인자 검증
    assert fake.call_count == 1
    assert fake.call_args.kwargs["json"]["amount"] == 1