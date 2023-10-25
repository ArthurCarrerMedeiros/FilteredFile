import re

def filter_file(first_filter, second_filter):
    if first_filter[0].isdigit() or second_filter[0].isdigit():
        raise ValueError('Incorrect value, please enter a letter!')
    
    return_values = ''
    with open("names.txt", encoding='utf-8') as file:
        for line in file:
            if re.search(f'^{first_filter}.+ {second_filter}.+', line, flags=re.IGNORECASE):
                return_values += line

    with open("filtered_names.txt", 'w') as file:
        file.write(return_values)
        
if __name__ == '__main__':
    try:
        first_filter = input("Enter the first letter of the first name to filter in the file:\n")[0]
        second_filter = input("Enter the first letter of the second name to filter in the file:\n")[0]
        filter_file(first_filter, second_filter)
    except ValueError as ex:
        print(str(ex))
    except IndexError as ex2:
        print('Please enter a character!')