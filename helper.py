from const import *

from ollama import chat
from time import sleep,time
from dataclasses import dataclass, field
from collections import deque
import minescript

def format_context(context):
    return "\n".join([f"<{data['user']}> {data['msg']}" for data in list(context)])

def ask(personality: str, context: list[str], actual_message: str) -> str:
    system_prompt = f"Here is the current context: {format_context(context)}\n{personality}"

    response = chat(
        model="llama3.2:latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": actual_message},
        ],
        options={"think": False},
    )

    return str(response.message.content)

def time_func(func):
    start = time()
    result = func()
    elapsed = time() - start
    return elapsed, result

class ChatMessageManager:
    def __init__(self):
        self._messages = []
    def add(self, message):
        self._messages.append(message)

    def send(self, delay):
        message = self._messages[0]

        minescript.chat(message)
        sleep(delay)

        self._messages.pop(0)

class ChatParser:

    def __init__(self):
        self.parser = PARSER

    def parse(self, event):
        try:
            message = event.message
            user = "??"
            if self.parser == "fresh":
                parts = message.split(" âž¡ ")
                user = parts[0].split(" ", 1)[1]

                minescript.log(f"parts: {parts}")
                minescript.log(f"user: {user}")
            elif self.parser == "cheese":
                parts = message.split(" âžœ ")
                user = parts[0].split(" ", 1)[1]

            elif self.parser == "minecraft":
                parts = message.split(" ", 1)
                user = parts[0][1:-1]

            elif self.parser == "colon":
                parts = message.split(":", 1)
                user = parts[0].strip()

            else:
                raise ValueError(f"Unknown parser: {self.parser}")

            msg = parts[1]
            return {"user": OWNER if user == "{MINECRAFT_USERNAME}" else user, "msg": msg}

        except Exception as e:
            return {"user": "???", "msg": event.message}

@dataclass
class Ai_data:
    prompt = DEFAUL_PROMPT
    chat_parse:ChatParser = field(default_factory=ChatParser)
    context:deque = field(default_factory=lambda: deque(maxlen=MAX_CONTEXT_LENGTH))
    has_commands = False 

commands = {}
user_roles = {"snakesnuggles": "owner"}
role_power = {"owner":3,"admin":2,"user":1}

def admin_command(name, permission = "admin"):
    def wrapper(func):
        commands[name] = (func,permission)
        return func
    return wrapper

def admin_parser(ai:Ai_data, data):
    user = data["user"].lower()
    msg:str = data["msg"].lower()
    if not msg.startswith(f"{NAME_SPACE}:"):
        return

    cmd_args = msg.split(":")[1]
    parts = cmd_args.split(" ")
    cmd_name = parts[0]

    if cmd_name not in list(commands.keys()):
        return

    args = parts[1:]
    command_func, role = commands.get(cmd_name, (None, "user"))
    usr_role = user_roles.get(user, "user")
    if role_power.get(usr_role, 1) < role_power.get(role, 3): 
        return 

    if command_func:
        command_func(ai, *args)
        return True
