class Individual:
    def __init__ ( self , iid,  **kwargs ):
        """
            This class holds details of the individuals at different locations
            in the lineage

        """
        self.id = iid
        self.name = kwargs.get('name' , None )
        ## pre-processing to make it easier for us to get nodes
        # self.children = sorted( children, key = lambda x : ( x is None, x ) )
        self.more = kwargs
    
    # def __cmp__ ( self , other ):
    #     if self.id > other.id:
    #         return 1
    #     elif self.id < other.id:
    #         return -1

    def __repr__ ( self ):
        if self.name is None:
            return str(self.id)
        else: 
            return str(self.name)
