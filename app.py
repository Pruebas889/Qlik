from fastapi import FastAPI
import subprocess
import datetime

app = FastAPI()

@app.post("/ejecutar")
def ejecutar_script():
    hoy = datetime.datetime.now().day

    if hoy == 1:
        resultado = subprocess.run(
            ["python", r"C:\Users\jperdomolc\Videos\Qliktabs copia\qliktabs.py"],
            capture_output=True,
            text=True
        )
    else:
        resultado = subprocess.run(
            ["python", "qlik.py"],
            capture_output=True,
            text=True
        )

    return {
        "stdout": resultado.stdout,
        "stderr": resultado.stderr,
        "code": resultado.returncode
    }