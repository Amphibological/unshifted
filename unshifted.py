"""A unique esoteric programming language with self-modifying code that uses a deque."""
__version__ = '0.1'

from collections import deque
import click

instructions = {
    '+': lambda d: d.push(d.pop() + d.pop()),
}

lq_instructions = {

}

class UnshiftedDeque(deque):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        self.left_side = True
    
    def push(self, val):
        if self.left_side:
            self.appendleft(val)
        else:
            self.append(val)
    
    def pop(self):
        if self.left_side:
            self.popleft()
        else:
            self.pop()
    
    @property
    def end(self):
        if self.left_side:
            return self[0]
        else:
            return self[-1]
    
    @end.setter
    def end(self, val):
        if self.left_side:
            self[0] = val
        else:
            self[-1] = val

def main():
    unshifted()


@click.command()
@click.option('-d', '--debug', is_flag=True, help='Print status on every debug character.')
@click.option('-D', '--full-debug', is_flag=True, help='Print status on every tick.')
@click.argument('filename', nargs=1, required=False, type=click.Path(exists=True, file_okay=True, 
    dir_okay=False, readable=True, resolve_path=True))
def unshifted(filename, debug, full_debug):
    if not filename:
        click.echo(f'Unshifted Version {__version__} by Amphibological.')
        click.echo('Please provide a file to interpret.')
        exit(0)
    with open(filename) as file:
        prog = file.read()
    deq = lex(prog)
    loop_queue = UnshiftedDeque()
    while deq:
        ins = deq.pop()
        if ins in instructions:
            instructions[ins](deq)
        else:
            lq_instructions[ins](deq, loop_queue)

    



def lex(prog):
    """Convert raw string into deque of tokens."""
    line = character = 1
    for ch in prog:
        if ch == '\n':
            line += 1
        elif ch not in instructions or ch not in lq_instructions:
            raise SyntaxError(f'Invalid character {ch} at {line}:{character}.')
        character += 1
    
    return UnshiftedDeque(prog)


if __name__ == '__main__':
    main()