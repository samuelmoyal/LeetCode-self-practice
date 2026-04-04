class Solution(object):

    def attempt(self,board,i,j,word,seen):
        if len(word)==0:
                return True

        else:
            up,left,right,down=False,False,False,False
            if i-1>=0:
                if board[i-1][j]==word[0] and (i-1,j) not in seen:
                    seen.add((i-1,j))
                    up=self.attempt(board,i-1,j,word[1:],seen)
                    if up==False:
                        seen.discard((i-1,j))
                    else: return True
            if j-1>=0:
                if board[i][j-1]==word[0] and (i,j-1) not in seen:
                    seen.add((i,j-1))
                    left=self.attempt(board,i,j-1,word[1:],seen)
                    if left==False:
                        seen.discard((i,j-1))
                    else: return True

            if i+1<len(board):
                if board[i+1][j]==word[0] and (i+1,j) not in seen:
                    seen.add((i+1,j))
                    down=self.attempt(board,i+1,j,word[1:],seen)
                    if down==False:
                        seen.discard((i+1,j))
                    else: return True
            if j+1<len(board[0]):
                if board[i][j+1]==word[0] and (i,j+1) not in seen:
                    seen.add((i,j+1))
                    right=self.attempt(board,i,j+1,word[1:],seen)
                    if right==False:
                        seen.discard((i,j+1))
                    else: return True
            return False
    def exist(self, board, word):
        seen=set()
        out=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    seen.add((i,j))
                    test=self.attempt(board,i,j,word[1:],seen)
                    seen.discard((i,j))
                    if test:
                        return test
        return False






                


        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        