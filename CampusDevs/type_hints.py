### Type Hints ###

# En Python no es obligatorio definir el tipo de dato de una variable.
# El intérprete lo deduce automáticamente según el valor asignado.

# Asignamos un string a la variable
my_string_variable = "My String variable"
print(my_string_variable)           # Imprime el valor: "My String variable"
print(type(my_string_variable))     # Muestra el tipo de dato: <class 'str'>

# Ahora reasignamos un número entero a la misma variable
my_string_variable = 5
print(my_string_variable)           # Imprime el valor: 5
print(type(my_string_variable))     # Muestra el tipo de dato: <class 'int'>

# -------------------------------------------------------
# Uso de Type Hints (anotaciones de tipo)
# -------------------------------------------------------

# Aquí indicamos con ": str" que la variable debería ser de tipo string
my_typed_variable: str = "My typed String variable"
print(my_typed_variable)            # Imprime el valor: "My typed String variable"
print(type(my_typed_variable))      # Tipo detectado en tiempo de ejecución: <class 'str'>

# Aunque hayamos anotado que debería ser un string, Python permite
# reasignar un valor de otro tipo (no hay restricción en tiempo de ejecución)
my_typed_variable = 5
print(my_typed_variable)            # Imprime el valor: 5
print(type(my_typed_variable))      # Tipo detectado: <class 'int'>

# NOTA: Las anotaciones de tipo (type hints) no obligan a Python a
# mantener el tipo, solo sirven como guía para el programador y
# para herramientas externas (linters, mypy, IDEs, etc.)
