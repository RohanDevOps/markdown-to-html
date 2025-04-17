import re
from typing import List, Dict


class TableExtension:
    def preprocess(self, document: List[Dict]) -> List[Dict]:
        new_document = []
        i = 0
        while i < len(document):
            element = document[i]

            # Check for table start
            if (i + 1 < len(document) and
                    element['type'] == 'paragraph' and
                    '|' in element['content'] and
                    '|' in document[i + 1]['content'] and
                    re.match(r'^[\s\|:-]+$', document[i + 1]['content'])):

                # Parse table header
                headers = [h.strip() for h in element['content'].split('|') if h.strip()]
                alignments = self._parse_alignments(document[i + 1]['content'])

                # Parse table rows
                rows = []
                i += 2  # Skip header and alignment row
                while i < len(document) and '|' in document[i]['content']:
                    row = [c.strip() for c in document[i]['content'].split('|') if c.strip()]
                    if len(row) == len(headers):
                        rows.append(row)
                    i += 1

                # Add table to document
                new_document.append({
                    'type': 'table',
                    'headers': headers,
                    'alignments': alignments,
                    'rows': rows
                })
                continue

            new_document.append(element)
            i += 1

        return new_document

    def _parse_alignments(self, alignment_row: str) -> List[str]:
        alignments = []
        for cell in alignment_row.split('|'):
            cell = cell.strip()
            if cell.startswith(':') and cell.endswith(':'):
                alignments.append('center')
            elif cell.endswith(':'):
                alignments.append('right')
            else:
                alignments.append('left')
        return alignments

    def post_render(self, html_lines: List[str]) -> List[str]:
        new_html = []
        for line in html_lines:
            if isinstance(line, dict) and line.get('type') == 'table':
                table_html = self._render_table(line)
                new_html.append(table_html)
            else:
                new_html.append(line)
        return new_html

    def _render_table(self, table: Dict) -> str:
        html = ['<table>']

        # Table header
        html.append('<thead><tr>')
        for header, align in zip(table['headers'], table['alignments']):
            html.append(f'<th style="text-align: {align}">{header}</th>')
        html.append('</tr></thead>')

        # Table body
        html.append('<tbody>')
        for row in table['rows']:
            html.append('<tr>')
            for cell, align in zip(row, table['alignments']):
                html.append(f'<td style="text-align: {align}">{cell}</td>')
            html.append('</tr>')
        html.append('</tbody>')

        html.append('</table>')
        return '\n'.join(html)