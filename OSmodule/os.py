import os

# os module contents observed in this environment:
#
# Categories:
# - File and directory operations:
#   listdir, mkdir, makedirs, remove, rename, walk, scandir, etc.
#
# - Path utilities:
#   path, sep, altsep, curdir, pardir, pathsep
#
# - Environment variables:
#   environ, getenv, putenv, unsetenv
#
# - Process management:
#   getpid, getppid, system, popen, spawnv, spawnve
#
# - File descriptor operations:
#   open, close, read, write, dup, dup2, fsync
#
# - Permission constants:
#   F_OK, R_OK, W_OK, X_OK
#
# - File open flags:
#   O_RDONLY, O_WRONLY, O_RDWR, O_CREAT, O_TRUNC, etc.
#
# - Internal/private members:
#   Names beginning with '_' are generally implementation details.
#
# - Windows-specific items detected:
#   startfile, add_dll_directory, O_BINARY,
#   O_NOINHERIT, listdrives, listvolumes, listmounts

print(dir(os))

#to see current working directory
print(os.getcwd())
#change directory
os.chdir(r'C:\Python')
print(os.getcwd())
#change directory see all files in cwd
print(os.listdir())

# os.mkdir() creates only the last directory; os.makedirs() creates all missing parent directories in the path.
# os.mkdir('OS-Demo-1')
# os.makedirs('OS-Demo-2/Sub-Dir-1')

#os.rmdir() removes one empty directory, while os.removedirs() removes the specified empty directory and keeps removing its empty parent directories recursively.
# os.rmdir('OS-Demo-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')

#Renaming the existing file rename(existing folder_filename,newfile_foldername)
# os.rename('Disctionery','Distionery')

#read the file
#os.stat(r'\Distionery\dictionery.py')
os.stat(r'OSmodule\os.py')



