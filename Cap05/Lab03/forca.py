# Author: Pedro Henrique Correa Mota da Silva

import random


class Hangman():

    def __init__(self):
        self.getWord()
        self.wrong_letters = []
        self.right_letters = []
        self.mask = []
        self.hits = 0

        for i in self.word:
            self.mask.append('_')

        self.drawBoard()

    def getWord(self):

        with open('palavras.txt', 'r') as file:
            words = file.readlines()
            self.word = words[random.randint(0, len(words)-1)].strip()

    def drawBoard(self):

        if len(self.wrong_letters) == 0:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
                |
                |
                |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 1:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 2:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 3:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 4:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 5:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''')
        elif len(self.wrong_letters) == 6:
            print('''
            >>>>>>>>>>Hangman<<<<<<<<<<


            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            ''')

    def run(self):

        while True:
            print(str(len(self.wrong_letters)))
            print('Palavra: ', end='')
            [print(x, end='') for x in self.mask]
            print('')

            print('Letras erradas: ')
            [print(wrong) for wrong in self.wrong_letters]

            print('Letras Corretas: ')
            [print(right) for right in self.right_letters]

            letter = input('Digite uma letra: ')

            if len(letter) != 1:
                print('Letra inválida')
            else:
                if letter in self.wrong_letters or letter in self.right_letters:
                    print('Essa letra já foi escolhida')
                else:
                    if letter in self.word:
                        pos = [pos for pos, char in enumerate(
                            self.word) if char == letter]

                        self.hits += len(pos)

                        for index in pos:
                            self.mask.pop(index)
                            self.mask.insert(index, letter)

                        self.right_letters.append(letter)
                    else:
                        self.wrong_letters.append(letter)

            self.drawBoard()

            if(len(self.word) == self.hits):
                print('Parabéns! Você venceu!!')
                print('Foi bom jogar com você! Agora vá estudar!')
                break
            elif len(self.wrong_letters) == 6:
                self.drawBoard()
                print('Game Over! Você perdeu.')
                print('A palavra era ' + self.word)
                print('Foi bom jogar com você! Agora vá estudar!')
                break


jogo = Hangman()
jogo.run()
