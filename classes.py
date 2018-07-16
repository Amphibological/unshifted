"""Module containing classes for Unshifted."""
from collections import deque


class ProgramEnd(Exception):
    pass


class UnshiftedDeque:
    def __init__(self, iterable=None):
        super().__init__()
        self.dp_left_side = False
        self.ip_left_side = True
        self.deq = deque(iterable if iterable else [])
    
    def push(self, val):
        if self.dp_left_side:
            self.deq.appendleft(val)
        else:
            self.deq.append(val)
    
    def pop(self):
        if self:
            if self.dp_left_side:
                return self.deq.popleft()
            else:
                return self.deq.pop()
        else:
            return 0
    
    @property
    def end(self):
        try:
            if self.dp_left_side:
                return self.deq[0]
            else:
                return self.deq[-1]
        except IndexError:
            return 0
    
    @end.setter
    def end(self, val):
        if self.dp_left_side:
            self.deq[0] = val
        else:
            self.deq[-1] = val
    
    def toggle_end(self):
        self.dp_left_side = not self.dp_left_side
    
    def toggle_ins_end(self):
        self.ip_left_side = not self.ip_left_side
    
    def pop_ins(self):
        if self.ip_left_side:
            return self.deq.popleft()
        else:
            return self.deq.pop()
    
    def __bool__(self):
        return bool(self.deq)
