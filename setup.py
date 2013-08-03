from setuptools import setup

setup(name='pandoc-gpp',
      version='0.2.2',
      scripts=['bin/pandoc-gpp'],
      data_files=[
            ('include', ['include/macros.gpp', 'include/html.gpp', 'include/latex.gpp']),
            ('share/bin', ['share/bin/evaluateExpression.py','share/bin/generate_tabular.py', 'share/bin/generate_graph.py', 'share/bin/includeFile.py']),
            ('share/doc/pandoc-gpp-readme', ['README'])
            ],
      description='pandoc-gpp is wrapper around pandoc and gpp to provide mode functionalities to pandoc users',
      author='David Loureiro',
      author_email='david.loureiro1@gmail.com',
      url='https://github.com/dloureiro/pandoc-gpp',
      install_requires=["pygal>=1.0.0", "CairoSVG>=0.5", "cssselect"],
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Console',
      'Intended Audience :: Education',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU Affero General Public License v3',
      'Natural Language :: English',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX',
      'Programming Language :: Python',
      'Topic :: Documentation',
      'Topic :: Internet :: WWW/HTTP',
      'Topic :: Multimedia :: Graphics',
      'Topic :: Software Development :: Documentation',
      'Topic :: Text Editors :: Documentation',
      'Topic :: Text Editors :: Text Processing',
      'Topic :: Text Processing :: Markup :: HTML',
      'Topic :: Text Processing :: Markup :: LaTeX',
      'Topic :: Utilities']
      )