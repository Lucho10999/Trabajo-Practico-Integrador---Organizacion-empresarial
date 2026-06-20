from datetime import datetime

# 1. BASE DE DATOS SIMULADA (2 Sectores, 2 Empleados por sector)
# Contiene los datos del diccionario de datos y las vacaciones ya tomadas (para superposición)
base_datos = {
    "Sistemas": {
        "1001": {
            "Nombre": "Juan Pérez",
            "Dias_Disponibles": 14,
            "Vacaciones_Asignadas": [("10/01/2027", "15/01/2027")] # Formato: (Inicio, Fin)
        },
        "1002": {
            "Nombre": "María López",
            "Dias_Disponibles": 21,
            "Vacaciones_Asignadas": [("01/02/2027", "10/02/2027")]
        }
    },
    "Administracion": {
        "2001": {
            "Nombre": "Carlos Gómez",
            "Dias_Disponibles": 7,
            "Vacaciones_Asignadas": [("15/03/2027", "20/03/2027")]
        },
        "2002": {
            "Nombre": "Ana Rodríguez",
            "Dias_Disponibles": 14,
            "Vacaciones_Asignadas": []
        }
    }
}

# Funciones auxiliares para el Bot (Validaciones y Lógica)
def buscar_empleado(legajo):
    """Busca al empleado por legajo en todos los sectores."""
    for sector, empleados in base_datos.items():
        if legajo in empleados:
            return sector, empleados[legajo]
    return None, None

def verificar_superposicion(sector, inicio_solicitado, fin_solicitado):
    """Verifica si las fechas se superponen con ALGUIEN DEL MISMO SECTOR (Viabilidad operativa)."""
    for legajo, datos in base_datos[sector].items():
        for inicio_asig, fin_asig in datos["Vacaciones_Asignadas"]:
            # Convertimos a objeto datetime para comparar correctamente
            i_asig = datetime.strptime(inicio_asig, "%d/%m/%Y")
            f_asig = datetime.strptime(fin_asig, "%d/%m/%Y")
            
            # Condición de superposición lógica
            if inicio_solicitado <= f_asig and fin_solicitado >= i_asig:
                return True, datos["Nombre"] # Hay superposición y devuelve con quién
    return False, ""

# 2. BUCLE PRINCIPAL DEL BOT
while True:
    print("\n" + "="*40)
    print("🤖 BOT DE GESTIÓN DE VACACIONES - MENÚ")
    print("="*40)
    print("1. Solicitar Vacaciones")
    print("2. Salir")
    
    opcion = input("Seleccione una opción (1-2): ").strip()
    
    if opcion == "1":
        print("""\n[Bot]: ¡Hola! Para iniciar el trámite, por favor ingresá tu legajo. #"2002" en el ejemplo de uso""")
        legajo_input = input("-> Legajo: ").strip() # "2002" en el ejemplo
        
        # Validación de legajo (Manejo de errores / Robustez)
        sector, empleado = buscar_empleado(legajo_input)
        if not empleado:
            print("❌ [Bot Error]: El legajo ingresado no existe en el sistema. Volviendo al menú.")
            continue
            
        print(f"🤖 [Bot]: Bienvenido/a {empleado['Nombre']} del sector {sector}.")
        print(f"🤖 [Bot]: Tu saldo disponible actual es de {empleado['Dias_Disponibles']} días.")
        
        if empleado['Dias_Disponibles'] <= 0:
            print("❌ [Bot]: No disponés de días suficientes para solicitar vacaciones. Trámite finalizado.")
            continue

        # Solicitar y validar Fecha de Inicio (Camino Infeliz controlado)
        while True:
            fecha_ini_str = input("-> Ingresá la Fecha de Inicio (DD/MM/AAAA): ").strip()
            try:
                fecha_inicio = datetime.strptime(fecha_ini_str, "%d/%m/%Y")
                break
            except ValueError:
                print("❌ [Bot Error]: Formato de fecha inválido. Recordá usar el formato DD/MM/AAAA (Ej: 05/01/2027).")

        # Solicitar y validar Fecha de Fin
        while True:
            fecha_fin_str = input("-> Ingresá la Fecha de Fin (DD/MM/AAAA): ").strip()
            try:
                fecha_fin = datetime.strptime(fecha_fin_str, "%d/%m/%Y")
                if fecha_fin < fecha_inicio:
                    print("❌ [Bot Error]: La fecha de fin no puede ser anterior a la fecha de inicio.")
                    continue
                break
            except ValueError:
                print("❌ [Bot Error]: Formato de fecha inválido. Recordá usar el formato DD/MM/AAAA.")

        # Cálculo automático de días solicitados (Diferencia de días + 1 para incluir ambos extremos)
        dias_solicitados = (fecha_fin - fecha_inicio).days + 1
        print(f"🤖 [Bot]: Estás solicitando un total de {dias_solicitados} días.")

        # --- VALIDACIÓN 1: SALDO DE DÍAS ---
        if dias_solicitados > empleado['Dias_Disponibles']:
            print(f"❌ [Bot - Solicitud Rechazada]: Saldo insuficiente. Solicitaste {dias_solicitados} días pero solo disponés de {empleado['Dias_Disponibles']}.")
            continue

        # --- VALIDACIÓN 2: SUPERPOSICIÓN / VIABILIDAD OPERATIVA ---
        hay_superposicion, con_quien = verificar_superposicion(sector, fecha_inicio, fecha_fin)
        if hay_superposicion:
            print(f"❌ [Bot - Solicitud Rechazada]: Inviabilidad operativa. Las fechas se superponen con las vacaciones ya aprobadas de {con_quien} en tu mismo sector.")
            continue

        # --- CASO POSITIVO: PRE-APROBACIÓN ---
        print("\n🟢 [Bot]: ¡Validaciones exitosas!")
        print("🤖 [Bot]: Solicitud PRE-APROBADA por el sistema.")
        print(f"🤖 [Bot]: Estado actualizado a 'Pendiente de aprobación'. Se derivó la notificación al Jefe de {sector} para el control humano final.")
        
        # Simulación de actualización en la base de datos tras el éxito
        empleado['Dias_Disponibles'] -= dias_solicitados
        empleado['Vacaciones_Asignadas'].append((fecha_ini_str, fecha_fin_str))
        print("📝 [Sistema]: Base de datos actualizada temporalmente.")

    elif opcion == "2":
        print("\n🤖 [Bot]: Gracias por utilizar el sistema de gestión de vacaciones. ¡Hasta luego!")
        break
        
    else:
        print("❌ [Bot Error]: Opción inválida. Por favor, seleccione 1 o 2.")
