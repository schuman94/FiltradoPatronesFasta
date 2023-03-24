import tkinter as tk
from tkinter import messagebox
import file_utils

def filtrar_secuencias():
    input_file = entrada_var.get()
    output_folder = salida_var.get()
    filter_option = patron_var.get()

    if not input_file or not output_folder:
        messagebox.showerror("Error", "Selecciona un archivo de entrada y una carpeta de salida")
        return

    def run_filtering():
        nonlocal progress_window
        file_utils.filtrar_secuencias(input_file, output_folder, filter_option)
        progress_window.destroy()
        messagebox.showinfo("Éxito", "El filtrado de secuencias se ha completado")

    progress_window = tk.Toplevel(ventana)
    progress_window.title("Filtrando secuencias")
    progress_window.geometry("250x100")
    tk.Label(progress_window, text="Filtrando secuencias, por favor espera...").pack(pady=10)
    ventana.after(100, run_filtering)  # Ejecuta el filtrado después de 100ms para dar tiempo a que se muestre la ventana


# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Filtrado de secuencias FASTA")
ventana.minsize(600, 200)

entrada_var = tk.StringVar()
salida_var = tk.StringVar()
patron_var = tk.StringVar()

tk.Label(ventana, text="Archivo de entrada (.fasta):").grid(row=0, column=0, sticky="e")
tk.Entry(ventana, textvariable=entrada_var, width=60).grid(row=0, column=1)
tk.Button(ventana, text="Seleccionar", command=file_utils.seleccionar_archivo(entrada_var)).grid(row=0, column=2)

tk.Label(ventana, text="Carpeta de salida:").grid(row=1, column=0, sticky="e")
tk.Entry(ventana, textvariable=salida_var, width=60).grid(row=1, column=1)
tk.Button(ventana, text="Seleccionar", command=file_utils.seleccionar_carpeta(salida_var)).grid(row=1, column=2)

tk.Label(ventana, text="Patrón de filtrado:").grid(row=2, column=0, sticky="e")
tk.OptionMenu(ventana, patron_var, "cuatro_cisteinas", "patron_alfa44", "patron_alfa47").grid(row=2, column=1, sticky="w")
patron_var.set("cuatro_cisteinas")

tk.Button(ventana, text="Iniciar filtrado", command=filtrar_secuencias).grid(row=3, column=1, pady=10)

ventana.mainloop()
