from PIL import ImageFont

class Marker:

    def marker(self, filepath, extra_func, name, font_size, f_color) :
        from PIL import Image, ImageDraw, ImageTk
        # get an image
        with Image.open( filepath ).convert( "RGBA" ) as base :
            # make a blank image for the text, initialized to transparent text color
            txt = Image.new( "RGBA", base.size, (255, 255, 255, 0) )

            # get a fon"arial
            fnt = ImageFont.truetype( "arial.ttf", font_size )
            # get a drawing context
            d = ImageDraw.Draw( txt )
            # getting base image size
            base_height = base.size[1]
            # draw text, half opacity
            d.text( (10, base_height - 60), "Created By", font=fnt, fill=(f_color[0], f_color[0], f_color[0], 128) )
            # draw text, full opacity
            d.text( (10, base_height - 30), name, font=fnt, fill=(f_color[0], f_color[0], f_color[0], 255) )

            out = Image.alpha_composite( base, txt )

            extra_func( out, name )


