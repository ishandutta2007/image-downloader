#coding=utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):

    base = Image.open(input_image_path).convert('RGBA')
    width, height = base.size
    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('arial.ttf', 50)

    d = ImageDraw.Draw(txt)
    x = width / 1.3
    y = height / 1.05

    # draw text, half opacity
    d.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
    out = Image.alpha_composite(base, txt)
    #out.show()
    out.convert('RGB').save(output_image_path)

if __name__ == '__main__':
    img = 'F://watermark//52085972.jpg'
    watermark_text(img, 'F://watermark//52085972_w.jpg',
                   text='ootdshare.com',
                   pos=(0, 0))
