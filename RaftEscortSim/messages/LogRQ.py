from RaftEscortSim.messages.BaseMessage import BaseMessage

class LogRQ(BaseMessage):
    '''
    l_term:leader current term
    '''
    def __init__(self,leaderId , l_term, log_len, log_term,l_commitlen, entries,f_id):
        super.__init__(leaderId)
        self.l_term=l_term
        self.log_len=log_len
        self.log_term=log_term
        self.l_commitlen=l_commitlen
        self.entries=entries
        self.f_id=f_id
        self.type="LogRQ"