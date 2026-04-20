def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    if valueDiff < 0:
        return False

    buckets = {}
    size = valueDiff + 1  # bucket size

