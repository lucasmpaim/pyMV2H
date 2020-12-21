

def inside_margin(value, another_value, margin) -> bool:
    return (value - margin) <= another_value < (value + margin)
