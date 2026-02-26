import operator
from PIL import Image


class WrapperImage:
    def __init__(self, size, bg_color=None):
        self.size = size
        self.bg_color = bg_color

    def dominant_color(self, image_path):
        img = Image.open(image_path).resize((150, 150)).convert("RGB")
        pixels = img.getdata()

        color_count = {}
        for pixel in pixels:
            color_count[pixel] = color_count.get(pixel, 0) + 1

        dominant_color = max(color_count.items(), key=operator.itemgetter(1))[0]
        self.bg_color = dominant_color

    def create_canvas(self):
        return Image.new("RGB", (self.size, self.size), self.bg_color)


class MainImage:
    def __init__(self, path, size):
        self.path = path
        self.size = size

    def resize(self):
        return Image.open(self.path).resize((self.size, self.size))

    def paste_to_center(self, canvas):
        padding = (canvas.size[0] - self.size) // 2
        canvas.paste(self.resize(), (padding, padding))


class SubImage:
    def __init__(self, path, position, size):
        self.path = path
        self.position = position
        self.size = size

    def resize(self):
        return Image.open(self.path).resize((self.size, self.size))

    def paste(self, canvas):
        canvas.paste(self.resize(), self.position)


def create_image(main_image, sub_images, wrapper_size):

    if main_image["size"] >= wrapper_size:
        print("Main image must be smaller than wrapper.")
        return

    # wrapper yaratish
    wrapper = WrapperImage(wrapper_size)
    wrapper.dominant_color(main_image["path"])
    canvas = wrapper.create_canvas()

    # main image
    main = MainImage(main_image["path"], main_image["size"])
    main.paste_to_center(canvas)

    # 4 katak pozitsiya
    half = wrapper_size // 2
    positions = [
        (0, 0),
        (half, 0),
        (0, half),
        (half, half),
    ]

    # sub images
    for sub in sub_images:
        pos = positions[sub["position_id"]]
        sub_img = SubImage(sub["path"], pos, half)
        sub_img.paste(canvas)

    canvas.save("result.jpg")
    print("Saved result.jpg")


# 🔥 TEST
small_images = [
    {"path": "./images/storm.png", "position_id": 3},
    {"path": "./images/sun.png", "position_id": 0}
]

main_image = {
    "path": "./images/cloud.png",
    "size": 500
}

create_image(main_image, small_images, 600)
