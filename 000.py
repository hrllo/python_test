#-*- coding:utf-8 -*-
'''
你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''

from PIL import Image, ImageDraw, ImageFont

def add_num_to_img(image_path, sign="42"):
    im = Image.open(image_path)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    font = ImageFont.load_default().font
    draw.text((width*0.75, height*0.075), sign, font=font, fill=(255,33,33, 255))

    left, right = image_path.rsplit(".", 1)
    #通过指定分隔符对字符串进行分割并返回一个列表，默认分隔符为所有空字符，包括空格、换行(\n)、制表符(\t)等。类似于 split() 方法，只不过是从字符串最后面开始分割。
    #指定的分隔符
    #可选参数，分割次数，默认为分隔符在字符串中出现的总次数
    new_image_path = left + "_" + sign + "." + right
    im.save(new_image_path)

if __name__ == '__main__':
    add_num_to_img("girl.jpg")
    print "Finished."



