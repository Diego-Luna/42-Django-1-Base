
# Todo: crear la funcion de generacion de shader

def generate_shader():
    
    colors = {
        "noir": (0, 0, 0),
        "rouge": (255, 0, 0),
        "vert": (0, 255, 0),
        "bleu": (0, 0, 255),
    }

    shade = []

    for i in range(50):

        factor = i / 100
        row = {}
        for color_name, base_color in colors.items():
            r = int(base_color[0] + (255 - base_color[0]) * factor)
            g = int(base_color[1] + (255 - base_color[1]) * factor)
            b = int(base_color[2] + (255 - base_color[2]) * factor)
            
            # * Convertir a formato hexadecimal para CSS
            row[color_name] = f'#{r:02x}{g:02x}{b:02x}'

        shade.append(row)
    
    return shade
