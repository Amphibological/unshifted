"""A unique esoteric programming language with self-modifying code that uses a deque."""
__version__ = '0.1'

import click

from instructions import instructions
from classes import UnshiftedDeque, ProgramEnd


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
    loop_mode = False

    while deq:
        ins = chr(deq.pop_ins())
        if loop_mode:
            if ins != '}':
                loop_queue.push(ins)
            else:
                loop_mode = False
                for _ in range(deq.pop()):
                    try:
                        for ch in loop_queue.deq:
                            execute(ch, deq)
                    except ProgramEnd:
                        break
        elif ins == '{':
            loop_mode = True
        elif ins in instructions or ins in '!@0123456789':
            try:
                execute(ins, deq)
            except ProgramEnd:
                break
        else:
            raise SyntaxError(f'Invalid char {ins}.')


def execute(ins, deq):
    """Executes a single Unshifted instruction on deq."""
    if ins == '!':
        deq.toggle_ins_end()
    elif ins == '@':
        raise ProgramEnd()
    elif ins in '0123456789':
        deq.push((deq.pop() * 10) + int(ins))
    else:
        instructions[ins](deq)


def lex(prog):
    """Convert raw string into deque of codepoints."""
    
    return UnshiftedDeque(map(ord, prog))


def main():
    unshifted()


if __name__ == '__main__':
    main()