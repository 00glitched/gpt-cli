# gpt-cli
python-based chat-gpt command line interface

## Dependencies
- Python 3 (with pip)
  - g4f
  - argparse
```sh
pip install PKGNAME
```

## How to install
- Give execution permission to ```install.sh```
```sh
chmod -x install.sh
```
- Run ```install.sh``` as super user
```sh
sudo ./install.sh
```
- Alternative automated install
```sh
sudo ./installwithdeps.sh
```
## How to use
- Run ```ai-cli``` command

## Arguments
```
	-m | --model 		: AI model to response
	-p | --pretty 		: Show text output as pretty markdown
	-t | --historial 	: Remember actual conversation
	-s | --save			: (Not implemented) save historial

```


## Examples
- Using by default option
```sh
ai-cli "Say hello world"
```
- Selecting model
```sh
ai-cli --model gpt-4o-mini "Say hello world"
```
- Selecting pretty mode
```sh
ai-cli --pretty "Say hello world"
```
- Selecting loop mode
```sh
ai-cli --historial "Say hello world"
```