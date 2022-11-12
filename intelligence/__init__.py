from intelligence import analysis
from intelligence import languageprocessing
from intelligence import states
from intelligence import data
from intelligence import quips
import gui

output = ""

objects = []
unknownObjects = []

currentState = states.GETTING_OBJECTS

def feed(string):
    global output
    global objects
    global unknownObjects
    global currentState

    print(currentState)

    gui.write("Loading ...", "grey50")
    gui.root.update()

    tok = languageprocessing.tokenize(string)

    if currentState == states.SEARCHING_OTHER_OBJECTS:
        if unknownObjects[0].properties["isRecyclable"] == None:
            output = "what bout is recyclable???"
            currentState == states.ASKING_IF_RECYCLABLE

        elif unknownObjects[0].properties["isCostEfficient"] == None:
            output = "what bout is cost efficient?"
            currentState == states.ASKING_IF_COST_EFFICIENT
        return 0

    if currentState == states.GETTING_OBJECTS:
        objects = languageprocessing.getNouns(string)
        unknownObjects = [languageprocessing.Item(obj[0], 1, isRecyclable=None, isCostEfficient=None) for obj in objects]

        for object in objects:
            if object[0] in data.shouldBeRecycled:
                print("NEW STATE: asking if recyclable")
                currentState = states.ASKING_IF_RECYCLABLE

                break

            if object[0] in data.shouldBeCostEfficient:
                print("NEW STATE: asking if cost efficient")
                currentState = states.ASKING_IF_COST_EFFICIENT

                break

        if currentState == states.ASKING_IF_RECYCLABLE:
            output = quips.interesting.get() + " Are the/these " + unknownObjects[0].name + " recyclable?"
            return 0

        if currentState == states.ASKING_IF_COST_EFFICIENT:
            output = quips.interesting.get() + " Are the/these " + unknownObjects[0].name + " at least reasonably priced?"
            return 0

    if currentState == states.ASKING_IF_RECYCLABLE:
        if any(substring in string for substring in data.affirmatives):
            unknownObjects[0].isRecyclable = True
        else:
            unknownObjects[0].isRecyclable = False
        currentState = states.SEARCHING_OTHER_OBJECTS
        output = quips.interesting.get()
        return 0

    if currentState == states.ASKING_IF_COST_EFFICIENT:
        if any(substring in string for substring in data.affirmatives):
            unknownObjects[0].isCostEfficient = True
        else:
            unknownObjects[0].isCostEfficient = False
        currentState = states.SEARCHING_OTHER_OBJECTS
        output = quips.interesting.get()
        return 0


def extract():
    # Get and return the global output

    global output

    return output
