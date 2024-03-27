#!/usr/bin/env python3
'''
    Entrez Retriever - Use the Entrez API to perform NCBI queries for sequences
    Copyright (C) 2024  fonors, goncalof21, MadalenaFranco2 & scmdcunha

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import argparse, requests, xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(
                    prog = 'Entrez Retriever',
                    description = 'Use the Entrez API to perform NCBI queries for sequences.')

def search_args(argparser):
    """
    Gets the arguments the user defined when running the script and returns them.
    """
    argparser.add_argument("-db", "--database", help="Database to search in.")
    argparser.add_argument("-t", "--term", help="Entrez text query.")
    argparser.add_argument("-w", "--webenv", help="Web environment string returned from a previous ESearch, EPost or ELink call.")
    argparser.add_argument("-q", "--querykey", help="Integer query key returned by a previous ESearch, EPost or ELink call.")
    argparser.add_argument("-Rs", "--retstart", help="Sequential index of the first UID in the retrieved set to be shown in the XML output.")
    argparser.add_argument("-Rm", "--retmax", help="Total number of UIDs from the retrieved set to be shown in the XML output.")
    argparser.add_argument("-Rt", "--rettype", help="Retrieval type. There are two allowed values for ESearch: 'uilist' (default), which displays the standard XML output, and 'count', which displays only the <Count> tag.")
    argparser.add_argument("-Rmd", "--retmode", help="Retrieval type. Determines the format of the returned output. The default value is 'xml' for ESearch XML, but 'json' is also supported to return output in JSON format.")
    argparser.add_argument("-s", "--sort", help="Specifies the method used to sort UIDs in the ESearch output.")
    argparser.add_argument("-f", "--field", help="Search field. If used, the entire search term will be limited to the specified Entrez field.")
    argparser.add_argument("-i", "--idtype", help="Specifies the type of identifier to return for sequence databases (nuccore, popset, protein).")
    argparser.add_argument("-dt", "--datetype", help="Type of date used to limit a search.")
    argparser.add_argument("-rd", "--reldate", help="When reldate is set to an integer n, the search returns only those items that have a date specified by datetype within the last n days.")
    argparser.add_argument("-md", "--mindate", help="Minimum date used to limit a search result by the date specified by datetype. Must be used together with maxdate to specify an arbitrary date range.")
    argparser.add_argument("-Md", "--maxdate", help="Maximum date used to limit a search result by the date specified by datetype. Must be used together with mindate to specify an arbitrary date range.")

    search_args = argparser.parse_args()
    return search_args

def search_query(search_args):
    """
    Performs a search query in the NCBI databases. Receives the database name and the search term, along with any additional parameters.
    Uses the 'history' feature.
    """
    search_params = {
        'db': search_args.database,
        'term': search_args.term,
        'retstart': search_args.retstart,
        'retmax': search_args.retmax,
        'rettype': search_args.rettype,
        'retmode': search_args.retmode,
        'sort': search_args.sort,
        'field': search_args.field,
        'idtype': search_args.idtype,
        'datetype': search_args.datetype,
        'reldate': search_args.reldate,
        'mindate': search_args.mindate,
        'maxdate': search_args.maxdate,
        'query_key': search_args.querykey,
        'WebEnv': search_args.webenv,
        'usehistory': 'y'
        }

    server_request = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/', params=search_params)
    return server_request

def seq_fetcher(query_results, og_search_args):
    """
    Uses the search_query() function to get the desired sequences, then it uses the 'history' feature to parse all the desired sequences and
    returns them in FASTA format.
    Outputs to STDOUT.
    """
    query_xml_elemtree = ET.fromstring(query_results.text)

    query_key = query_xml_elemtree.find("QueryKey").text
    webenv = query_xml_elemtree.find("WebEnv").text
    fetch_params = {
        'db': og_search_args.database,
        'rettype': 'fasta',
        'query_key': query_key,
        'WebEnv': webenv
    }

    server_request = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi', params=fetch_params)
    print(server_request.text)

if __name__ == "__main__":
    user_args = search_args(parser)
    server_info = search_query(user_args)
    seq_fetcher(server_info, user_args)
