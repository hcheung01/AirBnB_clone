#!/usr/bin/python3
"""
Contains the HBNBCommand class
"""
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
        Description:
            quit the console
        Returns:
            bool: True: exits the command loop
        """

        return True

    do_EOF = do_quit

    def help_quit(self):
        """help method

        Args:
            na
        Description:
            help command for quitting console
        Return:
            na
        """

        print("Quit command to exit the program")

    def help_EOF(self):
        """help method

        Args:
            na
        Description:
            help commad for end of file
        Return:
            na
        """

        print("Quit command to exit the program")

    def emptyline(self):
        """empty line or input
        """

        pass

    def do_create(self, args):
        """create instance method

        Args:
            args: cmdline input
        Description:
            create new instance with id and datetime
        Return:
            na
        """

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
        """show method

        Args:
            args: cmdline input
        Description:
            show specific instance with id number
        Return:
            na
        """

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
        """delete method

        Args:
            args: cmdline input
        Description:
            delete instance and update JSON
        Return:
            na
        """

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
        """all method

        Args:
            args: cmdline input
        Description:
            show all instances
        Return:
            na
        """

        args = args.split()
        all_objs = storage.all()
        if len(args) and args[0] not in self.__cls_list or not all_objs:
            print("** class doesn't exist **")
        elif len(args) and args[0] in self.__cls_list:
            __list = [str(v) for k, v in all_objs.items()
                      if k.split(".")[0] == args[0]]
            print(__list)
        else:
            __list = [str(v) for v in all_objs.values()]
            print(__list)

    def do_update(self, args):
        """Update Method
        Args:
            args: cmd line args
        Description:
            update or add class attributes
        Return:
            na
        """

        args = args.split()
        all_objs = storage.all()

        error = 0
        for i in range(4):
            try:
                args[i]
            except:
                if error == 0:
                    print("** class name missing **")
                elif error == 1:
                    print("** instance id missing **")
                elif error == 2:
                    print("** attribute name missing **")
                else:
                    print("** value missing **")
                break
            if i == 0:
                if args[i] not in self.__cls_list:
                    print("** class doesn't exist **")
                    break
            elif i == 1:
                name = args[0] + "." + args[1]
                if name not in all_objs.keys():
                    print("** no instance found **")
                    break
            elif i == 2:
                pass
            else:
                ban_attr = ["id", "create_at", "updated_at"]
                if args[2] not in ban_attr:
                    if hasattr(all_objs[name], args[2]):
                        get_type = type(getattr(all_objs[name], args[2]))
                        try:
                            args[3] = get_type(args[3])
                            setattr(all_objs[name], args[2], get_type(args[3]))
                            storage.save()
                        except:
                            pass
            if i < 3:
                error += 1

    def default(self, text):
        """default method

        Args:
            text: cmdline input
        Description:
            show text in dictionary mapping
        Return:
            na
        """

        text_maps = {
            'User.all()': 'User',
            'BaseModel.all()': 'BaseModel',
            'State.all()': 'State',
            'City.all()': 'City',
            'Amenity.all()': 'Amenity',
            'Place.all()': 'Place',
            'Review.all()': 'Review'
        }
        if text in text_maps.keys():
            return self.do_all(text_maps[text])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
