import pkg_resources


class Data:
    """Base class for example datasets"""
    @classmethod
    def _get_path(cls, fname: str) -> str:
        """Returns path to filename within this data directory"""
        return pkg_resources.resource_filename('mypackage', 'data/{}'
                                               .format(fname))


class NumberLists(Data):
    """Examples 1d lists of numbers"""
    _example_data_1 = None

    @classmethod
    def example_data_1(cls):
        """1d dataset within data/example_data1.txt

        Returns
        -------
        list
            Data from example_data1.txt
        """
        if cls._example_data_1 is None:
            cls._example_data_1 = []
            path = cls._get_path('example_data1.txt')
            with open(path, "r") as infile:
                for line in infile:
                    cls._example_data_1.append(float(line.strip()))
        return cls._example_data_1
