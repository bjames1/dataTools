def make_container(keyList, itemList):
    container = {};
    for j in range(len(itemList)):
        key = keyList[j]
        item = {key: { i : None for i in itemList}}
        container.update(item)
    return container
