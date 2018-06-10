from collect_image.func import get_image, show_images


def collect_image(url):
    data = get_image(url)
    show_images(data)
