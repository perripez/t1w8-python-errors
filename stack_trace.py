def function_a():
    print("Function A started")
    function_b()
    print("Function A ended")

def function_b():
    print("Function B started")
    function_c()
    print("Function B ended")

def function_c():
    print("Function C Started")
    #INtentionalError
    result =10/0
    print("FunctionC ended")

# Call the initial function
function_a()