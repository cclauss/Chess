# -*- coding: utf-8 -*-

"""Read Extended Position Description (EPD) notation.

Syntax:
    
    <EPD> ::=   <Piece Placement>
           ' ' <Side to move>
           ' ' <Castling ability>
           ' ' <En passant target square>
          {' ' <operation>}
    
    <Piece Placement> ::= equal to FEN piece placement
    
    <Side to move> ::= equal to FEN side to move
    
    <Castling ability> ::= equal to FEN castling ability
    
    <En passant target square> ::= equal to FEN en passant target square
    
    <operation> ::= <opcode> {' '<operand>} ';'
    <opcode>    ::= <letter> {<letter> | <digit> | '_'} (up to 14)
    <operand>   ::= <stringOperand>
                  | <sanMove>
                  | <unsignedOperand>
                  | <ingegerOperand>
                  | <floatOperand>
    <stringOperand> ::= '"' {<char>} '"'
    <sanMove>   ::= <PieceCode> [<Disambiguation>] <targetSquare> [<promotion>] ['+'|'#']
                  | <castles>
    <castles>   ::= 'O-O' | 'O-O-O'
    <PieceCode> ::= '' | 'N' | 'B' | 'R' | 'Q' | 'K'|
    <Disambiguation> ::= <fileLetter> | <digit18>
    <targetSquare> ::= <fileLetter> <digit18>
    <fileLetter> ::= letter a-h
    <promotion> ::= '=' <PiecePromotion>
    <PiecePromotion> ::= 'N' | 'B' | 'R' | 'Q'
    <unsignedOperand> ::= <digit19> { <digit> } | '0'
    <integerOperand> ::= ['-' | '+'] <unsignedIntegerOperand>
    <floatOperand> ::= <integerOperand> '.' <digit> {<digit>}
    <digit18>   ::= An integer in range(1, 9)
    <digit19>   ::= An integer in range(1, 10)
    <digit>     ::= '0' | <digit19>
    
Opcode mneumonics:

    Mneumonic      | Meaning
    ---------------+-----------------------------------------------
    acn            | analysis count nodes
    acs            | analysis count seconds
    am             | avoid move(s)
    bm             | best move(s)
    c0             | comment (primary, also c1 - c9)
    ce             | centipawn evaluation
    dm             | direct mate fullmove count
    draw_accept    | accept a draw offer
    draw_claim     | claim a draw
    draw_offer     | offer a draw
    draw_reject    | reject a draw
    eco            | Encyclopedia of Chess Openings opening code
    fmvn           | fullmove number
    hmvc           | halfmove clock
    id             | position identification
    nic            | _New In Chess_ opening code
    noop           | no operation (equivalent of 'pass' in Python)
    pm             | predicted move
    pv             | predcted variation
    rc             | repetition count
    resign         | game resignation
    sm             | supplied move
    tcgs           | telecommunication game selector
    tcri           | telecommunication receiver identification
    tcsi           | telecommunication sender identification
    v0             | variation (primary, also v1 - v9)
"""

from Phantom.core.coord.point import Coord
from Phantom.core.pieces import ChessPiece
from Phantom.core.board import Board
from Phantom.core.players import Side
from Phantom.constants import default_halfmove, default_fullmove, save_epd
import re

opcodes = {
'acn'         : 'analysis count nodes',
'acs'         : 'analysis count seconds',
'am'          : 'avoid move(s)',
'bm'          : 'best move(s)',
'ce'          : 'centipawn evaluation',
'dm'          : 'direct mate fullmove count',
'draw_accept' : 'accept a draw',
'draw_claim'  : 'claim a draw',
'draw_offer'  : 'offer a draw',
'draw_reject' : 'reject a draw',
'eco'         : 'ECO code',
'fmvn'        : 'fullmove number',
'hmvc'        : 'halfmove clock',
'id'          : 'positition identification',
'nic'         : 'NIC code',
'noop'        : 'no operation',
'pm'          : 'predicted move',
'pv'          : 'predcted variation',
'rc'          : 'repetiton count',
'resign'      : 'resign from game',
'sm'          : 'supplied move',
'tcgs'        : 'telecommunication game selector',
'tcri'        : 'telecommunication reciever identification',
'tcsi'        : 'telecommunication sender identification',}

def _load_name(name):
    import os, inspect
    workdir = os.path.split(inspect.getfile(_load_name))[0]
    read = os.path.join(workdir, save_epd)
    with open(read, 'r') as f:
        lines = f.readlines()
    ret = None
    for line in lines:
        line = line.strip()
        if (line[0] == '#') or (line == ''):
            continue
        split = line.index(':')
        lname = line[:split]
        val = line[split+1:].strip()
        if lname == name:
            ret = val
    return ret

def listgames():
    import os, inspect
    workdir = os.path.split(inspect.getfile(listgames))[0]
    read = os.path.join(workdir, save_epd)
    with open(read, 'r') as f:
        lines = f.readlines()
    ret = []
    for line in lines:
        line = line.strip()
        if (line[0] == '#') or (line == ''):
            continue
        ret.append(line[:line.index(':')])
    return ret

def load_epd(string):
    """Load an EPD from a string and return a board with namespace variables set accordingly."""
    halfmove = str(default_halfmove)
    fullmove = str(default_fullmove)
    fields = string.split()
    layout = fields[0]
    moving = fields[1]
    castling_rights = fields[2]
    en_passant_rights = fields[3]
    operations = ' '.join(fields[4:])
    op_fields = operations.split(';')[:-1]  # remove last '' element
    fen = ' '.join([layout, moving, castling_rights, en_passant_rights, halfmove, fullmove])
    b = Board(fen=fen)
    b.data.raw_operations = operations
    b.data.op_fields = op_fields
    op_data = {}
    for operation in op_fields:
        fields = operation.strip().split()
        opcode = fields[0]
        operand = fields[1:]
        name = opcodes[opcode]
        value = operand
        op_data.update({opcode: (name, value)})
    b.data.op_data = op_data
    if 'fmvn' in op_data:
        b.fullmove_clock = int(op_data['fvmn'])
    if 'hmvc' in op_data:
        b.halfmove_clock = int(op_data['hmvc'])
    return b

