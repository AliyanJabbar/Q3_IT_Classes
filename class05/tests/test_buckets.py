from inventory import Buckets


def test_buckets():
    # create a bucket instance
    bucket = Buckets("Test Bucket")
    # add an item to the bucket
    bucket.add_item("Laptop")
    # check if the item was added correctly
    assert "Laptop" in bucket.items
    assert len(bucket.items) == 1


# pytest need the file to be named -> start from test_ or ends with _test
