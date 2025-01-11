import tkinter as tk
from tkinter import ttk

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Tipos de Nubes")

# --- Diccionario con la descripción de cada tipo de nube ---

clouds_info = {
    "Cirrus": (
        "Los cirros son nubes finas y delicadas que aparecen a gran altitud "
        "(generalmente por encima de los 6000 m). Están compuestos casi en su "
        "totalidad por cristales de hielo debido a las bajas temperaturas a esas "
        "alturas. Suelen presentarse en forma de filamentos o mechones y, con "
        "frecuencia, muestran un aspecto sedoso o fibroso.\n\n"
        
        "Los cirros pueden indicar un cambio de tiempo inminente, especialmente "
        "si se van haciendo más numerosos o se unen con otras nubes de tipo alto. "
        "Cuando aparecen solos y dispersos, a menudo se asocian con condiciones "
        "estables. Por su forma ligera y la escasa densidad, no producen "
        "precipitación que alcance el suelo, aunque pueden generar un efecto "
        "halo alrededor del sol o de la luna al refractar la luz sobre sus "
        "cristales de hielo.\n\n"

        "Puntos clave sobre los Cirros:\n"
        "- Altitud: Se forman por encima de los 6000 metros.\n"
        "- Composición: Principalmente cristales de hielo.\n"
        "- Aspecto: Tienen apariencia fibrosa, a veces con forma de hebras o ‘plumas’ "
        "de color blanco brillante.\n"
        "- Indicadores de cambio: Cuando son cada vez más abundantes, pueden anunciar "
        "un cambio en las condiciones meteorológicas a corto plazo (por ejemplo, "
        "la aproximación de un frente cálido).\n"
        "- Fenómenos ópticos: En ocasiones, provocan halos alrededor del sol o la luna "
        "(arcos luminosos o circulares) debido a la refracción de la luz en sus "
        "cristales de hielo."
    ),
    # ... resto de nubes ...










    # ... resto de nubes ...


    
    
    "Cumulus": (
        "Los cúmulos son nubes algodonosas con base plana y gran "
        "desarrollo vertical. Indican buen tiempo si su desarrollo "
        "es moderado."
    ),
    "Stratus": (
        "Los estratos son nubes bajas que cubren grandes áreas del "
        "cielo como una capa uniforme."
    ),
    "Cumulonimbus": (
        "Los cumulonimbos son nubes muy grandes con enorme desarrollo "
        "vertical, suelen producir tormentas y chubascos intensos."
    ),
    "Nimbostratus": (
        "Los nimbostratos son nubes grises extensas que provocan lluvia "
        "o nieve continua."
    ),
    "Altocumulus": (
        "Los altocúmulos son nubes de altura media, en grupos de pequeñas "
        "masas algodonosas, indicando cambios de tiempo a corto plazo."
    ),
    "Altostratus": (
        "Los altoestratos son nubes de altura media que forman una capa "
        "gris o azulada, a través de la cual a veces se distingue "
        "débilmente el sol o la luna."
    )
}

# --- Diccionario para almacenar las imágenes de nubes ---
clouds_images = {}

# --- Cargamos la imagen de Altocumulus (ajusta la ruta a la tuya) ---
try:
    altocumulus_img = tk.PhotoImage(file="img/altocumulus.png")
    clouds_images["Altocumulus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Altocumulus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/cumulus.png")
    clouds_images["Cumulus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Cumulus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/cirrus.png")
    clouds_images["Cirrus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Altocumulus: {e}")
        
# --- Función que se llama cuando se selecciona una nube en el ComboBox ---
def mostrar_informacion(event):
    nube_seleccionada = combo_nubes.get()
    # Mostrar el texto de descripción
    lbl_descripcion.config(text=clouds_info[nube_seleccionada])

    # Mostrar la imagen si la tenemos en el diccionario
    if nube_seleccionada in clouds_images:
        lbl_imagen.config(image=clouds_images[nube_seleccionada])
        # Referencia para que Python no "limpie" la imagen
        lbl_imagen.image = clouds_images[nube_seleccionada]
    else:
        # Si no hay imagen para esa nube, no mostramos nada
        lbl_imagen.config(image='')
        lbl_imagen.image = None

# --- Widgets de la interfaz ---
# Título
lbl_titulo = tk.Label(ventana, text="Tipos de Nubes", font=("Arial", 16, "bold"))
lbl_titulo.pack(pady=10)

# Instrucción
lbl_instruccion = tk.Label(ventana, text="Selecciona un tipo de nube:")
lbl_instruccion.pack()

# ComboBox con las claves del diccionario
combo_nubes = ttk.Combobox(ventana, values=list(clouds_info.keys()), state="readonly")
combo_nubes.bind("<<ComboboxSelected>>", mostrar_informacion)
combo_nubes.pack(pady=5)

# Label que mostrará la descripción
lbl_descripcion = tk.Label(ventana, text="", wraplength=400, justify="left")
lbl_descripcion.pack(padx=20, pady=20)

# Label que mostrará la imagen
lbl_imagen = tk.Label(ventana)
lbl_imagen.pack()

# --- Iniciar bucle principal ---
ventana.mainloop()
