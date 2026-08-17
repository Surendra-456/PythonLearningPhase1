def greet():
    message = "Hello"  # Local variable
    print(message)

greet()
#LEGB is the order Python follows when looking for a variable's value.
#Loca(L): Inside the current function.
#Enclosing (E): Inside the outer function (for nested functions).
#Global (G): Defined at the module (file) level.
#Built-in (B): Python's built-in names like print(), len(), max().