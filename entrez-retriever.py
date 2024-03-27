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
import argparse, requests

parser = argparse.ArgumentParser(
                    prog = 'Entrez Retriever',
                    description = 'Use the Entrez API to perform NCBI queries for sequences.')

def search_args(parser):
    parser.add_argument("-db", "--database", help="")
    parser.add_argument("-t", "--term", help="")
    parser.add_argument("-w", "--webenv", help="")
    parser.add_argument("-q", "--querykey", help="")
    parser.add_argument("-Rs", "--retstart", help="")
    parser.add_argument("-Rm", "--retmax", help="")
    parser.add_argument("-Rt", "--rettype", help="")
    parser.add_argument("-Rmd", "--retmode", help="")
    parser.add_argument("-s", "--sort", help="")
    parser.add_argument("-f", "--field", help="")
    parser.add_argument("-i", "--idtype", help="")
    parser.add_argument("-dt", "--datetype", help="")
    parser.add_argument("-rd", "--reldate", help="")
    parser.add_argument("-md", "--mindate", help="")
    parser.add_argument("-Md", "--maxdate", help="")

    args = parser.parse_args()
    return args

def search_query():
    """
    Performs a search query in the NCBI databases. Receives the database and the search term, along with any additional parameters.
    Uses the 'history' feature.
    """
    search_params = {'db': args.database, 'term': args.term, 'usehistory': 'y'}
    server_request = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/', params=search_params)