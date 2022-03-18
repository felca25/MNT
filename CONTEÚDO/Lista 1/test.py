
def get_user_input():
    name = input('Por favor, digite seu nome:\n')
    age = input('Por favor, digite sua idade:\n')
    return name, age

def write_file(file_path):
    new_file = open(file_path, 'w')
    
    name, age = get_user_input()
    new_file.write(f'name: {name}\n')
    new_file.write(f'age: {age}\n')
    
    new_file.close()
    
def read_file(filepath):
    new_file = open(filepath, 'r')
    lines = new_file.readlines()
    for line in lines:
        print(line[:-1])
    new_file.close()

def main():
    write_file('user.txt')
    read_file('user.txt')

if __name__ == '__main__':
    main()