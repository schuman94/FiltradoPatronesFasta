import re

def get_filter_function(filter_option, gap1=None, gap2=None):
    if filter_option == "4C":
        return filter_four_cysteines
    elif filter_option == "Patron alfa":
        return filter_pattern_alfa(gap1, gap2)
    else:
        raise ValueError(f"Opción de filtro desconocida: {filter_option}")

def filter_four_cysteines(record):
    return record.seq.count("C") == 4

def filter_pattern_alfa(gap1, gap2):
    pattern = re.compile(f"CC[^C]{{{gap1}}}C[^C]{{{gap2}}}C")

    def inner(record):
        sequence = str(record.seq)
        matches = pattern.findall(sequence)
        return len(matches) == 1 and record.seq.count("C") == 4

    return inner
