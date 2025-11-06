import datetime
import webbrowser

width = 80
def print_header():
    """
    Prints a festive ASCII art header for the Advent calendar, boxed.
    """
    width = 80 # Our standard width

    print(f"+{"-"* (width - 2)}+" )
    print(f"|{' ' * (width - 2)}|") # Blank line inside
    
    # --- Header Line 1 (Adjusted spacing to be 80 chars) ---
    hl1 = "_ _   _ _   _ _   ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*   _ _   _ _   _ _"
    print(f"|{' ' * (int((width - 2 - len(hl1))/2))}{hl1}{' ' * (int((width - 2 - len(hl1))/2))}|")
    
    # --- Header Line 2 (The text) ---
    hl2 = "( v ) ( v ) ( v ) |  Luisa's Adventskalender 2025  | ( v ) ( v ) ( v )"
    print(f"|{' ' * (int((width - 2 - len(hl2))/2))}{hl2}{' ' * (int((width - 2 - len(hl2))/2))}|")
    
    # --- Header Line 3 ---
    hl3 = "\\ /   \\ /   \\ /   ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*   \\ /   \\ /   \\ /"
    print(f"|{' ' * (int((width - 2 - len(hl3))/2))}{hl3}{' ' * (int((width - 2 - len(hl3))/2))}|")
    
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
    num_str = f"{number}"
    padding = (width - 2 - len(num_str)) // 2
    print("|" + fill * padding + num_str + fill * (width - 2 - len(num_str) - padding) + "|")
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

def open_door(door_number: int, doors: dict):
    # takes picture path, song of the day, puzzle of the day from dict
    door_info = doors.get(door_number)
    if door_info:
        picture_path = door_info.get("picture")
        picture_info = door_info.get("picture_info", "")
        song_url = door_info.get("song")
        song_name = door_info.get("song_name")
        puzzle = door_info.get("puzzle")
        puzzle_solution = door_info.get("solution")
        puzzle_hints = door_info.get("hints", [])
        
        solved_puzzle = False
        while not solved_puzzle:
            user_answer = input(f"Puzzle for door {door_number}: {puzzle} > ")
            if user_answer.strip().lower() == puzzle_solution.strip().lower():
                print("Correct! Enjoy your surprise!")
                solved_puzzle = True
            elif user_answer.strip().lower() == 'h':
                if puzzle_hints:
                    print(f"Hint: {puzzle_hints[0]}")
                    puzzle_hints.pop(0)
                else:
                    print("You can always call me my labubu.")
            else:
                print("Incorrect. Try again or type 'h' for a hint my love.")
        
        # Open local picture
        if picture_info:
            print(f"Picture info: {picture_info}")
        if picture_path:
            webbrowser.open(picture_path.as_uri())
        
        print(f"The song of the day is: {song_name}. Enjoy my love!")
        if song_url:
            webbrowser.open(song_url)

print_header()
print_calendar_grid()

print("+" + "-" * (width - 2) + "+")
choice = input("Welcome! Which door would you like to open? > ")

from datetime import datetime
current_day = datetime.now().day
if choice.isdigit():
    choice_num = int(choice)
    if 1 <= choice_num <= 24:
        if datetime.now() >= datetime(datetime.now().year, 12, current_day + 1):
            print(f"Opening door {choice_num}...")
            open_door(choice_num)
        else:
            print(f"Sorry, door {choice_num} is not available yet. Please come back on December {choice_num}{"st" if choice_num%10 == 1 and choice_num != 11 else "nd" if choice_num%10 == 2 and choice_num != 12 else "rd" if choice_num%10 == 3 and choice_num != 13 else "th"}.")
    else:
        print("Please enter a number between 1 and 24.")
else:
    print("Invalid input. Please enter a number between 1 and 24.")