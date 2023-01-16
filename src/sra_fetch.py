#!/usr/bin/env python

import json
import sys, getopt
import os

def main(argv):
	arg_input = ''
	opts, args = getopt.getopt(argv,"hi:",["ifile="])
	for opt, arg in opts:
		if opt == '-h':
			print ('sra_fetch.py -i <inputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			arg_input = arg
	print('Input search file:', arg_input)

	# -------------------------------------------- #
	# EXTRACT SEARCH PARAMETERS
	config_file = open(arg_input)
	pars = json.load(config_file)

	output_folder = pars["output_folder"] if pars["output_folder"] != "" else "results"

	database = pars["database"] if pars["database"] != "" else "sra"

	query = pars["query"] if pars["query"] != "" else None
	accession = pars["accession"] if pars["accession"] != "" else None
	organism = pars["organism"] if pars["organism"] != "" else None
	layout = pars["layout"] if pars["layout"] != "" else None
	mbases = pars["mbases"] if pars["mbases"] != "" else None
	publication_date = pars["publication_date"] if pars["publication_date"] != "" else None
	platform = pars["platform"] if pars["platform"] != "" else None
	selection = pars["selection"] if pars["selection"] != "" else None
	source = pars["source"] if pars["source"] != "" else None
	strategy = pars["strategy"] if pars["strategy"] != "" else None
	max_results = pars["max_results"] if pars["max_results"] != "" else 20

	# SOME SANITY CHECKS
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)

	if all(p is None for p in (query, accession, organism, layout, mbases, publication_date, platform, selection, source, strategy)):
		sys.exit("Please select some query terms or other filtering criteria for your search. Quitting.")
	else:
		pass


	# -------------------------------------------- #
	# SEARCH ACCORDING TO DATABASE
	if database in ["sra", "Sra", "SRA"]:
		from pysradb.search import SraSearch
		print('Selected database is SRA')

		# create search
		instance = SraSearch(
			query = query, 
			accession = accession,
			organism = organism,
			layout = layout, 
			mbases = mbases,
			publication_date = publication_date,
			platform = platform,
			selection = selection,
			source = source,
			strategy = strategy,
			return_max = max_results)

	elif database in ["ena", "Ena", "ENA"]:
		from pysradb.search import EnaSearch
		print('Selected database is ENA')

		# create search
		instance = EnaSearch(
			query = query, 
			accession = accession,
			organism = organism,
			layout = layout, 
			mbases = mbases,
			publication_date = publication_date,
			platform = platform,
			selection = selection,
			source = source,
			strategy = strategy,
			return_max = max_results)

	elif database in ["geo", "Geo", "GEO"]:
		from pysradb.search import GeoSearch
		print('Selected database is GEO')

		# create search
		instance = GeoSearch(
			query = query, 
			accession = accession,
			organism = organism,
			layout = layout, 
			mbases = mbases,
			publication_date = publication_date,
			platform = platform,
			selection = selection,
			source = source,
			strategy = strategy,
			return_max = max_results)


	# -------------------------------------------- #
	# DO THE SEARCH
	instance.search()

	# SAVE RESULTS TO TABLE
	instance.get_df().to_csv(output_folder + "/search_results.csv", index = False)

	# SAVE STATS TO LOG FILE
	with open(output_folder + "/search_stats.log", "w") as sys.stdout:
		instance.show_result_statistics()

	# SAVE PLOTS
	instance.visualise_results(saveto = output_folder + "/search_plots/")

if __name__ == "__main__":
   main(sys.argv[1:])

