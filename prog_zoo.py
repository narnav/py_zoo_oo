from Zoo import Zoo
from helper import load, save

my_data_file='data.json'

def menu():
    print('a -add_animal')
    print('r -remove_animal')
    print('s -search_animal')
    print('p -print_all')
    print('z -show all as JSON')
    print("x - for shir")
    return input("your selection")

def main():
    zoo =Zoo()
    zoo.animals=load(my_data_file) #load data from file
    user_selection=''
    while user_selection != 'x':
        user_selection=menu()
        if user_selection =='a': zoo.add_animal(input("name?"),int(input("age")),bool( input("danger")))
        if user_selection =='r': zoo.remove_animal(zoo.search_animal( input("name?")))
        if user_selection =='s': print( zoo.search_animal(input("name?")))
        if user_selection =='z': print( zoo.get_animals_as_json_ar())
        if user_selection =='p': print( zoo)
        # x - do nothing
    
    save(zoo.get_animals_as_json_ar(),my_data_file) # save data to file

if __name__ == "__main__":
    main()