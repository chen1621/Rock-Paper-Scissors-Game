'''Program code of Rock Paper Scissors Game'''
# Student Name: Chen Chen
# Student Number: S360496
import random
import sys


class Game():
    ''' Rock Paper Scissors Game '''

    def is_input_valid(self, user_select):
        '''Check if user's input is valid.'''
        list_choice = ["rock", "paper", "scissors", "quit"]
        user_select = user_select.lower()
        return bool(user_select.lower() in list_choice)

    def get_result(self, user_select, computer_auto):
        '''
        Compare the options of user and computer.
        Decide who is the winner.
        '''
        if user_select == computer_auto:
            return "tie"
        if user_select == "rock" and computer_auto == "paper":
            return "computer"
        if user_select == "paper" and computer_auto == "scissors":
            return "computer"
        if user_select == "scissors" and computer_auto == "rock":
            return "computer"
        return "user"

    def game_start(self):
        '''
        One point is given to the winner.
        Whoever has five points wins the game.
        '''
        user_score = 0
        computer_score = 0
        total_rounds = 0

        while user_score < 5 and computer_score < 5:
            user_select = input("Please type (rock, paper, scissors or quit):")
            user_select = user_select.lower()
            if user_select == "quit":
                print("You end the game. See you next time!")
                sys.exit()
            elif not Game.is_input_valid(self, user_select):
                print("\nWrong input. Please try again.\n")
            elif Game.is_input_valid(self, user_select):
                total_rounds += 1
                actions = ["rock", "paper", "scissors"]
                computer_auto = random.choice(actions)
                winner = Game.get_result(Game, user_select, computer_auto)
                if user_select.lower() == "quit":
                    print("You end the game. See you next time!")
                    sys.exit()
                elif winner == "tie":
                    print(f"\n-------- ROUND {total_rounds} * Tie * --------")
                    print(f"You [{user_select}] vs Computer [{computer_auto}]")
                    print(f"SCORE   {user_score}:{computer_score}\n")
                elif winner == "user":
                    user_score += 1
                    print(f"\n-------- ROUND {total_rounds} * Win * --------")
                    print(f"You [{user_select}] vs Computer [{computer_auto}]")
                    print(f"SCORE   {user_score}:{computer_score}\n")
                elif winner == "computer":
                    computer_score += 1
                    print(f"\n-------- ROUND {total_rounds} * Lose * --------")
                    print(f"You [{user_select}] vs Computer [{computer_auto}]")
                    print(f"SCORE   {user_score}:{computer_score}\n")
        if user_score > computer_score:
            print(f"\n-------- Total Round {total_rounds} * End * --------")
            print(f"You [{user_select}] vs Computer [{computer_auto}]")
            print(f"SCORE   {user_score}:{computer_score}\n")
            print("Congratulations! You win the game!\n")
        else:
            print(f"\n-------- Total Round {total_rounds} * End * --------")
            print(f"You [{user_select}] vs Computer [{computer_auto}]")
            print(f"SCORE   {user_score}:{computer_score}\n")
            print("Game Over. You lose the game!\n")
