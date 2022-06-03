    # standby class for starting program
class Standby:
    def __init__(self, status):
        self.status = status


    # sets and gets standby status for the 
    def set_status(self, status):
        self.set_status = status


    def get_standby(self):
        return self.status


