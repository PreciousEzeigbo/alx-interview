def canUnlockAll(boxes):
    # Start with box 0 unlocked
    opened_boxes = set([0])
    # Stack to explore keys from opened boxes
    keys_to_explore = [0]
    
    # While there are keys to explore
    while keys_to_explore:
        # Get the next key
        current_box = keys_to_explore.pop()
        
        # Check all keys inside the current box
        for key in boxes[current_box]:
            # If the key opens a box that isn't opened yet
            if key not in opened_boxes and key < len(boxes):
                # Mark the box as opened
                opened_boxes.add(key)
                # Add the new box's keys to the stack for exploration
                keys_to_explore.append(key)
    
    # If the number of opened boxes matches the total number of boxes, return True
    return len(opened_boxes) == len(boxes)