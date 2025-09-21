# Libaries
```pip install ollama```
# Setup
- Download minescript mod for whatever version and follow their setup guide
- Download (ollama)[https://ollama.com/]
- Using ollama install llama3.2:latest this will take 5+ gigabytes 
  ```ollama run llama3.2:latest```
- create env.py inside of the minescript folder should look like this
```py
import os
if 'PATH' not in os.environ:
    os.environ['PATH'] = "PUT YOUR ENVIRONMENT VARIABLES HERE"
```
# Running
- in a server run \ai
- Make sure to set the text parser (found in `const.py`)
  - for regular minecraft chat set `PARSER = "minecraft"`
  - 
