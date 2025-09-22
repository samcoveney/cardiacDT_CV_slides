import cairo

for index in range(0,500):

    # set the canvas
    # ==============
    WIDTH, HEIGHT = 200, 200

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

    ctx.select_font_face("Courier", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)

    ctx.set_font_size(0.5)
    glyphs = [(index, 0.5, 0.5)]
    ctx.show_glyphs(glyphs) 

    surface.write_to_png(str(index) + ".png")  # Output to PNG
