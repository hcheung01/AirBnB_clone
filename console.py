#!/usr/bin/python3
""" Contains the HBNBCommand class """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from sys import argv
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Simple console for AirBnb """

    prompt = '(hbnb) '
    __cls_list = ["BaseModel"]

    def do_quit(self, line):
        """ Stops the command loop

        Args:
            line: text gotten from stdin

        Returns:
            bool: True: exits the command loop
        """
        return True

    # handles EOF to quit the console
    do_EOF = do_quit

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    # 7
    def do_create(self, args):
        args = args.split()
        if not len(args):
            print("** class name missing **")
        else:
            dictss = {"BaseModel": BaseModel}
            if args[0] in dictss.keys():
                new = dictss[args[0]]()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        args = args.split()
        if not len(args):
            print("** class name missing **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                name = args[0] + "." + args[1]
                all_objs = storage.all()
                if name in all_objs:
                    print(all_objs[name])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        args = args.split()
        if not len(args):
            print("** class name missing **")
        elif args[0] not in self.__cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            name = args[0] + "." + args[1]
            all_objs = storage.all()
            all_objs.pop(name)
            storage.save()

    def do_all(self, args):
        n_list = []
        args = args.split()
        all_objs = storage.all()
        for v in all_objs.values():
            n_list.append(str(v))
        print(n_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
