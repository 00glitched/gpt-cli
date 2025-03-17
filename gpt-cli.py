#!/usr/bin/env python3
parsing=True
import os
try:
    import argparse
except ImportError:
    print("Módulo no instalado: pip install argparse")
    parsing=False
try:
    from g4f.client import Client
except ImportError:
    print("Módulo no instalado: pip install g4f")
try:
    import mdv
except ImportError:
    print("Módulo no instalado: pip install mdv")

HOME=str(os.getenv("HOME"))

def chat_with_gpt(prompt, model="gpt-4o-mini", pretty=False):
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
        msg=""
        if pretty == True:
            msg=formatted = mdv.main(str(response.choices[0].message.content),"AXC_THEME")
            print(msg)
        elif pretty == False:
            msg=response.choices[0].message.content
            print(msg)
        else:
            print("Error: '"+pretty+"' no es un argumento valido.")
        
    finally:
        pass

def main():
    parser = argparse.ArgumentParser(description="CLI para consultar ChatGPT")
    parser.add_argument("prompt", type=str, help="Pregunta o mensaje para ChatGPT")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="Modelo de OpenAI a usar (por defecto: gpt-4o-mini)")
    parser.add_argument("-p","--pretty", action="store_true", help="Impresion bonita en pantalla estilo markdown")

    args = parser.parse_args()
    chat_with_gpt(args.prompt, args.model, args.pretty)

if __name__ == "__main__":
    main()
