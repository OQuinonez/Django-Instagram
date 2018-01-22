from PIL import Image, ImageFilter
from resizeimage import resizeimage

# def frozen_filter(path, side=800):
#     froze = Image.open(
#         '/home/basecamp/Projects/DailyExcersices/December/Django-Instagram/Instagram/static/Instagram/images/frozen.jpg'
#     ).convert('RGB')
#     froze = resizeimage.resize_cover(froze, [side, side], validate=False)
#     froze = froze.convert('RGB').quantize(64).convert('RGB')

#     image = Image.open(path).convert('RGB')
#     w, h = image.size
#     s = min([w, h])
#     box = ((w - s) // 2, (h - s) // 2, (s + w) // 2, (s + h) // 2)
#     image = image.crop(box=box)

#     image = resizeimage.resize_cover(image, [side, side], validate=False)
#     image = image.convert('RGB').quantize(255).convert('RGB')

#     # get size
#     w, h = image.size
#     pixel_data = list(image.getdata())

#     new_data = []
#     n = len(pixel_data)
#     for i in range(n):
#         t = pixel_data[i]
#         r, g, b = t
#         new_data.append((max(0, int(r - 255 * (i**2 / n**2))), max(
#             0, int(r - 255 * (i**2 / n**2))), b))

#     image = Image.new('RGB', (w, h))
#     image.putdata(new_data)
#     image = resizeimage.resize_cover(image, [side, side], validate=False)
#     image = image.convert('RGB')

#     finalimage = Image.blend(image, froze, .3)
#     finalimage.save(path)

#     return True