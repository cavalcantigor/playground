## Elasticsearch

> Easy to use and very high scalable.

### ELK

- **Kibana**: an analytics and data visualization platform. Provides management and configuration to Elasticsearch.
- **Logstash**: data processing pipeline. Consists of three parts - or stages: inputs, filters and outputs.
- **X-Pack**: a pack of features that adds additional functionality to Elasticsearch and Kibana. For example: security, monitoring, alerting, etc.
- **Beats**: a collection of data shippers.

### Basic Architecture

- **Node**: is essentially an instance of Elasticsearch that stores data. We can run as many as we want. A node refers to an instance of ES and not a machine, so you can run any number of nodes on the same machine. Each node belongs to a cluster.
- **Cluster**: collection of related nodes that together contain all of our data. We can have many clusters, but one is usually enough.
- **Document**: each unit of data that you store within your cluster is called a document. Documents are *JSON* objects containing whatever data you desire.
- **Index**: every document within Elasticsearch is stored within an *index*. An index groups documents together logically, as well as provide configurations options that are related to scalability and availability. Search queries runs against index.

> An Elasticsearch node will always be part of a cluster, even if there are no other nodes.


#### Sharding and scalability

 - **Sharding**: is a way to divide an index into separate pieces, where each piece is so called a *shard*. Sharding is done at the index level. The main purpose is to horinzontally scale the data volume.

Each shard is an Apache Lucene index. An ES index consists of one or more Lucene indices. Shards allows improve perfomance through parallelization of queries.

> Too many shards to an index can lead to over-sharding.


#### Replication

> What happens if a node's hard drive fails? Hardware can fail at any time, so we need to handle that somehow.

- **Replication**: ES suports replication for fault tolerance. It's supported natively and enabled by default. Replication is *extremly* easy with Elasticsearch.

Replication is configured at index level. It works by creating copies of shards, referred to as replica shards. A shard that has been replicated is called a *primary shard*. A replica shard can serve search requests exactly like its primary shard. Replica shards are never stored on the same node as their primary shard.

### Node Roles

- **Master-eligible**: The node may be elected as the cluster's master node. A master node is responsible for creating and deleting indices, among others. A node with this role will not automatically become the master node.
- **Data**: enables a node to store data. Storing data includes performing queries related to that data, such as search queries.
- **Ingest**: enables a node to run ingest pipelines.
- **Machine learning**: useful for running ML jobs.
- **Coordination**: coordination refers to the distribution of queries and the aggregation of result.
- **Voting-only**: rarely used. A node with this role will participate in the voting for a new master node, but cannot be elected as the master node itself.
