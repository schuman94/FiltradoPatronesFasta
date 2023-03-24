import tkinter as tk
from tkinter import filedialog, messagebox
from Bio import SeqIO
import os
import datetime

def seleccionar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos FASTA", "*.fasta")])
    entrada_var.set(file_path)

def seleccionar_carpeta():
    folder_path = filedialog.askdirectory()
    salida_var.set(folder_path)

def filtrar_secuencias():
    input_file = entrada_var.get()
    output_folder = salida_var.get()
    filter_option = patron_var.get()

    if not input_file or not output_folder:
        messagebox.showerror("Error", "Selecciona un archivo de entrada y una carpeta de salida")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = os.path.join(output_folder, f"filtrado_{timestamp}.fasta")

    if filter_option == "cuatro_cisteinas":
        def filter_func(record):
            return record.seq.count("C") == 4

    with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
        records = SeqIO.parse(in_handle, "fasta")
        filtered = filter(filter_func, records)
        SeqIO.write(filtered, out_handle, "fasta")

    messagebox.showinfo("Éxito", "El filtrado de secuencias se ha completado")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Filtrado de secuencias FASTA")
ventana.minsize(600, 200)  # Establecer tamaño mínimo de la ventana

entrada_var = tk.StringVar()
salida_var = tk.StringVar()
patron_var = tk.StringVar()

tk.Label(ventana, text="Archivo de entrada (.fasta):").grid(row=0, column=0, sticky="e")
tk.Entry(ventana, textvariable=entrada_var, width=60).grid(row=0, column=1)  # Aumentar el tamaño del cuadro de texto
tk.Button(ventana, text="Seleccionar", command=seleccionar_archivo).grid(row=0, column=2)

tk.Label(ventana, text="Carpeta de salida:").grid(row=1, column=0, sticky="e")
tk.Entry(ventana, textvariable=salida_var, width=60).grid(row=1, column=1)  # Aumentar el tamaño del cuadro de texto
tk.Button(ventana, text="Seleccionar", command=seleccionar_carpeta).grid(row=1, column=2)

tk.Label(ventana, text="Patrón de filtrado:").grid(row=2, column=0, sticky="e")
tk.OptionMenu(ventana, patron_var, "cuatro_cisteinas").grid(row=2, column=1, sticky="w")
patron_var.set("cuatro_cisteinas")

tk.Button(ventana, text="Iniciar filtrado", command=filtrar_secuencias).grid(row=3, column=1, pady=10)

ventana.mainloop()
