
class Color:

    _colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'cyan': '\033[36m',
        'reset': '\033[39m'
    }

    @staticmethod
    def red(msg):
        return Color._colors['red'] + msg + Color._colors['reset']

    @staticmethod
    def green(msg):
        return Color._colors['green'] + msg + Color._colors['reset']

    @staticmethod
    def yellow(msg):
        return Color._colors['yellow'] + msg + Color._colors['reset']

    @staticmethod
    def cyan(msg):
        return Color._colors['cyan'] + msg + Color._colors['reset']

    @staticmethod
    def reset(msg):
        return Color._colors['reset'] + msg


__author__ = 'lucio'
