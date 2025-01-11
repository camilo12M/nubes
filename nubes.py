import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import ttkbootstrap as tb
from ttkbootstrap.constants import *





# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Tipos de Nubes")
ventana.geometry("800x650")
ventana.iconbitmap('img/icono2.ico') 

# Estilo moderno con ttkbootstrap (puedes elegir otros temas)
style = tb.Style("superhero")  # "superhero", "cyborg", "flatly", etc.
style.master = ventana

# --- Diccionario con la descripción de cada tipo de nube ---
clouds_info = {
    "Cirrus": (
        "Los cirros son nubes finas y delicadas que aparecen a gran altitud "
        "(generalmente por encima de los 6000 m). Están compuestos casi en su "
        "totalidad por cristales de hielo debido a las bajas temperaturas a esas "
        "alturas. Suelen presentarse en forma de filamentos o mechones y, con "
        "frecuencia, muestran un aspecto sedoso o fibroso."
    ),
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
    ),
    "ciclo": (
        "En resumen, dentro de esa imagen, los altoestratos se ubican en el "
        "rango medio de la atmósfera y se muestran como una extensa nube grisácea "
        "no tan fina ni tan alta como los cirros, pero tampoco baja como "
        "los estratos. Y, a diferencia de otras nubes, los altoestratos "
        "suelen dejar pasar algo de luz solar o lunar, generando "
        "ese efecto de ver el sol o la luna tenuemente detrás de la nube."
    )
}

# --- Diccionario para almacenar las imágenes de nubes ---
clouds_images = {}

# --- Cargamos las imágenes (ajusta la ruta según tus archivos) ---
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
    print(f"No se pudo cargar la imagen de Cirrus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/stratus.png")
    clouds_images["Stratus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Stratus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/cumulonimbus.png")
    clouds_images["Cumulonimbus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Cumulonimbus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/nimbostratus.png")
    clouds_images["Nimbostratus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Nimbostratus: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/mapa_conceptual.png")
    clouds_images["ciclo"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de ciclo: {e}")

try:
    altocumulus_img = tk.PhotoImage(file="img/altostratus.png")
    clouds_images["Altostratus"] = altocumulus_img
except Exception as e:
    print(f"No se pudo cargar la imagen de Altostratus: {e}")

# --- Función para mostrar la información de la nube ---
def mostrar_informacion(event=None):
    nube_seleccionada = combo_nubes.get()
    # Actualizamos el contenido del ScrolledText
    txt_descripcion.config(state="normal")
    txt_descripcion.delete("1.0", "end")
    txt_descripcion.insert("end", clouds_info[nube_seleccionada])
    txt_descripcion.config(state="disabled")

    if nube_seleccionada in clouds_images:
        lbl_imagen.config(image=clouds_images[nube_seleccionada])
        lbl_imagen.image = clouds_images[nube_seleccionada]
    else:
        lbl_imagen.config(image="")
        lbl_imagen.image = None

# --- Widgets de la interfaz ---
# Frame principal con ttkbootstrap
frame_principal = ttk.Frame(ventana, padding=20, relief="solid", borderwidth=2)
frame_principal.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Título con diseño moderno
lbl_titulo = ttk.Label(frame_principal, text="Tipos de Nubes", font=("Arial", 20, "bold"))
lbl_titulo.pack(pady=10)

# Frame para la selección de nube
frame_seleccion = ttk.Frame(frame_principal)
frame_seleccion.pack(pady=10, fill="x")

lbl_instruccion = ttk.Label(frame_seleccion, text="Selecciona un tipo de nube:", font=("Arial", 12))
lbl_instruccion.pack(side="left", padx=5)

# Combobox con estilo moderno
combo_nubes = ttk.Combobox(frame_seleccion, values=list(clouds_info.keys()), state="readonly", width=20)
combo_nubes.bind("<<ComboboxSelected>>", mostrar_informacion)
combo_nubes.pack(side="left", padx=5)

# ScrolledText para la descripción, con bordes redondeados
txt_descripcion = ScrolledText(frame_principal, wrap="word", width=60, height=10, font=("Arial", 12))
txt_descripcion.pack(padx=20, pady=10)
txt_descripcion.config(state="disabled")

# Label para mostrar la imagen
lbl_imagen = ttk.Label(frame_principal)
lbl_imagen.pack(pady=10)

# --- Iniciar bucle principal ---
ventana.mainloop()
