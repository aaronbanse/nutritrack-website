'''
USAGE

Make sure to be in a virtual environment in which pandas is installed prior to running any command.

In the command line, run "python command_line.py [command]".

Currently implemented commands:
--list [category] : list out descriptions of all items in the given category.
--healthfacts [description] : list out nutrition facts for a specific food item, identified by description.

'''

import sys
from ProductionCode.datasource import DataSource

def main():
    ds = DataSource()
    args=sys.argv[1:]

    # parse arguments
    if len(args) < 1:
        print("No command given")
    elif args[0] == "--list":
        if len(args) < 2:
            print("No category given")
        else:
            category = args[1]
            items = ds.fromCategoryGetTypes(category=category)
            for item in items:
                print(item)
    elif args[0] == "--healthfacts":
        if len(args) < 2:
            print("No description given")
        else:
            labels, data = ds.fromDescriptionGetNutrition(args[1])
            if len(data) > 0:
                for i in range(len(labels)):
                    print(labels[i] + ": " + data[i])
            else:
                print("No food named {} found.".format(args[1]))
                
    else:
        print("No command \""+ args[0] +"\"")
        

if __name__ == "__main__":
    main()
