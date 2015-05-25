### WRITTEN BY ZAFARALI AHMED
### May 2015
import numpy as np

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
			size / int / 1000
				number of genes/bases in genome
		"""

		size = int( kwargs.get( 'size' , 1000 ) )
		assert size > 0 , 'genome_size must be non-zero positive'
		self.size = size

		self.mutation_rate = int( kwargs.get( 'mutation_rate' , 0 ) )
		assert self.mutation_rate > -1 , ' mutation rate cannot be negative '

		self.annotations = {}
		self.mutated_loci = []

	def replicate ( self ):
			replicated_genome = Genome( mutation_rate = self.mutation_rate , size = self.size )
			replicated_genome.mutated_loci.extend( self.mutated_loci )
			replicated_genome.annotations = dict( self.annotations )

			return replicated_genome


	def mutate ( self ):
		"""self.mutated_loci = []
			mutates the genome
		"""	
		# generate how many mutations we want
		number_of_mutations = np.random.poisson( self.mutation_rate )
		# generate random numbers representing loci
		loci = np.random.randint( self.size , size = number_of_mutations )
		# store the loci in mutated_loci if they aren't already there to represent
		for locus in loci:
			if locus in self.mutated_loci:
				# If they are there, remove that loci to represent 
				self.mutated_loci.remove( locus )
			else:
				# a bit flip to 0
				self.mutated_loci.append( locus )

		

	def get_mutated_loci ( self ):
		""" 
			@params: None
			@return: list of ints
				location of the loci of the mutation (bits that are 1)
		"""
		return self.mutated_loci

	def annotate ( self , locus , name ):
		self.annotations[name] = locus

	def is_mutated ( self , **kwargs ):
		"""
			is_mutated
				returns if a locus or specified annotation is mutated (i.e bit == 1)
			@params
				locus: index of gene
				name: annotation of the locus (use Genome.annotate to annotate loci)
				annotation: annotation of the locus (use Genome.annotate to annotate loci)
			@return
				boolean: depending on if the gene has been mutated
		"""
		# get locus
			# if no locus, get the name
			# get the locus of that name
			# if no locus related to the name, return None
		location = kwargs.get( 'locus' , self.annotations.get( kwargs.get( 'name' , None ) or kwargs.get( 'annotation' , None ) , None ) )
		assert location is not None , 'locus or name were non-valid'

		return location in self.mutated_loci



"""
	GenomeCompare
	allows easy analysis of two genomes
"""

class GenomeCompare:
	def __init__ ( self, genomes = [ None , None ] ):
		assert len( genomes ) == 2 , 'GenomeCompare only supports comparisons between two genomes for now '
		assert isinstance( genomes[0] , Genome ) and isinstance( genomes[1] , Genome ) , 'genomes must contain Genome objects only'
		
		self.g1 = genomes[0]
		self.g2 = genomes[1]

	def diff( self ):
		"""
			returns the number and loci of genes that
			are unqiue between the two genomes supplied
			[optional] if diff_map = True then it returns a n*n matrix with 1's 
			wherever the genes are different
		"""
		size = ( self.g1.size + self.g2.size ) / 2
		
		g1_mutated = self.g1.get_mutated_loci()
		g2_mutated = self.g2.get_mutated_loci()

		different_genes = 0
		different_loci = []


		for locus in g1_mutated:
			if not (locus in g2_mutated):
				different_genes += 1
				different_loci.append(locus)


		for locus in g2_mutated:
			if not(locus in g1_mutated) and not(locus in different_loci):
				different_genes +=1 
				different_loci.append(locus)
			


		
		return ( different_genes , different_loci )


