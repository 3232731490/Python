import urllib.request as ur

response=ur.urlopen('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1605268884940&di=d740bfd505e245d570ab01ff0c31892f&imgtype=0&src=http%3A%2F%2Fa0.att.hudong.com%2F30%2F29%2F01300000201438121627296084016.jpg')
picture_img=response.read()
with open('picture.jpg','wb') as f:
    f.write(picture_img)