import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url')
    return parser


urls = [
    'https://w.forfun.com/fetch/55/55413c98d9b7198c8a08ac25b9514594.jpeg',
    'https://pichold.ru/wp-content/uploads/2019/03/Doberman-Pinscher-Dog-Pics-Background-Wallpapers.jpg',
    'https://klkfavorit.ru/wp-content/uploads/0/6/f/06f26bab69ff58c33353c45fb83e6e3d.jpeg',
    'https://gas-kvas.com/uploads/posts/2023-02/1675460865_gas-kvas-com-p-sobaki-na-fonovii-risunok-25.jpg',
    'https://w-dog.ru/wallpapers/16/15/343921452307181/letom-dalmatin-sobaki.jpg',
    'https://proprikol.ru/wp-content/uploads/2020/02/porodistye-sobaki-krasivye-kartinki-39-1.jpg',
    'http://gamerwall.pro/uploads/posts/2022-09/1662316408_1-gamerwall-pro-p-sobaka-zolotistii-retriver-vkontakte-1.jpg',
    'https://proprikol.ru/wp-content/uploads/2021/01/krasivye-kartinki-sobak-31.jpg'
]

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    urls.append(namespace.url)