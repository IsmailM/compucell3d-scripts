## AUTHOR: ZAFARALI AHMED (@ZAFARALI)
## GITHUB.COM/ZAFARALI
## DIVISION TRACKER TO TRACK MITOTIC EVENTS
## ALSO ALLOWS US TO CONVERT BETWEEN MITOTIC EVENTS AND NEWICK FILEFORMAT


class DivisionTracker:
    def __init__ ( self, fileName = '../divisionTrackerOutput.csv' ):
        self.fileName = fileName
        
    ## this function saves a division event into the file
    ## in the format: time, parent, child1, child2
    def saveDivisionInfo ( self , time = 0 , parent = 1 , child1 = 2, child2 = 3 ):
        import csv
        with open ( self.fileName, 'a' ) as f:
            c = csv.writer( f )
            c.writerow( [ time , parent , child1, child2 ] )


    ## this function transfrms the output file
    ## into a newick standard tree format
    ## (A,B,(C,D),E);
    def outputToNewick ( self , newickFileName = None ):
    	if newickFileName is None:
    		newickFileName = self.fileName.split('csv')[0].join('newick')



# ## PHYLOGENY
# ## A tree that stores a lineage in terms of individuals
# class Phylogeny:
#     def __init__ ( self , parent ):
#         self.root = parent

# ## INDIVIDUAL
# ## An individual in the lineage, has an id and children as
# ## basic attributes, possible to extend with other kwargs



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


#### CODE SCAFFOLDING BY SIMON GRAVEL
#### MODIFICATIONS BY ZAFARALI AHMED
class Lineage:

    def __init__ ( self , sub1 = None , sub2 = None, time = 0, isRoot = False ):
        """
            The lineage class is used to describe ancestral lineages. A lineage 
            either starts from a sample at time 0 (a leaf) or it is the result of the 
            coalescence of two lineages. In either case, it traces back in time 
            until it coalesces.
        
            attributes: 
                sub1:the first descendant lineage (default: None if the lineage starts at present)
                sub2:the second descendant lineage (default: None if the lineage starts at present)
                If the lineage starts at present, both sub1 and sub2 are None. 
                If it is formed by coalescence, both are lineages. 
                T0: the time at which the lineage was first encountered (the most recent time)
                T1:  the time at which the lineage coalesces (typically not known when the lineage is first created)
                nsamples: the number of samples that trace their ancestry to this lineage
                length=T1-T0, the total times spent in the lineage. 
        """

        self.isRoot = isRoot

        if isRoot:
            self.sub1 = sub1
            self.sub2 = None
            return
        assert sub1 is not None, 'Sub1 cannot be none'
        assert sub2 is not None, 'sub2 cannot be none'
        assert isinstance( sub1 , Lineage ) or isinstance ( sub1 , Individual ), 'sub1 must either be a lineage or an individual'
        assert isinstance( sub2 , Lineage ) or isinstance ( sub2 , Individual ), 'sub2 must either be a lineage or an individual'
        assert time >= 0, 'time cannot be negative'

        self.sub1 = sub1 #the first descendant lineage
        self.sub2 = sub2 #the second descendant lineage 
        self.time = 0 #stores the time that the lineage came about

        if isinstance ( sub1, Individual ) and isinstance ( sub2, Individual ) :
            self.nsamples = 1 #since this is a leaf, there are only 2 individuals at this position
        elif isinstance ( sub1, Individual ) and isinstance ( sub2, Lineage ) :
            self.nsamples = sub2.nsamples
        elif isinstance ( sub1, Lineage ) and isinstance ( sub2, Individual ):
            self.nsamples = sub1.nsamples
        else:
            self.nsamples = sub1.nsamples + sub2.nsamples
        #     #then the lineage is a leaf, we store individuals as leaves or none
        #     assert isinstance( sub2, Individual ), 'Both sub1 and sub2 should be individuals'
            
        #     self.time = sub1

        #     

        # elif isinstance( sub1, Lineage ): 
        #     #we haven't defined T1 yet, but we assume that coalescing lineages will 
        #     #have a coalescing time:

        #     assert isinstance( sub2, Lineage ), 'sub2 must also be a lineage!'

        #     assert sub1.time == sub2.T1,"coalescing lineages should coalesce at the same time!"
            
        #     self.time = sub2.time #the founding time of the coalesced lineage is the coalescing time of 
        #     #the desending lineages.
        #     #Now compute the number of samples descending from the current lineage. 
        #     #Recursion makes this very simple! We can just add up the number of samples in each
        #     #sublineages
        #     self.nsamples = sub1.nsamples + sub2.nsamples #s/=.*/=.../
        # else:
        #     raise Exception(' sub1 is not a supported type, it must be either a lineage or an individual ')

    # def coalesce( self , lineage2 , time ):
    #     """
    #         coalesce the current lineage with a second lineage lineage2 at time t
    #         Updates the coalescence time in both lineages, and returns the coalesced lineage
    #     """
    #     self.T1 = time
    #     lineage2.T1 = time
    #     return Lineage ( self , lineage2 )

    # def plot(self,width,center):
    #     """
    #         Plots the lineage and all its descending lineages. To avoid overlap when plotting
    #         multiple lineages, we specify the width and center of the lineage along the x-axis.
    #         Time is plotted along the y axis, and uses the lineage T0 and T1
    #     """
    #     plt.plot([center,center],[self.T0,self.T1],'b') #plot vertical lineage
    #     if self.T0!=0:
    #         #assign width proportional to the number of lineages in each sub-lineage
    #         n1=self.sub1.nsamples
    #         n2=self.sub2.nsamples
    #         w1=n1*1./(n1+n2)*width
    #         w2=n2*1./(n1+n2)*width
    #         mid1=center-width/2.+w1/2. #Find the center of each window
    #         mid2=center+width/2.-w2/2.
    #         plt.plot([mid1,mid2],[self.T0,self.T0],'b') #plot horizontal connector
    #         self.sub1.plot(w1,mid1) #plot descending lineages
    #         self.sub2.plot(w2,mid2)

    # def get_length(self):
    #     """
    #         returns a tuple whose first element is the time spent in the current lineage, 
    #         and the second element is total length spent in the present lineage plus all descending lineages
    #     """
    #     self.length=self.T1-self.T0
    #     if self.sub1 is None: #then the time spent in the lineage and the total time are the same
    #         return (self.length,self.length)
    #     else:
    #         #to get the total time, use the recursion property again!
    #         #First compute the total length within the sub1 and sub2 lineages
    #         lengths1=self.sub1.get_length()[1]#s/=.*/.../
    #         lengths2=self.sub2.get_length()[1]#s/=.*/.../
            
    #         return (self.length,self.length+lengths1+lengths2) #s/\,self.*/,...)/
    
    def __repr__( self ):
        return '('+str(self.sub1)+', '+str(self.sub2)+')'

    def find ( self , key ):
        """
            Returns a tuple of (lineage, individual, LR) where the lineage contains 
            the individual we are searching for and LR(int) contains if its the first or second
            child or False otherwise
        """
        if isinstance( self.sub1 , Individual ):

            if self.sub1.id == key or self.sub1.name == key:

                return ( self , self.sub1 , 1 )


        if isinstance( self.sub2 , Individual ):

            if self.sub2.id == key or self.sub2.name == key:

                return ( self , self.sub2, 2 )

        ## we didn't find the individual, thus we continue searching downward
        if isinstance( self.sub1 , Lineage ):

            return self.sub1.find( key )

        if isinstance( self.sub1 , Lineage ):

            return self.sub2.find( key )

        ## we didn't find the individual even though we checked the subtrees, thus we return False

        return False

    def divide ( self , parent , child1 , child2 = None , time = 0 ):
        """
            replaces an individual with children
        """


        search = self.find( parent )
        if search is None:
            return False

        container, replaced, lr = search #lineage that contains the parent
        
        if child2 is None:
            child2 = replaced
        
        if self.isRoot:
            self.sub1 = child1
            self.sub2 = child2
            self.isRoot = False
            return

        if lr == 1:
            container.sub1 = Lineage( sub1 = child1 , sub2 = child2 , time = time )
        elif lr == 2: 
            container.sub2 = Lineage( sub1 = child1 , sub2 = child2 , time = time )



    def to_newick ( self ): 
        """
            convert this lineage to the newick standard for representing
            phylogeny for easy use later
        """
        return str(self)+';'
        pass