# 🧩 Exportador MySQL → Excel (.xlsx)

Script en Python que permite exportar fácilmente tablas de una base de datos **MySQL** a archivos **Excel (.xlsx)**, seleccionando interactivamente qué tabla exportar.  
Los archivos se guardan automáticamente en la carpeta `/files` con nombre dinámico basado en la tabla y la fecha/hora de exportación.

---

## 🚀 Requisitos

```bash
pip install pandas pymysql python-dotenv openpyxl
```

- **Python 3.10 o superior** (recomendado: 3.12)
- Acceso a una base de datos MySQL
- Conexión local o remota habilitada

---

## ⚙️ Instalación

### 1️⃣ Clonar o copiar el proyecto

```bash
git clone https://github.com/tuusuario/convert-sql-xlsx.git
cd convert-sql-xlsx
```

O simplemente copia los archivos en una carpeta local.

### 2️⃣ Crear y activar entorno virtual

🔹 En Windows

```bash
Copiar código
python -m venv venv
venv\Scripts\activate
```

🔹 En macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

Instala todos los paquetes necesarios desde requirements.txt:

```bash
pip install -r requirements.txt
```

📦 Esto instalará automáticamente:

- pandas

- pymysql

- python-dotenv

- openpyxl (para exportar a Excel)

### 4️⃣ Configurar variables de entorno

Copia el archivo de ejemplo y actualiza tus credenciales de base de datos:

```bash
cp .env.example .env
```

Luego edita .env con tus valores:

```bash
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=tu_password
DB_NAME=tu_base_de_datos
```

⚠️ Importante: No subas tu .env a GitHub.
Está incluido en .gitignore para mantener tus credenciales seguras.

---

### ▶️ Ejecución

Con el entorno activado, ejecuta:

```bash
python main.py
```

El script:

- Se conectará a tu base de datos MySQL.

- Mostrará las tablas disponibles.

- Te pedirá escribir (o seleccionar) la tabla que deseas exportar.

- Guardará el archivo en la carpeta /excel con formato:

```
nombre_tabla_YYYY-MM-DD_HH-MM-SS.xlsx
```

### 📁 Estructura del proyecto

```bash
convert-sql-xlsx/
│
├─ .env.example
├─ .env # (tu copia personalizada)
├─ main.py # Script principal
├─ requirements.txt # Dependencias del proyecto
├─ excel/ # Carpeta donde se guardan los .xlsx
│ ├─ productos_2025-10-30_17-45-12.xlsx
│ ├─ usuarios_2025-10-30_17-46-08.xlsx
```

### 🧠 Notas

- Si obtienes el error secure-file-priv, usa este método con pymysql, ya que evita esa restricción.

- Los saltos de línea y comillas dentro de los textos no dañan el archivo Excel.

- Si el Excel no aparece, revisa permisos de escritura o asegúrate de tener activa la carpeta /excel.
