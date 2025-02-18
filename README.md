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

## How to use
- Run ```gpt-cli``` command

## Examples
- Using by default option
```sh
gpt-cli "Say hello world"
```
- Selecting model
```sh
gpt-cli --model gpt-4o-mini "Say hello world"
```
