# Run queries

A query can be submitted to Spark as follows.

ZIP up the source code (Spark needs this to run the query):

```bash
zip -r defoe.zip defoe
```

Submit the source code to Spark along with information about your query:

```bash
spark-submit --py-files defoe.zip defoe/run_query.py <DATA_FILE> <MODEL_NAME> <QUERY_NAME> <QUERY_CONFIG_FILE> [-r <RESULTS_FILE>] [-n <NUM_CORES>]
```

where:

* `<DATA_FILE>` is a file that lists either URLs or file paths which are the files over which the query is to be run, one per line. Either URLs or file paths should be exclusively used, not both.
* `<MODEL_NAME>` specifies which text model is to be used, one of:
  -  `books`: British Library Books
  - `papers`: British Library Newspapers
  - `fmp`: Find My Past Newspapers
  - For example, `books` tells the code that the data files listed in `data.txt` are books so should be parsed into a books data model.
* `<QUERY_NAME>` is the name of a Python module implementing the query to run, for example `defoe.alto.queries.find_words_group_by_word` or `defoe.papers.queries.articles_containing_words`. The query must be compatible with the chosen model.
* `<QUERY_CONFIG_FILE>` is a query-specific configuration file. This is optional and depends on the query implementation.
* `<RESULTS_FILE>` is the query results file, to hold the query results in YAML format. If omitted the default is `results.yml`.
* `<NUM_CORES>` is the number of computer processor cores requested for the job. If omitted the default is 1.

**Note for Urika users**

* It is recommended that the value of 144 be used for `<NUM_CORES>`. This, with the number of cores per node, determines the number of workers/executors and nodes. As Urika has 36 cores per node, this would request 144/36 = 4 workers/executors and nodes.
* This is required as `spark-runner --total-executor-cores` seems to be ignored.

For example, to submit a query to search a set of books for occurrences of some words (e.g. "heart" or "hearts") and return the counts of these occurrences grouped by year, you could run:

```bash
spark-submit --py-files defoe.zip defoe/run_query.py data.txt books defoe.alto.queries.find_words_group_by_year queries/hearts.txt
```

where:

* `data.txt` is the file with the paths to the books files to run the query over.
* `defoe.alto.queries.find_words_group_by_year` is the module that runs the query.
* `queries/hearts.txt` is a configuration file for the query which contains a list of the words, one per line, to search for.

For example, to submit a query to search a set of newspapers for occurrences of gender-specific words (e.g. "she", "he" etc.) and return the counts of these occurrences grouped by year, you could run:

```bash
spark-submit --py-files defoe.zip defoe/run_query.py ~/data/papers.2.txt papers defoe.papers.queries.articles_containing_words queries/gender.txt
```

where:

* `data.txt` is the file with the paths to the papers files to run the query over.
* `defoe.papers.queries.articles_containing_words` is the module that runs the query.
* `queries/gender.txt` is a configuration file for the query which contains a list of the words, one per line, to search for.

If successful the results will be written into a new file (by default called `results.yml`) in the current directory.

---

## Submit a job to Spark as a background process

To submit a job to Spark as a background process, meaning you can do other things while Spark is running your query, use `nohup` and capture the output from Spark in ` log.txt` file. For example:

```bash
nohup spark-submit --py-files defoe.zip defoe/run_query.py <DATA_FILE> <MODEL_NAME> <QUERY_NAME> <QUERY_CONFIG_FILE> [-r <RESULTS_FILE>] [-n <NUM_CORES>] > log.txt &
```

---

## Check number of executors used

A quick-and-dirty way to check the number of executors used is, if you have used `nohup` and output capture to `log.txt`, to run:

```bash
grep Exec log.txt | wc -l
```

---

## Troubleshooting: `spark-submit: command not found`

If running `spark-submit` locally you get:

```
bash: spark-submit: command not found...
```

Then add Apache Spark to your `PATH` e.g.

```bash
export PATH=~/spark-2.4.0-bin-hadoop2.7/bin:$PATH
```

---

## Troubleshooting: `No such file or directory: ''` and `Error reading file: ''`
If you get an error like:

```
IOError: [Errno 2] No such file or directory: ''
```

or:

```
IOError: Error reading file '': failed to load external entity ""
```

then check for blank lines in your data file and, if there are any, then remove them.

---

## Troubleshooting: `result.yml` is `{}`

If you run:

```bash
head result.yml
```

and see:

```
{}
```

then check that the files the query is being run over exist.

If the files are on the local file system then also check their permissions. This error can arise if, for example, a data file has permissions like:

```bash
ls -l /mnt/lustre/<user>/blpaper/0000164_19010101.xml
```
```
---------- 1 <user> at01 3374189 May 31 13:57
```

---

## Troubleshooting: `raise BadZipfile, "File is not a zip file"`

If you get an exception

```
raise BadZipfile, "File is not a zip file"
```

then check that the files the query is being run over exist.
