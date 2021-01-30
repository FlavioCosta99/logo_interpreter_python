from src.Parser import Parser

with open("input.txt", mode="r") as fh:
        contents = fh.read().lower()

print('A gerar ficheiro...')
parser = Parser()
parser.Parse(contents)
