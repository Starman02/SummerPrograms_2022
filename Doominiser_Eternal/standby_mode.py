    # standby class for starting program
class Standby:
    def __init__(self, status=0):
        self.status = status


    # sets and gets standby status for the 
    def set_status(self, status):
        self.status = status


    def get_standby(self):
        return self.status


