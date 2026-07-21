# Kleppmann - Conflict-Free Replicated JSON Datatype

## Problem it solves

### Abstract
From my understanding from reading the abstract this paper provides an algorithm and implications behind modified concurrent intended behariour on multiple devices. The paper utilises to obtian a JSON data structure that resovles to a singular output with no data loss, and all relevant devices converging to a singular state - i.e a conflict free replicated datatype or CRDT. The algorithm does not depend on the network to order the data nd instead merges inputs obtained on the client side.

## Questions
How does this data structure not depend on the network? How can two different devices merge their versions and get the correct version out without sharing orders through the network?