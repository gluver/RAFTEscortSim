from RaftEscortSim.messages.BaseMessage import BaseMessage

class VoteRequestRQ(BaseMessage):
    '''
    cid:candidate id
    '''
    def __init__(self,c_id,c_term,c_loglen,c_lastterm):
        super().__init__(c_id)
        self.type='VoteRequestRQ'
        self.c_id=c_id
        self.c_term=c_term
        self.c_loglen=c_loglen
        self.c_lastterm=c_lastterm