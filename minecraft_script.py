import time
import pyautogui

# Path to your text file containing Minecraft commands
input_file = 'setblock_commands.txt'

def execute_commands_slowly(input_file, delay=2):
    # Open the input file and read all lines (commands)
    print(f"Move to Minecraft window in 10 seconds...")

    time.sleep(10)

    with open(input_file, 'r') as infile:
        commands = infile.readlines()

    # Iterate through each command and send it to Minecraft
    for command in commands:
        command = command.strip()  # Remove leading/trailing spaces
        if command:  # Skip empty lines
            # Simulate typing the command in Minecraft
            pyautogui.typewrite('t')  # Open the chat
            # time.sleep(1)
            pyautogui.typewrite(command)
            pyautogui.press('enter')  # Press Enter to execute the command
            print(f"Executed: {command}")
            time.sleep(0.05)  # Delay between commands (in seconds)

    print("All commands executed.")

if __name__ == "__main__":
    execute_commands_slowly(input_file, delay=2)  # Delay between commands set to 2 seconds
