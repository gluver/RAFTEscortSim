import yaml
with open("/home/credog/GitRepos/RAFTEscortSim/RaftEscortSim/ClusterConfig.yaml",'r') as file:
   ClusterConfig=yaml.load(file, Loader=yaml.FullLoader) 
print(ClusterConfig[10002])