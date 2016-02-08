#!/usr/bin/env python

from closure_linter import gjslint
import errorrules

if __name__ == '__main__':
    errorrules.InjectErrorReporter()
    gjslint.main()
