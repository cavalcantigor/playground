## Elasticsearch

> Easy to use and very high scalable.

#### EKS

- **Kibana**: an analytics and data visualization platform. Provides management and configuration to Elasticsearch.
- **Logstash**: data processing pipeline. Consists of three parts - or stages: inputs, filters and outputs.
- **X-Pack**: a pack of features that adds additional functionality to Elasticsearch and Kibana. For example: security, monitoring, alerting, etc.
- **Beats**: a collection of data shippers.

#### Basic Architecture

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

