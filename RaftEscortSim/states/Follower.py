from RaftEscortSim.messages.LogRP import LogRP
from RaftEscortSim.messages.LogRQ import LogRQ
from RaftEscortSim.log.Log import LogEntity
from typing import List
from RaftEscortSim.messages.VoteResponseRP import VoteRequestRP
from RaftEscortSim.messages.VoteRequestRQ import VoteRequestRQ
# from RaftEscortSim.nodes.ServerNode import Node # remove after 
from RaftEscortSim.states.State import State


class Follower(State):
    def __init__(self,node):
        super().__init__(node)
   

    def append_entiries(self,logLength, leaderCommit, entries:List[LogEntity]):
        if len(entries)>0 and len(self.node.log)>logLength:
            if self.node.log[logLength].term != entries[0].term:
                self.node.log=self.node.log
        if logLength+len(entries)>len(self.node.log):
            for i in range(len(self.node.log)-logLength,len(entries)):
                self.node.log.append(entries[i])
            if leaderCommit > self.node.commit_length:
                for i in range(self.node.commit_length,leaderCommit-1):
                    pass
                    ### Todo deliver log[i].msg to the application
            self.node.commit_length=leaderCommit


if __name__=="__main__":
    f=Follower()
