import re
from typing import List, Dict


class CodeBlockExtension:
    def preprocess(self, document: List[Dict]) -> List[Dict]:
        new_document = []
        i = 0
        while i < len(document):
            element = document[i]

            # Check for code block start
            if element['type'] == 'paragraph' and element['content'].startswith('```'):
                language = element['content'][3:].strip() or None
                code_lines = []
                i += 1

                # Collect code lines
                while i < len(document) and not document[i]['content'].startswith('```'):
                    code_lines.append(document[i]['content'])
                    i += 1

                # Add code block to document
                if i < len(document) and document[i]['content'].startswith('```'):
                    new_document.append({
                        'type': 'codeblock',
                        'language': language,
                        'content': '\n'.join(code_lines)
                    })
                    i += 1
                continue

            new_document.append(element)
            i += 1

        return new_document

    def post_render(self, html_lines: List[str]) -> List[str]:
        new_html = []
        for line in html_lines:
            if isinstance(line, dict) and line.get('type') == 'codeblock':
                code_html = self._render_codeblock(line)
                new_html.append(code_html)
            else:
                new_html.append(line)
        return new_html

    def _render_codeblock(self, codeblock: Dict) -> str:
        language = codeblock.get('language')
        code = codeblock['content']

        if language:
            return f'<pre><code class="language-{language}">{code}</code></pre>'
        return f'<pre><code>{code}</code></pre>'