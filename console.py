#!/usr/bin/python3
""" This Module contains the entry point of the command interpreter """
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import re
from models import storage


class HBNBCommand(cmd.Cmd):
    """Cmd Interpreter
    Args:
        cmd (ob): object of the module cmd
    """

    prompt = "(hbnb) "
    __ALLOWED_CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def default(self, arg):
        command_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        match = re.search(r"\.(\w+)\((.*?)\)$", arg)
        if match is not None:
            class_name = arg[: match.start()]
            command = match.group(1)
            args = match.group(2).split(", ")
            if command in command_map.keys():
                if len(args) == 0:
                    full_command = "{} {}".format(command, class_name)
                elif len(args) == 1:
                    full_command = "{} {} {}".format(command,
                                                     class_name, args[0])
                elif len(args) == 3:
                    full_command = "{} {} {} {} {}".format(command,
                                                           class_name, args[0],
                                                           args[1], args[2])
                self.onecmd(full_command)
            else:
                print("{}: does not exit".format(arg))
        else:
            return cmd.Cmd.default(self, arg)

    def check_argument(self, args, id=True):
        """Check the command line arguments"""
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif id and len(args) == 1:
            print("** instance id missing **")
            return False
        elif args[0] not in HBNBCommand.__ALLOWED_CLASSES:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel """
        args = shlex.split(arg)
        if not self.check_argument(args, False):
            return
        new_instance = HBNBCommand.__ALLOWED_CLASSES[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not self.check_argument(args):
            return
        object_dict = storage.all()
        key = args[0] + "." + args[1]
        self.print_instance(object_dict, key)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not self.check_argument(args):
            return
        object_dict = storage.all()
        key = args[0] + "." + args[1]
        self.del_instance(object_dict, key)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if len(args) == 0:
            self.prnt_all_inst(storage.all().values())
        elif not self.check_argument(args, False):
            return
        else:
            self.prnt_all_inst_by_class(storage.all().values(), args[0])

    def do_update(self, arg):
        """Updates an instance based on the class"""
        args = shlex.split(arg)
        if not self.check_argument(args):
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            key = args[0] + "." + args[1]
            obj_dict = storage.all()
            self.update_instance_attribute(obj_dict, key, args[2], args[3])

    def update_instance_attribute(self, object_dict, key, attribute_name, attribute_value):
        """Updates an attribute of an instance"""
        if key in object_dict:
            if attribute_name not in ["id", "created_at", "updated_at"]:
                if hasattr(object_dict[key], attribute_name):
                    attribute_type = type(getattr(object_dict[key], attribute_name))
                    setattr(object_dict[key], attribute_name, attribute_type(attribute_value))
                else:
                    setattr(object_dict[key], attribute_name, attribute_value)

                object_dict[key].save()
            else:
                print("** attribute can't be updated **")
        else:
            print("** no instance found **")

    def del_instance(self, object_dict, key):
        """ Deletes an instance from the object dictionary"""
        if key in object_dict:
            del object_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def prnt_all_inst(self, instances):
        """ Prints all the instances"""
        print([str(object) for object in instances])

    def prnt_all_inst_by_class(self, instances, class_name):
        """Prints the string representation of instances of
        a specific class"""
        print([str(object)
               for object in instances if object.__class__.__name__ == class_name])

    def print_instance(self, obj_dict, key):
        """
        Prints the string of an instance
        """
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_quit(self, line):
        """Quit Command to exit the program"""
        return True

    def do_EOF(self, line):
        """Ctr-D exit the program"""
        print()
        return True

    def emptyline(self):
        """Ensures that empty line + ENTER doesn't execute anything"""
        pass

    def do_count(self, arg):
        """Counts the number of instances of a specific class"""
        count = 0
        for object in storage.all().values():
            if arg == object.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
