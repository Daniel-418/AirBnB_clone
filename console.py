#!/usr/bin/python3
"""Entry point for the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.__init__ import storage
import sys
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Command line for the AirBnB program
    """
    prompt = '(hbnb) '

    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

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

    def do_destroy(self, line):
        """
        destroys an object
        """
        if line:
            objects = storage.all()
            arguments = line.split()

            if arguments[0] not in self.classes:
                print("** class doesn't exist **")
                return

            if len(arguments) < 2:
                print("** instance id missing **")
                return

            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

        else:
            print("** class name is missing **")

    def help_destroy(self):
        """
        Help method for the destroy command
        """
        print("Usage: destroy [class name] [id]")
        print("destroys an object")

    def do_all(self, line):
        """
        method to print all the objects in memory
        """
        objects = storage.all()
        final_list = []

        if line and line not in self.classes:
            print("** class does not exist **")
            return

        for key, obj_data in objects.items():
            obj_class_name = key.split(".")[0]
            if not line or line == obj_class_name:
                if obj_class_name in self.classes:
                    obj = self.classes[obj_class_name](**obj_data)
                    final_list.append(str(obj))
                else:
                    print("** class does not exist **")
                    return

        print(final_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        arguments = line.split() if line else []
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objects_dict = storage.all()
            search_key = arguments[0] + "." + arguments[1]
            if search_key not in objects_dict:
                print("** no instance found **")
            elif len(arguments) == 2:
                print("** attribute name missing **")
            elif len(arguments) == 3:
                print("** value missing **")
            else:
                attr_name = arguments[2]
                val_type = type(arguments[3])
                attr_value = val_type(arguments[3])
                obj_dict = objects_dict[search_key]
                value = arguments[3].strip('"').strip("'")
                obj_dict[attr_name] = val_type(value)
                storage.save()

    def help_update(self):
        """
        help method for the update class
        """
        print("Usage: update [class name] [id]" +
              "[attribute name] [attribute value]")
        print("Updates the attributes of a class")

    def help_all(self):
        """
        Help method for the all command
        """
        print("Usage: all [class name]\nor\nUsage: all")
        print("prints all the objects based on the classname or not")

    def do_show(self, line):
        """
        Shows the string representation of an object
        """
        if line == "":
            print("** class name is missing **")
            return

        objects = storage.all()
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
