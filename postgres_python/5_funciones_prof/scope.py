#alcance variables or scope

var_global = "valor global"
print(var_global)

def scope():
    
    var_local = "var local"
    print(var_local)
    global var_global

    var_global = "new valor global"
    print(var_global)

scope()