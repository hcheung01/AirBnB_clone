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
    dummy_list = []

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
        """ Defines the contents of the help_create
        """
        print()
        print("Creates a new instance of <class-name>, ", end='')
        print("prints the id of instance, and ", end='')
        print("saves the instance to the json file.")
        print()
        print("Valid Class Names: {}".format(self.__cls_list))
        print("Usage: (hbnb) create <valid class name>")
        print()
        print("Possible errors that can print:")
        print("**class name missing **: ", end='')
        print("prints when a class name is not given to create")
        print("** class doesn't exist **:", end='')
        print(" prints when an invalid class name is given to create")
        print()

    def do_create(self, args):
        """Creates a new instance of <class name> and <id>,
            prints the id of instance, and
            saves the instance to the json file.
        Args:
            args: arguments given to `create`

        Usage:
            (hbnb) create <valid class name>
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
        """prints the string representation of an instance
            based on the class name and id
        Args:
            args: arguments given to 'show'
        Description:
            shows a specific instance on the stdout
        Usage:
            show <class name> <id>
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

    def help_show(self):
        """ Statements that print when help is called on show
        """
        print()
        print("prints the string representation of an ", end='')
        print("instance based on the class name and id")
        print()
        print("Valid Class Names: {}".format(self.__cls_list))
        print("Usage: (hbnb) show <class name> <valid id>")
        print()
        print("Possible errors that can print:")
        print("** class name missing **", end='')
        print(": prints when a class name is not given to show")
        print("** class doesn't exist **", end='')
        print(": prints when an invalid class name is given")
        print("** instance id missing **", end='')
        print(": prints if the id wasn't typed in after a valid class name")
        print("** no instance found **", end='')
        print(": prints when a bad ID is typed after a valid class name")
        print()

    def do_destroy(self, args):
        """
        Deletes an instance based on 'class name' and 'id'.
        Saves the deletion to the json file.

        Args:
            args: input given to 'destroy'
        Usage:
            (hbnb) destroy <class name> <id>
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

    def help_destroy(self):
        """ Defines the statements printing on stdout
            when "help destroy is called
        """
        print()
        print("Deletes an instance based on <class name> and <id>", end='')
        print(". Saves the deletion to the json file.")
        print()
        print("Valid Class Names: {}".format(self.__cls_list))
        print("Usage: (hbnb) destroy <class name> <id>")
        print()
        print("Common errors that can print:")
        print("** class name missing **: ", end='')
        print("e.g (hbnb) destroy")
        print("** class doesn't exist **: ", end='')
        print("prints when an invalid class name was given to destroy")
        print("** instance id missing **: ", end='')
        print("prints when an ID was not typed after a valid class name")
        print("** no instance found **: ", end='')
        print("when an instance of a valid class name doesn't exist for id")
        print()

    def do_all(self, args):
        """Print a list of instances(string representations) that match
           the class name. If a class name wasn't provided, it prints all
           instances in the json file
        Args:
            args: arguments given to `all`
        Usage:
            all --Shows everything in the json file
            all <Class Name> -- Shows only certain instances
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
                    self.dummy_list = inst_list.copy()
                    if len(inst_list) == 0:
                        break
                    else:
                        print([str(item) for item in inst_list])
                        break

            error += 1

    def help_all(self):
        """ Defines the statements that print when
            `help all` is called
        """
        print()
        print("Print a list of instances(string representations)", end='')
        print(" that match the class name.", end='')
        print(" If a class name wasn't provided, it prints", end='')
        print(" all instances in the json file")
        print()
        print("Usage:")
        print("Valid Class Names: {}".format(self.__cls_list))
        print("(hbnb) all......prints all instances in the json file")
        print("(hbnb) all <valid class name>....prints instances of", end='')
        print(" that class")
        print()
        print("Common errors:")
        print("** class doesn't exist **: ", end='')
        print(" prints when an invalid class name was given to all")
        print()

    def do_update(self, args):
        """
        Updates an instance of 'class name' and 'id' with an attribute
        and value. Saves the change to the json file.

        Args:
            args: arguments given to 'update'
        Description:
            updates existing attributes or adds a new attribute to the
            instance
        Usage:
            (hbnb) update <class name> <id> <attribute> <value>
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

    def help_update(self):
        """
        Defines the statements that print when `help update` is called
        """
        print()
        print("Updates an instance of <class name> and <id>", end='')
        print(" with an attribute and value", end='')
        print(". Saves the change to the json file.")
        print()
        print("You cannot update 'id', 'created_at', 'updated_at'")
        print("The command ignores everything after the first ", end='')
        print("attribute-value pair")
        print()
        print("Valid Class Names: {}".format(self.__cls_list))
        print("Usage: (hbnb) update <class name> <id> <attribute> <value>")
        print()
        print("Common errors that can print:")
        print("** class name missing **: ", end='')
        print("e.g (hbnb) update")
        print("** class doesn't exist **: ", end='')
        print("prints when an invalid class name was given to update")
        print("** instance id missing **: ", end='')
        print("prints when an ID was not typed after a valid class name")
        print("** no instance found **: ", end='')
        print("when an instance of a valid class name doesn't exist for id")
        print("** attribute name missing **: ", end='')
        print("prints when an attribute name wasn't typed in after id")
        print("** value missing **: ", end='')
        print("prints when the value wasn't typed after a valid attribute")
        print()

    def default(self, text):
        """Runs when input to the console doesn't match any command

        Args:
            text: input received from stdin
        Description:
            Runs the specified command by parsing the text for certain
            characters
        Return:
            The correct command that was defined previously
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
        clsName_func_list = text.split('.')

        if clsName_func_list[1] == 'all()':
            return self.do_all(clsName_func_list[0])
        elif clsName_func_list[1] == 'count()':
            storage_keys = storage.all().keys()
            count = 0
            for key in storage_keys:
                if key.split('.')[0] == clsName_func_list[0]:
                    count += 1
            print(count)
        elif "show" in clsName_func_list[1]:
            full_show = clsName_func_list[1]
            show_list = list(full_show)
            for i in range(len(show_list)):
                if show_list[i] in ('(', ')'):
                    show_list[i] = " "
                if show_list[i] == '"':
                    show_list[i] = ""
            norm_show = ''.join(show_list)
            string_id = norm_show.split(" ")[1]
            cls_name_with_id = clsName_func_list[0] + ' ' + string_id
            return self.do_show(cls_name_with_id)
        elif "destroy" in clsName_func_list[1]:
            full_destroy = clsName_func_list[1]
            destroy_list = list(full_destroy)
            for i in range(len(destroy_list)):
                if destroy_list[i] in ('(', ')'):
                    destroy_list[i] = " "
                if destroy_list[i] == '"':
                    destroy_list[i] = ""
            norm_destroy = ''.join(destroy_list)
            string_id = norm_destroy.split(" ")[1]
            cls_name_with_id = clsName_func_list[0] + ' ' + string_id
            return self.do_destroy(cls_name_with_id)
        elif "update" in clsName_func_list[1]:
            full_update = clsName_func_list[1]
            update_list = list(full_update)
            for i in range(len(update_list)):
                if update_list[i] in ('(', ')'):
                    update_list[i] = " "
                if update_list[i] == '"':
                    update_list[i] = ""
                if update_list[i] == ',':
                    update_list[i] = ""
            norm_update = ''.join(update_list)
            update_remove = norm_update.split(' ')[1:]
            cls_name_add = clsName_func_list[0] + ' ' + ' '.join(update_remove)
            return self.do_update(cls_name_add)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
