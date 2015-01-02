Sally
=====

Checks the status of all repositories in subdirectories.

Sally goes into every subdirectory to see if there's a git and/or a mercurial repo. In case there is one (there may be
both!), sally runs :code:`git/hg status` to see if there's any uncommited changes.
