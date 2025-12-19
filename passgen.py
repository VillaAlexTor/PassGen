import random 
import string
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
class GeneradorContraseniaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contrasenias Seguras")
        self.root.geometry("500x550")
        # Variables de control
        self.longitud_var = tk.IntVar(value=12)
        self.mayusculas_var = tk.BooleanVar(value=True)
        self.minusculas_var = tk.BooleanVar(value=True)
        self.digitos_var = tk.BooleanVar(value=True)
        self.especiales_var = tk.BooleanVar(value=True)
        self.contrasenia_var = tk.StringVar()
        # Crear interfaz
        self.crear_interfaz()
        # Generar primera contrasenia al iniciar
        self.generar_contrasenia()
    def crear_interfaz(self):
        # Crear todos los elementos de la interfaz
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Titulo
        title_label = tk.Label(
            main_frame,
            text="GENERADOR DE CONTRASENIAS SEGURAS",
            font=('Arial', 16, 'bold')
        )
        title_label.pack(pady=(0, 15))
        # Separador
        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=5)
        # SECCION 1: LONGITUD 
        longitud_frame = ttk.LabelFrame(main_frame, text="1. Longitud", padding="10")
        longitud_frame.pack(fill='x', pady=(0, 10))
        # Slider para longitud
        longitud_slider = tk.Scale(
            longitud_frame,
            from_=8,
            to=128,
            orient=tk.HORIZONTAL,
            variable=self.longitud_var,
            length=350
        )
        longitud_slider.pack()
        # Label para mostrar longitud actual
        self.longitud_label = tk.Label(
            longitud_frame,
            text=f"Longitud: {self.longitud_var.get()} caracteres",
            font=('Arial', 10, 'bold')
        )
        self.longitud_label.pack(pady=(5, 0))
        # SECCIÓN 2: TIPOS DE CARACTERES 
        tipos_frame = ttk.LabelFrame(main_frame, text="2. Tipos de caracteres", padding="10")
        tipos_frame.pack(fill='x', pady=(0, 10))
        # Checkbuttons para tipos de caracteres
        tipos_opciones = [
            ("Letras MAYUSCULAS (A-Z)", self.mayusculas_var),
            ("Letras minusculas (a-z)", self.minusculas_var),
            ("Digitos (0-9)", self.digitos_var),
            ("Caracteres especiales (!@#$%...)", self.especiales_var)
        ]
        for texto, variable in tipos_opciones:
            cb = ttk.Checkbutton(tipos_frame, text=texto, variable=variable)
            cb.pack(anchor='w', pady=2)
        # Botones rapidos
        botones_frame = ttk.Frame(tipos_frame)
        botones_frame.pack(pady=(10, 0))
        btn_todo = ttk.Button(
            botones_frame,
            text="SELECCIONAR TODO",
            command=self.seleccionar_todo
        )
        btn_todo.pack(side='left', padx=5)
        btn_limpiar = ttk.Button(
            botones_frame,
            text="LIMPIAR SELECCION",
            command=self.limpiar_seleccion
        )
        btn_limpiar.pack(side='left', padx=5)
        # SECCION 3: CONTRASENIA GENERADA 
        contrasenia_frame = ttk.LabelFrame(main_frame, text="3. Contrasenia generada", padding="10")
        contrasenia_frame.pack(fill='x', pady=(0, 10))
        # Campo para mostrar contrasenia
        contrasenia_entry = tk.Entry(
            contrasenia_frame,
            textvariable=self.contrasenia_var,
            font=('Courier', 12, 'bold'),
            justify='center',
            state='readonly'
        )
        contrasenia_entry.pack(fill='x', pady=(0, 10), ipady=8)
        # Boton para copiar
        btn_copiar = ttk.Button(
            contrasenia_frame,
            text="COPIAR AL PORTAPAPELES",
            command=self.copiar_portapapeles
        )
        btn_copiar.pack()
        # SECCIÓN 4: BOTONES DE ACCION 
        acciones_frame = ttk.Frame(main_frame)
        acciones_frame.pack(pady=(10, 0))
        # Boton generar
        btn_generar = ttk.Button(
            acciones_frame,
            text="GENERAR NUEVA CONTRASENIA",
            command=self.generar_contrasenia
        )
        btn_generar.pack(side='left', padx=5)
        # Botón salir
        btn_salir = ttk.Button(
            acciones_frame,
            text="SALIR",
            command=self.root.quit
        )
        btn_salir.pack(side='left', padx=5)
        # SECCIÓN 5: INFORMACION 
        info_frame = ttk.LabelFrame(main_frame, text="Informacion", padding="10")
        info_frame.pack(fill='x', pady=(10, 0))
        info_text = "• Contrasenia generada aleatoriamente\n• Cuantos mas tipos seleccione, mas segura sera\n• Recomendado: usar todos los tipos + 12+ caracteres"
        info_label = tk.Label(
            info_frame,
            text=info_text,
            justify=tk.LEFT
        )
        info_label.pack()
    def actualizar_longitud_label(self):
        # Actualizar el label de longitud
        self.longitud_label.config(text=f"Longitud: {self.longitud_var.get()} caracteres")
        self.generar_contrasenia()
    def seleccionar_todo(self):
        # Seleccionar todos los tipos de caracteres
        self.mayusculas_var.set(True)
        self.minusculas_var.set(True)
        self.digitos_var.set(True)
        self.especiales_var.set(True)
        self.generar_contrasenia()
    def limpiar_seleccion(self):
        # Limpiar toda la selección
        self.mayusculas_var.set(False)
        self.minusculas_var.set(False)
        self.digitos_var.set(False)
        self.especiales_var.set(False)
        self.generar_contrasenia()
    def generar_contrasenia(self):
        # Generar una nueva contrasenia
        # Verificar que al menos un tipo este seleccionado
        if not (self.mayusculas_var.get() or self.minusculas_var.get() or 
                self.digitos_var.get() or self.especiales_var.get()):
            messagebox.showwarning("Advertencia", 
                "Debe seleccionar al menos un tipo de caracteres.\nSe usaran todos por defecto.")
            self.seleccionar_todo()
            return
        # Construir cadena de caracteres permitidos
        caracteres = ""
        if self.mayusculas_var.get():
            caracteres += string.ascii_uppercase
        if self.minusculas_var.get():
            caracteres += string.ascii_lowercase
        if self.digitos_var.get():
            caracteres += string.digits
        if self.especiales_var.get():
            caracteres += string.punctuation
        # Generar contrasenia
        try:
            longitud = self.longitud_var.get()
            if not caracteres:
                raise ValueError("No hay caracteres disponibles")
            contrasenia = ''.join(random.choice(caracteres) for _ in range(longitud))
            self.contrasenia_var.set(contrasenia)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar la contrasenia: {str(e)}")
    def copiar_portapapeles(self):
        # Copiar la contrasenia al portapapeles
        contrasenia = self.contrasenia_var.get()
        if contrasenia:
            self.root.clipboard_clear()
            self.root.clipboard_append(contrasenia)
            messagebox.showinfo("Copiado", "Contrasenia copiada al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "No hay contrasenia para copiar")
def main():
    # Funcion principal para iniciar la aplicacion
    try:
        root = tk.Tk()
        app = GeneradorContraseniaApp(root)
        # Centrar ventana en pantalla
        root.update_idletasks()
        ancho = root.winfo_width()
        alto = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (root.winfo_screenheight() // 2) - (alto // 2)
        root.geometry(f'+{x}+{y}')
        # Iniciar loop principal
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicacion: {e}")
if __name__ == "__main__":
    main()