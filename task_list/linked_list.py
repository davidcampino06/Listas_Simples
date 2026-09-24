
class Node:
    """Each Node represents one task."""
    def __init__(self, task):
        self.task = task          # name of the task
        self.done = False         # False = pending, True = completed
        self.next = None          # link to the next node (starts empty)


class LinkedList:
    """Singly linked list that holds Node objects."""
    def __init__(self):
        self.head = None          # first node of the list (empty at start)

    def add_task(self, task_name):
        """Add a new task at the end of the list."""
        new_node = Node(task_name)

        # if the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # otherwise, walk to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # last node now points to the new node
        current.next = new_node

    def show_tasks(self):
        """Return a simple list of dictionaries with task info (for Flask)."""
        tasks = []
        current = self.head
        index = 0
        while current is not None:
            tasks.append({
                "index": index,
                "task": current.task,
                "done": current.done
            })
            current = current.next
            index += 1
        return tasks

    def delete_task(self, index):
        """Delete the task at the given position (index starts at 0)."""
        if self.head is None:
            return

        # case 1: delete the head
        if index == 0:
            self.head = self.head.next
            return

        # case 2: find the node before the one we want to delete
        current = self.head
        position = 0
        while current.next is not None and position < index - 1:
            current = current.next
            position += 1

        # skip the node to remove it from the chain
        if current.next is not None:
            current.next = current.next.next

    def complete_task(self, index):
        """Mark the task at the given position as completed."""
        current = self.head
        position = 0
        while current is not None:
            if position == index:
                current.done = True
                return
            current = current.next
            position += 1
