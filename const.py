class ConstStr:
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return str(self.val)
    def __setattr__(self, name: str, value):
        if name == "val" and hasattr(self, "val"):
            raise AttributeError("No no changing constants")
        super().__setattr__(name,value)
class ConstInt:
    def __init__(self,val):
        self.val = val
    def __int__(self):
        return int(self.val)
    def __setattr__(self, name: str, value):
        if name == "val" and hasattr(self, "val"):
            raise AttributeError("No no changing constants")
        super().__setattr__(name,value)

OWNER                  = "SnakeSnuggles"
PARSER                 = "fresh"
BOT_NAME               = "SnakeBot"
NAME_SPACE             = "snakebot"
HAS_COMMANDS           = True
DEFAUL_PROMPT          = "default"
MAX_CONTEXT_LENGTH     = 20
TIME_TO_STOP_FOLLOWING = 15
