# High availability

* Raft Consensus Algorithm
  - guarantee fault-tolerance and consistency, both for regular tablets and for master data. Through Raft, multiple replicas of a tablet elect a leader, which is responsible for accepting and replicating writes to follower replicas. Once a write is persisted in a majority of replicas it is acknowledged to the client. A given group of N replicas (usually 3 or 5) is able to accept writes with at most (N - 1)/2 faulty replicas.
