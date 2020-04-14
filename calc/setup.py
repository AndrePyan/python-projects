#.exe con python setup

from distutils.core import setup
import py2exe

setup(name="Calc",
 version="1.0",
 description="Nada",
 author="andre",
 author_email="email del autor",
 url="wev",
 license="gpl",
 scripts=["calculadora.py"],
 console=["calculadora.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)