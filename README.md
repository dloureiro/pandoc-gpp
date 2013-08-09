# pandoc-gpp

`pandoc-gpp` is a wrapper aroung `pandoc` and `gpp` allowing pandoc users who want to go from markdown to pdf/html to :

 * include files
 * add missing features : underline, color
 * include code directly
 * include images with specific ratio
 * include graphs
 * include tables based on csv files

The code is still evolving to cope with different type of limitations of the markdown specifications.

# Installation

## Python dependencies

`pandoc-gpp` depends on three external python packages :

 * **pygal** (version >= 1.0.0) for the generation of graphs in svg
 * **CairoSVG** (version >= 0.5) for the conversion of png from svg
 * **cssselect** (version >= 0.8) extra dependency for CairoSVG

These dependencies will be installed (if not present) during the installation of `pandoc-gpp`.

## Prerequisites

To use `pandoc-gpp` some packages are required : **python** (version 2.6 is ok). It's needed to run `pandoc-gpp` (which is written in python), **python-dev**, **python-cairo**, **gpp**, **build-essential** (you need a gcc compiler), **libxslt1-dev** (cairosvg needs lxml which needs xslt and libxml2)

## Installation

To install `pandoc-gpp`, simply do :

```
$ sudo python setup.py install
```

# Limitations

`pandoc-gpp` is able to manage only `markdown` input files and html` and `pdf` output files.

# License

This software is licensed under the AGPL v3.0 License. See the `COPYING` file in the top distribution directory for the full license text.
