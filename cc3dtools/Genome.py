### WRITTEN BY ZAFARALI AHMED
### May 2015


"""
	Genome
		emulates a 'genome' of a cell. has replication and mutation capabilities
		the genome contains 0s and 1s. If a base is mutated it is represented by 1
"""
class Genome:
	def __init__ ( self, **kwargs ):
		"""
			creates a new genome
			@params:
			mutation_rate / float or int / 0
				the rate at which bases of the genome are mutated (i.e bit flipped from 0 --> 1)
			replication_event / boolean
				specifies if this initialization event is a replication of a previously existing genome
			genome_to_copy / Genome / False
				the genome that must be replicated	

		"""

		# (1) is this genome being created due to a replication event?

		replication_event = kwargs.get( 'replication_event' , False )

		if replication_event:
			# get the genome we need copied
			# assign the same loci to this genome as the reference one
			# we now have a duplicate
			genome_to_copy = kwargs.get( 'genome_to_copy' , None )
			assert genome_to_copy is not None, 'Cannot replicate a Genome that doesn\'nt exist!'
			assert isinstance( genome_to_copy , Genome ) , 'cannot copy a non-Genome object!'
			## @TODO: do we use deep_copy or a shallow_copy?
			## since these are ints to they really matter?
			return

		self.mutated_loci = []
		self.mutation_rate = kwargs.get( 'mutation_rate' , 0 )




	def mutate ( self ):
		"""
			mutates the genome
		"""	
		# generate how many mutations we want
		# generate random numbers representing loci
		# store the loci in mutated_loci if they aren't already there to represent
		# a bit flip to 1. If they are there, remove that loci to represent 
		# a bit flip to 0
		pass

	def get_mutated_loci ( self ):
		""" 
			@params: None
			@return: list of ints
				location of the loci of the mutation (bits that are 1)
		"""
		return self.mutated_loci
