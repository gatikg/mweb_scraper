from scraper import scrape_google_top_stories_selenium
import pandas as pd
from extract_info import extract_publisher_and_time
from previous_sheet_data import sheet_data
import sys

def main(sport):
    query = {"cricket": ["cricket"]}
    data = {"Links":[],"Publisher":[],"Publishing Time":[],"Summary":[]}
    for i in query[sport]:
        soup = scrape_google_top_stories_selenium(i)
        links,publishers,publishing_timing,summaries = extract_publisher_and_time(soup,data,sport)
        #data["Blocks"].append(blocks)
        for j in links:
            data["Links"].append(j)
        for j in publishers:
            data["Publisher"].append(j)
        for j in publishing_timing:
            data["Publishing Time"].append(j)
        for j in summaries:
            data["Summary"].append(j)

   # print(pd.DataFrame(data))
    sheet_data(sport,1,data)
        

  #  spreadsheet_name = 'Google Search Results'
   # worksheet_name = 'Top Stories'
   # save_to_google_sheets(data, spreadsheet_name, worksheet_name)

if __name__ == "__main__":
  sport ="cricket"
  main(sport)