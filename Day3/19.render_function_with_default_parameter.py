
def render(width, height, symbol="$"):
    
    first_line = symbol * width + "\n"

    middle_lines = (symbol + " " * (width-2) + symbol  + "\n") * (height - 2)

    last_line = symbol * width

    return  first_line + middle_lines + last_line

print(render(10, 5))
print(render(10, 5, "@"))