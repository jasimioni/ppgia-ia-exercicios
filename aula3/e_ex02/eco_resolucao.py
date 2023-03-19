#!/usr/bin/env python3

import random

class Tile():
    def __init__(self, id):
        self.id = id
        self.on_top_of_me = None

    def __repr__(self):
        return self.id

    def fmt(self, width):
        return '-' * width

    def is_free(self):
        if self.on_top_of_me is None:
            return True
        return False
    
    def free(self):
        self.on_top_of_me = None
    
    def set_on_top_of_me(self, piece):
        if not self.is_free():
            raise Exception(f"{self.id} is not free")
        self.on_top_of_me = piece

class Piece(Tile):
    def __init__(self, id, size):
        super().__init__(id)
        self.size = size
        self.on_top_of = None

    def set_objective(self, objective):
        self.objective = objective

    def fmt(self, width):
        return ('#' * self.size).center(width)

    def is_satisfied(self):
        if self.on_top_of == self.objective:
            return True

    def set_on_top_of(self, item):
        if item == self:
            raise Exception("On top of self")
        
        top = self.on_top_of_me 

        while top is not None:
            if top == item:
                raise Exception("Can't be on top of my top or someone above")
            top = top.on_top_of_me

        item.set_on_top_of_me(self) # Set myself on top of item

        if self.on_top_of is not None:
            self.on_top_of.free()

        self.on_top_of = item

def random_position(tiles, pieces):
    all = [ *tiles, *pieces ]
    for piece in pieces:
        print(f'Trying to position {piece}')
        limit = 10
        while piece.on_top_of is None:
            print(f'Attempt {11 - limit}')
            if limit == 0:
                print("Giving up")
                return
            limit -= 1
            pick = random.choice(all)
            try:
                print(f'\tTrying to place {piece} on top of {pick}')
                piece.set_on_top_of(pick)
                print(f'\t{piece} is on top of {pick}\n')
            except Exception as e:
                print(f'\t{e}')

def print_status(tiles, pieces):
    tile_size = max([ piece.size for piece in pieces ])

    lines = [ tiles ]

    while True:
        stop = True
        new_line = []
        for item in lines[-1]:
            if item is not None:
                new_line.append(item.on_top_of_me)
                if item.on_top_of_me is not None:
                    stop = False
            else:
                new_line.append(None)
        if stop:
            break

        lines.append(new_line)

    for line in reversed(lines):
        line_str = ' '.join( list(map(lambda x: ' ' * tile_size if x is None else x.fmt(tile_size), line)) )
        print(line_str)


if __name__ == '__main__':
    tile_count = 5
    piece_count = 15

    tiles = []
    for x in range(tile_count):
        tiles.append(Tile(f'Tile_{x+1}'))

    pieces = []
    for x in range(piece_count):
        pieces.append(Piece(f'Piece_{x+1}', x * 2 + 1))
    
    random_position(tiles, pieces)
    print_status(tiles, pieces)
    