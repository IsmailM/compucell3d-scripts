## MAY 2015

"""
	GenomeCompare
	allows easy analysis 
"""

from Genome import Genome

class GenomeCompare:
	def __init__ ( self, genomes = [ None , None ] ):
		assert len( genomes ) > 1 , 'Must provide at least two genomes to initiatile GenomeCompare'
		assert isinstance( genomes[0] , Genome ) and isinstance( genomes[1] , Genome ) , 'genomes must contain Genome objects only'
		self.genomes = genomes		
		
	def diff( self , genome1 , genome2 ):
		"""
			returns the number and loci of genes that
			are unqiue between the two genomes supplied whos id are supplied
			@params
				genome1 / int / index of the first genome to compare
				genome2 / int / index of the second genome to compare
			@return
				object with properties specified
		"""

		g1 = self.genomes[genome1]
		g2 = self.genomes[genome2]

		size = ( g1.size + g2.size ) / 2
		
		g1_mutated = g1.get_mutated_loci()
		g2_mutated = g2.get_mutated_loci()

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
			
		return { 'total_unique_mutations': different_genes , 'loci_different': different_loci  }

	def comm( self , genome1 , genome2 ):
		"""
			returns the number and loci common to
			a pair of genomes whos id are supplied
		"""

		g1 = self.genomes[genome1]
		g2 = self.genomes[genome2]


		size = ( g1.size + g2.size ) / 2

		g1_mutated = g1.get_mutated_loci()
		g2_mutated = g2.get_mutated_loci()

		common_mutations = 0
		common_mutation_loci = []

		for locus in g1_mutated:
			if locus in g2_mutated:
				common_mutations += 1
				common_mutation_loci.append(locus)

		for locus in g2_mutated:
			if locus in g1_mutated and not (locus in common_mutation_loci):
				common_mutations += 1 
				common_mutation_loci.append(locus)

		return { 'total_common_mutations': common_mutations , 'loci_common': common_mutation_loci }


	@staticmethod
	def from_gen_file ( file_name ):
		"""
			imports a gen_file and returns a GenomeCompare object
		"""

		import csv
		genomes = []
		with open( file_name , 'r' ) as f:
			reader = csv.reader( f ) 
			for row in reader:
				genomes.append( Genome.from_mutated_loci( row ) )
		return GenomeCompare( genomes = genomes )
