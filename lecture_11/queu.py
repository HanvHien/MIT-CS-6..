class Queue(object):

    def __init__(self):
        self.vals = []

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def insert(self, e):
        self.vals.append(e)

    def remove(self):
        if len(self.vals) > 0:
            retval = self.vals[0]
            self.vals.remove(retval)
            return retval
        else:
            raise ValueError()
