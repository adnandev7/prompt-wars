#!/usr/bin/env python3

import random
import time
import os

class PromptWars:
    def __init__(self):
        self.ai1_score = 0
        self.ai2_score = 0
        self.round = 1
        self.max_rounds = 5
        self.ai_names = ["Synapse", "Cortex"]
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_intro(self):
        """Display the game introduction."""
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                     PROMPT WARS                     ")
        print("=" * 60)
        print("\nWelcome, Prompt Engineer!")
        print("\nIn this battle of artificial minds, you'll write prompts")
        print("that will influence two competing AI assistants:")
        print(f"\n  * {self.ai_names[0]}: The logical and precise assistant")
        print(f"  * {self.ai_names[1]}: The creative and unpredictable assistant")
        print("\nYour prompts will help one AI while confusing the other.")
        print("After 5 rounds, the AI with the highest score wins!")
        print("\nPress Enter to begin your prompt engineering challenge...")
        input()
        
    def display_status(self):
        """Display the current game status."""
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"                  ROUND {self.round} of {self.max_rounds}                  ")
        print("=" * 60)
        print(f"\n{self.ai_names[0]}'s Score: {self.ai1_score}")
        print(f"{self.ai_names[1]}'s Score: {self.ai2_score}")
        print("\n" + "-" * 60)
        
    def generate_prompt_options(self):
        """Generate three prompt options for the player to choose from."""
        prompts = [
            # Prompts that favor AI 1 (Synapse)
            [
                "Explain the logical steps to solve this mathematical problem.",
                "Analyze this data set and provide statistical insights.",
                "Define these technical terms with precision.",
                "Compare these algorithms based on efficiency metrics.",
                "Outline the systematic approach to troubleshooting this issue."
            ],
            # Prompts that favor AI 2 (Cortex)
            [
                "Create a story that incorporates these random elements.",
                "Design an unconventional solution to this everyday problem.",
                "Imagine a world where this technology evolved differently.",
                "Generate metaphors that explain this complex concept.",
                "Describe how emotions might influence this decision-making process."
            ],
            # Confusing prompts (unpredictable outcome)
            [
                "Explain quantum physics using only cooking terminology.",
                "Translate this technical document into a children's bedtime story.",
                "Describe colors to someone who can only perceive sound.",
                "Create a logical argument using only paradoxes.",
                "Write instructions that are simultaneously precise and ambiguous."
            ]
        ]
        
        # Select one prompt from each category
        return [random.choice(prompts[0]), random.choice(prompts[1]), random.choice(prompts[2])]
        
    def display_prompt_options(self, options):
        """Display the prompt options to the player."""
        print("\nChoose a prompt to send to the AIs:")
        print("\n1. " + options[0])
        print("   (Likely to favor " + self.ai_names[0] + ")")
        
        print("\n2. " + options[1])
        print("   (Likely to favor " + self.ai_names[1] + ")")
        
        print("\n3. " + options[2])
        print("   (Unpredictable outcome)")
        
    def get_player_choice(self, options):
        """Get the player's choice of prompt."""
        while True:
            try:
                choice = int(input("\nEnter your choice (1-3): "))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")
                
    def simulate_ai_responses(self, prompt_index):
        """Simulate the AIs responding to the prompt and update scores."""
        print("\nSending prompt to AIs...")
        time.sleep(1.5)
        
        print(f"\n{self.ai_names[0]} is processing...")
        time.sleep(1)
        print(f"{self.ai_names[1]} is processing...")
        time.sleep(1.5)
        
        # Determine outcome based on prompt type
        if prompt_index == 0:  # Favors AI 1
            ai1_points = random.randint(2, 4)
            ai2_points = random.randint(-2, 1)
            outcome = f"{self.ai_names[0]} provided a precise, logical response!"
        elif prompt_index == 1:  # Favors AI 2
            ai1_points = random.randint(-2, 1)
            ai2_points = random.randint(2, 4)
            outcome = f"{self.ai_names[1]} created an innovative, unexpected solution!"
        else:  # Unpredictable
            # Both AIs might gain or lose points
            ai1_points = random.randint(-3, 3)
            ai2_points = random.randint(-3, 3)
            
            if ai1_points > ai2_points:
                outcome = f"{self.ai_names[0]} managed to make sense of the confusing prompt!"
            elif ai2_points > ai1_points:
                outcome = f"{self.ai_names[1]} thrived with the creative challenge!"
            else:
                outcome = "Both AIs were equally confused by your prompt!"
        
        # Update scores
        self.ai1_score += ai1_points
        self.ai2_score += ai2_points
        
        # Ensure scores don't go below zero
        self.ai1_score = max(0, self.ai1_score)
        self.ai2_score = max(0, self.ai2_score)
        
        # Display results
        print("\n" + "-" * 60)
        print(outcome)
        print(f"\n{self.ai_names[0]} {'+' if ai1_points >= 0 else ''}{ai1_points} points")
        print(f"{self.ai_names[1]} {'+' if ai2_points >= 0 else ''}{ai2_points} points")
        print("\nPress Enter to continue...")
        input()
        
    def display_winner(self):
        """Display the game results and winner."""
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                  GAME OVER!                  ")
        print("=" * 60)
        print(f"\nFinal Scores:")
        print(f"{self.ai_names[0]}: {self.ai1_score} points")
        print(f"{self.ai_names[1]}: {self.ai2_score} points")
        
        if self.ai1_score > self.ai2_score:
            print(f"\n{self.ai_names[0]} is the winner!")
            print("\nLogic and precision prevailed in this battle of artificial minds.")
        elif self.ai2_score > self.ai1_score:
            print(f"\n{self.ai_names[1]} is the winner!")
            print("\nCreativity and adaptability won the day!")
        else:
            print("\nIt's a tie! Both AIs performed equally well.")
            print("\nA perfect balance of logic and creativity.")
            
        print("\nThank you for playing Prompt Wars!")
        print("\nPress Enter to exit...")
        input()
        
    def play_game(self):
        """Main game loop."""
        self.display_intro()
        
        while self.round <= self.max_rounds:
            self.display_status()
            options = self.generate_prompt_options()
            self.display_prompt_options(options)
            choice = self.get_player_choice(options)
            self.simulate_ai_responses(choice - 1)
            self.round += 1
            
        self.display_winner()

if __name__ == "__main__":
    game = PromptWars()
    game.play_game()
