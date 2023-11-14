#!/usr/bin/python3
''' This module is the entry point of the command
line interpreter for the program
'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
import re


class_list = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    '''This class defines the command processor
    '''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''This method exits the interpreter
        just like the EOF method does
        '''
        return True

    def do_EOF(self, line):
        '''This method exits te program if the
        user enters ctrl + D
        '''
        print()
        return True

    def emptyline(self):
        pass

    def help_quit(self):
        print("Quit command to exit the program.")

    def help_create(self):
        print("Create a new class instance.")

    def help_show(self):
        print("Prints the string representation of an instance.")

    def help_destroy(self):
        print("Deletes an instance based on class name and id.")

    def help_all(self):
        print("Prints all string representation of all instances.")

    def help_update(self):
        print("Updates an instance based on the class name and id")

    def help_count(self):
        print("Retrieves the number of instances of a class")

    def help_precmd(self):
        print("Pre-processes commands before execution")

    def do_create(self, line):
        '''This method creates new istance
        of a class parsed and an argument
        in line
        '''

        if not line:
            print("** class name missing **")
        elif line in class_list:
            instance = class_list[line]()
            storage.reload()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        '''This method prints the string
        representation of an instance
        '''

        storage.reload()
        if not line:
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in class_list:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            key = "{:s}.{:s}".format(tokens[0], tokens[1])
            all_objs = storage.all()
            if key in all_objs:
                obj = all_objs[key]
                print(obj.__str__())
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''This method deletes instances based
        on the class name and id provided
        '''

        storage.reload()
        if not line:
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in class_list:
            print("** class doesn't exist **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        else:
            key = "{:s}.{:s}".format(tokens[0], tokens[1])
            storage.reload()
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        '''This method prints the string
        representation of all instances
        '''
        storage.reload()
        instance_list = []
        new_list = []

        if not line:
            for key, value in storage.all().items():
                instance_list.append(value.__str__())
            print(instance_list)
        elif "." in line:
            line = line.strip(".")
            for key, value in storage.all().items():
                if line in key:
                    instance_list.append(value)
            print(instance_list)
        elif line in class_list:
            for key, value in storage.all().items():
                if line in key:
                    instance_list.append(value.__str__())
            print(instance_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        '''This method updates an instance based
        on the class name and id
        '''

        storage.reload()
        if not line:
            print("** class name missing **")
            return
        tokens = line.split(" ")
        if tokens[0] not in class_list:
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        instance_key = "{}.{}".format(tokens[0], tokens[1].strip('"'))
        if instance_key in storage.all():
            if len(tokens) == 4:
                for key, value in storage.all().items():
                    if instance_key == key:
                        setattr(
                                value, tokens[2].strip('"'),
                                tokens[3].strip('"')
                                )
                        storage.save()
                        break
            else:
                # Use regular expressions to extract the components
                matches = re.match(r'([a-zA-Z]+)\s([0-9a-z-]+)\s({.+})', line)
                if matches:
                    # Extract the dictionary string
                    data = matches.group(3)
                for key, value in storage.all().items():
                    if instance_key == key:
                        for keys, val in dict(eval(data)).items():
                            setattr(value, keys, val)
                        storage.save()
        else:
            print("** no instance found **")

    def do_count(self, line):
        '''This method counts the number of instances in a class
        '''
        instance = line.split()
        counts = 0
        for key, value in storage.all().items():
            if instance[0] in key:
                counts += 1
        print(counts)

    def precmd(self, line):
        '''Redefining the precmd method to pre-process the
        entry on the command prompt so that the do_functions
        can handle and execute them accordingly.
        '''

        pattern = re.compile(r'([a-zA-Z]+)\.([a-zA-z]+)\((.+)?\)')
        matches = pattern.finditer(line)
        groups = ()
        for match in matches:
            groups = match.groups()

        if groups and (groups[1] == "all" or groups[1] == "count"):
            modified_line = "{} {}{}".format(groups[1], groups[0], ".")
            return modified_line
        elif groups and (groups[1] == "show" or groups[1] == "destroy"):
            modified_line = "{} {} {}".format(
                    groups[1], groups[0], groups[2].strip('\"')
                    )
            return modified_line
        elif groups and groups[1] == "update":
            if '{' in groups[2]:
                # Find the index of the comma
                comma_index = groups[2].find(',')
                # Split the string into two parts
                arg1 = groups[2][:comma_index].strip()
                arg2 = groups[2][comma_index + 1:].strip()
                modified_line = "{} {} {} {}".format(
                        groups[1], groups[0],
                        arg1.strip('"'), arg2
                        )
            else:
                args = groups[2].split(',')
                modified_line = "{} {} {} {} {}".format(
                        groups[1], groups[0], args[0],
                        args[1].strip(), args[2].strip()
                        )
            return modified_line
        else:
            return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
