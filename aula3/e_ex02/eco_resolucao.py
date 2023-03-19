#!/usr/bin/env python3

import random

# Tile():
# Base class - can check if it's free and can receive a piece on top of it
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

# Piece():
# Extendes the base class (Tile) and add the methods to move, check if satisfied, set status and objective
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
            raise Exception("Can't be on top of myself")       

        # Look up to see if I'm trying to be on top of someone above me
        top = self.on_top_of_me 
        while top is not None:
            if top == item:
                raise Exception("Can't be on top of my top or someone above")
            top = top.on_top_of_me
 
        # Tell the item I'm on top of it
        item.set_on_top_of_me(self)

        # I moved, so let's free who I was blocking before
        if self.on_top_of is not None:
            self.on_top_of.free()

        # Now let's register who I'm on top of
        self.on_top_of = item

# random_position:
# Takes all the tiles and pieces and generates a random positioning of the pieces
def random_position(tiles, pieces):
    all = [ *tiles, *pieces ]
    for piece in pieces:
        print(f'Trying to position {piece}')
        limit = 30
        count = 1
        for pick in random.sample(all, len(all)):
            try:
                print(f'\tTrying to place {piece} on top of {pick}')
                piece.set_on_top_of(pick)
                print(f'\t{piece} is on top of {pick}\n')
                break
            except Exception as e:
                print(f'\t{e}')

# print_status:
# Print the current positioning (Tiles and Pieces)
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
        tiles.append(Tile(f'Tile{x+1:02}'))

    pieces = []
    for x in range(piece_count):
        pieces.append(Piece(f'Piece{x+1:02}', x * 2 + 1))
    
    for x in range(piece_count - 1):
        pieces[x].set_objective(pieces[x+1])
    
    pieces[-1].set_objective(tiles[-1])

    random_position(tiles, pieces)

    for piece in pieces:
        print(f'{piece} has objective {piece.objective}')

    print("\n\n")

    print_status(tiles, pieces)
    