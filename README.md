# Entrez Retriever
Uses the Entrez API to query the NCBI servers for sequences.

## Usage
***WARNING: Most of these parameters will only be applied to the search query and not the fetch query. The only exception is the `database` parameter.***

### Mandatory arguments
You must use these arguments in order for the query to return any result.

`-db` or `--database`: Database to search in.

`-t` or `--term`: Entrez text query.

### Optional arguments
`-w` or `--webenv`: Web environment string returned from a previous ESearch, EPost or ELink call.

`-q` or `--querykey`: Integer query key returned by a previous ESearch, EPost or ELink call.

`-Rs` or `--retstart`: Sequential index of the first UID in the retrieved set to be shown in the XML output.

`-Rm` or `--retmax`: Total number of UIDs from the retrieved set to be shown in the XML output.

`-Rt` or `--rettype`: Retrieval type. There are two allowed values for ESearch: 'uilist' (default), which displays the standard XML output, and 'count', which displays only the \<Count> tag.

`-Rmd` or `--retmode`: Retrieval type. Determines the format of the returned output. The default value is 'xml' for ESearch XML, but 'json' is also supported to return output in JSON format.

`-s` or `--sort`: Specifies the method used to sort UIDs in the ESearch output.

`-f` or `--field`: Search field. If used, the entire search term will be limited to the specified Entrez field.

`-i` or `--idtype`: Specifies the type of identifier to return for sequence databases (nuccore, popset, protein).

`-dt` or `--datetype`: Type of date used to limit a search.

`-rd` or `--reldate`: When reldate is set to an integer n, the search returns only those items that have a date specified by datetype within the last n days.

`-md` or `--mindate`: "Minimum date used to limit a search result by the date specified by datetype. Must be used together with maxdate to specify an arbitrary date range.

`-Md` or `--maxdate`: Maximum date used to limit a search result by the date specified by datetype. Must be used together with mindate to specify an arbitrary date range.

## Credits
This program was developed by fonors, goncalof21, MadalenaFranco2 & scmdcunha.
