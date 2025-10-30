import os
import pymysql
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from tkinter import Tk, simpledialog, messagebox

# ==== CARGAR VARIABLES DE ENTORNO ====
load_dotenv()

config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASS"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": "utf8mb4"
}

try:
    conn = pymysql.connect(**config)
    print("✅ Conexión exitosa a MySQL")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tablas = [t[0] for t in cursor.fetchall()]

    if not tablas:
        messagebox.showerror("Error", "No se encontraron tablas en la base de datos.")
        conn.close()
        exit()

    Tk().withdraw()
    tabla = simpledialog.askstring(
        "Seleccionar tabla",
        f"Tablas disponibles:\n\n{',\n '.join(tablas)}\n\nEscribe el nombre exacto de la tabla a exportar:"
    )

    if tabla not in tablas:
        messagebox.showerror("Error", f"La tabla '{tabla}' no existe en la base.")
        conn.close()
        exit()

    query = f"SELECT * FROM `{tabla}`;"
    df = pd.read_sql(query, conn)

    if df.empty:
        messagebox.showinfo("Información", f"La tabla '{tabla}' está vacía.")
    else:
        # Carpeta de exportación
        export_dir = os.path.join(os.getcwd(), "files")
        os.makedirs(export_dir, exist_ok=True)
        
        # Nombre de archivo dinámico
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{tabla}_{timestamp}.xlsx"
        filepath = os.path.join(export_dir, filename)
        
        # Exportar
        df.to_excel(filepath, index=False)
        messagebox.showinfo("Éxito", f"✅ Exportación completada:\n\n{filepath}")
        print(f"Archivo exportado: {filepath}")

except pymysql.MySQLError as e:
    messagebox.showerror("Error MySQL", str(e))
    print("❌ Error MySQL:", e)

finally:
    if 'conn' in locals() and conn.open:
        conn.close()
