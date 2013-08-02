from setuptools import setup
setup(name='pandoc-gpp',
      version='0.2',
      scripts=['bin/pandoc-gpp'],
      data_files=[('include', ['include/macros.gpp', 'include/html.gpp', 'include/latex.gpp']),
      ('share/bin', ['share/bin/evaluateExpression.py','share/bin/generate_tabular.py', 'share/bin/generate_graph.py', 'share/bin/includeFile.py']),
      ('share/doc/pandoc-gpp-readme.md', ['README.md'])],
      description='pandoc-gpp is wrapper around pandoc and gpp to provide mode functionalities to pandoc users',
      author='David Loureiro',
      author_email='david.loureiro1@gmail.com',
      url='https://github.com/dloureiro/pandoc-gpp',
      install_requires=["pygal>=1.0.0", "CairoSVG>=0.5", "cssselect"]
      )