# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Ad-Hoc Backup Restore ("abr") with Ansible'
copyright = 'none. Dedicated to Public Domain'
author = 'Emerson Rocha'

# The full version, including alpha/beta/rc tags
release = '2020'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
# html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]

html_theme_options = {
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    # 'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    # 'css/custom.css',
    'custom.css',
]

def setup(app):
    app.add_stylesheet("css/theme.css")
    app.add_stylesheet("css/custom.css")


# See https://www.sphinx-doc.org/en/master/usage/configuration.html?highlight=master_doc
master_doc = 'index'