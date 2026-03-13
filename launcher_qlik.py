import datetime
import subprocess
import os

base_path = r"C:\Users\jperdomolc\Pictures\Qlik"

try:
    # 🔴 SOLO PARA PRUEBAS - Simular que es día 1
    # Comenta esta línea después de las pruebas
    hoy = 1  # Forzar día 1 para prueba
    
    # Descomenta esta línea para producción
    # hoy = datetime.datetime.now().day
    
    if hoy == 1:
        print("Es día 1 → Ejecutando cambio de mes...")
        subprocess.run([
            "python",
            r"C:\Users\jperdomolc\Videos\Qliktabs copia\qliktabs.py"
        ])
    else:
        print("Proceso normal diario...")
        subprocess.run([
            "python",
            os.path.join(base_path, "qlik.py")
        ])
        
except Exception as e:
    print(f"Error: {e}")
    print("Fallo al ejecutar el script")