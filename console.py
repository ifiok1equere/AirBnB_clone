#!/usr/bin/python3
''' This module is the entry point of the command
line interpreter for the program
'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
    

class_list = {'BaseModel': BaseModel}

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

        if not line:
            for key, value in storage.all().items():
                instance_list.append(value.__str__())
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
        tokens = line.split(" ")
        if tokens[0] not in class_list:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        instance_key = "{}.{}".format(tokens[0], tokens[1])
        for key, value in storage.all().items():
            if instance_key  == key:
                setattr(value, tokens[2].strip('"'), tokens[3].strip('"'))
                storage.save()
                break
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
