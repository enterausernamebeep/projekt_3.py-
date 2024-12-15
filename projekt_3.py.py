"

projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Petr Vrba
email: pvrba01@gmail.com
discord: petrv_95056

"


import sys
import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://volby.cz/pls/ps2017nss/"
HEADERS = ['Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky', 'Platné hlasy']


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Fetching data from: {url}")
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        sys.exit(1)

def parse_main_page(html):
    towns = []
    links = []
    town_ids = []
    
    town_rows = html.find_all("tr")[2:]
    for row in town_rows:
        id_cell = row.find("td", {"class": "cislo"})
        name_cell = row.find("td", {"class": "overflow_name"})

        if id_cell and name_cell:
            link = id_cell.a["href"]
            town_ids.append(id_cell.text.strip())
            towns.append(name_cell.text.strip())
            links.append(BASE_URL + link)

    return town_ids, towns, links

def parse_municipality_page(html):
    voters = html.find("td", {"headers": "sa2"}).text.strip().replace('\xa0', '')
    envelopes = html.find("td", {"headers": "sa3"}).text.strip().replace('\xa0', '')
    valid_votes = html.find("td", {"headers": "sa6"}).text.strip().replace('\xa0', '')

    parties = []
    votes = []
    results = html.find_all("td", {"headers": "t1sb3"})
    for result in results:
        party_name = result.find_previous_sibling("td", {"class": "overflow_name"}).text.strip()
        vote_count = result.text.strip().replace('\xa0', '')
        parties.append(party_name)
        votes.append(vote_count)

    return voters, envelopes, valid_votes, parties, votes

def write_csv(file_name, headers, rows):
    print(f"Saving data to {file_name}")
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        writer.writerows(rows)

def election_scraper(start_url, output_file):
    main_html = fetch_html(start_url)
    town_ids, town_names, links = parse_main_page(main_html)

    all_rows = []
    party_set = set()

    for town_id, town_name, link in zip(town_ids, town_names, links):
        town_html = fetch_html(link)
        voters, envelopes, valid_votes, parties, votes = parse_municipality_page(town_html)

        party_set.update(parties)
        row = [town_id, town_name, voters, envelopes, valid_votes]
        row.extend(votes)
        all_rows.append(row)

    sorted_parties = sorted(party_set)
    headers = HEADERS + sorted_parties

    complete_rows = []
    for row in all_rows:
        base_data = row[:5]
        party_votes = row[5:]
        party_map = dict(zip(parties, party_votes))
        sorted_votes = [party_map.get(party, "0") for party in sorted_parties]
        complete_rows.append(base_data + sorted_votes)

    write_csv(output_file, headers, complete_rows)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scraper.py <URL> <output_file.csv>")
        sys.exit(1)

    start_url = sys.argv[1]
    output_file = sys.argv[2]
    election_scraper(start_url, output_file)
