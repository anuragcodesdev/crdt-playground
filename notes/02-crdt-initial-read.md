# Kleppmann - Conflict-Free Replicated JSON Datatype

### Abstract
From my understanding from reading the abstract this paper provides an algorithm and implications behind modified concurrent intended behariour on multiple devices. The paper utilises to obtian a JSON data structure that resovles to a singular output with no data loss, and all relevant devices converging to a singular state - i.e a conflict free replicated datatype or CRDT. The algorithm does not depend on the network to order the data nd instead merges inputs obtained on the client side.

### Introduction
If we want concurrency regardless of network availability, we need to assume users can make modifications concurrently on different devices, and that any resulting conflict must be resolved. Presently, we may look at discarding data when conflicts occur, with rules such as "last writer takes precedence", however, this is extremely undesirable. 

The goal is to create and utilise a JSON data structure to record conflicting updates to the leaf nodes in the JSON data structure. 

### JSON Data Model
The paper is based on a JSON structure, and is specifically based on untyped JSON, without an explicit schema. 

A JSON document is a **tree** with two types of branch nodes:

- **Map (Object)**: Unordered collection of key-value pairs.
  - Children are identified by unique string keys.
  - Keys are immutable, whilst values are mutable.
  - Key-value pairs can be added or removed.

- **List (Array)**: Ordered collection of elements.
  - Order is defined by the application.
  - Elements can be inserted or deleted.

Nodes can contain:
- **Branch nodes** -> another map or list.
- **Leaf nodes** -> primitive values (`string`, `number`, `boolean`, `null`).

Primitive values are immutable but can be replaced with a new value.


The JSON model can represent different applications. For example, a text document can be represented as a list of character strings, where edits become insertions and deletions of list elements.

### Replication and Conflict Resolution
- JSON document is fully replicated across multiple devices.
- Each device can edit their local copy independently (optimistic update).
- Changes are synced asynchronously between replicas.

#### Network Assumptions:
- Messages are eventually delivered.
- Messages may be delayed, reordered, or duplicated.

#### CRDT algorithm:
- Runs client-side.
- Does not require a central server to merge or transform updates.
- Supports peer-to-peer and encrypted messaging due to server-independence.

### CRDTs

CRDTs are established data structures that support concurrent modification while guaranteeing convergence of concurrent updates. The key idea behind them is attaching additional metadata to operations, allowing modification operations to become commutative by construction. In other words, even if two replicas receive operations in different orders, they will still converge to the same final state.

Well-defined use cases for CRDTs include registers, counters, maps and sets. However, in almost all of these cases we assume that each element in the CRDT is a primitive value, rather than another CRDT. This becomes a limitation when modelling nested structures such as JSON, where objects can contain arrays, which themselves can contain other objects or arrays.

The main idea behind CRDTs is that multiple replicas of the same document can be edited independently and later merged automatically. There is no need for a central server to resolve conflicts, and eventually every replica converges to the same final state.

In this context, concurrent doesn't necessarily mean changes happening at the exact same millisecond. It simply means multiple replicas make changes before they've seen each other's updates. When those replicas eventually synchronise, the CRDT guarantees that all updates are merged correctly instead of one replica overwriting another.

One of the key ideas is commutativity. By attaching metadata (such as unique identifiers and causal information) to each operation, replicas can deterministically resolve conflicts regardless of the order operations arrive. This means processing operation A then B produces the same final state as processing B then A.

Several algorithms have been proposed for ordered-list CRDTs, including WOOT, RGA, Treedoc, Logoot and LSEQ. These solve collaborative editing for lists, but they assume each element is a primitive value and do not support arbitrary nesting.

The contribution of this paper is allowing these CRDTs to be composed into an arbitrarily nested JSON structure. Since JSON behaves like a tree, each node may contain another object, an array or a primitive value, allowing collaborative editing of complex nested documents rather than just flat lists or maps.

## Questions
How does this data structure not depend on the network? How can two different devices merge their versions and get the correct version out without sharing orders through the network?