from renderables import *
import re

# TODO: USE REGEX FOR SPLITTING THE ENTIRE FRAGMENTS
# splitter = r'({{.+}})|((}})*(\s*|[^{}]*)+{{)'


counter = 0

def parse_special_tag(line):
    global counter

    line = line.replace('{', '').replace('}', '').replace('\n', '')
    
    command, *arguments_str = line.split(' ')

    arguments_dict = {}

    for argument_str in arguments_str:
        argument, value = argument_str.split('=')
        arguments_dict[argument] = value


    if command == 'slide':
        counter += 1

        arguments = {**{'id': counter, 'data_x': counter * 1500, 'data_y': 0}, **arguments_dict}

        return TemplateRenderable('slide_start.j2', arguments)

    elif command == 'slide_end':
        return TemplateRenderable('slide_end.j2', arguments_dict)

    elif command == 'asciinema':
        arguments = {**{'id': counter}, **arguments_dict}

        return AsciinemaRenderable(arguments)
    else:
        raise ValueError(f'No such command: {command}')


splitter = r'{{.+}}'

output_renderables = [ TemplateRenderable('start.html') ]

with open('cli.md') as file:

    markdown_text = ''

    for line in file:
        if re.match(splitter, line):
            output_renderables.append(MarkdownRenderable(markdown_text))
            markdown_text = ''

            output_renderables.append(
                parse_special_tag(line)
            )

        else:
            markdown_text += line


output_renderables.append(TemplateRenderable('end.html'))
for renderable in output_renderables:
    # print('#####')
    print(renderable.render())