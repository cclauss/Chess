# -*- coding: utf-8 -*-

"""Exceptions used in Phantom."""

class ChessError (Exception): 
    def __init__(self, msg='No error message supplied', caller=None):
        self.msg = msg
        self.caller = caller
    
    def __str__(self):
        if self.caller is not None:
            return repr(self.msg) + " sourced at {}".format(repr(self.caller))
        else:
            return repr(self.msg) + " with no source"
    
    def __repr__(self):
        return self.__str__()

class InvalidMove (ChessError): pass
class InvalidDimension (ChessError): pass
class LogicError (ChessError): pass

