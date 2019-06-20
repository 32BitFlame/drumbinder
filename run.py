import pygame
import pynput
from sys import platform

pygame.init()
pygame.joystick.init()
disp = pygame.display.set_mode((500, 500))
objects = []
pygame.font.init()
fonts = {}
if platform.startswith("win"):
    fonts["Large"] = pygame.font.SysFont("Comic Sans MS", 30)
    fonts["Small"] = pygame.font.SysFont(None, 20)

clock = pygame.time.Clock()
def color(r,g,b):
    return((r,g,b))

def  passMacro(a,b):
    pass
class Text():
    global fonts
    global disp
    global objects

    def __init__(self, text, font, cords=(0, 0)):
        self.text = text
        self.font = fonts[font]
        self.surface = None
        self.x, self.y = cords
        objects.append(self)

    def update(self):
        print("update " + self.text)
        self.surface = self.font.render(self.text, 1, color(255, 100, 0))
        disp.blit(self.surface, (self.x, self.y))

controllers=[]
for i in range(pygame.joystick.get_count()):
    controllers.append(pygame.joystick.Joystick(i))
closed: bool = False
buttons = {}
mainControllerIndex: int = 0
started: bool = False
keystatus = {}
for controller in controllers:
    controller.init()

inputTick = 0
macroDelay = 120
macroStarted = False
startKey = "none"
left = False
right = False
InputLog = open("InputLog.inpLog", "a")
#Button 3 is left
#Button 0 is right
while not closed:
    disp.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
            InputLog.close()
    if not started:
        text1 = Text("Press right on drum", "Large", cords=(100, 200))
        for controllerIndex in range(len(controllers)):
            if controllers[controllerIndex].get_button(3):
                print("pressed")
                mainControllerIndex = controllerIndex
                started = True
                objects = []
    else:
        prevLeft = controllers[mainControllerIndex].get_button(3)
        prevRight = controllers[mainControllerIndex].get_button(0)
        if ((controllers[mainControllerIndex].get_button(3) or controllers[mainControllerIndex].get_button(0)) and (not macroStarted)):
            macroStarted = True
            if controllers[mainControllerIndex].get_button(3):

            inputLog = []
            inputTick = macroDelay

        if macroStarted:
            if(inputTick != 0):
                if(controllers[mainControllerIndex].get_button(3) and not left):
                    left = True
                if(controllers[mainControllerIndex].get_button(0) and not right):
                    right = True
                inputTick -= 1
            else:
                macroStarted = False




    for obj in objects:
        obj.update()
    pygame.display.flip()
    clock.tick(120)
