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
		return self

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

	@staticmethod
	def from_mutated_loci ( mutated_loci, size = 1000 ):
		to_return = Genome(size=size)
		to_return.mutated_loci = sorted(list(mutated_loci))
		return to_return

"""
	GenomeCompare
	allows easy analysis of two genomes
"""

class GenomeCompare:
	def __init__ ( self, genomes = [ None , None ] ):
		raise DeprecationWarning('GenomeCompare has been moved to its own file. Reimport from cc3dtools.GenomeCompare' )

def save_genomes( genomes , file_name = 'genomes_saved_output.csv' ):
	"""
		saves an array of genomes to a file
		@params:
			genomes / array
				an array of genomes to be genomes to be saved
			file_name / string / 'genomes_saved_output.csv'
				file name to save the genomes into

		(!) this only saves the mutated loci and not genome sizes etc.
	"""
	assert genomes is not None ,  'you must supply an array of genomes as the first argument'
	assert len( genomes ) > 0 , 'you must supply at least one genome'
	import csv

	with open( file_name, 'w' ) as f:
		writer = csv.writer( f )
		for k, genome in enumerate( genomes ):
			writer.writerow( sorted( genome.get_mutated_loci() ) )
	pass


