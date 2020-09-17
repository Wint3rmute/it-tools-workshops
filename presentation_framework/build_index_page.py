import jinja2
import os

build_path = os.path.join(os.path.dirname(__file__), 'build')

files = os.listdir(build_path)

html_files = list(filter(
    lambda filename: filename.endswith('.html') and filename != 'index.html' and 'secret' not in filename and 'wip' not in filename, files
))

# print(html_files)
html_files.sort()

loader = jinja2.FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), 'templates'))
    # loader = jinja2.FileSystemLoader(searchpath="./templates")
environment = jinja2.Environment(loader=loader)
template = environment.get_template('index.j2')

result = template.render(html_files=html_files)

print(result)