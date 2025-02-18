#!/usr/bin/env python3
import os
import argparse
from g4f.client import Client

HOME=str(os.getenv("HOME"))

def chat_with_gpt(prompt, model="gpt-4o-mini"):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
            print("Error: Debes configurar la variable de entorno OPENAI_API_KEY.")
            return
    try:
        client = Client()
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            web_search=False
        )
        print(response.choices[0].message.content)
    finally:
        pass

def main():
    parser = argparse.ArgumentParser(description="CLI para consultar ChatGPT")
    parser.add_argument("prompt", type=str, help="Pregunta o mensaje para ChatGPT")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="Modelo de OpenAI a usar (por defecto: gpt-4o-mini)")
    args = parser.parse_args()
    chat_with_gpt(args.prompt, args.model)

if __name__ == "__main__":
    main()
