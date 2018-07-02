from jinja2 import Environment, FileSystemLoader
from os.path import dirname, abspath

THIS_DIR = dirname(abspath(__file__))
THEME_DIR = '/theme/'

def main():
    env = Environment(
        loader=FileSystemLoader(THIS_DIR + THEME_DIR),
        trim_blocks=True
    )

    template = env.get_template('index.html')
    print (template.render(title='Test', content='Test2'))


if __name__ == '__main__':
    main()