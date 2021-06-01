from RaftEscortSim.messages.VoteResponseRP import VoteRequestRP
from RaftEscortSim.states.State import State


class Candidate(State):
    def __init__(self,node):
        super().__init__(node)
        self.votes_received=[self.node.node_id]
    def handle_vote_response(self, msg:VoteRequestRP):
        print(f"VoteRequestResponse from {msg.v_id},for {msg.c_id},granted={msg.granted}")
        # print(self.node.state_str=='Candidate',msg.v_term==self.node.current_term,msg.granted and msg.c_id==self.node.node_id)
        if self.node.state_str=='Candidate' and msg.v_term==self.node.current_term \
        and msg.granted and msg.c_id==self.node.node_id:
            if msg.v_id not in self.votes_received:
                self.votes_received.append(msg.v_id)
            if len(self.votes_received)>=(len(self.node.neighbours)+1)/2:
                self.node.current_leader=self.node.node_id
                self.node.change_state('Leader')
                #Todo:cancel election timer
                #replicate code in note ,now move to Leader __init__() 
            elif msg.v_term>self.node.current_term:
                self.node.current_term=msg.v_term
                self.node.vote_for=None
                self.node.change_state('Follower')
                #Todo:cancel election timer
        print(f"Votes_recived {self.node.node_id}==>{len(self.votes_received)}/{len(self.node.neighbours)+1}")
            

        