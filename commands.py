from helper import *
from prompts import *
import const

@admin_command("mode")
def Mode(ai, *args):
    mode = args[0]
    if mode in list(PROMPTS_.keys()):
      ai.prompt = mode 
      minescript.echo(ai.prompt)

@admin_command("debug")
def Debug(ai,*args):
    minescript.echo(f"prompt: {ai.prompt}")
    minescript.echo(f"prompt list: {list(PROMPTS_.keys())}")
    minescript.echo(f"Context:\n{format_context(ai.context)}")

@admin_command("prompts")
def Prompt(ai,*args):
    prmt_str = ", ".join(list(PROMPTS_.keys()))
    if len(args) == 0:
        minescript.echo(prmt_str)
        return
    if args[0] == "chat":
        sleep(3)
        minescript.chat(prmt_str)
        return

@admin_command("commands")
def Commands(ai,*args):
    cmd_str = ", ".join(list(commands.keys()))
    if len(args) == 0:
        minescript.echo(cmd_str)
        return
    if args[0] == "chat":
        sleep(3)
        minescript.chat(cmd_str)
        return

@admin_command("kill", "owner")
def Kill(ai,*args):
    exit()

@admin_command("admin", "owner")
def make_admin(ai,*args):
    if len(args) == 0:
        return
    user_roles[args[0].lower()] = "admin"
    minescript.echo(f"Made {args[0]} admin")

@admin_command("unadmin", "owner")
def make_unadmin(ai,*args):
    if len(args) == 0:
        return
    user_roles[args[0].lower()] = "user"
    minescript.echo(f"Removed {args[0]} as an admin")

@admin_command("list_admins")
def list_admins(ai,*args):
    admins = [user for user,role in user_roles.items() if role == "admin"]
    admin_str = f"Admins: {", ".join(admins)}"
    if len(args) == 0:
        minescript.echo(admin_str)
        return
    if args[0] == "chat":
        sleep(3)
        minescript.chat(admin_str)
        return

@admin_command("move")
def toggle_move(ai, *args):
    ai.has_commands = not ai.has_commands

