#!/usr/bin/python3
""" Airbnb clone interpreter """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Entry point for the command interpreter for the AirBnB clone """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ command to exit the program """
        return True

    def emptyline(self):
        """ Nothing is done when an empty line is entered """
        pass

    def do_EOF(self, arg):
        """ Uses Ctrl-D (EOF) to exit the program """
        print("")
        return True

    def do_crete(self, arg):
        """ Creates a new instance of BaseModel, saves it in the JSON file """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg + "()")
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ The string representation of an instance is printed """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and saves the changes into the JSON file:(structure: [class name] [id] """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key in storage.all():
            storage.all().pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """ All string representations of instances is printed """
        args = arg.split()
        if args and args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        odj_list = []
        for key, obj in storage.all().items():
            if not args or key.split(".")[0] == args[0]:
                obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """ Updates an instance based on class name and id by adding or updating attribute:(saves changes to JSON file) """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key in storage.all():
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3].strip('"')
                setattr(instance, attr_name, attr_value)
                instance.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
