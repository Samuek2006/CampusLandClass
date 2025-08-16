import modules.corefiles as corafiles
import modules.menu as menu
import modules.utilidades as utilidades
from datetime import datetime
import time

# Archivo donde se guardarán las cuentas
DB_FILE = "data/cuentasBancarias.json"
time = utilidades.Stop()
consola = utilidades.Limpiar_consola()

# Inicializamos el archivo si no existe
corafiles.initialize_json(DB_FILE)

def crear_cuenta():
    """
    Crea una nueva cuenta bancaria y la guarda en el archivo JSON
    """
    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")
    cc = input("Ingrese el número de cédula: ")
    titular = input("Ingrese el nombre del titular: ")
    correo = input("Ingrese el correo electrónico: ")
    edad = int(input("Ingrese la edad: "))
    movil = input("Ingrese el número de celular: ")
    fijo = input("Ingrese el número de teléfono fijo: ")
    pais = input("Ingrese el país: ")
    dep = input("Ingrese el departamento: ")
    ciudad = input("Ingrese la ciudad: ")
    direccion = input("Ingrese la dirección: ")

    # Producto inicial
    idProducto = input("Ingrese un ID para el producto (ej: P001): ")
    producto = menu.menuPortafolio()
    estado = "Activa"

    nueva_cuenta = {
        numeroCuenta: {
            "CC": cc,
            "titular": titular,
            "Correo": correo,
            "Edad": edad,
            "Contacto": {
                "Movil": movil,
                "Fijo": fijo
            },
            "Ubicacion": {
                "Pais": pais,
                "Departamento": dep,
                "Ciudad": ciudad,
                "Direccion": direccion
            },
            "Productos": {
                idProducto: {
                    "NombreProducto": producto,
                    "Saldo": 0,
                    "Estado": estado,
                    "Historial": {}
                }
            }
        }
    }

    corafiles.update_json(DB_FILE, nueva_cuenta, ["cuentasBancarias"])
    print(f"✅ Cuenta {numeroCuenta} creada correctamente.")
    time
    consola



def depositar():
    """
    Permite depositar dinero en un producto de una cuenta
    """
    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")
    idProducto = input("Ingrese el ID del producto donde desea depositar: ")
    monto = float(input("Ingrese el monto a depositar: "))

    data = corafiles.read_json(DB_FILE)
    consola

    # Verificamos si existe la cuenta y el producto
    try:
        cuenta = data["cuentasBancarias"][numeroCuenta]
        producto = cuenta["Productos"][idProducto]

        # Actualizamos el saldo
        producto["Saldo"] += monto

        # Registramos en el historial
        producto["Historial"][str(datetime.now())] = f"Depósito de {monto}"

        # Guardamos cambios
        corafiles.write_json(DB_FILE, data)
        print(f"💰 Se depositaron {monto} en el producto {idProducto} de la cuenta {numeroCuenta}.")
        time
        consola

    except KeyError:
        print("⚠ La cuenta o el producto no existen.")
        time

def solicitarCredito():
    """
    Permite solicitar un crédito
    """
    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")

    # Leer la base de datos
    data = corafiles.read_json(DB_FILE)

    if numeroCuenta not in data["cuentasBancarias"]:
        print("⚠ La cuenta no existe.")
        time
        return

    consola
    print('\n¿Qué tipo de crédito deseas solicitar?')
    producto = menu.menuCreditos()

    # Datos para evaluación
    ingresosMensuales = float(input('Ingresa el total de ingresos mensuales: '))
    montoSolicitado = float(input('Ingresa el monto de crédito solicitado: '))
    plazoMeses = int(input('Ingresa el plazo (meses) para pagar: '))
    consola

    # Calculo del RCI - Relación Cuota Ingresos
    cuota = montoSolicitado / plazoMeses
    RCI = cuota / ingresosMensuales

    if RCI <= 0.4:
        print("✅ Crédito aprobado.")
        time
        consola

        # Generar un ID de producto único
        idProducto = str(len(data["cuentasBancarias"][numeroCuenta]["Productos"]) + 1)

        # Registrar el crédito en la cuenta
        data["cuentasBancarias"][numeroCuenta]["Productos"][idProducto] = {
            "NombreProducto": producto,
            "TipoProducto": "credito",
            "Saldo": montoSolicitado,
            "Estado": "Activo",
            "Historial": {
                1: {
                    "FechaMovimiento": time.strftime("%Y-%m-%d"),
                    "Valor": montoSolicitado,
                    "TipoMovimiento": "Crédito Aprobado"
                }
            }
        }

        # Guardar cambios en el archivo JSON
        corafiles.write_json(DB_FILE, data)

        print(f"Crédito {producto} creado con ID {idProducto} y saldo {montoSolicitado}")
        time
        consola

    else:
        print("❌ No eres apto para el crédito (RCI mayor a 0.4).")
        time
        consola

    input("Enter para continuar...")

def retirar():
    """
    Permite retirar dinero en un producto de una cuenta
    """

    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")
    idProducto = input("Ingrese el ID del producto donde desea retirar: ")
    monto = float(input("Ingrese el monto a retirar: "))
    time
    consola

    data = corafiles.read_json(DB_FILE)

    try:
        cuenta = data["cuentasBancarias"][numeroCuenta]
        producto = cuenta["Productos"][idProducto]

        # Validar fondos suficientes
        if producto["Saldo"] < monto:
            print("⚠ Fondos insuficientes para realizar el retiro.")
            time
            consola
            return

        # Actualizar saldo (ahora sí resta)
        producto["Saldo"] -= monto

        # Registrar en historial
        producto["Historial"][str(datetime.now())] = f"Retiro de {monto}"

        # Guardar cambios
        corafiles.write_json(DB_FILE, data)
        print(f"💸 Se retiraron {monto} del producto {idProducto} de la cuenta {numeroCuenta}.")
        time
        consola

    except KeyError:
        print("⚠ La cuenta o el producto no existen.")
        time

def pagoCuota():
    """
    Permite pagar una cuota de un crédito que tenga el usuario
    """

    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")
    idProducto = input("Ingrese el ID del crédito que desea pagar: ")
    time
    consola

    data = corafiles.read_json(DB_FILE)

    try:
        cuenta = data["cuentasBancarias"][numeroCuenta]
        producto = cuenta["Productos"][idProducto]

        # Validar que sea crédito
        if producto["Tipo"] != "Credito":
            print("⚠ El producto seleccionado no es un crédito.")
            time
            consola
            return

        # Validar que tenga saldo pendiente
        if producto["SaldoPendiente"] <= 0:
            print("✅ Este crédito ya está totalmente pagado.")
            time
            consola
            return

        # Valor de la cuota
        cuota = producto.get("Cuota", 0)
        if cuota <= 0:
            print("⚠ Este crédito no tiene definida la cuota.")
            time
            consola
            return

        # Validar saldo disponible en la cuenta de ahorros/corriente
        saldoDisponible = cuenta["SaldoTotal"]
        if saldoDisponible < cuota:
            print("⚠ Fondos insuficientes para pagar la cuota.")
            time
            consola
            return

        # Descontar la cuota del saldo de la cuenta
        cuenta["SaldoTotal"] -= cuota

        # Reducir saldo pendiente del crédito
        producto["SaldoPendiente"] -= cuota

        # Guardar movimiento
        if "Movimientos" not in producto:
            producto["Movimientos"] = []
        producto["Movimientos"].append({
            "Tipo": "Pago Cuota",
            "Monto": cuota,
            "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S")
        })

        corafiles.write_json(DB_FILE, data)

        print(f"✅ Pago de cuota realizado con éxito. Nuevo saldo pendiente: {producto['SaldoPendiente']}")
        time
        consola

    except KeyError:
        print("⚠ La cuenta o el producto no existen.")
        time

def cancelarCuenta():
    """
    Permite cancelar un producto de una cuenta
    """

    consola
    numeroCuenta = input("Ingrese el número de cuenta: ")
    idProducto = input("Ingrese el ID del producto que desea cancelar: ")
    time
    consola

    data = corafiles.read_json(DB_FILE)

    try:
        cuenta = data["cuentasBancarias"][numeroCuenta]
        producto = cuenta["Productos"][idProducto]

        # Validar fondos suficientes
        if producto["Saldo"] != 0:
            print("⚠ La cuenta tiene fondos, no puede se cancelada.")
            time
            consola
            return

        # Eliminar el producto
        del cuenta["Productos"][idProducto]

        # Guardar cambios en el JSON
        corafiles.write_json(DB_FILE, data)
        print(f"✅ El producto {idProducto} ha sido cancelado correctamente.")
        time
        consola

    except KeyError:
        print("⚠ La cuenta o el producto no existen.")
        time

