# -*- coding: utf-8 -*-
import sys
import os

# import doc.sphinx_bootstrap_theme
#import sphinx_bootstrap_theme


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../../'))
print('Looking within following pathes:')
for i in sys.path:
    print(i)

import bin.shngversion as shngversion
import plugins as pluginsversion

import datetime
import locale
locale.setlocale(locale.LC_TIME, 'de_DE.utf8')
now = datetime.datetime.now()
import calendar


# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# Disabled: , 'sphinx.ext.intersphinx'
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosummary',
  'sphinx.ext.todo',
  'sphinx.ext.ifconfig',
  'sphinx.ext.viewcode',
  'sphinx.ext.githubpages',
  'sphinx_autodoc_typehints',
  'sphinx_tabs.tabs',
  'myst_parser']
#  'rst2pdf.pdfbuilder']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Markdown Support via MyST
# without the following, we will get warnings from Parsing old Readme.md as described in
# https://myst-parser.readthedocs.io/en/latest/using/howto.html#suppress-warnings
suppress_warnings = ["myst.header"]

# Not used any more
#from recommonmark.parser import CommonMarkParser

# for autostructify
#import recommonmark
#from recommonmark.transform import AutoStructify

# deprecated: source_parsers = { '.md': CommonMarkParser }

# The suffix of source filenames.
# deprecated: source_suffix = ['.md','.rst']

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# To get rid of the ¶ sign on descriptions over a box
#html_add_permalinks = "" is deprecated since version 3.5
html_permalinks = True

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = '1.3c'
shversion = shngversion.get_shng_main_version()

# General information about the project.
#project = u'SmartHomeNG'
project = u'Dokumentation '
copyright = u'2016-2024 SmartHomeNG Team  -  SmartHomeNG is based on smarthome.py © Marcus Popp'

# The full version, including alpha/beta/rc tags.
#release = '1.3a dev (as of 13. October 2017)'  13. October 2017 is replaced by makefile with a date in the form of '2. September 2017'
#release = '1.3c dev (as of 13. October 2017)'
#
#plgrelease = '1.3c dev (as of 13. October 2017)'
if os.path.isfile(os.getcwd()+'/doc_version.flg'):
    release = '1.4.x'
    with open(os.getcwd()+'/doc_version.flg', encoding='UTF-8') as f:
        release = f.readline()
    branch = 'master'
    commit = ''
    comit_short = ''
    describe = ''
else:
    release = shngversion.get_shng_docversion()
    commit, commit_short, branch, describe = shngversion._get_git_data()
if branch == 'master':
  release += ' (Stand ' + shngversion.get_shng_version_date() + ')'
else:
    release += ' (Stand ' + now.strftime("%-d. %B %Y") + ', commit '+commit_short + ')'
#release = sphinx_bootstrap_theme.__version__

plgrelease = shngversion.get_shng_plugins_version()
plgbranch = pluginsversion.plugin_branch()
if plgbranch != 'master':
    copyright = u'2016-2024 SmartHomeNG Team  -  ACHTUNG: Dokumentation zum Develop Branch - Work in Progress'
    plgrelease += ' ' + plgbranch
version = plgrelease

if plgrelease > shversion:
    project += plgrelease
else:
    project += shversion

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None
#for multi language (of developer documentation)
language = 'de'
locale_dirs = ['locale/']
gettext_compact = True

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
#exclude_patterns = ['plugins/backend_shng_1_3', 'plugins/backend/static', '._*']
#exclude_patterns = ['plugins/deprecated_plugins', 'plugins/backend_shng_1_3/static', 'plugins/backend/static', '**/._*md']
#exclude_patterns = ['**/._*.rst', '**/priv_*', '**/user_doc_en.rst', 'plugins/deprecated_plugins', 'modules/http/webif/gstatic', 'plugins/blockly/webif/static', '**/_pv_*', '**/pv_*', '**/._*md', '**/developer_doc.*']
exclude_patterns = ['**/._*.rst', '**/priv_*', '**/user_doc_en.rst', 'plugins/deprecated_plugins', 'modules/http/webif/gstatic', 'plugins/blockly/webif/static', '**/_pv_*', '**/pv_*', '**/._*md']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Options for HTML output ---------------------------------------------------

def setup(app):
# deprecated in Sphinx 4: app.add_stylesheet('custom.css')
    app.add_css_file('custom.css')

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'navigation_depth': 5,
}


# Add any paths that contain custom themes here, relative to this directory.
# ``get_html_theme_path`` returns a list, so you can concatenate with
# any other theme directories you would like.
#html_theme_path = doc.sphinx_bootstrap_theme.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = "Demo"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = "_static/img/logo_long_inverse3.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None
html_favicon = "_static/img/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_static/img","_static/css"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
#html_sidebars = {'plugins/**': ['localtoc.html'],
#                 'install': ['localtoc.html'],
#                 'logic': ['localtoc.html'],
#                 'config': ['localtoc.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'SmartHomeNGDoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# for autostructify
#def setup(app):
#    app.add_config_value('recommonmark_config', {
#            'url_resolver': lambda url: github_doc_root + url,
#            'auto_toc_tree_section': 'Contents',
#            }, True)
#    app.add_transform(AutoStructify)


# -- Options for PDF output via rst2pdf ---------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document. For example:
#
# ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
#
# would mean that specific document would be compressed
# regardless of the global 'pdf_compressed' setting.
pdf_documents = [
 ('index', 'SmartHomeNG', 'SmartHomeNG', 'SmartHomeNG Team'),
]
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'kerning', 'a4']
# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']
# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
# pdf_language = "en_US"
pdf_language = "de_DE"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
# pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
# pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0
pdf_verbosity = 1

# If false, no index is generated.
# pdf_use_index = True
pdf_use_index = False

# If false, no modindex is generated.
# pdf_use_modindex = True
pdf_use_modindex = False

# If false, no coverpage is generated.
# pdf_use_coverpage = True

# Name of the cover page template to use
# pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules
# pdf_extensions = []

# Page template name for "regular" pages
# pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
# pdf_use_toc = True

# How many levels deep should the table of contents be?
pdf_toc_depth = 9999

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True
