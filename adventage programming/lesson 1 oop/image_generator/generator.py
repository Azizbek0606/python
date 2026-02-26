# import operator
#
# from PIL import Image
#
# class WrapperImage:
#     def __init__(self, size, child_count,max_child_count, bg_color):
#         self.size = size
#         self.child_count = child_count
#         self.max_child_count = max_child_count
#         self.bg_color = bg_color
#
#     def dominant_color(self, main_image):
#         img = Image.open(main_image.path)
#         img = img.resize((150, 150))
#         img = img.convert('RGB')
#         pixels = img.getdata()
#         color_count = {}
#
#         for pixel in pixels:
#             if pixel in color_count:
#                 color_count[pixel] += 1
#             else:
#                 color_count[pixel] = 1
#
#         dominant_color = max(color_count.items(), key=operator.itemgetter(1))
#
#         self.bg_color =  dominant_color
#
#     def add_child(self, amount):
#         self.child_count += amount
#
#     def create_canvas(self):
#         image = Image.new("RGB", (self.size, self.size), self.bg_color)
#         return image
#
#
# class MainImage:
#     def __init__(self, path, padding, size):
#         self.path = path
#         self.padding = padding
#         self.size = size
#
#     def resize(self):
#         image = Image.open(self.path).resize((self.size, self.size))
#         return image
#
#     def set_main_image(self, new_canvas):
#         image = self.resize()
#         new_image = new_canvas.paste(image, self.padding, self.padding)
#         return new_image
#
#
# class SubImage:
#     def __init__(self, path, position, size):
#         self.path = path
#         self.position = position
#         self.size = size
#
#     def resize(self):
#         image = Image.open(self.path).resize((self.size, self.size))
#         return image
#
#
# def create_image(main_image, sub_images, size):
#     const_pos = [[0,0],[size/2, 0],[0, size/2],[size/2, size/2]]
#     if main_image["size"] >= size:
#         print("main image should be smaller than wrapper size")
#         return
#     if size - main_image["size"] <= 99:
#         print("main image should be minimum 100px smaller than wrapper size")
#         return
#
#     main_image_class = MainImage(main_image["path"],((size - main_image["size"]) // 2), main_image["size"])
#     wrapper_image = WrapperImage(main_image_class, 0, 3,None)
#     sub_image_classes = []
#     for sub_image in sub_images:
#         x = SubImage(sub_image['path'], const_pos[sub_image["position_id"]], size // 2)
#         sub_image_classes.append(x)
#
#     wrapper_image.dominant_color(main_image_class)
#     wrapper_image.create_canvas()
#     main_image_class.set_main_image(wrapper_image)
#
# # const pos| 0 =  t_r, 1 = t_l, 2 = b_r, 3 = b_l
#
#
# small_images = [{"path":'./storm.png',"position_id": 3},{"path":'./wind.png',"position_id": 0}]
# main_image = [{"path:":'./cloud.png', "size":500}]
# create_image(main_image, small_images, 600)