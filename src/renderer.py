from typing import List, Dict


class HTMLRenderer:
    def __init__(self, extensions=None):
        self.extensions = extensions or []
        self.renderers = self._init_renderers()

    def _init_renderers(self) -> Dict:
        """Initialize HTML renderers for each element type"""
        return {
            'h1': lambda x: f'<h1>{x}</h1>',
            'h2': lambda x: f'<h2>{x}</h2>',
            'h3': lambda x: f'<h3>{x}</h3>',
            'h4': lambda x: f'<h4>{x}</h4>',
            'h5': lambda x: f'<h5>{x}</h5>',
            'h6': lambda x: f'<h6>{x}</h6>',
            'ul': lambda x: f'<li>{x}</li>',
            'ol': lambda x: f'<li>{x}</li>',
            'paragraph': lambda x: f'<p>{x}</p>',
            'bold': lambda x: f'<strong>{x}</strong>',
            'italic': lambda x: f'<em>{x}</em>',
            'code': lambda x: f'<code>{x}</code>',
            'link': lambda x: f'<a href="{x[1]}">{x[0]}</a>',
            'image': lambda x: f'<img src="{x[1]}" alt="{x[0]}">',
        }

    def render(self, document: List[Dict]) -> str:
        """Render parsed document to HTML"""
        html = []
        in_list = False
        list_type = None

        # Apply extensions preprocessing
        for extension in self.extensions:
            if hasattr(extension, 'pre_render'):
                document = extension.pre_render(document)

        for element in document:
            if element['type'] in ('ul', 'ol'):
                if not in_list:
                    in_list = True
                    list_type = element['type']
                    html.append(f'<{list_type}>')
                html.append(self._render_element(element))
            else:
                if in_list:
                    in_list = False
                    html.append(f'</{list_type}>')
                html.append(self._render_element(element))

        if in_list:
            html.append(f'</{list_type}>')

        # Apply extensions postprocessing
        for extension in self.extensions:
            if hasattr(extension, 'post_render'):
                html = extension.post_render(html)

        return '\n'.join(html)

    def _render_element(self, element: Dict) -> str:
        """Render a single document element"""
        renderer = self.renderers.get(element['type'], lambda x: x)
        content = element['content']

        # Handle special cases (like links/images with multiple groups)
        if isinstance(content, str) and element['type'] in ('link', 'image'):
            content = content.split('](')
            content[1] = content[1].rstrip(')')

        return renderer(content)