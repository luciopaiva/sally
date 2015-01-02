"""
Sally
Check status of all repositories in subdirectories.
Goes into every subdirectory to see if there's a git and/or a mercurial repo. In case there is one, run ``git status``
and see if there's any uncommited changes.
"""
# TODO also check if there's any pending pushes relative to the 'origin' remote

import subprocess
import argparse
import os

from sally.lib.color import Color

_arguments = None


def get_subdirectories(root):
    """
    :param root: a string, the path to the root directory
    :return: a list of subdirectories
    """
    t = next(os.walk(root))
    subdirs = t[1]
    return subdirs


def vcs_status(vcs, command, root):
    """
    :param vcs: a string, name of the versioning control system
    :param command: list of parameters to run
    :param root: a string, the path to the root directory
    :return:
    """
    title = '{} ({})'.format(Color.green(root), Color.yellow(vcs))
    try:
        os.chdir(root)
        output = subprocess.check_output(command).decode('utf-8')

        lines = output.splitlines()
        if _arguments.all_directories or len(lines) > 0:
            print(title)
            for line in lines:
                print(Color.reset('\t' + line))
    except subprocess.CalledProcessError:
        print(title)
        print(Color.red('\tNot a valid {} repo'.format(vcs)))
    except FileNotFoundError:
        print('{} was not found. You need to install it in your system first.'.format(vcs))
        exit(1)


def hg_status(root):
    vcs_status('mercurial', ['hg', 'status', '--color', 'never', '--pager', 'never'], root)


def git_status(root):
    vcs_status('git', ['git', 'status', '-s', '--porcelain'], root)


def repo_status(root, parent):

    is_versioned = False
    subdirs = get_subdirectories(root)

    if _arguments.git and '.git' in subdirs:
        git_status(root)
        os.chdir(parent)
        is_versioned = True

    if _arguments.mercurial and '.hg' in subdirs:  # Do not use elif here; a directory may use both git and hg.
        hg_status(root)
        os.chdir(parent)
        is_versioned = True

    if not is_versioned and _arguments.all_directories:
        print('{}\n\t{}'.format(Color.green(root), Color.cyan('No repository here.')))


def repo_all_status(root):
    """
    :param root: a string, the path to the root directory
    """
    for subdir in get_subdirectories(root):
        repo_status(subdir, root)


def parse_args():
    global _arguments

    parser = argparse.ArgumentParser(description="Check status of all git/hg repositores in subdirectories.")
    parser.add_argument('-a', '--all', action='store_true', dest='all_directories',
                        help='Show info on all folders, including those that are clean or doesn\'t have a repo.')
    parser.add_argument('-g', '--git', action='store_true', help='Check only git repos.')
    parser.add_argument('-m', '--mercurial', action='store_true', help='Check only mercurial repos.')
    _arguments = parser.parse_args()

    # If neither git nor hg were specified, default to check both:
    if not (_arguments.git or _arguments.mercurial):
        _arguments.git = True
        _arguments.mercurial = True


#if __name__ == '__main__':
def main():
    parse_args()
    repo_all_status(os.getcwd())
