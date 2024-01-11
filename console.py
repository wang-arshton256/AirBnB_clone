#!usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

the_current_classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Class for Command interpreter"""
    
    prompt = "(hbnb) "

#   HELPCREATE    
    def help_create(self):
        print('\n'.join([
            "Usage: create <class>" ,
            "\n which creates a new <classname> instance\n"]))

#   DOCREATE        
    def do_create(self, arg: str):
        args = arg.split()
        if not validate_class_name(args):
            return

        created_object = the_current_classes[args[0]]()
        created_object.save()
        print(created_object.id)

#   HELPSHOW        
    def help_show(self):
        print('\n'.join(["Usage: show <classname> <id>",
            "\n This prints a string representation of an instance\n"]))


#   DOSHOW        
    def do_show(self, arg):
        args = arg.split()

        if not validate_class_name(args, check_id=True):
            return

        the_instance_objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        required_instance = the_instance_objects.get(key, None)

        if required_instance is None:
            print("** no instance found **")
            return

        print(required_instance)

#   DOHELP    
    def do_help(self, arg):
        """gives help on cammand in the program\n"""
        return super().do_help(arg)

#   DOQUIT    
    def do_quit(self, arg):
        """Quit command for exiting the program\n"""
        return True

#   VALIDATECLASSNAME    
    def validate_class_name(args, check_id=False):
        """Checks args to validate an entered class name."""
    if len(args) < 1:
        print("** class name missing ** ")
        return False
    if args[0] not in current_classes.keys():
        print("** class doesn't exist ** ")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return
    return True

#   EOF
    def do_EOF(self, line):
        """EOF command that exits the program\n"""
        return True

#   EMPTYLINE    
    def emptyline(self):
        """Overrides empty line from executing previous command\n"""
        pass
    
    
    if __name__ == '__main__':
    HBNBCommand().cmdloop()