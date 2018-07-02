from jinja2 import Environment, FileSystemLoader
import os
from sys import argv
from shutil import copytree
import mistune

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

    if (os.path.exists(CURRENT_DIR) 
        # and os.path.isfile(CURRENT_DIR + 'cloudy.yml')
        and os.path.exists(CURRENT_DIR + '/static')
        and os.path.exists(CURRENT_DIR + '/posts')):
        
        date, title, body = parse_markdown()
        generate_template(date, title, body)

    else:
        print('Not in a cloudy project directory')

def parse_markdown():
    with open(CURRENT_DIR + '/posts/example_post.md', 'r') as f:
        metadata = next(f).split(";")
        date = eval(metadata[0])
        title = eval(metadata[1])

        body = mistune.markdown(f.read())
    
    return (date, title, body)


def generate_template(date, title, body):
    env = Environment(
        loader=FileSystemLoader(THEME_DIR),
        trim_blocks=True
    )

    template = env.get_template('index.html')

    header_title = "Test blog"
    posts = [
        (title, date, body)
    ]

    template.stream(header_title=header_title, posts=posts).dump(CURRENT_DIR + '/static/index.html')


if __name__ == '__main__':
    main()