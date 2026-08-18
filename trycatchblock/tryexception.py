try:
    # f = open('curruptfile.txt')
    # if(f.name=='curruptfile.txt'):
    #     raise Exception
    f = open('cu.txt')

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)

else:
    print(f.read())
    f.close()

finally:
    print("Executing Finally...")

# try:Contains code that might raise an exception.
# except FileNotFoundError: Handles the specific case where cu.txt does not exist.
# except Exception: Catches any other unexpected exception.
# else: Executes only when no exception occurs in the try block.
# finally: Always executes, whether an exception occurred or not. Commonly used for cleanup operations.