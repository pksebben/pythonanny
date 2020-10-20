from distutils.core import setup
from distutils import sysconfig
import getpass
import configparser
import os
import site

user = getpass.getuser()
site_packages_path = site.USER_SITE
user_docs_path = os.path.expanduser('~/Documents')

# TODO: provide a cleared nanny.log -- or just have subprocess touch a nanny.log in the user docs file
setup(
    name='pythonanny',
    version='0.1',
    py_modules=['nanny'],
    data_files=[(site_packages_path, ["usercustomize.py"]), (user_docs_path, ["nanny.log"])],
)
