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

    def help_create(self):
        print("""Creates a new instance of <class-name>
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
            Usage: show <class name> <id>
        Return:
            na
        """

        args = args.split()
        error = 0
        for i in range(2):
            try:
                args[i]
            except:
                if error == 0:
                    print("** class name missing **")
                    break
                else:
                    print("** instance id missing **")
                    break
            if i == 0:
                if args[i] not in self.__cls_list:
                    print("** class doesn't exist **")
                    break
            else:
                key = args[0] + "." + args[1]
                obj_dict = storage.all()
                if key not in obj_dict.keys():
                    print("** no instance found **")
                else:
                    print(obj_dict[key])
            error += 1

    def do_destroy(self, args):
        """delete method

        Args:
            args: cmdline input
        Description:
            delete instance and update JSON
            Usage: destroy <class name> <id>
        Return:
            na
        """

        args = args.split()
        error = 0
        for i in range(2):
            try:
                args[i]
            except:
                if error == 0:
                    print("** class name missing **")
                    break
                else:
                    print("** instance id missing **")
                    break
            if i == 0:
                if args[i] not in self.__cls_list:
                    print("** class doesn't exist **")
                    break
            else:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                if key not in all_objs.keys():
                    print("** no instance found **")
                    break
                else:
                    all_objs.pop(key)
                    storage.save()
            error += 1

    def do_all(self, args):
        """all method

        Args:
            args: cmdline input
        Description:
            show all instances
        Usage:
            all --Shows everything in the json file
            all <Class Name> -- Shows only certain instances
        Return:
            na
        """
        args = args.split()
        all_objs = storage.all()
        error = 0
        for i in range(2):
            try:
                args[i]
            except:
                if error == 0:
                    if len(all_objs) == 0:
                        break
                    else:
                        print([str(v) for v in all_objs.values()])
                        break
            if i == 0:
                if args[i] not in self.__cls_list:
                    print("** class doesn't exist **")
                    break
                else:
                    inst_list = []
                    [inst_list.append(v) for k, v in all_objs.items()
                        if k.split(".")[0] == args[0]]
                    if len(inst_list) == 0:
                        break
                    else:
                        print([str(item) for item in inst_list])
                        break

            error += 1

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
                            args[3] = args[3].strip("'")
                            setattr(all_objs[name], args[2],
                                    get_type(args[3].strip('"')))
                            storage.save()
                        except:
                            pass
                    else:
                        args[3] = args[3].strip("'")
                        setattr(all_objs[name], args[2], args[3].strip('"'))
                        storage.save()
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
