"""Module containing instructions."""
import sys


def input_decimal(d):
    line = [ch for ch in input() if ch in '0123456789']
    if not line:
        raise ValueError(f'{line} is not a number.')
    d.push(int(line))


def input_ascii(d):
    d.push(ord(sys.stdin.read(1)))


def output_ascii(d):
    print(chr(d.pop()), end='')


def output_decimal(d):
    print(d.pop(), end='')

def swap_ends(d):
    d[0], d[-1] = d[-1], d[0]


instructions = {
    '(': lambda d: d.push(d.pop() - 1),
    ')': lambda d: d.push(d.pop() + 1),
    '-': lambda d: d.push(d.pop() - d.pop()),
    '+': lambda d: d.push(d.pop() + d.pop()),
    '[': lambda d: None,
    ']': lambda d: None,
    '/': lambda d: d.push(d.pop() // d.pop()),
    '\\': lambda d: None,
    '*': lambda d: d.push(d.pop() * d.pop()),
    '%': lambda d: d.push(d.pop() % d.pop()),
    ',': input_decimal,
    '.': output_decimal,
    ':': output_ascii,
    ';': input_ascii,
    '^': lambda d: d.push(d.pop() ^ d.pop()),
    '_': lambda d: d.pop(),
    '`': lambda d: d.push(d.end),
    '"': lambda d: None, # TODO implement debug.
    "'": lambda d: d.toggle_end(),
    '#': lambda d: d.push(0),
    '$': swap_ends,
    '!': lambda d: None,  # handled specially...
    '?': lambda d: swap_ends(d) if d.end else None,
    '@': lambda d: None,  # handled specially...
    ' ': lambda d: None,  # NO-OP
    '&': lambda d: d.push(d.pop() & d.pop()),
    '|': lambda d: d.push(d.pop() | d.pop()),
    '<': lambda d: d.push(1 if d.pop() < d.pop() else 0),
    '>': lambda d: d.push(1 if d.pop() > d.pop() else 0),
    '=': lambda d: d.push(1 if d.pop() == d.pop() else 0),
    '~': lambda d: d.push(~d.pop()),
}
