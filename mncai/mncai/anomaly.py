"""
anomaly.py: Anomaly detection.
"""

class Anomaly(object):
    """
    Anomaly detection.
    """

    def __init__(self, data, threshold=0.5):
        """
        Initialize the anomaly detection.

        :param data: The data to be analyzed.
        :param threshold: The threshold for the anomaly detection.
        """
        self.data = data
        self.threshold = threshold

    def detect(self):
        """
        Detect the anomalies.

        :return: The list of anomalies.
        """
        raise NotImplementedError("This method must be implemented.")

    def __str__(self):
        """
        Return a string representation of the anomaly detection.

        :return: The string representation of the anomaly detection.
        """
        return "Anomaly detection: {}".format(self.__class__.__name__)

    def __repr__(self):
        """
        Return a string representation of the anomaly detection.

        :return: The string representation of the anomaly detection.
        """
        return self.__str__()
    
    
    
if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    import sys
    print(sys.path)