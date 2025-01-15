

def render(width, height):
    
    first_line = "#" * width + "\n"

    middle_lines = ("#" + " " * (width-2) + "#"  + "\n") * (height - 2)

    last_line = "#" * width


    return  first_line + middle_lines + last_line

print(render(10, 5))