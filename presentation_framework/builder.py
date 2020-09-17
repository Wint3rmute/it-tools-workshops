from renderables import *
import re
import markdown
import sys
import insertables

class BuildContext():
    '''
    BuildContext is passed to every Renderable when building.
    Access to the current slide_number is currently all thats
    needed (to setup some JS scripts)
    '''
    def __init__(self):
        self.slide_num = 0
        self.video_num = 0

    def next_slide(self):
        self.slide_num += 1


class Builder():
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file


    def build(self):
        # I just wrote a fucking regex omg
        splitter = r'(?s)((?<=}}).*?(?={{)|({{.+?}}))'
        '''
        Alright so this baby above splits the text into
            * markdown fragments
            * special-tag fragments

        The markdown fragments are then converted into html using the
        markdown library. Special tags on the other hand are converted
        to html using the jinja2 library

        '''

        build_context = BuildContext()
        output_renderables = []

        # The top of the HTML file: css, js, opening divs and other tags
        output_renderables.append(PresentationStartRenderable())

        with open(self.input_file) as markdown_file:
            presentation_txt = markdown_file.read()

            for key, value in insertables.insertables.items():
                presentation_txt = presentation_txt.replace(key, value)

            for segment in re.finditer(splitter, presentation_txt):
                output_renderables.append(
                    self.make_segment_into_renderable(segment.group(), build_context)
                )

        # The bottom of the HTML file - closing the divs and other tags
        output_renderables.append(PresentationEndRenderable())

        # Save the whole thing to file
        output = open(self.output_file, 'w')
        for renderable in output_renderables:
            output.write(f'<!-- Building {renderable.__class__.__name__} -->')

            output.write(renderable.render(build_context))
            # build_context.next_slide() # NOPE: next slide only if the tag is the end_slide tag
        output.close()

    def make_segment_into_renderable(self, segment, build_context):
        # Matches if segment is a special tag
        if re.match(r'{{.+?}}', segment):
            return self.make_special_tag_into_renderable(segment, build_context)
        else:
            return MarkdownRenderable(segment)

    def make_special_tag_into_renderable(self, segment, build_context):
        segment = segment[2:-2]  # TODO: can this go tits up?
        tag = re.search(r'^([\w\-]+)', segment).group()
        
        arguments = {}
        
        if re.search(r'(?<=\s)(.*?)$', segment):
            # If there are arguments
            str_arguments = re.search(r'(?<=\s)(.*?)$', segment).group().split()
            # print(arguments)
            for argument in str_arguments:
                name, value = argument.split('=')
                arguments[name] = value
                
        if not tag in tags_to_renderables:
            raise ValueError(f'Unknown tag: {tag}')

        return tags_to_renderables[tag](arguments)
        # print('found', tags_to_renderables[tag], 'with args', arguments)

