from dotenv import load_dotenv
from litellm import completion

load_dotenv()

PRIMARY = "gemini/gemini-2.0-flash"
FALLBACK = "groq/llama-3.3-70b-versatile"


def ask_llm(prompt):
    """
    Single LLM call with automatic Gemini -> Groq fallback.
    """

    response = completion(
        model=PRIMARY,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        fallbacks=[FALLBACK],
        num_retries=2,
        timeout=30,
    )

    return response.choices[0].message.content