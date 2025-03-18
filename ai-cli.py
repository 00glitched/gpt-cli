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
PATH=str(os.getcwd())+"/"
LANG=str(os.getenv("LANG"))[0:2]
system=""
if LANG=="es":
    system="Eres una IA"
else:
    system="You are an AI"
input_history=[{"role": "system", "content": system}]
client = Client()


def chat(input_prompt,model="gpt-4o-mini",pretty=False,save=False):
    input_history.append({"role": "user", "content": input_prompt})
    chat_completion = client.chat.completions.create(model="gpt-4o", 
            max_tokens=1024, temperature=0.9,#top_p=1, top_k=0,
            messages=input_history, 
            stream=True)
    
    #file = os.open(PATH+"ai_historial.md",os.O_CREAT|os.O_APPEND)
    #if save==True:
    #   os.write(file,str.encode("===> "+input_prompt))
    message=""
    for msg in chat_completion:
        message+=str(msg.choices[0].delta.content)
    message=message[0:len(message)-4]
    if pretty==True:
        print(mdv.main(message,c_theme=...),end="",flush=True)#,"AXC_THEME"))
    else:
        print(message+"\n")
    #    if save==True:
    #        os.write(file,str.encode(msg.choices[0].delta.content))
    #os.close(file)
 

def main():
    args={}
    if LANG=="es":
        parser = argparse.ArgumentParser(description="CLI para consultar con IA")
        parser.add_argument("prompt", type=str, help="Pregunta o mensaje")
        parser.add_argument("-m","--model", type=str, default="gpt-4o-mini", help="Modelo a usar (por defecto: gpt-4o-mini)")
        parser.add_argument("-p","--pretty", action="store_true", help="Impresion bonita en pantalla estilo markdown")
        parser.add_argument("-t","--historial", action="store_true", help="Usar el chat en modo bucle")
        parser.add_argument("-s","--save", action="store_true", help="Guardar el historial")
        args = parser.parse_args()
    else:
        parser = argparse.ArgumentParser(description="CLI to consult with AI")
        parser.add_argument("prompt", type=str, help="Question or message")
        parser.add_argument("-m","--model", type=str, default="gpt-4o-mini", help="Model to use (default: gpt-4o-mini)")
        parser.add_argument("-p","--pretty", action="store_true", help="Pretty print on screen in markdown style")
        parser.add_argument("-t","--historial", action="store_true", help="Use chat in loop mode")
        parser.add_argument("-s","--save", action="store_true", help="Save the history")
        args = parser.parse_args()
    
    history = exit = False
    history = args.historial
    if history==False:
        print("\n\033[96m===> "+args.prompt)
        print("\033[1;37m")
        chat(args.prompt,args.model,args.pretty,args.save)
        return
    else:
        print("\n\033[96m===> "+args.prompt)
        print("\033[1;37m")
        chat(args.prompt,args.model,args.pretty,args.save)
        print("\033[0;39m\033[1;39m[exit] to exit")
        while exit==False:
            user_prompt = str(input("\033[96m===> "))
            print("\033[1;37m")
            if user_prompt != "exit":
                chat(user_prompt,args.model,args.pretty,args.save)
            else:
                print("\033[0;39m\033[1;39m")
                return False


if __name__ == "__main__":
    main()
