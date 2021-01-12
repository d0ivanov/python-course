def validate_file_type(filename, allowed_types):
    '''
    Check if the file type is valid.
    Allowed types must be an array
    '''
    return filename.split(".")[-1] in allowed_types


def split_in_groups(lst, group_size=3):
    offset = 0
    limit = min(group_size, len(lst))
    res = [lst[0:limit]]
    while limit < len(lst):
        offset = limit
        limit = min(limit + group_size, len(lst))
        res.append(lst[offset:limit])
    return res

def generate_room_id(sender, receiver):
    return '_'.join(sorted([str(sender), str(receiver)]))

