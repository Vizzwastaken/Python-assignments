import os

while True:
    try:
        dir_search = input('Please type in the path to a directory to search.\n')
        os.chdir(dir_search)
        dir_search = os.path.abspath('.')
        print('Searching ' + dir_search + '...')
        break
    except FileNotFoundError:
        print('Path not found. Please enter a complete path.')

for folder_name, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filename = os.path.join(folder_name, filename)
        size = os.path.getsize(filename)
        if size > 100000000:
            print(os.path.abspath(filename) + ' - ' + str(size))

print('Done.')