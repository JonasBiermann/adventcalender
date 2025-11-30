import datetime
import webbrowser
import json
from pathlib import Path
import os

width = 80
red = "\033[91m"
black = "\033[0m"
green = "\033[92m"
blue = "\033[94m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """
    Prints a festive ASCII art header for the Advent calendar, boxed.
    """
    width = 80 # Our standard width

    print(f"+{"-"* (width - 2)}+" )
    print(f"|{' ' * (width - 2)}|") # Blank line inside
    
    # --- Header Line 1 (Adjusted spacing to be 80 chars) ---
    hl1 = f"{red}_ _   _ _   _ _{black}   ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*   {red}_ _   _ _   _ _{black}"
    print(f"|{' ' * (int((width - 2 - len(hl1)+2*len(red) + 2 * len(black))/2))}{hl1}{' ' * (int((width - 2 - len(hl1) + 2*len(red) + 2*len(black))/2))}|")
    
    # --- Header Line 2 (The text) ---
    hl2 = f"{red}( v ) ( v ) ( v ){black} |  Luisa's Adventskalender 2025  | {red}( v ) ( v ) ( v ){black}"
    print(f"|{' ' * (int((width - 2 - len(hl2) + 2*len(red) + 2*len(black))/2))}{hl2}{' ' * (int((width - 2 - len(hl2) + 2*len(red) + 2*len(black))/2))}|")
    
    # --- Header Line 3 ---
    hl3 = f"{red}\\ /   \\ /   \\ /{black}   ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*   {red}\\ /   \\ /   \\ /{black}"
    print(f"|{' ' * (int((width - 2 - len(hl3) + 2*len(red) + 2*len(black))/2))}{hl3}{' ' * (int((width - 2 - len(hl3) + 2*len(red) + 2*len(black))/2))}|")
    
    print(f"|{' ' * (width - 2)}|") # Blank line inside
    print(f"+{"-"* (width - 2)}+" )
    print(f"|{' ' * (width - 2)}|")

def print_box(number: int):
    """
    Prints a box with the given number centered inside.
    """
    fill = " "
    if number < datetime.datetime.now().day and datetime.datetime.now() >= datetime.datetime(datetime.datetime.now().year, 12, number + 1):
        fill = "#"
    
    width = 11
    print("+" + "-" * (width - 2) + "+")
    
    print("|" + fill * (width - 2) + "|")
    num_str = f"{red}{number}{black}"
    padding = (width - 2 - len(num_str) + len(red) + len(black)) // 2
    print("|" + fill * padding + num_str + fill * (width - 2 - len(num_str) - padding + len(red) + len(black)) + "|")
    print("|" + fill * (width - 2) + "|")
    print("+" + "-" * (width - 2) + "+")

def print_calendar_grid(width = 80):
    """
    Prints the 6x4 grid of 24 "doors" for the calendar.
    """
    
    # This is the left padding to center the grid within our 73-char width
    left_padding = "| " 
    right_padding = " |"
    
    # We will print 4 rows of 6 boxes
    # A list of the starting numbers for each row
    for row_start in [1, 7, 13, 19]:
        
        row_boxes = []
        for i in range(6):
            box_number = row_start + i
            # Capture the box output
            from io import StringIO
            import sys
            
            old_stdout = sys.stdout
            sys.stdout = mystdout = StringIO()
            
            print_box(box_number)
            
            sys.stdout = old_stdout
            box_output = mystdout.getvalue().splitlines()
            row_boxes.append(box_output)
        
        # Now print the boxes line by line
        for line_index in range(5): # Each box has 5 lines
            line_to_print = left_padding
            for i, box in enumerate(row_boxes):
                if i == len(row_boxes) - 1:
                    line_to_print += box[line_index] # No extra spaces after last box
                else:
                    line_to_print += box[line_index] + "  " # Two spaces between boxes
            print(line_to_print + right_padding)

        print(f"|{" " * (width - 2)}|") # Blank line between rows
    print("+" + "-" * (width - 2) + "+")

def open_door(door_number: int, door: dict):
    # takes picture path, song of the day, puzzle of the day from dict
    if door:
        picture_path = door.get("picture_path")
        picture_info = door.get("picture_info")
        picture_note = door.get("picture_note")
        song_url = door.get("song_url")
        song_name = door.get("song_name")
        puzzle = door.get("puzzle")
        puzzle_solution = door.get("solution")
        puzzle_hints = door.get("hints", [])
        
        solved_puzzle = False
        while not solved_puzzle:
            user_answer = input(f"Puzzle for door {door_number}: {puzzle} > ")
            if user_answer.strip().lower() == puzzle_solution.strip().lower():
                print(f"{green}Correct!{black} Enjoy your surprise!")
                solved_puzzle = True
            else:
                if puzzle_hints:
                    hint = puzzle_hints.pop(0)
                    print(f"Hint: {hint}")
                else:
                    print("Don't worry, the correct solution is: ", puzzle_solution)
                    print("Love you - enjoy your surprise!")
                    solved_puzzle = True
            
        # Open local picture
        if picture_info:
            print(f"Picture info: {picture_info}")
        if picture_note:
            print(f"Picture note: {picture_note}")
        if picture_path:
            abs_path = Path(os.path.abspath(picture_path))
            webbrowser.open(abs_path.as_uri())
        
        print(f"The song of the day is: {song_name}. Enjoy!")
        if song_url:
            webbrowser.open(song_url)

def main():
    running = False
    while True:
        if not running:
            print_header()
            print_calendar_grid()
            running = True
        print("\nType 'q' to quit.")
        choice = input("Which door would you like to open? > ")

        if choice.lower() == 'q':
            print("Merry Christmas! Bye!")
            break
        
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= 24:
                door_date = datetime.datetime(2024, 12, choice_num) 
                now = datetime.datetime.now()
                if now >= door_date:
                    with open('data.json', 'r', encoding='utf-8') as f:
                        doors = json.load(f)
                    door = doors[choice_num]
                    open_door(choice_num, door)
                else:
                    print(f"You can't open Door {choice_num} yet.")
                    print(f"You have to wait until December {choice_num}.")
                    input("\nPress Enter to behave yourself...")
            elif choice_num == 67:
                print(f"{red}6-7 I just bibbed right on the highway!{black}")
            elif choice_num == 73:
                print(f"{green}OH ja meine Lieblingszahl juhu{black}")
            elif choice_num == 42:
                print(f"{blue}The answer to everything?{black}")
            elif choice_num == 69:
                print(f"{red}Wann machen wir es endlich??? (Vielleicht haben wir es ja schon gemacht hihi){black}")
            else:
                print("Please enter a number between 1 and 24.")
                input("Press Enter...")
        else:
            print("Invalid input.")
            input("Press Enter...")

if __name__ == "__main__":
    main()
    print("\033[92m" + "   * " + "\033[0m") # Green star
    print("\033[92m" + "  / \\  " + "\033[0m")
    print("\033[91m" + "Merry Christmas!" + "\033[0m") # Red text