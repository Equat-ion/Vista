import os
import subprocess
import psutil
import math

#LOL Comments

# Command modules

def calculator_adv():
    print("Advanced Calculator: Type your expression.")
    print("Supported operations: +, -, *, /, ** (exponentiation), sqrt (square root), sin, cos, tan, log, etc.")
    print("ANGLE_MODE: Radians")
    while True:
        expression = input("Enter expression: ").strip().lower()

        if expression == "exit":
            break
        
        try:
            result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "pi": math.pi, "e": math.e})
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


def sysinfo():
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")
    print(f"Disk usage: {psutil.disk_usage('/').percent}%")

def openapp(app):
    try:
        subprocess.Popen([app], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"SUCCESS: {app} opened successfully.")
    except FileNotFoundError:
        print(f"Error: '{app}' not found.")
    except TypeError:
        print(f"Error: Please enter the name of the application to open.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to open {app}.")

def help():
    print("Help Yourself")

def greet():
    user = os.getlogin()
    print(f"Welcome {user} to PaShcal")
    print('For a list of commands type "help". To exit type "exit".')

# Main

def main():
    command_index = {
        "greet": greet,
        "exit": exit,
        "help": help,
        "open": openapp,
        "sysinfo": sysinfo,
        "calc": calculator_adv,
    }

    greet()

    while True:
        command = input("==> ").strip().lower().split()

        if len(command) == 0:
            print("No command entered.")
            continue
        
        if command[0] in command_index:
            if command[0] == "open" and len(command) > 1:
                openapp(command[1])
            else:
                command_index[command[0]]()  # Call other commands like 'help' and 'greet'
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()
