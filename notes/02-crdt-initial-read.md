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
- **Branch nodes** → another map or list.
- **Leaf nodes** → primitive values (`string`, `number`, `boolean`, `null`).

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

## Questions
How does this data structure not depend on the network? How can two different devices merge their versions and get the correct version out without sharing orders through the network?