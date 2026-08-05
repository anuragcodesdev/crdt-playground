class Node:
    def __init__(self, id, parent_id, value, actor_id, timestamp, deleted=False):
        self.id = id
        self.parent_id = parent_id
        self.value = value
        self.actor_id = actor_id
        self.timestamp = timestamp
        self.deleted = deleted