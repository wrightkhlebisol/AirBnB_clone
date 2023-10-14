#!/usr/bin/python3
"""Entry point of the command interpreter
"""
import cmd
import sys

from models import base_model


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

    def do_create(self, line):
        """Creates new instance of BaseModel, save it to JSON file
        Usage: create <class name>
        Args:
            class_name: The name of the class to create instance of
        Returns:
            None
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if not hasattr(base_model, cls_name):
            print("** class doesn't exist **")
            return

        cls_obj = getattr(base_model, cls_name)
        model = cls_obj()
        model.save()
        print(model.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        Usage: show <class name> <id>
        Args:
            class_name: The name of the class to show
                        the string representation
        Returns:
            None
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if not hasattr(base_model, cls_name):
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        id_num = args[1]

        cls_obj = getattr(base_model, cls_name)
        model = getattr(cls_obj, id_num)

        if model is None:
            print("** no instance found **")
            return

        print(model)


    def postcmd(self, stop, line):
        """Program exit cleanly in response to the quit command
        """
        if stop:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()