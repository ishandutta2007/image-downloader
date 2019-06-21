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
    fnt = ImageFont.truetype('arial.ttf', 72)

    d = ImageDraw.Draw(txt)
    x = width / 5.5
    y = height / 1.3

    # draw text, half opacity
    d.text((x, y), text, font=fnt, fill=(255, 255, 255, 128))
    out = Image.alpha_composite(base, txt)
    #out.show()
    out.convert('RGB').save(output_image_path)

if __name__ == '__main__':
    import os
    for path, directories, files in os.walk('C://Users//wu//influencers//maisie_williams'):
        for name in files:
            if name.endswith("jpg"):
            #img = 'F://watermark//115461607.jpg'
                print name
                full_file = os.path.join(path, name)
                try:
                    watermark_text(full_file, full_file,
                        text='ootdshare.com',
                        pos=(0, 0))
                except Exception,e:
                    print e
                    continue