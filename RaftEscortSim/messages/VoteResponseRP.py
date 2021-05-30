from RaftEscortSim.messages.BaseMessage import BaseMessage

class VoteRequestRP(BaseMessage):
    '''
    v_id:voter id
    v_term:voter current term
    granted: boolean of if voted c_id
    '''
    def __init__(self,v_id,v_term, granted,c_id):
        super().__init__(c_id)
        self.type='VoteRequestRP'
        self.c_id=c_id
        self.v_id=v_id
        self.v_term=v_term
        self.granted=granted