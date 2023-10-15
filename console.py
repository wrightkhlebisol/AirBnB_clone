#!/usr/bin/python3
"""Entry point of the command interpreter
"""
import cmd

from models import base_model
from models import storage


class HBNBCommand(cmd.Cmd):
    """Implements various commands as methods
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel"
    }

    def do_quit(self, line):
        """Quit command to exit the program
        Usage: quit
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        Usage: ctrl + D
        """
        print()
        return True

    def emptyline(self):
        """Empty line + Enter should do nothing
        Usage: Empty line + Enter
        """
        return

    def do_create(self, line):
        """Creates new instance of BaseModel, save it to JSON file
        Usage: create <class name>
        Args:
            <class name>: The name of the class to create instance of
        Returns:
            None
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name not in self.__classes:
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
            <class name>: The name of the class to show
                        the string representation
            <id>: the id of the particular instance
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

        if f"{cls_name}.{id_num}" not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[f"{cls_name}.{id_num}"])
    
    def do_destroy(self, line):
        """Deletes an instance
        based on the class name and id
        Usage: delete <class name> <id>
        Args:
            <class name>: The name of the class to be deleted
            <id>: the id of the particular instance
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

        if f"{cls_name}.{id_num}" not in storage.all():
            print("** no instance found **")
            return
        
        del(storage.all()[f"{cls_name}.{id_num}"])
        storage.save()


    def postcmd(self, stop, line):
        """Program exit cleanly in response to the quit command
        """
        if stop:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
