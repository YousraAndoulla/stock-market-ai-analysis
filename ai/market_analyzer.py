from openai import OpenAI

from src.config import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_market(context):

    response = client.responses.create(
        model="gpt-5.6",
        instructions="""
You are a professional market analysis assistant.

Analyze the provided market context.

Your analysis should:
1. Describe the current market situation.
2. Explain the recent price movement.
3. Discuss trading activity.
4. Discuss the bid-ask spread.
5. Clearly distinguish observations from interpretations.

Do not make an automatic BUY or SELL decision.
The final trading decision belongs to the trader.
""",
        input=context,
    )

    return response.output_text