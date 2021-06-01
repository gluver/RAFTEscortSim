class Coordinator():
    def __init__(self,current_leader) -> None:
        self.leader=current_leader
    def move_flag(self,node_coordinates):
        self.coordins=node_coordinates
        print(self.coordins)
        if self.coordins['flag'][0]<100:
            self.coordins['flag']=(self.coordins['flag'][0]+1,0)
            self.coordins[self.leader]=self.coordins['flag']
        return self.coordins