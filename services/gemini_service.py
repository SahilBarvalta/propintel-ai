import json

from google import genai

from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt):

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown fences if Gemini adds them
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)