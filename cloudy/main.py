from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath

THIS_DIR = dirname(abspath(__file__))
THEME_DIR = '/theme/'
STATIC_DIR = '/static/'

def main():
    env = Environment(
        loader=FileSystemLoader(THIS_DIR + THEME_DIR),
        trim_blocks=True
    )

    template = env.get_template('index.html')

    title = "Test blog"
    posts = [
        ('Post 1', 'July 2, 2018', 'Test content')
    ]

    template.stream(title=title, posts=posts).dump(THIS_DIR + STATIC_DIR + 'index.html')


if __name__ == '__main__':
    main()