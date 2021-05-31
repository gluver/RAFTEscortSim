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

    def handle_log_response(self, msg):
        return super().handle_log_response(msg)

    def replicate_log(self,follower_id):
        i=self.sentLength[follower_id]
        entires=self.node.log[i,-1]
        prevLogTerm=0
        if i>0:
            prevLogTerm=self.node.log[i,-1].term
        msg=LogRQ(self.node.current_leader,self.node.current_term,len(self.node.log),self.node.commit_length,entires,follower_id)
        self.node.queue.put(msg)
        
    def broadcast(self):
        for neighbour_id,neighbour_info in self.node.neighbours:
            self.replicate_log(neighbour_id)
        

if __name__=="__main__":
    f=Leader()