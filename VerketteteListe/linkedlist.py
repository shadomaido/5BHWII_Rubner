class ChainedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_entry = Entry(data)
        if not self.head:
            self.head = new_entry
            return

        current_item = self.head
        while current_item.next:
            current_item = current_item.next
        current_item.next = new_entry

    def get_length(self):
        count = 0
        current_item = self.head
        while current_item:
            count += 1
            current_item = current_item.next
        return count

    def print_all(self):
        current_element = self.head
        while current_element:
            print(current_element.data, end=" ")
            current_element = current_element.next
        print()

    def __iter__(self):
        current_element = self.head
        while current_element:
            #yield liefert werte, ohne whileschleife zu unterbrechen
            #stückweise verarbeitung der Elemente
            #kümmert sich um die __next__ methode, implementiert __next__ methode, ohne
            #dass wir sie ausprogrammeiren müssen
            yield current_element.data
            current_element = current_element.next

class Entry:
    def __init__(self, data):
        self.data = data
        self.next = None


