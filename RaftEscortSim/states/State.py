class State():
    '''
    Class Summary:
        Responsibale for behaviour logic of the nodes,while ServerNode class in charge of network config initializtion
    '''
    def __init__(ServerNode):
        pass
    def persistent():
        '''
        Each server persists the following to stable storage
        synchronously before responding to RPCs:
        currentTerm
        latest term server has seen (initialized to 0
        on first boot)
        votedFor
        candidateId that received vote in current
        term (or null if none)
        log[]
        log entries
        '''
        pass
    def handle_recv_RPC():
        pass
    def send_RPC():
        pass