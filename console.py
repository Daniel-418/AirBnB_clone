#!/usr/bin/python3
"""Entry point for the console"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command line for the AirBnB program
    """
    prompt = '(hbnb) '

    classes = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """
        Quits the console
        """
        sys.exit(0)

    def help_quit(self):
        print("Usage: exit\nExits the application")

    def do_EOF(self, line):
        """
        Quits the console
        """
        return True

    def do_create(self, line):
        """
        Creates a class
        """
        if line == "":
            print("** class name missing **")
        else:
            if line in self.classes:
                new_class = self.classes[line]()
                storage.new(new_class)
                storage.save()
            else:
                print("** class does not exists **")

    def do_show(self, line):
        """
        Shows the string representation of an object
        """
        objects = storage.all()
        if line == "":
            print("** class name is missing **")
            return

        words = line.split()
        if words[0] not in self.classes:
            print("** class doesn't exists **")
            return

        if len(words) < 2:
            print("** instance id missing **")
            return

        object_key = "{}.{}".format(words[0], words[1])
        if object_key not in objects:
            print("** no instance found **")
            return
        instance = self.classes[words[0]](**objects[object_key])
        print(instance)


    def help_show(self):
        """
        Help for the show command
        """
        print("Usage: show [class name][id]")
        print("Shows the string representation of a specific object")

    def emptyline(self):
        pass

    def help_create(self):
        print("Usage: create [class name]\nCreates a class")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
