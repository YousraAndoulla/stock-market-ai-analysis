from ai.pipeline import run_market_analysis


def test_run_market_analysis(monkeypatch):

    snapshot = {
        "symbol": "NVDA",
        "latest_price": 224.62,
        "price_change_5m": -0.03,
        "volume_5m": 1668,
        "bid": 224.60,
        "ask": 224.63,
        "spread": 0.03,
    }

    class FakeAnalysis:
        market_state = "Stable"
        price_observation = "Slight decline"
        volume_observation = "Moderate activity"
        liquidity_observation = "Tight spread"
        risk_notes = "Short window"

    def fake_analyze_market(context):
        return FakeAnalysis()

    monkeypatch.setattr(
        "ai.pipeline.analyze_market",
        fake_analyze_market
    )

    result = run_market_analysis(snapshot)

    assert result.market_state == "Stable"
    assert result.price_observation == "Slight decline"
    assert result.volume_observation == "Moderate activity"
    assert result.liquidity_observation == "Tight spread"
    assert result.risk_notes == "Short window"