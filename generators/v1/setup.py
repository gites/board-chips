from distutils.core import setup
import py2exe

setup(
    console=[{'script': 'gen4.py'}, {'script': 'colorizer.py'}, {'script': 'icon-indexer.py'}, {'script': 'icon2bw.py'}],
    options={
        'py2exe': 
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'gzip'],
        }
    }
)