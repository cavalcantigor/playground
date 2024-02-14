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

### Operations

  - Create a document
     ```
     POST products/_doc
     {
       "name": "Coffee Maker",
       "price": 64,
       "in_stock": 10
     }
     ```
  - Create a document with id
     ```
     POST products/_doc/100
     {
       "name": "Coffee Maker",
       "price": 64,
       "in_stock": 10
     }
     ```
  - Update a document
     ```
     POST products/_update/100
     {
       "doc": {
         "tags": ["electronics"]
       }
     }
     ```
  - Update a document with script
     ```
     POST products/_update/100
     {
       "script": {
         "source": "ctx._source.in_stock--"
       }
     }
     
     POST products/_update/100
     {
       "script": {
         "source": "ctx._source.in_stock = 10"
       }
     }
     
     POST products/_update/100
     {
       "script": {
         "source": "ctx._source.in_stock -= params.quantity",
         "params": {
           "quantity": 4
         }
       }
     }
     ```
  - Replace a document
     ```
     POST products/_doc/100
     {
       "name": "Coffee Maker",
       "price": 64,
       "in_stock": 10
     }
     ```
  - Delete a document
     ```
     DELETE /products/_doc/100
     ```

### Routing

How does ES know where to store documents? How are documents found once the have been indexed? The answer is *routing*.

- **Routing**: is the process of resolving a shard for a document. It's possible to customize routing for various purposes. The default routing strategy ensures that documents are distributed evenly.

```
shard_num = hash(_routing) % num_primary_shards
```
> Because that formula the number of primary shards of an index cannot be changed at any time.

### Reading data

- A read request is received and handled by a *coordinating node*.
- Routing is used to resolve the document's *replica group*.
- ARS (adaptive replica selection) is used to send the query to the best available shard.
- The coordinating node collects the response and sends it to the client.

### Writing data

- Write operations are sent to primary shards.
- The primary shards forwards the operation to its replica shards.
- Primary terms and sequence numbers are used to recover from failures.
- Global and local checkpoints help to speed up the recovery process.
- Primary terms and sequence numbers are available within responses.

#### Primary terms
- A way to distinguish between old and new primary shards.
- Essentially a counter for how many times the primary shard has changed.
- The primary term is appended to write operations.

#### Sequence numbers
- Appended to write operations together with the primary term.
- Essentially a counter that is incremented for each write operation.
- The primary shard increases the sequence number.
- Enables ES to order write operations.

#### Global and local checkpoints
- Essentially sequence numbers.
- Each replication group has a *global* checkpoint.
- Each replica shard has a *local* checkpoint.
- **Global checkpoints**: The sequence number that all active shards within a replication group have been aligned at least up to.
- **Local checkpoints**: The sequence number for the last write operation that was performed.

### Mapping and Analysis

#### Analysis
- Sometimes referred to as *text analysis*.
- Applicable to text field/values.
- Text values are analyzed when indexing documents.
- The result is stored in data structures that are effcient for searching, etc.
- The *_source* object is **not** used when searching for documents. It contains the exact values specified when indexing a document.

#### Analyzer

- **Character filters**
  - Adds, removes, or changes characters.
  - Analyzers contain zero or more characters filters.
  - Character filters are applied in the order in which they are specified.
  - Example (`html_strip` filter):
    - **Input**: `"I&apos;m in a <em>good</em> mood&nbsp;-&nbsp;and I <strong>love</strong> açaí!"`
    - **Output**: `"I'm in a good mood - and I love açaí!"`
   
- **Tokenizers**
  - An analyzer contain **one** tokenizer.
  - Tokenizes a string, i.e. splits it into tokens.
  - Characters may be stripped as part of the tokenization.
  - Example:
    - **Input**: `"I REALLY like beer!"`
    - **Output**: `["I", "REALLY", "like", "beer"]`
   
- **Token filters**
  - Receive the output of tokenizers as input (i.e. the tokens).
  - A token filter can add, remove or modify tokens.
  - An analyzer contains zero or more token filters.
  - Token filters are applied in the order which they are specified.
  - Example (`lowercase` filter):
    - **Input**: `["I", "REALLY", "like", "beer"]`
    - **Output**: `["i", "really", "like", "beer"]`
   
#### Standard analyzer
<img width="995" alt="image" src="https://github.com/cavalcantigor/playground/assets/8291170/72faa478-9226-4fb9-b8de-728a83ec7cb2">
