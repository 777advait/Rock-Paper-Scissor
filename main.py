from PyInquirer import prompt
from rich.console import Console
from rich.markdown import Markdown
from examples import custom_style_1
import random

CHOICES = ["Rock", "Paper", "Scissors"]
console = Console()

comp_points = 0
player_points = 0

def main():
	global player_points, comp_points

	while True:
		questions = [{
			'type':'input',
			'name':'rounds',
			'message':'Enter the number of rounds you would like to play:'
		}]

		answers = prompt(questions, style=custom_style_1)
		console.clear()
		md = Markdown("""
### Welcome to **Rock-Paper-Scissors game!**
#### Rules
- Rock wins over scissors.
- Paper wins over rock.
- Scissors win over paper.
""")
		
		console.print(md)
		print("\n")

		rounds = int(answers["rounds"])
		x = 0

		while x != rounds:
			questions = [{
				"type":"list",
				"name":"choice",
				"message":"Select your move",
				"choices":CHOICES
			}]

			answers = prompt(questions, style=custom_style_1)

			player_choice = answers["choice"]
			comp_choice = random.choice(CHOICES)

			console.print(f"\nYou chose [bold green]{player_choice}[/]\nComputer\'s choice was [bold red]{comp_choice}[/]")
			check_winner(player_choice, comp_choice)

			x += 1

		md = Markdown(f"""
- Your Points: {player_points}
- Computer's Points: {comp_points}
""")

		console.print(md)

		if player_points > comp_points:
			console.print("\nKudos! You won the game.", style="bold green")
		elif comp_points > player_points:
			console.print("\nHard luck! You lost the game.", style="bold red")
		else:
			console.print("\nIt is a draw... Better luck next time!", style="bold black")

		questions = [{
			"type":"confirm",
			"name":"replay",
			"message":"Would you like to play again",
			"default":True
		}]
		
		answers = prompt(questions, style=custom_style_1)

		if answers["replay"] == True:
			continue
		else:
			break

def check_winner(player_choice, comp_choice):
	global player_points, comp_points

	if (player_choice == "Rock" and comp_choice == "Scissors") or (player_choice == "Paper" and comp_choice == "Rock") or (player_choice == "Scissors" and comp_choice == "Paper"):
		player_points += 1
		console.print("\nYou win!", style="bold green")

	elif (comp_choice == "Rock" and player_choice == "Paper") or (comp_choice == "Paper" and player_choice == "Rock") or (comp_choice == "Scissors" and player_choice == "Paper"):
		comp_points += 1
		console.print("\nYou lose!", style="bold red")

	else:
		console.print("\nIt is a draw!", style="bold black")

if __name__ == '__main__':
	main()