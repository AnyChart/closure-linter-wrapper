#!/usr/bin/env python

from closure_linter import fixjsstyle
import errorrules

if __name__ == '__main__':
    errorrules.InjectErrorReporter()
    fixjsstyle.main()
