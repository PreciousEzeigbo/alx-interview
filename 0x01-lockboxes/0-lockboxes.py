#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    # Auxiliary dictionary to track opened boxes and their keys
    aux = {}
    
    # Start by opening box 0
    aux[0] = {
        'status': 'opened',
        'keys': boxes[0],
    }
    
    while True:
        # Look for the next opened box to explore its keys
        keys = look_next_opened_box(aux)
        
        # If there are keys to explore
        if keys:
            for key in keys:
                # Only process valid keys and unopened boxes
                if key < len(boxes) and not aux.get(key):
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
        # If no more keys are available for unopened boxes
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        
        # If all boxes have been opened, we're done
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()