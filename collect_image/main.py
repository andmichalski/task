import sys

from func import get_image, show_images


def collect_image(url):
    data = get_image(url)
    show_images(data)


def main():
    collect_image(sys.argv[1])


if __name__ == "__main__":
    main()
