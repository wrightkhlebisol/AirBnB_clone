#!/usr/bin/python3
"""Entry point of the command interpreter
"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Implements various commands as methods
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
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

        new_instance = eval(f"{cls_name}")()
        print(new_instance.id)

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

        if cls_name not in self.__classes:
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

        if cls_name not in self.__classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        id_num = args[1]

        if f"{cls_name}.{id_num}" not in storage.all():
            print("** no instance found **")
            return

        del (storage.all()[f"{cls_name}.{id_num}"])

        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all <class name> or all
        Args:
            <class name>: The class name
        Returns:
            None
        """
        args = line.split()

        if len(args) == 0:
            print([str(v) for v in storage.all().values()])
            return

        cls_name = args[0]

        if cls_name not in self.__classes:
            print("** class doesn't exist **")
            return

        print([str(v) for k, v in storage.all().items()
               if k.startswith(cls_name)])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Args:
            <class name>: The class name
            <id>: the class name id
            <attribute name>: the class attribute name
            "<attribute value>": the class attribute value
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

        if len(args) == 1:
            print("** instance id missing **")
            return

        id_num = args[1]

        if f"{cls_name}.{id_num}" not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        obj_id = args[1]
        obj_key = cls_name + "." + obj_id
        obj = storage.all()[obj_key]

        attr_name = args[2]
        attr_value = args[3]

        if attr_value[0] == '"':
            attr_value = attr_value[1:-1]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            if attr_type in [str, float, int]:
                attr_value = attr_type(attr_value)
                setattr(obj, attr_name, attr_value)
        else:
            setattr(obj, attr_name, attr_value)
        storage.save()

    def default(self, line):
        """ Retrieves all instances of a class
            Retrieves the number of instances of a class
            Retrieves an instance based on its ID
            Destroys an instance based on its ID
            Updates an instance based on its ID
            Updates an instance based on it's ID with a dict

        Usage:  
            <class name>.all()
            <class name>.count()
            <class name>.show(<id>)
            <class name>.destroy(<id>)
            <class name>.update(<id>, <attribute name>, <attribute value>)
            <class name>.update(<id>, <dictionary representation>)

        Args:
                <class name>: The class name
                all(): count command
                count(): count command
        Returns:
            None
        """
        args = line.split('.')

        cls_name = args[0]
        cls_cmd = args[1]

        if cls_name in self.__classes:
            if cls_cmd == "all()":
                self.do_all(cls_name)
            elif cls_cmd == "count()":
                _list = [v for k, v in storage.all().items()
                         if k.startswith(cls_name)]
                print(len(_list))

    def postcmd(self, stop, line):
        """Program exit cleanly in response to the quit command
        """
        if stop:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
