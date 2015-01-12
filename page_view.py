


class Session(object):
    def __init__(self, first_page_view):
        self.first_page_view = first_page_view
    def get_first_page_view(self):
        return self.first_page_view

class PageView(object):
    def __init__(self, item, purchased):
        self.item = item
        self.purchased = purchased
        self.next_page_view = None
    def set_next_page_view(self, next_page_view):
        self.next_page_view = next_page_view
    def get_next_page_view(self):
        return self.next_page_view
    def __str__(self):
        return self.item + ":" + str(self.purchased)

def handler_one(session, specific_item_name, next_count):
    cur_page_view = session.get_first_page_view()
    cur_index = 0
    specific_page_view = None
    specific_index = 0
    results = []
    while cur_page_view:
        if cur_page_view.item == specific_item_name:
            specific_page_view = cur_page_view
            specific_index = cur_index
            print specific_page_view
        if specific_page_view and (specific_index + next_count) == cur_index and cur_page_view.purchased:
            results.append(cur_page_view)
        cur_page_view = cur_page_view.get_next_page_view()
        cur_index += 1
        continue
    return results

def flat(list_in_list):
    return [item for sublist in list_in_list for item in sublist]

def most_common(lst):
    return max(set(lst), key=lst.count)    


def most_bought_after_seeing(specific_item_name, sessions, next_count):
    results = [handler_one(session, specific_item_name, next_count) for session in sessions]
    flaten_results = flat(results)
    most_one = most_common(flaten_results)
    return (most_one, flaten_results.count(most_one))



if __name__ == '__main__':
    from minitest import *
    
    pv21 = PageView("ItemC", False)
    pv22 = PageView("ItemA", False)
    pv23 = PageView("ItemC", True)
    pv24 = PageView("ItemD", True)
    s2 = Session(pv21)
    pv21.set_next_page_view(pv22)
    pv22.set_next_page_view(pv23)
    pv23.set_next_page_view(pv24)

    handler_one(s2, "ItemC", 1).pp()


