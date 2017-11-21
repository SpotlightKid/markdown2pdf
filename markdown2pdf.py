#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""Convert Markdown markup text to a PDF file.

Converts Markdown text to HTML with Python, using markdown2_ to convert the
Markdown source to HTML first and the output then to PDF with xhtml2pdf_.

"""

__all__ = (
    'DEFAULT_CSS',
    'DEFAULT_EXTRAS',
    'html2pdf',
    'markdown2pdf'
)

import logging
import os
import sys

from markdown2 import markdown
from xhtml2pdf import pisa
from xhtml2pdf.default import DEFAULT_CSS


__author__ = 'Christopher Arndt'
__version__ = '0.1.0'

DEFAULT_CSS += """\
html {
    font-family: Times New Roman, serif;
    font-size: 14pt;
}

pre,
code,
kbd,
samp,
tt {
    font-size: 12pt;
}

"""

DEFAULT_EXTRAS = [
    'fenced-code-blocks',
    'footnotes',
    'metadata',
    'pyshell',
    'smarty-pants',
    'tag-friendly',
    'wiki-tables'
]


def html2pdf(html, filename, css=DEFAULT_CSS):
    with open(filename, "wb") as fp:
        # convert HTML to PDF
        status = pisa.CreatePDF(html, dest=fp, default_css=css)
        return status.err


def markdown2pdf(text, filename, css=DEFAULT_CSS, extras=DEFAULT_EXTRAS, **kw):
    return html2pdf(markdown(text, extras=extras, **kw), filename, css)


def main(args=None):
    logging.basicConfig(level=logging.WARNING)

    if args is None:
        args = sys.argv[1:]

    if args:
        infile = args.pop(0)
    else:
        return "Usage: markdown2pdf infile.md [outfile.pdf]"

    if args:
        outfile = args.pop()
    else:
        outfile = os.path.splitext(infile)[0] + '.pdf'

    with open(infile) as fp:
        markdown2pdf(fp.read(), outfile)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]) or 0)
