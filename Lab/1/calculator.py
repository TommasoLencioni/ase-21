import operations as c

class Calculator(object):

    #empty constructor
    def __init__(self):
        pass

    def sum(self, m, n):
        return c.sum(m,n)

    def divide(self, m, n):
        return c.divide(m,n)
    
if __name__ == "__main__":
    x= calculator()
    print(x.sum(2,3))