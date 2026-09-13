from ai.context import build_market_context
from ai.market_analyzer import analyze_market


def run_market_analysis(snapshot):

    context = build_market_context(snapshot)

    analysis = analyze_market(context)

    return analysis