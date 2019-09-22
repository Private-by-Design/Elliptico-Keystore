from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
Customer = {
    "1": {
        "CustomerId": "1",
        "TouchpointHashA": "5ba5d1088be355928aa9fd95ba3ee660ab9953d2e9f6a3d7dc804749c57c2ece",
        "Timestamp": get_timestamp()
    },
    "2": {
        "CustomerId": "2",
        "TouchpointHashA": "3f8a9067126ecd617c323b72b70730f993f6ff6f4556e607f79e8cf5f4423b8c",
        "Timestamp": get_timestamp()
    },
    "3": {
        "CustomerId": "3",
        "TouchpointHashA": "3f8a9067126ecd617c323b72b70730f993f6ff6f4556e607f79e8cf5f4423b8c",
        "Timestamp": get_timestamp()
    }
}


# Create a handler for our read (GET) customers
def read():
    """
    This function responds to a request for /api/customers
    with the complete lists of customers

    :return:        sorted list of customers
    """
    # Create the list of customers from our data
    return [Customer[key] for key in sorted(Customer.keys())]