def get_filter_function(filter_option):
    if filter_option == "cuatro_cisteinas":
        return filter_four_cysteines
    else:
        raise ValueError(f"Opción de filtro desconocida: {filter_option}")

def filter_four_cysteines(record):
    return record.seq.count("C") == 4
