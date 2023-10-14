#!/usr/bin/python3
"""Entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Implements various commands as methods
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        sys.exit()

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        print()
        sys.exit()

    def emptyline(self):
        """Empty line + Enter should do nothing
        """
        sys.exit()

    def postcmd(self, stop, line):
        """Program exit cleanly in response to the quit command
        """
        if stop:
            return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
