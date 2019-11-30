from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")

name    = "PyBuilderRestAPI"
version = "1.0"

requires_python = ">=2.7,<3.7"

summary = "Example PyBuilder / Git project"
url     = "https://github.com/Udayaprasad/PyBuilderRestAPI"

description = """ This WebService is responsible for returning filtered quotes by movie and character fields """

authors      = [Author("Uday Vakalapudi", "uday.vakalapudi@gmail.com")]
license      = "None"
default_task = "publish"

@init
def initialize(project):
    project.depends_on("requests", "==2.22.0")
    project.depends_on("configparser", "==4.0.2")
    project.depends_on("Flask", "==1.1.1")
    project.depends_on("urllib3", "==1.25.7")
    project.depends_on("parameterized", "==0.7.1")


@init
def set_properties(project):
    pass
