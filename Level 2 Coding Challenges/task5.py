def triangle(integer, mode="left"):
    correct_mode = ["left", "right", "isosceles"]
    space_top = abs(integer) - 1
    space_bottom = 0
    triangle_up = [i for i in range(1, 2 * abs(integer) + 1, 2)]
    triangle_down = triangle_up[::-1]

    if mode not in correct_mode:
        raise ValueError(
            "Please enter 'left', 'right' or 'isosceles' as a string for the mode."
        )

    if integer > 0:
        for triangle_size in range(1, abs(integer) + 1):
            if mode == "left":
                print("#" * triangle_size)
            elif mode == "right":
                print(space_top * " " + "#" * triangle_size)
                space_top += -1
        if mode == "isosceles":
            for triangle_size in triangle_up:
                print(space_top * " " + triangle_size * "#" + space_top * " ")
                space_top += -1
    else:
        for triangle_size in range(abs(integer), 0, -1):
            if mode == "left":
                print("#" * triangle_size)
            elif mode == "right":
                print(space_bottom * " " + "#" * triangle_size)
                space_bottom += 1
        if mode == "isosceles":
            for triangle_size in triangle_down:
                print(space_bottom * " " + triangle_size * "#" + space_bottom * " ")
                space_bottom += 1
