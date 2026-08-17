def outer():
    x = "Outer Variable"  # Enclosing scope

    def inner():
        print(x)

    inner()

outer()