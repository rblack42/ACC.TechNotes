# -*- coding: utf-8 -*-

import sys, os
import cloud_sptheme as csp

extensions = ['sphinx.ext.todo']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Roie Black\'s Tech Notes'
copyright = u'2013, Roie R. Black'
version = '1.0.1'
release = '1.0.1'
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build','Syllabus','_unpublished','**/.git','**/_meta.rst','**/_code']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'cloud'
html_theme_path = [csp.get_theme_dir()]
html_title = "Roie Black\'s Tech Notes"
html_short_title = "TechNotes"
html_logo = 'ACClogo.png'
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- Options for LaTeX output --------------------------------------------------
latex_paper_size = 'letter'
latex_font_size = '12pt'
latex_documents = [
  ('index', 'TechNotes.tex', u'Roie Black\'s Tech Notes',
   u'Roie R. Black', 'manual'),
]
latex_logo = '../../images/ACClogo.png'
# Additional stuff for the LaTeX preamble.
latex_preamble = ''
