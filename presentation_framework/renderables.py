from abc import ABC, abstractmethod
import markdown
import jinja2
import os

tags_to_renderables = {}


def register_tag(tag_name):
    '''
    Creates the tag_name -> Renderable binding and stores it in `tags_to_renderables`
    '''
    def decorator(some_class):
        tags_to_renderables[tag_name] = some_class
        return some_class
    return decorator


class Renderable(ABC):
    '''
    Every component that can be rendered onto the presentation,
    usually using markdown -> html converter
    or jinja2 templates
    '''

    @abstractmethod
    def render(self, build_context):
        pass


class MarkdownRenderable(Renderable):
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text

    def render(self, build_context):
        return markdown.markdown(self.markdown_text)


class HtmlRenderable(Renderable):
    def __init__(self, html_text):
        self.html_text = html_text

    def render(self, build_context):
        return self.html_text


class JinjaRenderable(Renderable):
    '''
    This is where the fun begins - base class for all
    jinja2 renderable templates.
    '''
    loader = jinja2.FileSystemLoader(searchpath=os.path.join(os.path.dirname(__file__), 'templates'))
    # loader = jinja2.FileSystemLoader(searchpath="./templates")
    environment = jinja2.Environment(loader=loader)
    template = None  # To be overriden in subclasses

    # Dict containing default arguments
    default_arguments = {
        # Nothing by default
    }

    def __init__(self, arguments={}):
        for key in arguments.keys():
            if key not in self.default_arguments:
                raise ValueError(
                    f'"{key}" not in possible arguments of {self.__class__.__name__}')

        self.arguments = {**self.default_arguments, **arguments}

    def render(self, build_context):
        self.arguments['build_context'] = build_context
        return self.template.render(**self.arguments)


@register_tag('asciinema')
class AsciinemaRenderable(JinjaRenderable):
    '''
    Example of a JinjaRenderable subclass.
    Things to do:
    * override the dict `default_arguments` with the data that will
        be passed to the jinja2 template
    * override the static `template` field with a chosen template 
    '''
    default_arguments = {'src': None}
    template = JinjaRenderable.environment.get_template('asciinema.j2')


    def render(self, build_context):
        build_context.video_num += 1
        return super().render(build_context)


@register_tag('slide')
class SlideBeginRenderable(JinjaRenderable):
    default_arguments = {'extra_class': ''}
    template = JinjaRenderable.environment.get_template(
        'slide_start.j2')


@register_tag('slide_end')
class SlideEndRenderable(JinjaRenderable):
    template = JinjaRenderable.environment.get_template('slide_end.j2')

    def render(self, build_context):
        build_context.next_slide()
        return super().render(build_context)


class PresentationStartRenderable(JinjaRenderable):
    template = JinjaRenderable.environment.get_template(
        'presentation_start.html')


class PresentationEndRenderable(JinjaRenderable):
    template = JinjaRenderable.environment.get_template(
        'presentation_end.html')



if __name__ == '__main__':
    print(tags_to_renderables)
