def iterate_parents(parents_ids: list, category):
    if category.parent:
        parents_ids.append(category.parent.id)
        return iterate_parents(parents_ids, category.parent)


def iterate_parents_titles(parents_titles: list, category):
    if category.parent:
        parents_titles.append(category.parent.title)
        return iterate_parents(parents_titles, category.parent)


def iterate_children(children_ids: list, category):
    for child in category.children.all():
        children_ids.append(child)
        return iterate_children(children_ids, child)
