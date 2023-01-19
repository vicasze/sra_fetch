# Metadata searching with sra_fetch

This repo describes an interface that uses *pysradb* to retrieve sequencing metadata from SRA, ENA, or GEO databases. It allows the user to select the filtering criteria of interest, and retrieve results metadata, as well as relevant statistics and visualisations summarising the search.


## Installation
To use this software, clone the repository; then create and activate a conda environment with pysradb and all the necessary dependencies, with
```
conda env create -n pysradb -f env/pysradb.yaml
conda activate pysradb
```

## Usage
In order to run the software, the user needs to specify the searching criteria with the use of a json file, as exemplified in `/config/search_params.json`.

The searching criteria are:
```
* "output_folder" : name of the output folder. Default: "results".
* "database" : database to search in. Available are: "sra", "geo", "ena". Default: "sra".
* "query" : query terms of interest.
* "accession" : an accession id of interest.
* "organism" : name of species of interest.
* "layout" : library layout: "paired" or "single".
* "mbases" : sample size rounded to nearest mb.
* "publication"date" : publication date of the metadata in the format: "dd-mm-yyyy", or "dd-mm-yyyy:dd-mm-yyyy".
* "platform" : sequencing platform, e.g. "Illumina".
* "selection" : library selection, e.g. "cdna".
* "source" : library source, e.g. "transcriptomic".
* "strategy" : library preparation protocol, e.g. "rna-seq".
* "max"results" : number of results to output. Default: 20
```

Note: a query needs at least one criteria among: *query*, *accession*, *organism*, *layout*, *mbases*, *publication*date*, *platform*, *selection*, *source*, *strategy*. Fields not relevant for the search can be left blank, with "".


Run the software by passing the json file as input (-i) to the main function, e.g.:
```
python ./src/sra_fetch.py -i config/search_params.json
```
Note that this run will not work, as the config file describes the parameters in general terms. For use-cases, see te "Test" section below.

## Output
The output of the module will be located in the specified output folder (results by default) and includes:
* *search_results.csv*: table with the results metadata corresponding to your search.
* *search_stats.log*: summary statistics of the data.
* *search_plots*: a folder containing different plots summarising the results.

## Test
You can test the module with two examples located in the test folder.The first test takes some time to run, as it is a wide search of "ribosome profiling" experiments done since 2013. The second test example is a narrower serch and so quite fast to run.
To run the tests:
```
cd test

python ../src/sra_fetch.py -i search_params_1.json

python ../src/sra_fetch.py -i search_params_2.json
```

## Future developments
Some ideas for future development are:
* implementation of the rest of pysradb functions, such as the format converters, and the data download. The latter could for example be implemented by adding a last parameter to the config file where the user specifies if they want to download the result data (e.g. a "download" : true/false parameter.)
* other visualizations, not included in the package: for example, one in which we can visualize all statistics (rows) at once as a function of accession id (columns) in a heatmap. 
* this tools could be built into a web-app, using streamlit or similar tools. This would be particularly useful for non-computational scientists to search and visualise metadata without any need for config preparation and script running. 