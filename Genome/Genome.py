

class Genome:
	def __init__ ( self, mutationRate, **kwargs ):

		# is this genome being created due to a replication event?

		replication_event = kwargs.get( 'replication_event' , False )

		if replication_event:
			# get the genome we need copied
			# assign the same loci to this genome as the reference one
			# we now have a duplicate
			genome_to_copy = kwargs.get( 'genome_to_copy' , None )
			assert genome_to_copy is not None, 'Cannot replicate a genome that doesn\'nt exist!'
			assert isinstance( genome_to_copy , Genome ) , 'cannot copy a non-Genome object!'
			## @TODO: do we use deep_copy or a shallow_copy?
			## since these are ints to they really matter?
			return

		self.mutatedLoci = []
		self.mutationRate = mutationRate




	def mutate ( self ):
		# generate how many mutations we want
		# generate random numbers
		# store the numbers in mutatedLoci if they aren't there to represent
		# a bit flip to 1. If they are there, remove that loci to represent 
		# a bit flip to 0
		pass

	def replicate( self ):
		# create a copy of this genome and return that genome
		pass
