#!/usr/bin/env python3

import random
import time
import logging
import sys
import argparse

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))

# Avoid using strings all the time
BS, BF, F, S = 'BS', 'BF', 'F', 'S'

# Tile():
# Base class - can check if it's free and can receive a piece on top of it
class Tile():
    def __init__(self, id):
        self.id = id
        self.above_me = None

    def __repr__(self):
        return self.id

    def fmt(self, width):
        return '-' * width

    def is_free(self):
        if self.above_me is None:
            return True
        return False
    
    def free(self):
        self.above_me = None
    
    def set_above_me(self, piece):
        if not self.is_free():
            raise Exception(f"{self.id} is not free")
        self.above_me = piece

# Piece():
# Extendes the base class (Tile) and add the methods to move, check if satisfied, set status and objective
class Piece(Tile):
    def __init__(self, id, size, fmt_names=False, restrictions=set()):
        super().__init__(id)
        self.size = size
        self.below_me = None
        self.state = ['BS']
        self.temp_restrictions = set([])
        self.perm_restrictions = restrictions
        self.aggressed = False
        self.fmt_names = fmt_names

    def set_objective(self, objective):
        self.objective = objective

    def fmt(self, width):
        if self.fmt_names:
            return self.id.center(width)
        return ('#' * self.size).center(width)

    def is_satisfied(self):
        if self.below_me == self.objective:
            return True
        
    def details(self):
        return f'{self.id}, Objective: {self.objective}, Restrictions: {self.restrictions}, State: {self.state}, Aggressed: {self.aggressed}'

    @property
    def restrictions(self):
        return self.temp_restrictions.union(self.perm_restrictions)

    @property
    def BS(self):
        return self.state[-1] == BS

    @property
    def BF(self):
        return self.state[-1] == BF

    @property
    def S(self):
        return self.state[-1] == S

    @property
    def F(self):
        return self.state[-1] == F

    def set_BF(self):
        if not self.BF:
            self.state.append(BF)

    def set_BS(self):
        if not self.BS:
            self.state.append(BS)

    def set_F(self):
        if not self.F:
            self.state.append(F)

    def set_S(self):
        if not self.S:
            self.state.append(S)

    def clear_restrictions(self):
        self.temp_restrictions = set([])
        self.aggressed = False

    def aggress_blocker(self):
        self.above_me.aggressed = True
        self.above_me.set_BF()
        self.above_me.restrictions.update([ self.objective, self ])
    
    def move(self, item):
        if item == self:
            raise Exception("Can't be on top of myself")       

        # Look up to see if I'm trying to be on top of someone above_me me
        top = self.above_me 
        while top is not None:
            if top == item:
                raise Exception("Can't be on top of my top or someone above_me")
            top = top.above_me
 
        # Tell the item I'm on top of it
        item.set_above_me(self)

        # I moved, so let's free who I was blocking before
        if self.below_me is not None:
            self.below_me.free()

        # Now let's register who I'm on top of
        self.below_me = item

def teacher_position():
    tiles = []
    for x in range(3):
        tiles.append(Tile(f'T{x+1}'))

    t1, t2, t3 = tiles

    pieces = [
        Piece('A', 1, fmt_names=True),
        Piece('B', 3, fmt_names=True),
        Piece('C', 5, fmt_names=True),
    ]

    a, b, c = pieces

    a.set_objective(c)
    b.set_objective(t3)
    c.set_objective(b)

    a.move(t2)
    b.move(a)
    c.move(b)

    return tiles, pieces

# random_position:
# Takes all the tiles and pieces and generates a random positioning of the pieces
def random_position(tile_count, piece_count, disks):
    tiles = []
    for x in range(tile_count):
        tiles.append(Tile(f'T{x+1:02}'))

    pieces = []
    for x in range(piece_count):
        pieces.append(Piece(f'P{x+1:02}', x * 2 + 1))
    
    for x in range(piece_count - 1):
        pieces[x].set_objective(pieces[x+1])
    
    pieces[-1].set_objective(tiles[-1])
    all = [ *tiles, *pieces ]
    for piece in pieces:
        logger.debug(f'Trying to position {piece}')
        limit = 30
        count = 1
        for pick in random.sample(all, len(all)):
            try:
                logger.debug(f'\tTrying to place {piece} on top of {pick}')
                piece.move(pick)
                logger.debug(f'\t{piece} is on top of {pick}\n')
                break
            except Exception as e:
                logger.debug(f'\t{e}')
    
    return tiles, pieces

# default_position:
# Setup a default position on tile1
def default_position(tile_count, piece_count, disks):
    tiles = []
    for x in range(tile_count):
        tiles.append(Tile(f'T{x+1:02}'))

    pieces = []
    for x in range(piece_count):
        pieces.append(Piece(f'P{x+1:02}', x * 2 + 1))
    
    for x in range(piece_count - 1):
        pieces[x].set_objective(pieces[x+1])
        pieces[x].move(pieces[x+1])

    pieces[-1].set_objective(tiles[-1])
    pieces[-1].move(tiles[0])

    if disks:
        for x in range(1, piece_count):
            for y in range(piece_count-1):
                pieces[x].perm_restrictions.add(pieces[y])

    return tiles, pieces

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
                new_line.append(item.above_me)
                if item.above_me is not None:
                    stop = False
            else:
                new_line.append(None)
        if stop:
            break

        lines.append(new_line)

    for line in reversed(lines):
        line_str = ' '.join( list(map(lambda x: ' ' * tile_size if x is None else x.fmt(tile_size), line)) )
        logger.info(line_str)

    #for piece in pieces:
    #    print(piece.details())

def solver(tiles, pieces, delay=False):
    all = [ *tiles, *pieces ]

    logger.info("Starting solver - initial status:\n")
    print_status(tiles, pieces)
    logger.info('')

    moves = []

    limit = 1
    while sum([ piece.S for piece in pieces ]) < len(pieces):
        if delay:
            time.sleep(1)
        if limit == 500:
            break
        logger.info(f"Execution {limit}")
        limit += 1
        for piece in pieces:
            logger.debug(piece.details())
            if piece.aggressed and not piece.BF:
                piece.set_BF()
            elif piece.BS:
                if piece.objective == piece.below_me:
                    piece.set_S()
                else:
                    if piece.is_free():
                        # Free to move,trying to move to objective
                        if piece.objective.is_free():
                            piece.move(piece.objective)
                            moves.append([ piece, piece.objective ])
                            logger.debug(f"=====> Moving {piece} over {piece.objective}")
                            piece.set_S()
                    else:
                        piece.aggress_blocker()
            elif piece.F:
                piece.set_BS()
            elif piece.BF:
                if piece.is_free():
                    if piece.objective.is_free() and piece.objective not in piece.restrictions:
                        piece.move(piece.objective)
                        moves.append([ piece, piece.objective ])
                        logger.debug(f"=====> Moving {piece} over {piece.objective}")
                        piece.set_F()
                        piece.clear_restrictions()
                    else:
                        for option in all:
                            if option != piece and option.is_free() and option not in piece.restrictions:
                                piece.move(option)
                                moves.append([ piece, option ])
                                logger.debug(f"=====> Moving {piece} over {option}")
                                piece.set_F()
                                piece.clear_restrictions()
                                break
                else:
                    piece.aggress_blocker()
        logger.info('')
        print_status(tiles, pieces)
        logger.info('')

    return moves

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--debug",
        help="Print additional information",
        action='store_true'
    )

    parser.add_argument(
        "--class_example",
        help="Create the Pieces as the class example (3 tiles, 3 pieces)",
        action='store_true'
    )

    parser.add_argument(
        "--tiles",
        help="Number o tiles to create",
        default=5
    )

    parser.add_argument(
        "--pieces",
        help="Number o pieces to create",
        default=9
    )

    parser.add_argument(
        "--delay",
        help="Add a delay between steps",
        action='store_true'
    )

    parser.add_argument(
        "--random",
        help="Randomize pieces positions",
        action='store_true'
    )

    parser.add_argument(
        "--disks",
        help="Add a perm restriction - bigger disks can't go over smaller ones",
        action='store_true'
    )

    args = parser.parse_args()

    logger.setLevel(logging.INFO)
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    if args.class_example:
        logger.info(f'Loading default class example')
        tiles, pieces = teacher_position()
    elif args.random:
        logger.info(f'Creating random setup with {args.tiles} tiles and {args.pieces} pieces')
        tiles, pieces = random_position(int(args.tiles), int(args.pieces), args.disks)
    else:
        logger.info(f'Creating default setup with {args.tiles} tiles and {args.pieces} pieces')
        tiles, pieces = default_position(int(args.tiles), int(args.pieces), args.disks)

    for piece in pieces:
        logger.info(f'{piece} has objective {piece.objective}')

    logger.info("\n\n")

    moves = solver(tiles, pieces, delay=args.delay)

    logger.info("\n#############\nFinal result:\n#############\n")

    for piece in pieces:
        logger.info(piece.details())

    logger.info('')
    print_status(tiles, pieces)

    print("\nList of movements:\n------------------\n")
    logger.info(' | '.join(f'Moved {move[0]} over {move[1]}' for move in moves))
    
