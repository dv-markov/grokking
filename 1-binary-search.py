import string
import math


def print_with_spacers(input_string: string, **kwargs):
    dashed_line = "\n" + "-" * 150 + "\n"
    print(dashed_line + input_string + dashed_line, **kwargs)

print_with_spacers("Binary search algorythm")

while not (max_number := input("Enter the max number (positive integer): ")).isdigit():
    print("Wrong input, please try again")
max_number = int(max_number) + 1
print_with_spacers(f"🤖: Pick any integer number between zero and {max_number - 1} remember it!")
max_steps = math.ceil(math.log(max_number, 2))
input("Press enter to continue...")
print_with_spacers(f"🤖: {"*" * max_steps} > I bet I will guess your number not more than in {max_steps} steps! < {"*" * max_steps}")

start_number = 0
guess_number = max_number // 2
trials_count = 1
while  (user_reply := input(f"Step {trials_count}: Have you chosen number {guess_number}? \n"
             f"Type 'y' if correct, '>' if your number is bigger or '<' if your number is smaller: ")) != "y":
    if user_reply == ">":
        start_number = guess_number
        guess_number = (start_number + max_number) // 2
    elif user_reply == "<":
        max_number = guess_number
        guess_number = (start_number + max_number) // 2
    else:
        print("Wrong input, please try again")
        continue
    trials_count += 1

win_phrase = f"\n🤖: Ha-ha-ha!!! As promised, not more than {max_steps} !" if trials_count <= max_steps else ""

print_with_spacers(f"""🤖: The game is over in {trials_count} steps.{win_phrase}
🤖: Thank you for playing, human!""")
