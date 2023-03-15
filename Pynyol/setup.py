from distutils.core import setup

setup(
    name='Pynyol',
    version='0.1.0',
    author='Juanma López',
    author_email='lopezjuanma96@gmail.com',
    packages=['pynyol', 'pynyol.test'],
    scripts=['bin/express_a_num.py'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Package aimed at helping with processing the spanish language.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)