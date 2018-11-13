#!/usr/bin/python3
""" Contains the HBNBCommand class """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ Simple console for AirBnb """

    prompt = '(hbnb) '
    __cls_list = ["BaseModel", "User", "Place", "State",
                  "City", "Amenity", "Review"]

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

    def do_create(self, args):
        args = args.split()
        if not len(args):
            print("** class name missing **")
        else:
            dictss = {"BaseModel": BaseModel, "User": User, "Place": Place,
                      "State": State, "City": City, "Amenity": Amenity,
                      "Review": Review}
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
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in self.__cls_list:
            print("** class doesn't exist **")
        else:
            name = args[0] + "." + args[1]
            all_objs = storage.all()
            if name not in all_objs:
                print("** no instance found **")
            else:
                all_objs.pop(name)
                storage.save()

    def do_all(self, args):
        args = args.split()
        all_objs = storage.all()
        if len(args) and args[0] not in self.__cls_list:
            print("** class doesn't exist **")
        elif len(args) and args[0] in self.__cls_list:
            __list = [str(v) for k, v in all_objs.items()
                      if k.split(".")[0] == args[0]]
            print(__list)
        else:
            __list = [str(v) for v in all_objs.values()]
            print(__list)

    def do_update(self, args):
        args = args.split()
        if not len(args):
            print("** class name missing **")
        elif args[0] not in self.__cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            name = args[0] + "." + args[1]
            all_objs = storage.all()
            if name not in all_objs:
                print("** no instance found **")
            else:
                ban_attr = ["id", "create_at", "updated_at"]
                if args[2] not in ban_attr:
                    if hasattr(all_objs[name], args[2]):
                        get_type = type(getattr(all_objs[name], args[2]))
                        setattr(all_objs[name], args[2], get_type(args[3]))
                        storage.save()
                    else:
                        setattr(all_objs[name], args[2], args[3])
                        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
