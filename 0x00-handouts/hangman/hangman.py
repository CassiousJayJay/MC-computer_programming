import random

def main():
    game_start = HangmanGame()
    game_start.start_game()

class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "durain", "elderberry", "fig", "grapefruit"]
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6

    def start_game(self):
        self.random.choice(self.word_list)
        self.guessed_letters = []
        self.attempts = 6

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "Please enter a single letter"
    
        if letter in self.guessed_letters:
            return "You have already guessed that letter. Try again"
    
        if letter not in self.word:
            self.attempts = 1
            return "Incorrect guess, You have {} attempts left.".format(self.attempts)
        else:
            self.guessed_letters.append(letter)

        word_progress = ''
        for char in self.word:
            if char in self.guessed_letters:
                word_progress += char + ""
            else:
                word_progress += "_"

        if "_" not in word_progress:
            return"Congratulations! You guessed the word correctly" 
        else:
            return word_progress
    
if __name__=="__main__":
    main()   