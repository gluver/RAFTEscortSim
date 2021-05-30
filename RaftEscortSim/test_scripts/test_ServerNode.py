from RaftEscortSim.messages import BaseMessage,LogRP,LogRQ,VoteRequestRQ,VoteResponseRP
msg=BaseMessage.BaseMessage("localtest1")
print(msg.senderId)