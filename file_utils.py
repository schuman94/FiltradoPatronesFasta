from tkinter import filedialog
from Bio import SeqIO
import os
import datetime
import filters

def seleccionar_archivo(var):
    def inner():
        file_path = filedialog.askopenfilename(filetypes=[("Archivos FASTA", "*.fasta")])
        var.set(file_path)
    return inner

def seleccionar_carpeta(var):
    def inner():
        folder_path = filedialog.askdirectory()
        var.set(folder_path)
    return inner

def filtrar_secuencias(input_file, output_folder, filter_option, gap1=None, gap2=None):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    output_file = os.path.join(output_folder, f"filtrado_{timestamp}.fasta")

    filter_func = filters.get_filter_function(filter_option, gap1, gap2)

    with open(input_file, "r") as in_handle, open(output_file, "w") as out_handle:
        records = SeqIO.parse(in_handle, "fasta")
        filtered = filter(filter_func, records)
        SeqIO.write(filtered, out_handle, "fasta")
