# gpt-cli
python-based chat-gpt command line interface

## Dependencies
- Python 3 (with pip)
  - g4f
  - argparse
  - mdv
```sh
pip install PKGNAME
```

## How to install
- Give execution permission to ```install.sh```
```sh
chmod -x install.sh
```
- Run ```install.sh```
```sh
./install.sh
```
- Alternative automated install
```sh
./installwithdeps.sh
```
## How to use
- Run ```ai-cli``` command

## Arguments
```
	-h | --help			: Show arguments
	-m | --model 		: AI model to response
	-p | --pretty 		: Show text output as pretty markdown
	-t | --talk 		: Remember actual conversation
	-s | --save		: (Not implemented) save in a file
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
ai-cli --talk "Say hello world"
```