class ChessError (Exception): pass

class InvalidMove (ChessError): pass
class InvalidDimension (ChessError): pass
class LogicError (ChessError): pass
