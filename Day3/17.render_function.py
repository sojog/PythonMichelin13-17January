
def render_v1(width, height):
    print("#" * width)

    for _ in range(height - 2):
        print("#" + " " * (width-2) + "#")

    print("#" * width)

def render(width, height):
    print("#" * width)
    
    count = 0
    while count < height - 2:
        print("#" + " " * (width-2) + "#")
        count += 1

    print("#" * width)

render(10, 5)
render(8, 8)