# crawldisk.py
# crawls the disc searching for files with a specific extension
# and searching within the files for certain words
#
# The usage is for a given repository, whether there are certain data structures.

import os

# ...
def get_files_of_subdirectory(rootdir, EXT_LIST):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            filepath = subdir + os.sep + file
            file_name, file_extension = os.path.splitext(file)
            if file_extension in EXT_LIST:
                # and file != 'helper.py':
                print (filepath)
    return


# returns all detected file extensions
def get_file_extension_list(rootdir):
    extlist=[] # list of detected extensions
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            # filepath = subdir + os.sep + file
            file_name, file_extension = os.path.splitext(file)
            extlist.append(file_extension)
    shortlist = list(set(extlist))
    print(shortlist)            
    return


# FLAG 
#           0: only filnames as output
#           1: show also the text
def get_files_with_strings(rootdir, EXT_LIST, stichwort, FLAG):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # print(os.path.join(subdir, file))
            filepath = subdir + os.sep + file
            file_name, file_extension = os.path.splitext(file)
            # print(file_name,' ----', file_extension)
            # if filepath.endswith(".py"):
            if file_extension in EXT_LIST:
                # and file != 'helper.py':
                with open(filepath) as f:
                    contents = f.read()
                    # print(contents)
                    if stichwort in contents:
                        
                        print('>', filepath)
                        if FLAG == 1:
                            print('------------------ NxT ------------------')
                            print(contents)
                            print('\n\n\n-------------... -----------------------\n')

def main():
    rootdir = os.getcwd() # current directory

    rootdir = '/'
    rootdir = '/Users/mac/'
    rootdir = '~/'

    EXT_LIST=['.py', '.html', '.po', '.sql', '.md', '.ini', '.json', '.subject', '.css', '.txt', '.email', '.js', '.scss','.yml']
    EXT_LIST=['.py']
    # get_files_of_subdirectory(rootdir, EXT_LIST)    
    # get_files_of_subdirectory('/Users/mac/', ['.py', '.html',])
    # get_file_extension_list('/Users/mac/Desktop')

    # stichwort = 'SECRET_KEY'
    # stichwort = 'sql'
    # stichwort = 'MAP_BASEURL'
    # stichwort = 'sqlite3'
    # stichwort = 'DATABASES'
    # stichwort = 'postgres'
    # stichwort = 'commit'        
    # stichwort = 'SELECT'
    stichwort = 'MBS'

    # get_files_with_strings(rootdir, EXT_LIST, stichwort, FLAG):
    # get_files_with_strings('/Users/mac/Desktop', ['.py'], 'SECRET_KEY', 0)

    print('FLAG 0/1')
    get_files_with_strings('/Users/mac/Desktop', ['.py'], 'MBS', 0)
    get_files_with_strings('/Users/mac/Desktop', ['.py'], 'MBS', 1)

if __name__ == "__main__":
    main()
