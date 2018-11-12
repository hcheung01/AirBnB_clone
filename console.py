#!/usr/bin/python3
""" Contains the HBNBCommand class """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Simple console for AirBnb """

    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
