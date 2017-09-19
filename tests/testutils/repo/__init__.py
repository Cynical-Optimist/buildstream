from collections import OrderedDict
import pytest
from ..site import HAVE_OSTREE

from .git import Git
from .bzr import Bzr
from .ostree import OSTree
from .tar import Tar

ALL_REPO_KINDS = OrderedDict()
ALL_REPO_KINDS['git'] = Git
ALL_REPO_KINDS['bzr'] = Bzr
ALL_REPO_KINDS['ostree'] = OSTree
ALL_REPO_KINDS['tar'] = Tar


# create_repo()
#
# Convenience for creating a Repo
#
# Args:
#    kind (str): The kind of repo to create (a source plugin basename)
#    directory (str): The path where the repo will keep a cache
#
def create_repo(kind, directory):
    try:
        constructor = ALL_REPO_KINDS[kind]
    except KeyError as e:
        raise AssertionError("Unsupported repo kind {}".format(kind)) from e

    return constructor(directory)
