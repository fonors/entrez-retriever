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
from sys import stderr, exit

parser = argparse.ArgumentParser(
                    prog = 'Entrez Retriever',
                    description = 'Use the Entrez API to perform NCBI queries for sequences.')

parser.add_argument("-db", "--database", help="Database to parse in")
parser.add_argument("-t", "--term", help="Search term for the query")
args = parser.parse_args()

def search_query():
    """
    Performs a search query in the NCBI databases. Receives the database and the search term, along with any additional parameters.
    Uses the 'history' feature.
    """
    search_params = {'db': args.database, 'term': args.term, 'usehistory': 'y'}
    server_request = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/', params=search_params)