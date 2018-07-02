from jinja2 import Environment, FileSystemLoader
import os
from sys import argv
from shutil import copytree

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
THEME_DIR = THIS_DIR + '/theme/'
STATIC_DIR = THIS_DIR + '/static/'
CURRENT_DIR = os.getcwd() + '/'

def main():
    if len(argv) == 1:
        print('Helptext')

    elif len(argv) > 3:
        print('Too many parameters')

    else:
        if argv[1] == 'create':
            if len(argv) < 3:
                print('The create command needs a folder name')

            else:
                create(argv[2])

        elif argv[1] == 'render':
            render()
            
        else:
            print('Unknown command')

def create(name):
    print('Creating folder structure')
    
    workspace = CURRENT_DIR + name

    if not os.path.exists(workspace):
        os.makedirs(workspace)
        os.makedirs(workspace + '/static')
        os.makedirs(workspace + '/posts')

        copytree(THEME_DIR + 'css', workspace + '/static/css')


def render():
    print('Rendering HTML from templates')

def generate_template():
    env = Environment(
        loader=FileSystemLoader(THEME_DIR),
        trim_blocks=True
    )

    template = env.get_template('index.html')

    title = "Test blog"
    posts = [
        ('Post 1', 'July 2, 2018', 'Test content')
    ]

    template.stream(title=title, posts=posts).dump(STATIC_DIR + 'index.html')


if __name__ == '__main__':
    main()