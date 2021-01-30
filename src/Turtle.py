import math
import webbrowser
import os


class Turtle:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.rot = -90
        self.penDown = True
        self.color = "black"
        self.file = ""

    def __repr__(self):
        return f"Turtle: ({self.x}, {self.y}, {self.rot}, {self.penDown}, {self.color}, {self.title})"

    def forward(self, value):
        startX = self.x
        startY = self.y
        rotRadian = math.radians(self.rot)
        self.x += math.cos(rotRadian) * value
        self.y += math.sin(rotRadian) * value
        if self.penDown: self.WriteToFile(startX, startY)

    def setPos(self, x, y):
        startX = self.x
        startY = self.y
        self.x = x
        self.y = y
        if self.penDown: self.WriteToFile(startX, startY)

    def setX(self, x):
        startX = self.x
        self.x = x
        if self.penDown: self.WriteToFile(startX, self.y)

    def setY(self, y):
        startY = self.y
        self.y = y
        if self.penDown: self.WriteToFile(self.x, startY)

    def home(self):
        startX = self.x
        startY = self.y
        self.x = 500
        self.y = 500
        self.rot = -90
        if self.penDown: self.WriteToFile(startX, startY)

    def WriteToFile(self, startX, startY):
        self.file += f"<line x1='{startX}' y1='{startY}' x2='{self.x}' y2='{self.y}' style='stroke: {self.color}; stroke-width:1px'/>\n"

    def save(self):
        print('Ficheiro gerado com sucesso!')
        f = open("output.svg", "w+")
        f.write(self.file)
        f.close()
        webbrowser.open_new_tab(os.path.join("output.svg"))

