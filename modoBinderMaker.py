"""
Date: 01/05/2020 - 20:36

Overview: A tool to make a MODO binder comprised of cards from a selected deck
(your colection), and exclude cards from another selected deck (your deck).

This is built to combat the fact that trade bots don't care if you thata card
is in your deck, the bot only cares that its in your collection.

Author: Bengfoyle - github.com/BenGfoyle
"""
import xml.etree.ElementTree as ET
from tkinter import *
#===============================================================================
def readDeck(file):
    deck = ET.parse(file).getroot()
    deck = [type_tag.get("Name") for type_tag in deck]
    return deck
#===============================================================================

#===============================================================================
def binderMaker():
    collection = readDeck(colIn.get())
    deckNames = deckIn.get().split(",")
    allDecks = [readDeck(deck) for deck in deckNames]
    myDeck = []
    for deck in allDecks:
        myDeck += deck
    print(myDeck)
    trades = [card for card in collection if card not in myDeck]
    with open('tradeBinder.txt', 'w') as f:
        for card in trades:
            f.write("4 %s\n" % card)
#===============================================================================

"""
GUI
"""
#Define window, name, and parameters
window = Tk()
window.title("MODO Binder Maker")
window.geometry('750x350')

#Insert text with user input text field.
colLab = Label(window, text = "Enter name of collection file (myCollection.dek)")
colLab.grid(column = 0, row = 0)
colIn = Entry(window, width = 20)
colIn.grid(column = 1, row = 0)

deckLab = Label(window, text = "Enter name(s) of decks to be removed seperated by commas (RDW.dek, kasetoEDH.dek)")
deckLab.grid(column = 0, row = 1)
deckIn = Entry(window,width = 40)
deckIn.grid(column = 1, row = 1)

#button that runs "clicked" function on click
make = Button(window, text = "Make Binder", command = binderMaker)
make.grid(column = 0, row = 4)

#loop until closed
window.mainloop()
#==============================================================================
