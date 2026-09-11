from pydantic import BaseModel


class MarketAnalysis(BaseModel):
    market_state: str
    price_observation: str
    volume_observation: str
    liquidity_observation: str
    risk_notes: str