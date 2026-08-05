# Understanding RGA

## Objective
The goal here is to understand the RGA data structure, starting from a single node and building out an implementation in Python. This implementation will act as a foundation for implementing the main CRDT in TypeScript later in the project.

The reason for choosing Python is simply because I am most familiar with the language.

### Data Structure
A simple data structure representing a node. Each node needs to contain the following properties:

- Unique ID
- Parent ID
- Value
- Deleted status
- Actor ID
- Timestamp

### Basic Operations
The general operations needed for the CRDT to function at a basic level are:

- Insert
- Delete
- Render
- Merge

### Replica
We need some way to create multiple replicas, modify each independently, and then synchronise them to verify that they converge to the same state.