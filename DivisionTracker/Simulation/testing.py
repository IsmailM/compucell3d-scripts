from DivisionTrackerPackage import Individual, Lineage

# print l

print Lineage.load_file('divisionTrackerOutput.csv').to_newick()