from gpt_2 import initialize
import os
from character import Character, NullCharacter


class StoryRunner:

    def __init__(self, character = None):
        self.model = initialize()
        if character:
            self.character = character
        else:
            self.character = NullCharacter()

    def load(self, adventure_name):
        adventure_name = f'adventures/{adventure_name}'
        with open(adventure_name, 'r') as story:
            starting_prompt = story.read()

        with open(adventure_name, 'a') as story:
            prompt = starting_prompt
            while True:
                max_length = len(prompt.split(' ')) + 70
                res = self.model(prompt, max_length=max_length, num_return_sequences=3)
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
        adventure_name = input('Please name your adventure:')
        starting_prompt = input('Please enter your starting prompt:')
        with open(f'adventures/{adventure_name}', 'w') as story:
            story.write(starting_prompt)
        self.load(adventure_name)





