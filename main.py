from random import randint
from colorama import Fore
import argparse

parser = argparse.ArgumentParser(description="Create random pattern")

parser.add_argument("-w","--width",help="Width of the pattern",required=True,type=int)

parser.add_argument("-he","--height",help="Height of the pattern",required=True,type=int)

parser.add_argument("-s","--symbol",help="Symbol of the pattern",required=False,type=str, default="X")

args = parser.parse_args()





def losuj():
    return (randint(0, 1))

class RandomPattern:
    def __init__(self, height, width,symbol):
        self.height = height
        self.width = width
        self.symbol = symbol

        self.pattern = self.create()
        self.output()

    def create(self):
        pattern = []
        for i in range(self.height):
            pattern.append([])
            for j in range(self.width):
                if losuj() == 0:
                    pattern[i].append(self.symbol)
                    continue
                pattern[i].append(" ")
        return pattern

    def output(self):
        for i in range(self.height):
            for j in range(self.width):
                print(Fore.WHITE + self.pattern[i][j], end="")
            print()

obiekt = RandomPattern(args.height, args.width,args.symbol)