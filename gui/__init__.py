import packages                      # for our UI
import settings                      # for settings, etc.
from gui import entrywithplaceholder # for its contents, which is the
                                     # EntryWithPlaceholder class
import intelligence                  # for interacting with the intelligence

# See the write function for more on this.
ctag = 1

# UI setup function - creates the variables, roots, callbacks, and widgets
# necessary to assemble the UI

def cycleIntelligence(evt=None):
    global entry

    inp = entry.get()
    write(inp, "white")
    intelligence.feed(inp)
    entry.delete("0", "end")
    write(intelligence.extract(), "lime")

def setupUI():
    global root
    global titleFrame
    global titleLabel
    global titleSlogan
    global titleQuestioningPadding
    global questioningFrame
    global questioningText
    global entry

    # Tkinter root UI object - sets up the window
    root = packages.tkinter.Tk()

    # Set the background color to the background color found in the settings and
    # set the window title to whatever the app's name is. Maybe get the icon
    # right too?
    root.config(bg=settings.BACKGROUND_COLOR)
    root.title(settings.NAME)
    root.iconbitmap("icon.ico")

    def leave(evt=None):
        root.destroy()
        exit()

    root.bind("<Escape>", leave)

    # Tkinter Frame object, to store the title bar
    titleFrame = packages.tkinter.Frame(root, bg=settings.BACKGROUND_COLOR)

    # Add the widget
    titleFrame.grid(row=1, column=1)

    # Tkinter Label object, which comprises the actual title bar
    titleLabel = packages.tkinter.Label(titleFrame,
        text=settings.NAME,
        font=settings.font(48),
        bg=settings.BACKGROUND_COLOR,
        fg=settings.FOREGROUND_COLOR
    )

    # Add the widget
    titleLabel.grid(row=1, column=1)

    # Tkinter Label object, which stores the slogan beneath the title bar
    titleSlogan = packages.tkinter.Label(titleFrame,
        text="Sustainability is hard. AI makes it easier.",
        font=settings.font(24),
        bg=settings.BACKGROUND_COLOR,
        fg=settings.FOREGROUND_COLOR
    )

    # Add the widget
    titleSlogan.grid(row=2, column=1)

    # Tkinter Label object, to add a bar between the title frame and the
    # questioning frame
    titleQuestioningPadding = packages.tkinter.Label(titleFrame,
        text="Questioning Area",
        bg="grey50",
        fg="grey50",
        width=200,
        font=settings.font(6)
    )

    # Add the widget
    titleQuestioningPadding.grid(row=3, column=1)

    # Tkinter Frame object, to store the questioning area
    questioningFrame = packages.tkinter.Frame(root,
        bg=settings.BACKGROUND_COLOR
    )

    # Add the widget
    questioningFrame.grid(row=2, column=1)

    # Tkinter Text object, to allow user connection with the intelligence.
    questioningText = packages.tkinter.Text(questioningFrame,
        width=80,
        height=15,
        font=settings.font(16),
        bg=settings.BACKGROUND_COLOR,
        fg=settings.FOREGROUND_COLOR,
        bd=1
    )

    # Disable the widget; writing can be input through the entry or by the
    # intelligence, in either case the Text shouldn't be enabled except while
    # writing.

    questioningText.config(state=packages.tkinter.DISABLED)

    # Add the widget
    questioningText.grid(row=1, column=1)

    # Customized Tkinter Entry object, to allow the user to input their content
    entry = entrywithplaceholder.EntryWithPlaceholder(questioningFrame,
        placeholder="Say something...",
        width=50,
        color="grey50"
    )

    # Add the widget
    entry.grid(row=2, column=1)

    entry.bind("<Return>", cycleIntelligence)

# Write something to the output.

def write(string, color=None):
    global questioningText
    global ctag

    # Re-enable the text to allow writing to it.
    questioningText.config(state=packages.tkinter.NORMAL)

    # Insert the text.
    questioningText.insert("end", str(string) + "\n")

    # Scroll to the bottom automatically.
    questioningText.see("end")

    if color != None:
        # Add a lime color to the text if it was specified
        questioningText.tag_add(str(ctag),
            str(ctag) + ".0",
            str(ctag * (string.count("\n") + 1)) + "." + str(len(string))
        )
        questioningText.tag_config(str(ctag), foreground=color)

    # Increment ctag to make sure that coloring works out
    ctag += (string.count("\n") + 1)

    # Disable the text again; we're done writing to it.
    questioningText.config(state=packages.tkinter.DISABLED)

# Start the UI with the tkinter.Tk.mainloop() function

def startUI(firstTimeRunning=True):
    global root
    global titleFrame
    global titleLabel
    global titleSlogan
    global titleQuestioningPadding
    global questioningFrame
    global questioningText
    global entry

    try:
        # Try to start the root

        write("Your connection with the artificial intelligence is starting.",
            "grey50",
        )
        write("Hello. My name is " + settings.AI_NAME + ". I\'m an artificial \
intelligence system designed to evaluate the sustainability\nof your \
actions. Why don't we start by talking about what you're doing? Tell me about \
what you want\nme to analyze.", "lime")

        root.mainloop()

    except NameError as error:
        # If for some reason the root variable doesn't exist, try and set up the
        # UI which should create it, then retry

        if firstTimeRunning:
            setupUI()
            startUI(firstTimeRunning=False)

        # If that fails, re-raise the error
        else:
            raise error

    except Exception as error:
        # Throw other errors

        raise error
