import pandas as pd
import sweetviz as sv

# Solicitar al usuario el nombre del archivo
file_path = './Resources/Alumnos.csv'

# Leer datos desde el archivo proporcionado por el usuario
if file_path.endswith('.csv'):
    df = pd.read_csv(file_path, encoding='unicode_escape')
elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
else:
    raise ValueError("Formato de archivo no compatible. Utiliza archivos .csv, .xls o .xlsx.")

# Crear el perfil de análisis exploratorio de datos (EDA)
report = sv.analyze(df)

# Generar el informe y guardarlo como archivo HTML
report.show_html('profiling.html')
