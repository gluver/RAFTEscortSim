from RaftEscortSim.messages.LogRP import LogRP
from RaftEscortSim.messages.LogRQ import LogRQ
from RaftEscortSim.log.Log import LogEntity
from RaftEscortSim.states.State import State

class Leader(State):
    def __init__(self,node):
        super().__init__(node)    
        self.sentLength=dict()
        self.ackedLength=dict()
        for neighbour_id,neighbour_info in self.node.neighbours:
            self.sentLength[neighbour_id]=len(self.node.log)
            self.ackedLength[neighbour_id]=0

    def handle_log_response(self, msg:LogRP):
        if msg.f_term==self.node.current_term and self.node.state_str=='Leader':
            if msg.success==True and msg.ack_len >= self.ackedLength[msg.senderId]:
                self.sentLength[msg.senderId]=msg.ack_len
                self.ackedLength[msg.senderId]=msg.ack_len
                self.commit_log_entries()
            elif self.sentLength[msg.senderId]>0:
                self.sentLength[msg.senderId]-=1
                
        elif msg.f_term>self.node.current_term:
            self.node.current_term=msg.f_term
            self.node.change_state('Follower')
            self.node.vote_for=None

    def commit_log_entries(self):
        def acks(ack_len):
            return len([n for n in self.sentLength.keys() if self.sentLength[n]>ack_len])
        minAcks=(len(self.node.neighbours)+1)/2
        ready=[i for i in range(1,(len(self.node.log)+1)) if acks(i)>=minAcks]
        if len(ready) != 0 and max(ready) > self.node.commit_length and \
            self.node.log[max(ready)-1].term==self.node.current_term:
            for i in range(self.node.commit_length,max(ready)):
                ###deliver log[i].msg to the application
                pass
            self.node.commit_length=max(ready)

    def replicate_log(self,follower_id):
        i=self.sentLength[follower_id]
        entires=self.node.log[i,-1]
        prevLogTerm=0
        if i>0:
            prevLogTerm=self.node.log[i-1].term
        msg=LogRQ(self.node.current_leader,self.node.current_term,i,prevLogTerm,self.node.commit_length,entires,follower_id)
        self.node.queue.put(msg)

    def broadcast(self):
        for neighbour_id,neighbour_info in self.node.neighbours:
            self.replicate_log(neighbour_id)
        

if __name__=="__main__":
    f=Leader()