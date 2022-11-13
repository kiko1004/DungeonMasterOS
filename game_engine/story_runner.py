import os

from game_engine.gpt_2 import initialize
from game_engine.character import Character, NullCharacter


class StoryRunner:

    def __init__(self, adventure, mode, character):
        self.model = initialize()
        self.mode = mode
        self.adventure = adventure
        if character:
            self.character = character
        else:
            self.character = NullCharacter()

    def load(self, adventure_name):
        adventure_name = f'adventures/{adventure_name}.txt'
        with open(adventure_name, 'r') as story:
            starting_prompt = story.read()

        with open(adventure_name, 'a') as story:
            prompt = starting_prompt
            while True:
                max_length = len(prompt.split(' ')) + 70
                res = self.model(prompt, num_return_sequences=3, max_new_tokens=20)
                output = [
                    res[0]['generated_text'][len(prompt):],
                    res[1]['generated_text'][len(prompt):],
                    res[2]['generated_text'][len(prompt):]
                ]

                print(prompt)
                print('option 1:', output[0])
                print('option 2:', output[1])
                print('option 3:', output[2])
                print('enter c for custom')

                while True:
                    choice = input('Please enter your choice? 1,2,3,c')
                    if choice in ['1', '2', '3']:
                        continuation = output[int(choice) - 1]
                        prompt += continuation
                        break
                    elif choice == 'c':
                        continuation = input('Please enter custom continuation: ')
                        prompt += continuation
                        break
                    else:
                        print('Invalid choice, please try again!')

                story.write(continuation)

    def new(self):
        adventure_name = self.adventure
        starting_prompt = input('Please enter your starting prompt:')
        with open(f'adventures/{adventure_name}.txt', 'w') as story:
            story.write(starting_prompt)
        self.load(adventure_name)

    def run(self):
        if self.mode == 'new':
            self.new()
        else:
            self.load(self.adventure)
