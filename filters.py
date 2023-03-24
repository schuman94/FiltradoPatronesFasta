import re

def get_filter_function(filter_option):
    if filter_option == "cuatro_cisteinas":
        return filter_four_cysteines
    elif filter_option == "patron_alfa44":
        return filter_pattern_alfa44
    elif filter_option == "patron_alfa47":
        return filter_pattern_alfa47
    else:
        raise ValueError(f"Opción de filtro desconocida: {filter_option}")

def filter_four_cysteines(record):
    return record.seq.count("C") == 4

def filter_pattern_alfa44(record):
    pattern = re.compile("CC[^C]{4}C[^C]{4}C")
    sequence = str(record.seq)
    matches = pattern.findall(sequence)
    return len(matches) == 1 and record.seq.count("C") == 4

def filter_pattern_alfa47(record):
    pattern = re.compile("CC[^C]{4}C[^C]{7}C")
    sequence = str(record.seq)
    matches = pattern.findall(sequence)
    return len(matches) == 1 and record.seq.count("C") == 4
