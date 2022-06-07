import random
import tkinter
import json
from tkinter import Menu
from tkinter import filedialog
from tkinter.messagebox import showinfo


class Pawn:

    def __init__(self, pos, board):
        self.pos = pos
        self.color = board.getColor(pos)
        self.b = board

    def attacking(self):
        m = []
        if self.color:
            if self.pos[1] != '8':
                if abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 7][0])) < 2:
                    m.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 7])
                if abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 9][0])) < 2:
                    m.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 9])
        else:
            if self.pos[1] != '1':
                if abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 7][0])) < 2:
                    m.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 7])
                if abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 9][0])) < 2:
                    m.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 9])

        return m

    def legal(self):
        moves = []
        if self.color:
            a = self.b.getColor(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 7])
            b = self.b.getColor(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 9])
            if a == False and abs(
                    ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 7][0])) < 2:
                moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 7])
            if b == False and abs(
                    ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 9][0])) < 2:
                moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 9])
            if '2' in self.pos:
                a = self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 8]
                b = self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 16]
                if self.b.isOccupied(b):
                    if self.b.isOccupied(a) == False:
                        moves.append(a)
                elif self.b.isOccupied(a) == False:
                    moves.append(a)
                    moves.append(b)
            else:
                if self.b.SQUARE_NAMES.index(self.pos) + 8 < 64:
                    if self.b.isOccupied(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 8]) == False:
                        moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + 8])
        else:
            a = self.b.getColor(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 7])
            b = self.b.getColor(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 9])
            if a and abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 7][0])) < 2:
                moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 7])
            if b and abs(ord(self.pos[0]) - ord(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 9][0])) < 2:
                moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 9])

            if '7' in self.pos:
                a = self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 8]
                b = self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 16]
                if self.b.isOccupied(b):
                    if self.b.isOccupied(a) == False:
                        moves.append(a)
                elif self.b.isOccupied(a) == False:
                    moves.append(a)
                    moves.append(b)
            else:
                if self.b.SQUARE_NAMES.index(self.pos) - 8 > -1:
                    if self.b.isOccupied(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 8]) == False:
                        moves.append(self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) - 8])

        return moves


class Knight:
    def __init__(self, pos, board):
        self.pos = pos
        self.color = board.getColor(pos)
        self.b = board
        self.attack_protect = []

    def legal(self):
        moves = []
        possible = [15, 17, 6, 10, -15, -17, -6, -10]
        for i in possible:
            if -1 < (self.b.SQUARE_NAMES.index(self.pos) + i) < 64:
                new_pos = (self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + i])
                if abs(int(self.pos[1]) - int(new_pos[1])) < 3 and (abs(ord(self.pos[0]) - ord(new_pos[0])) < 3):
                    if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                        moves.append(new_pos)
                    self.attack_protect.append(new_pos)

        return moves

    def atprot(self):
        self.legal()
        return self.attack_protect


class Rook:
    def __init__(self, pos, board):
        self.pos = pos
        self.color = board.getColor(pos)
        self.b = board
        self.attack_protect = []

    def legal(self):
        moves = []
        # Pos -> UP
        for i in range(int(self.pos[1]) + 1, 9):
            new_pos = self.pos[0] + str(i)
            if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                moves.append(new_pos)
                self.attack_protect.append(new_pos)
                if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                    self.attack_protect.append(new_pos)
                    break
            else:
                self.attack_protect.append(new_pos)
                break

        # Pos => DOWN
        for i in range(int(self.pos[1]) - 1, 0, -1):
            new_pos = self.pos[0] + str(i)
            if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                moves.append(new_pos)
                self.attack_protect.append(new_pos)
                if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                    self.attack_protect.append(new_pos)
                    break
            else:
                self.attack_protect.append(new_pos)
                break

        # Pos => RIGHT
        for i in range(ord(self.pos[0]) + 1, 105):
            new_pos = chr(i) + self.pos[1]
            if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                moves.append(new_pos)
                self.attack_protect.append(new_pos)
                if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                    self.attack_protect.append(new_pos)
                    break
            else:
                self.attack_protect.append(new_pos)
                break
        # Pos => LEFT
        for i in range(ord(self.pos[0]) - 1, 96, -1):
            new_pos = chr(i) + self.pos[1]
            if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                moves.append(new_pos)
                self.attack_protect.append(new_pos)
                if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                    self.attack_protect.append(new_pos)
                    break
            else:
                self.attack_protect.append(new_pos)
                break

        return moves

    def atprot(self):
        self.legal()
        return self.attack_protect


class Bishop:
    def __init__(self, pos, board):
        self.pos = pos
        self.color = board.getColor(pos)
        self.b = board
        self.attack_protect = []

    def legal(self):
        moves = []
        j = int(self.pos[1]) + 1
        # Pos => UP RIGHT

        for i in range(ord(self.pos[0]) + 1, 105):
            if j < 9:
                new_pos = chr(i) + str(j)
                if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                    moves.append(new_pos)
                    self.attack_protect.append(new_pos)
                    if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                        self.attack_protect.append(new_pos)
                        break
                else:
                    self.attack_protect.append(new_pos)
                    break
                j += 1
        # pos => UP left
        j = int(self.pos[1]) + 1
        for i in range(ord(self.pos[0]) - 1, 96, -1):
            if j < 9:
                new_pos = chr(i) + str(j)
                if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                    moves.append(new_pos)
                    self.attack_protect.append(new_pos)
                    if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                        self.attack_protect.append(new_pos)
                        break
                else:
                    self.attack_protect.append(new_pos)
                    break
                j += 1

        # pos => down left
        j = int(self.pos[1]) - 1
        for i in range(ord(self.pos[0]) - 1, 96, -1):
            new_pos = chr(i) + str(j)
            if j > 0:
                if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                    moves.append(new_pos)
                    self.attack_protect.append(new_pos)
                    if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                        self.attack_protect.append(new_pos)
                        break
                else:
                    self.attack_protect.append(new_pos)
                    break
                j -= 1

        # pos => down right
        j = int(self.pos[1]) - 1
        for i in range(ord(self.pos[0]) + 1, 105):
            new_pos = chr(i) + str(j)
            if j > 0:
                if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                    moves.append(new_pos)
                    self.attack_protect.append(new_pos)
                    if self.b.isOccupied(new_pos) and self.b.getColor(new_pos) != self.color:
                        self.attack_protect.append(new_pos)
                        break
                else:
                    self.attack_protect.append(new_pos)
                    break
                j -= 1

        return moves

    def atprot(self):
        self.legal()
        return self.attack_protect


class Queen:
    def __init__(self, pos, board):
        self.pos = pos
        self.b = board

    def legal(self):
        moves = []
        for i in Rook(self.pos, self.b).legal():
            moves.append(i)
        for i in Bishop(self.pos, self.b).legal():
            moves.append(i)

        return moves

    def atprot(self):
        moves = []
        for i in Rook(self.pos, self.b).atprot():
            moves.append(i)
        for i in Bishop(self.pos, self.b).atprot():
            moves.append(i)
        return moves


class King:
    def __init__(self, pos, board):
        self.pos = pos
        self.color = board.getColor(pos)
        self.b = board

        if self.color:
            self.enemy_k = self.b.getBkPos()
        else:
            self.enemy_k = self.b.getWkPos()

    def legal(self):
        moves = []
        possible = [9, 8, 7, 1, -1, -7, -8, -9]
        for i in possible:
            if -1 < (self.b.SQUARE_NAMES.index(self.pos) + i) < 64:
                new_pos = (self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.pos) + i])
                if self.b.getColor(self.pos) != self.b.getColor(new_pos):
                    if abs(ord(self.pos[0]) - ord(new_pos[0])) < 2:
                        moves.append(new_pos)
        # kontroluje ci ten isty tah nemoze urobit kral opacnej farby
        for i in possible:
            if -1 < (self.b.SQUARE_NAMES.index(self.enemy_k) + i) < 64:
                new_pos = (self.b.SQUARE_NAMES[self.b.SQUARE_NAMES.index(self.enemy_k) + i])
                if self.b.getColor(self.enemy_k) != self.b.getColor(new_pos):
                    if abs(ord(self.enemy_k[0]) - ord(new_pos[0])) < 2:
                        if new_pos in moves:
                            moves.remove(new_pos)

        return moves


class Board(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.config(height=128 * 8, width=128 * 8)
        self.pack()

        self.IMAGE_ROOT = {
            "r": tkinter.PhotoImage(file="images/br.png"),
            "n": tkinter.PhotoImage(file="images/bn.png"),
            "b": tkinter.PhotoImage(file="images/bb.png"),
            "q": tkinter.PhotoImage(file="images/bq.png"),
            "k": tkinter.PhotoImage(file="images/bk.png"),
            "p": tkinter.PhotoImage(file="images/bp.png"),
            "R": tkinter.PhotoImage(file="images/wr.png"),
            "N": tkinter.PhotoImage(file="images/wn.png"),
            "B": tkinter.PhotoImage(file="images/wb.png"),
            "Q": tkinter.PhotoImage(file="images/wq.png"),
            "K": tkinter.PhotoImage(file="images/wk.png"),
            "P": tkinter.PhotoImage(file="images/wp.png"),
            'e': tkinter.PhotoImage(file="images/empty.png"),
            'd': tkinter.PhotoImage(file="images/dot.png"),
        }
        self.ANIMATION_IMAGES = [tkinter.PhotoImage(file=f"images/anim/{i}.png") for i in '12345678']
        self.squares = {}
        self.SQUARE_NAMES = self.makeSquareNames()
        self.selected_piece_moves = []
        self.castling_moves = []
        self.prev_sel_color = None
        self.on_turn = True
        self.sq1 = None
        self.changed_bgs = {}
        self.move_order = ['1.', ]
        self.move_counter = 1
        self.bk_pos = 'e8'
        self.wk_pos = 'e1'
        self.white_in_check = False
        self.black_in_check = False
        self.wra_moved = False
        self.wrh_moved = False
        self.bra_moved = False
        self.brh_moved = False
        self.attacked_squares_by_white = []
        self.attacked_squares_by_black = []
        self.white_pieces = {}
        self.black_pieces = {}
        self.computerColor = True

        # metody vytvarania
        self.createBoard()
        self.populateBoard()
        if self.computerColor:
            self.computerMove()

    def resetValues(self):
        self.selected_piece_moves = []
        self.castling_moves = []
        self.prev_sel_color = None
        self.on_turn = True
        self.sq1 = None
        self.changed_bgs = {}
        self.move_order = ['1.', ]
        self.move_counter = 1
        self.bk_pos = 'e8'
        self.wk_pos = 'e1'
        self.white_in_check = False
        self.black_in_check = False
        self.wra_moved = False
        self.wrh_moved = False
        self.bra_moved = False
        self.brh_moved = False
        self.attacked_squares_by_white = []
        self.attacked_squares_by_black = []
        self.white_pieces = {}
        self.black_pieces = {}
        self.computerColor = False
        self.createBoard()

    def createBoard(self):
        color1, color2 = 'CornFlowerBlue', 'ivory'
        c = 0
        for x in range(8):
            for y in range(8):
                btn = tkinter.Button(self, bg=color1, activebackground='aquamarine', height=128, width=128,
                                     image=self.IMAGE_ROOT['e'])
                self.squares[self.SQUARE_NAMES[c]] = btn
                self.squares[self.SQUARE_NAMES[c]].config(command=lambda pos=self.SQUARE_NAMES[c]: self.pressed(
                    pos))
                c += 1
                btn.grid(row=8 - x, column=y)
                color1, color2 = color2, color1
            color1, color2 = color2, color1

    def animate(self, turn):
        if turn:
            for i in range(1, 4):
                self.squares[self.wk_pos].config(image=self.ANIMATION_IMAGES[i])
                self.parent.update()
                self.parent.after(150)
            self.squares[self.wk_pos].config(image=self.IMAGE_ROOT['K'])
        else:
            for i in range(5, 8):
                self.squares[self.bk_pos].config(image=self.ANIMATION_IMAGES[i])
                self.parent.update()
                self.parent.after(150)
            self.squares[self.bk_pos].config(image=self.IMAGE_ROOT['k'])

    def populateBoard(self, file='start.json'):
        startpos = self.readPositionFile(file)
        for k, v in startpos.items():
            self.squares[k].config(
                image=self.IMAGE_ROOT[v], height=128, width=128)
            if v in 'pnbrqk':
                self.black_pieces[k] = v
                if v == 'k': self.bk_pos = k
            if v in 'PNBRQK':
                self.white_pieces[k] = v
                if v == 'K': self.wk_pos = k

    def makeSquareNames(self):
        file_names = ["a", "b", "c", "d", "e", "f", "g", "h"]

        rank_names = ["1", "2", "3", "4", "5", "6", "7", "8"]

        return [f + r for r in rank_names for f in file_names]

    def pressed(self, pos):
        computerLoop = False
        if self.computerColor == self.on_turn:
            computerLoop = True
        if self.getColor(pos) == self.on_turn or self.getColor(self.sq1) == self.on_turn:  # striedane tahov
            if self.sq1 is None:
                self.sq1 = pos
                self.selected_piece_moves = self.legalMoves(pos)
                if self.getPiece(pos) in 'kK':
                    self.castling_moves = self.castles(pos)
                self.selected_piece_moves = self.removeIllegal(self.on_turn, self.selected_piece_moves, pos)
                self.showPossibleMoves(self.castling_moves)
                self.showPossibleMoves(self.selected_piece_moves)
                if self.selected_piece_moves == [] or self.selected_piece_moves is None:  # neexistuju ziadne tahy alebo bolo kliknute prazdne pole
                    self.sq1 = None
                    self.selected_piece_moves = []
                else:
                    self.prev_sel_color = self.squares[pos].cget('bg')
                    self.squares[pos].config(bg='deepskyblue')
                print('legalne:', self.selected_piece_moves, self.castling_moves)
            else:
                if self.sq1 == pos:  # opat stlacene tlacidlo figurky, resetuje vyber
                    self.squares[self.sq1].config(bg=self.prev_sel_color)
                    self.sq1 = None
                    self.removeDots(self.selected_piece_moves)
                    self.selected_piece_moves = []

                if pos in self.selected_piece_moves:  # vybrany tah je legalny
                    print('vybrata', pos)
                    if not self.on_turn:
                        self.move_counter += 1
                        print('Moves made:', ' '.join(self.move_order))
                        self.move_order.append(str(self.move_counter) + '.')

                    # updatuje poziciu krala a vezi pre rosadu
                    if self.getPiece(self.sq1) in 'k': self.bk_pos = pos
                    if self.getPiece(self.sq1) in 'K': self.wk_pos = pos
                    if self.getPiece(self.sq1) in 'R' and self.sq1[0] == 'a': self.wra_moved = True
                    if self.getPiece(self.sq1) in 'R' and self.sq1[0] == 'h': self.wrh_moved = True
                    if self.getPiece(self.sq1) in 'r' and self.sq1[0] == 'a': self.bra_moved = True
                    if self.getPiece(self.sq1) in 'r' and self.sq1[0] == 'h': self.brh_moved = True

                    self.makeMove(pos)
                    self.selected_piece_moves.remove(pos)
                    if pos in self.changed_bgs.keys():
                        self.squares[pos].config(bg=self.changed_bgs[pos])
                        if self.on_turn:
                            self.black_pieces.pop(pos)
                        else:
                            self.white_pieces.pop(pos)

                    self.removeDots(self.selected_piece_moves)
                    # sach
                    self.isCheck(True)
                    self.isMaterialDraw()
                    self.isStalemate()

                    # self.animate(self.on_turn)
                    self.selected_piece_moves = []
                    self.sq1 = None
                    self.on_turn = not self.on_turn
                    if self.white_in_check or self.black_in_check:
                        self.isCheckmate()
                    self.promotion(pos)
                if len(self.castling_moves) > 0:
                    if pos in self.castling_moves:
                        self.makeCastles(pos)
                self.removeDots(self.castling_moves)
                self.castling_moves = []
        self.getEval(self.white_pieces, self.black_pieces)
        if self.on_turn == self.computerColor and not computerLoop:
            self.computerMove()

    def makeMove(self, pos):
        moveImage = self.squares[self.sq1].cget('image')
        self.squares[pos].config(image=moveImage)
        self.squares[self.sq1].config(image=self.IMAGE_ROOT["e"], bg=self.prev_sel_color)
        self.addMove(pos)
        # updatuje posunutie figurky
        if self.on_turn:
            self.white_pieces[pos] = self.white_pieces.pop(self.sq1)
        else:
            self.black_pieces[pos] = self.black_pieces.pop(self.sq1)

    def makeCastles(self, pos):
        if pos == 'g1':
            # king
            self.sq1 = 'e1'

            self.makeMove('g1')
            # rook
            self.prev_sel_color = self.squares['h1'].cget('bg')
            self.sq1 = 'h1'
            self.makeMove('f1')
        if pos == 'c1':
            # king
            self.sq1 = 'e1'
            self.makeMove('c1')
            # rook
            self.prev_sel_color = self.squares['a1'].cget('bg')
            self.sq1 = 'a1'
            self.makeMove('d1')

        if pos == 'g8':
            # king
            self.sq1 = 'e8'
            self.makeMove('g8')
            # rook
            self.prev_sel_color = self.squares['h8'].cget('bg')
            self.sq1 = 'h8'
            self.makeMove('f8')
        if pos == 'c8':
            # king
            self.sq1 = 'e8'
            self.makeMove('c8')
            # rook
            self.prev_sel_color = self.squares['a8'].cget('bg')
            self.sq1 = 'a8'
            self.makeMove('d8')

        self.removeDots(self.selected_piece_moves)
        self.castling_moves = []
        self.sq1 = None
        self.on_turn = not self.on_turn

    def getAttackedSquares(self, color):
        if color:
            self.attacked_squares_by_white = []
            for val in self.white_pieces.keys():
                if self.getPiece(val) == 'P':
                    if val[1] != '8':
                        for i in Pawn(val, self).attacking():
                            self.attacked_squares_by_white.append(i)
                            self.attacked_squares_by_white = list(set(self.attacked_squares_by_white))
                else:
                    if self.legalMoves(val, False) is not None:
                        for i in self.legalMoves(val, False):
                            self.attacked_squares_by_white.append(i)
                            self.attacked_squares_by_white = list(set(self.attacked_squares_by_white))
        else:
            self.attacked_squares_by_black = []
            for val in self.black_pieces.keys():
                if self.getPiece(val) == 'p':
                    if val[1] != '1':
                        for i in Pawn(val, self).attacking():
                            self.attacked_squares_by_black.append(i)
                            self.attacked_squares_by_black = list(set(self.attacked_squares_by_black))
                else:
                    if self.legalMoves(val, False) is not None:
                        for i in self.legalMoves(val, False):
                            self.attacked_squares_by_black.append(i)
                            self.attacked_squares_by_black = list(set(self.attacked_squares_by_black))

    def isCheck(self, prnt=False):
        self.getAttackedSquares(True)
        self.getAttackedSquares(False)
        if self.wk_pos in self.attacked_squares_by_black:
            self.white_in_check = True
        else:
            self.white_in_check = False
            if self.bk_pos in self.attacked_squares_by_white:
                self.black_in_check = True

            else:
                self.black_in_check = False
        if prnt:
            print('white in check:', self.white_in_check, 'black in check:', self.black_in_check)

    def removeIllegal(self, color, moves, pos):
        out = [i for i in moves]
        if color:
            check = self.white_in_check
            if self.getPiece(pos) == 'K':
                for i in moves:
                    if i in self.attacked_squares_by_black:
                        out.remove(i)
            else:
                for i in moves:
                    self.white_pieces[i] = self.white_pieces.pop(pos)
                    self.isCheck()
                    if self.white_in_check:
                        out.remove(i)
                    self.white_pieces[pos] = self.white_pieces.pop(i)
                    self.white_in_check = check
        else:
            check = self.black_in_check
            if self.getPiece(pos) == 'k':
                for i in moves:
                    if i in self.attacked_squares_by_white:
                        out.remove(i)
            else:
                for i in moves:
                    self.black_pieces[i] = self.black_pieces.pop(pos)
                    self.isCheck()
                    if self.black_in_check:
                        out.remove(i)
                    self.black_pieces[pos] = self.black_pieces.pop(i)
                    self.black_in_check = check
        return out

    def isCheckmate(self):
        win = True
        if self.white_in_check:
            self.getAttackedSquares(False)
            fake = {k: v for k, v in self.white_pieces.items()}
            for k, v in fake.items():
                if self.legalMoves(k) is not None:
                    if len(self.removeIllegal(True, self.legalMoves(k), k)) > 0:
                        if win:
                            win = False

        if self.black_in_check:
            self.getAttackedSquares(True)
            fake = {k: v for k, v in self.black_pieces.items()}
            for k, v in fake.items():
                if self.legalMoves(k) is not None:
                    if len(self.removeIllegal(False, self.legalMoves(k), k)) > 0:
                        if win:
                            win = False

        if win:
            if self.white_in_check:
                self.winHandler('Black')
            elif self.black_in_check:
                self.winHandler('White')

    def isMaterialDraw(self):
        if len(self.black_pieces) == 1 and len(self.white_pieces) == 1:
            self.on_turn = None
            showinfo(title='The game has ended.',
                     message=f'Game has ended in a draw due to insufficient material')
            return

    def isStalemate(self):
        if len(self.white_pieces) == 1:
            pos = self.getKey(self.white_pieces, 'K')
            if self.removeIllegal(True, King(pos, self).legal(), pos) == []:
                self.on_turn = None
                showinfo(title='The game has ended.',
                         message=f'Game has ended in a stalemate')
                return
        if len(self.black_pieces) == 1:
            pos = self.getKey(self.black_pieces, 'k')
            if self.removeIllegal(False, King(pos, self).legal(), pos) == []:
                self.on_turn = None
                showinfo(title='The game has ended.',
                         message=f'Game has ended in a stalemate')
                return

    def legalMoves(self, pos, default=True):
        piece = self.getPiece(pos)
        if piece in 'Pp':
            if default:
                moves = Pawn(pos, self).legal()
            else:
                moves = Pawn(pos, self).attacking()
            return moves
        elif piece in 'Nn':
            if default:
                moves = Knight(pos, self).legal()
            else:
                moves = Knight(pos, self).atprot()
            return moves
        elif piece in 'Rr':
            if default:
                moves = Rook(pos, self).legal()
            else:
                moves = Rook(pos, self).atprot()
            return moves
        elif piece in 'Bb':
            if default:
                moves = Bishop(pos, self).legal()
            else:
                moves = Bishop(pos, self).atprot()
            return moves
        elif piece in 'Qq':
            if default:
                moves = Queen(pos, self).legal()
            else:
                moves = Queen(pos, self).atprot()
            return moves
        elif piece in 'Kk':
            moves = King(pos, self).legal()
            return moves
        return

    def computerMove(self):
        possible_moves = self.generateAllMoves(self.computerColor)
        possible_moves.sort(key=lambda y: y[2])
        if self.computerColor:
            best = possible_moves[-3:]
        else:
            best = possible_moves[:3]
        chosen = random.choice(best)
        print('Chosen:', chosen, best)
        self.pressed(chosen[0])
        self.pressed(chosen[1])

    def generateAllMoves(self, color):
        def getAttacked(pos, piece):
            moves = []
            if piece in 'Pp':
                moves = Pawn(pos, self).attacking()
            elif piece in 'Nn':
                moves = Knight(pos, self).atprot()
            elif piece in 'Rr':
                moves = Rook(pos, self).atprot()
            elif piece in 'Bb':
                moves = Bishop(pos, self).atprot()
            elif piece in 'Qq':
                moves = Queen(pos, self).atprot()
            return moves

        out = []
        if color:
            numofMoves = 0
            white = self.white_pieces
            for pos in list(white.keys()):
                moves = self.legalMoves(pos)
                moves = self.removeIllegal(color, moves, pos)
                for i in moves:
                    mvs = white.copy()
                    mvs[i] = mvs.pop(pos)
                    # print(pos, i, mvs[i], end=' | ')
                    eval = self.getEval(mvs, self.black_pieces, getAttacked(i, mvs[i]))
                    out.append((pos, i, eval))
                if moves:
                    numofMoves += len(moves)
        else:
            numofMoves = 0
            black = self.black_pieces
            for pos in list(black.keys()):
                moves = self.legalMoves(pos)
                moves = self.removeIllegal(color, moves, pos)
                for i in moves:
                    mvs = black.copy()
                    mvs[i] = mvs.pop(pos)
                    # print(pos, i, mvs[i], end=' | ')
                    eval = self.getEval(self.white_pieces, mvs, getAttacked(i, mvs[i]))
                    out.append((pos, i, eval))
                if moves:
                    numofMoves += len(moves)
        print('Num of moves:', numofMoves, color)
        return out

    def getEval(self, white, black, attacked=[]):
        vals = {'K': 900, 'k': -900, 'Q': 90, 'q': -90, 'R': 50, 'r': -50, 'B': 30, 'b': -30, 'N': 30, 'n': -30,
                'P': 10,
                'p': -10, }

        def evalTables(piece, pos):
            pos = 63 - self.SQUARE_NAMES.index(pos)
            pawns = [0, 0, 0, 0, 0, 0, 0, 0, 50, 50, 50, 50, 50, 50, 50, 50, 10, 10, 20, 30, 30, 20, 10, 10, 5,
                     5, 10,
                     25, 25, 10, 5, 5, 0, 0, 0, 20, 20, 0, 0, 0, 5, -5, -10, 0, 0, -10, -5, 5, 5, 10, 10, -20, -20, 10,
                     10, 5, 0, 0, 0, 0, 0, 0, 0, 0]
            knights = [-50, -40, -30, -30, -30, -30, -40, -50, -40, -20, 0, 0, 0, 0, -20, -40, -30, 0, 10, 15, 15, 10,
                       0, -30, -30, 5, 15, 20, 20, 15, 5, -30, -30, 0, 15, 20, 20, 15, 0, -30, -30, 5, 10, 15, 15, 10,
                       5, -30, -40, -20, 0, 5, 5, 0, -20, -40, -50, -40, -30, -30, -30, -30, -40, -50]
            bishops = [-20, -10, -10, -10, -10, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 10, 10, 5, 0, -10,
                       -10, 5, 5, 10, 10, 5, 5, -10, -10, 0, 10, 10, 10, 10, 0, -10, -10, 10, 10, 10, 10, 10, 10, -10,
                       -10, 5, 0, 0, 0, 0, 5, -10, -20, -10, -10, -10, -10, -10, -10, -20, ]
            rooks = [0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 10, 10, 10, 10, 10, 5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0,
                     0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, 0, 0, -5, 0, 0, 0, 5, 5,
                     0, 0, 0]
            queens = [-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 0, 0, 0, 0, 0, -10, -10, 0, 5, 5, 5, 5, 0, -10, -5,
                      0, 5, 5, 5, 5, 0, -5, 0, 0, 5, 5, 5, 5, 0, -5, -10, 5, 5, 5, 5, 5, 0, -10, -10, 0, 5, 0, 0, 0, 0,
                      -10, -20, -10, -10, -5, -5, -10, -10, -20]
            if piece == 'P':
                return pawns[pos]
            if piece == 'p':
                return pawns[63 - pos] * (-1)
            if piece == 'N':
                return knights[pos]
            if piece == 'n':
                return knights[63 - pos] * (-1)
            if piece == 'B':
                return bishops[pos]
            if piece == 'b':
                return bishops[63 - pos] * (-1)
            if piece == 'R':
                return rooks[pos]
            if piece == 'r':
                return rooks[63 - pos] * (-1)
            if piece == 'Q':
                return queens[pos]
            if piece == 'q':
                return queens[63 - pos] * (-1)
            if piece in 'Kk':
                return 0

        eval = 0
        for k, v in white.items():
            if k in self.black_pieces.keys():
                ''' taking is more advantageous'''
                if self.black_pieces != 'k':
                    eval += vals[self.black_pieces[k]]
            if attacked != []:
                if self.getBkPos() in attacked:
                    '''checking is cool'''
                    eval += 50
            eval += vals[v] + evalTables(v, k)

        for k, v in black.items():
            if k in self.white_pieces.keys():
                ''' taking is more advantageous'''
                if self.white_pieces[k] != 'K':
                    eval += -(vals[self.white_pieces[k]])
            if attacked != []:
                if self.getWkPos() in attacked:
                    '''checking is cool'''
                    eval -= 50
            eval += vals[v] + evalTables(v, k)
        # print('Eval:', eval)
        return eval

    def getKey(self, dictionary, val):
        for k, v in dictionary.items():
            if val == v:
                return k

    def getPiece(self, pos):
        if pos in self.white_pieces.keys():
            return self.white_pieces[pos]
        if pos in self.black_pieces.keys():
            return self.black_pieces[pos]
        else:
            try:
                return self.getKey(self.IMAGE_ROOT, self.squares[pos].cget('image'))
            except KeyError:
                return None

    def getColor(self, pos):  # white - True, black - False
        if pos is not None:
            if pos in self.black_pieces.keys():
                return False
            if pos in self.white_pieces.keys():
                return True
        return None

    def isOccupied(self, pos):
        if self.getColor(pos) is not None:
            return True
        else:
            return False

    def showPossibleMoves(self, m):
        if m is not None:
            for i in m:
                if not self.isOccupied(i):
                    self.squares[i].config(image=self.IMAGE_ROOT["d"])
                else:
                    self.changed_bgs[i] = self.squares[i].cget('bg')
                    self.squares[i].config(bg='lightcoral')

    def removeDots(self, m):
        for i in m:
            if not self.isOccupied(i):
                self.squares[i].config(image=self.IMAGE_ROOT["e"])
            elif len(self.changed_bgs) > 0:

                self.squares[i].config(bg=self.changed_bgs[i])
                self.changed_bgs.pop(i)

        self.changed_bgs = {}

    def addMove(self, pos):
        if self.getPiece(self.sq1) in 'Pp':
            self.move_order.append(pos)
        else:
            self.move_order.append(self.getPiece(self.sq1).capitalize() + pos)

    def readPositionFile(self, path):
        with open(path) as f:
            return json.load(f)

    def savePositionFile(self, path):
        game_board = {}
        for k in self.squares.keys():
            if self.getPiece(k) is not None:
                game_board[k] = self.getPiece(k)
            else:
                game_board[k] = 'e'
        with open(path, 'w') as outFile:
            json.dump(game_board, outFile, indent=4)

    def winHandler(self, who):
        self.on_turn = None
        answer = showinfo(title='The game has ended.',
                          message=f'{who} has won the game by checkmate.')

    def promotion(self, pos):
        def return_piece(piece):
            self.squares[pos].config(image=self.IMAGE_ROOT[piece])
            if self.getColor(pos):
                self.white_pieces[pos] = piece
            else:
                self.black_pieces[pos] = piece
            self.isCheck()
            promotion_window.destroy()
            return

        if self.getPiece(pos) in 'pP':
            if pos[1] in '18':
                promotion_window = tkinter.Tk()
                promotion_window.title('What do you wish to promote to')
                if self.getColor(pos):
                    promoButton1 = tkinter.Button(promotion_window, text=chr(9816), font='Arial 50',
                                                  command=lambda: return_piece('N'))
                    promoButton1.grid(row=0, column=0)
                    promoButton2 = tkinter.Button(promotion_window, text=chr(9815), font='Arial 50',
                                                  command=lambda: return_piece('B'))
                    promoButton2.grid(row=0, column=1)
                    promoButton3 = tkinter.Button(promotion_window, text=chr(9814), font='Arial 50',
                                                  command=lambda: return_piece('R'))
                    promoButton3.grid(row=0, column=2)
                    promoButton4 = tkinter.Button(promotion_window, text=chr(9813), font='Arial 50',
                                                  command=lambda: return_piece('Q'))
                    promoButton4.grid(row=0, column=3)
                else:
                    for i in 'nbrq':
                        promoButton1 = tkinter.Button(promotion_window, text=chr(9822), font='Arial 50',
                                                      command=lambda: return_piece('n'))
                        promoButton1.grid(row=0, column=0)
                        promoButton2 = tkinter.Button(promotion_window, text=chr(9821), font='Arial 50',
                                                      command=lambda: return_piece('b'))
                        promoButton2.grid(row=0, column=1)
                        promoButton3 = tkinter.Button(promotion_window, text=chr(9820), font='Arial 50',
                                                      command=lambda: return_piece('r'))
                        promoButton3.grid(row=0, column=2)
                        promoButton4 = tkinter.Button(promotion_window, text=chr(9819), font='Arial 50',
                                                      command=lambda: return_piece('q'))
                        promoButton4.grid(row=0, column=3)

                promotion_window.mainloop()
            return

    def castles(self, pos):
        moves = []
        # rosady
        if self.getPiece(pos) == 'K' and 'K' not in ''.join(self.move_order):
            # kratka
            if 'e1' not in self.attacked_squares_by_black and 'f1' not in self.attacked_squares_by_black and 'g1' not in self.attacked_squares_by_black:
                if not self.isOccupied('f1') and not self.isOccupied('g1') and not self.wrh_moved:
                    moves.append('g1')
            # dlha
            if 'e1' not in self.attacked_squares_by_black and 'd1' not in self.attacked_squares_by_black and 'c1' not in self.attacked_squares_by_black:
                if not self.isOccupied('b1') and not self.isOccupied('c1') and not self.isOccupied(
                        'd1') and not self.wra_moved:
                    moves.append('c1')

        if self.getPiece(pos) == 'k' and 'k' not in ''.join(self.move_order):
            # kratka
            if 'e8' not in self.attacked_squares_by_white and 'f8' not in self.attacked_squares_by_white and 'g8' not in self.attacked_squares_by_white:
                if not self.isOccupied('f8') and not self.isOccupied('g8') and not self.brh_moved:
                    moves.append('g8')
            # dlha
            if 'e8' not in self.attacked_squares_by_white and 'd8' not in self.attacked_squares_by_white and 'c8' not in self.attacked_squares_by_white:
                if not self.isOccupied('b8') and not self.isOccupied('c8') and not self.isOccupied(
                        'd8') and not self.bra_moved:
                    moves.append('c8')
        return moves

    def getWkPos(self):
        return self.wk_pos

    def getBkPos(self):
        return self.bk_pos


class Program:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('1152x1152')
        self.board = Board(self.root)
        self.root.title('Ultimate chess game')
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        game_menu = Menu(menubar)
        game_menu.add_command(label='New', command=self.newGame)
        game_menu.add_command(label='Open', command=self.openGame)
        game_menu.add_command(label='Save', command=self.saveGame)
        game_menu.add_command(label='Exit', command=self.root.destroy)

        menubar.add_cascade(label="Game", menu=game_menu)

        self.board.mainloop()

    def newGame(self):
        self.board.resetValues()
        self.board.populateBoard()

    def openGame(self):
        filename = filedialog.askopenfilename()
        self.board.resetValues()
        self.board.populateBoard(filename)

    def saveGame(self):
        filename = filedialog.asksaveasfilename()
        self.board.savePositionFile(filename)

    def doAnimation(self):
        return


p = Program()
