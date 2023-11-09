#!/usr/bin/python3
''' This module is the entry point of the command
line interpreter for the program
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''This class defines the command processor
    '''

    prompt = "(hbnb) "

    def do_quit(self, line):
        '''This method exits the interpreter
        just like the EOF method does'''

        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        '''This method exits te program if the
        user enters ctrl + D'''

        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
