from RaftEscortSim.messages.VoteResponseRP import VoteRequestRP
from RaftEscortSim.states.State import State


class Candidate(State):
    def __init__(self,node):
        super().__init__(node)
        self.votes_received=set()
    def handle_vote_response(self, msg:VoteRequestRP):
        if self.node.state_str=='Candidate' and msg.v_term==self.node.current_term \
        and msg.granted and msg.c_id==self.node.node_id:
            self.votes_received.add(msg.v_id)
            if len(self.votes_received)>=(len(self.node.neighbours)+1)/2:
                self.node.change_state('Leader')
                self.node.current_leader=self.node.node_id
                #Todo:cancel election timer
                #replicate code in note ,now move to Leader __init__() 
            elif msg.v_term>self.node.current_term:
                self.node.current_term=msg.v_term
                self.node.change_state('Follower')
                self.node.vote_for=None
                #Todo:cancel election timer

            

        