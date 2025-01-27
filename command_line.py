'''
USAGE

In the command line, run "python command_line.py [command]".

Make sure to be in a virtual environment in which pandas is installed prior to running the command.

Currently implemented commands:
--list [category] : list out descriptions of all items in the given category.
--healthfacts [description] : list out nutrition facts for a specific food item, identified by description.

'''

import sys
from ProductionCode.get_food_data import fetch_category
from ProductionCode.get_food_data import health_facts

def main():
    args=sys.argv[1:]

    # parse arguments
    if len(args) < 1:
        print("No command given")
    elif args[0] == "--list":
        if len(args) < 2:
            print("No category given")
        else:
            items=list(fetch_category(args[1]))
            for item in items:
                print(item)
    elif args[0] == "--healthfacts":
        if len(args) < 2:
            print("No description given")
        else:
            facts=health_facts(args[1])
            labels=facts.columns.to_list()
            values=facts.iloc[0].tolist()
            for i in range(len(labels)):
                print(labels[i][5:] + ": " + str(values[i]))
                
    else:
        print("No command \""+ args[0] +"\"")
        

if __name__ == "__main__":
    main()
