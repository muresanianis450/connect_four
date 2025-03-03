from logging import exception

from connect_four.ui.ui import UI
from connect_four.ui.gui import ConnectFourGUI as GUI, main as gui_main
from connect_four.tests.tests import TestConnectFourApp
import unittest

if __name__ == '__main__':
    try:
        print("Welcome to the Connect Four Game, before we start")
        print("Do you want to test the game?")
        while True:
            choice = input("1. Yes\n2. No\n")
            if choice == '1':
                unittest.main(exit=False)
            break
    except Exception as e:
        print(exception(e))

    try:
        print("Do you want to start:")
        print("1. UI\n2. GUI")
        choice = input()
        while True :
            if choice == '1':
                ui = UI()
                ui.run()
                break
            elif choice == '2':
                gui_main()
            else:
                raise ValueError("Invalid choice")
    except ValueError as e:
        print(exception(e))