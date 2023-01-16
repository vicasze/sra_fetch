# Metadata searching with sra_fetch

This wrapper uses *pysradb* to retrieve sequencing metadata from SRA, ENA, or GEO databases. It allows the user to select the filtering criteria of interest, and retrieve results metadata, as well as relevant statistics and visualisations summarising the search.


## Installation
To use this software, you can first create and activate a conda environment with pysradb and all the necessary dependencies, with
```
conda env create -n pysradb -f env/pysradb.yaml
conda activate pysradb
```

## Usage
In order to run the software, the user needs to specify the searching criteria with the use of a json file, as defined in `/config/search_params.json`.

The searching criteria are:
```
- *output_folder* : name of the output folder. Default: "results".
- *database* : database to search in. Available are: "sra", "geo", "ena". Default: "sra".
- *query* : query terms of interest.
- *accession* : an accession id of interest.
- *organism* : name of species of interest.
- *layout* : library layout: "paired" or "single".
- *mbases* : sample size rounded to nearest mb.
- *publication_date* : publication date of the metadata in the format: "01-11-2020", or "01-01-2012:01-01-2023".
- *platform* : sequencing platform, e.g. "Illumina".
- *selection* : library selection, e.g. "cdna".
- *source* : library source, e.g. "transcriptomic".
- *strategy* : library preparation protocol, e.g. "rna-seq".
- *max_results* : number of results to output. Default: 20
```

Note: a query needs at least one criteria among: *query*, *accession*, *organism*, *layout*, *mbases*, *publication-date*, *platform*, *selection*, *source*, *strategy*. Field not relevant for the search can be left blank, with "".


To run the software, you need to pass the json file as input to the main function, as:
```
python ./src/sra_fetch.py -i search_params.json
```

## Output
The output of the module will be located in the specified output folder (results by default) and includes:
- *search_results.csv*: table with the results metadata corresponding to your search.
- *search_stats.log*: summary statistics of the data.
- *search_plots*: a folder containing different plots summarising the results.

## Test
You can test the module with two examples located in the test folder, that you can run with:
```
cd test

python ../src/sra_fetch.py -i search_params_1.json

python ../src/sra_fetch.py -i search_params_2.json
```

## Future developments
Some ideas for future development are:
- implementation of the rest of pysradb functions, such as the format converters and the search by accession id. 
- other visualizations, not included in the package: for example, one in which we can visualize all statistics as heatmap with accession ids as columns and the different statistics as rows. 
- this tools could be built into a web-app, using streamlit or similar tools. This would be particularly useful for non-computational scientists to search and visualise metadata without any need for config preparation and script running. 