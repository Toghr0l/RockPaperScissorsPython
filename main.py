import colorama
from colorama import Fore, Back
import random

Options = ["rock", "paper", "scissors"]
computerScore = 0
playerScore = 0

isRunning = True
while isRunning:
    playerChoice = input("Enter your choice among (Rock, Paper, and Scissors): ").lower()
    computerChoice = random.choice(Options)
    
    # Player's win zone
    if playerChoice == "paper" and computerChoice == "rock":
        print(f"{Fore.GREEN}You won{Fore.RESET}")
        print(f"{Fore.BLUE}Player score + 1{Fore.RESET}")
        playerScore += 1
    elif playerChoice == "scissors" and computerChoice == "paper":
        print(f"{Fore.GREEN}You won{Fore.RESET}")
        print(f"{Fore.BLUE}Player score + 1{Fore.RESET}")
        playerScore += 1
    elif playerChoice == "rock" and computerChoice == "scissors":
        print(f"{Fore.GREEN}You won{Fore.RESET}")
        print(f"{Fore.BLUE}Player score + 1{Fore.RESET}")
        playerScore += 1
        
    # Computer's win zone
    elif playerChoice == "scissors" and computerChoice == "rock":
        print(f"{Fore.RED}You lost{Fore.RESET}")
        print(f"{Fore.BLUE}Computer score + 1{Fore.RESET}")
        computerScore += 1
    elif playerChoice == "paper" and computerChoice == "scissors":
        print(f"{Fore.RED}You lost{Fore.RESET}")
        print(f"{Fore.BLUE}Computer score + 1{Fore.RESET}")
        computerScore += 1
    elif playerChoice == "rock" and computerChoice == "paper":
        print(f"{Fore.RED}You lost{Fore.RESET}")
        print(f"{Fore.BLUE}Computer score + 1{Fore.RESET}")
        computerScore += 1
    
    # Draw zone
    elif playerChoice == computerChoice.lower():
        print(f"{Fore.YELLOW}Draw!{Fore.RESET}")
        print(f"{Fore.BLUE}Player score + 0{Fore.RESET}")
        print(f"{Fore.BLUE}Computer score + 0{Fore.RESET}")

    elif playerChoice == "q":
        print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
        print("-------------ScoreBord-------------")
        print(f"Player score is: {playerScore}")
        print(f"Computer score is: {computerScore}")
        print("-----------------------------------")
        print(f"{Fore.YELLOW}GitHub: https://github.com/toghr0l{Fore.RESET}")
        isRunning = False
    else:
        print("Invalid operation!")
