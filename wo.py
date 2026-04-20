def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    if valueDiff < 0:
        return False

    buckets = {}
    size = valueDiff + 1  # bucket size

    def get_bucket_id(num):
        return num // size  # works for negative too

    for i, num in enumerate(nums):
        bucket_id = get_bucket_id(num)

        # Same bucket
        if bucket_id in buckets:
            return True

        # Neighbor buckets
        if (bucket_id - 1 in buckets and 
            abs(num - buckets[bucket_id - 1]) <= valueDiff):
            return True

        if (bucket_id + 1 in buckets and 
            abs(num - buckets[bucket_id + 1]) <= valueDiff):
            return True

        # Add current number
        buckets[bucket_id] = num

        # Maintain sliding window
        if i >= indexDiff:
            old_bucket_id = get_bucket_id(nums[i - indexDiff])
            del buckets[old_bucket_id]

    return False
