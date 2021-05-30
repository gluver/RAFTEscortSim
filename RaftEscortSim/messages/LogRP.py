from RaftEscortSim.messages.BaseMessage import BaseMessage

class LogRP(BaseMessage):
    def __init__(self,f_Id , f_term, ack_len, success):
        super().__init__(f_Id)
        self.f_term=f_term
        self.ack_len=ack_len
        self.success=success
        self.type="LogRP"