from env import * 
from const import *
from prompts import *
from helper import * 
from commands import * 
import minescript
from time import sleep
import re
from threading import Timer

'''
Ideas:
    mimic personallities of players
    Be able to walk around
    Be able to auto change the prompt based on the message and context
'''
def get_prompt(ai:Ai_data,data):
    prompt_function = PROMPTS_.get(ai.prompt, PROMPTS_["default"])
    ai_message = ask(prompt_function(ai), list(ai.context), f"<{data["user"]}> {data["msg"]}")
    return ai_message
def stop_function():
    minescript.chat("#stop")
def handle_bot_commands(ai,bot_text:str):
    if not ai.has_commands:
        return
    if "GOTO" not in bot_text:
        return

    starting_point = bot_text.find("GOTO")
    
    player_name = []
    for char in bot_text[starting_point+5:]:
        if char in [" ",",",".","?",":",";"]:
            break
        player_name.append(char)

    player_name = "".join(player_name)
    minescript.echo(player_name)

    minescript.chat(f"#follow player {player_name}")
    stop_time = Timer(TIME_TO_STOP_FOLLOWING, stop_function)
    stop_time.start()

def send_ai_message(ai, data):
    if not data["msg"].lower().startswith(f"{NAME_SPACE}"):
        return

    total_time, ai_message = time_func(lambda: get_prompt(ai, data)) 

    sleep(max(0,4 - total_time))
    text = re.sub(r"<[^>]+>", "", "".join(ai_message.split("\n")))

    bot_message = f"<{BOT_NAME}> {text}"[:256]


    handle_bot_commands(ai, text)

    minescript.chat(bot_message)
    minescript.log(f"{ai_message}")

    ai.context.append(data)
    ai.context.append({"user":BOT_NAME, "msg": text})

def handle_chat_message(ai:Ai_data, event_queue):
    event = event_queue.get()
    if event.type != minescript.EventType.CHAT:
        return

    try:
        data = ai.chat_parse.parse(event)
        minescript.log(data)
        result = admin_parser(ai, data)
        if result:
            return
        send_ai_message(ai, data)

    except Exception as e:
        minescript.echo(f"Error: {e}")
        return

def main():
    ai = Ai_data()

    # parsers = ["fresh", "minecraft", "colon"]
    # if len(sys.argv) < 1:
    #     if sys.argv[1] and sys.argv[1] in parsers: 
    #         ai.chat_parse.parser 
    with minescript.EventQueue() as event_queue:
        event_queue.register_chat_listener()
        while True:
            handle_chat_message(ai,event_queue)

if __name__ == "__main__":
    main()
