from urllib.parse import urlparse
from previous_sheet_data import sheet_data
from summary_generation import Summary_Generation
excluded_domains = ["google.com", "facebook.com", "meta.com", "twitter.com", "youtube.com"]

def extract_publisher_and_time(soup,data,sport):
    blocks = soup.find_all("div", {"class": "EDblX GpHuwc y74B4 ifNoke"})
    links =[ ]
    publishers= []
    publishing_timing =[ ]
    summaries = []
    previous_lists = sheet_data(sport)
    for block in blocks:
        for link in block.find_all("a"):
            href = link.get('href')
            if any(domain in href for domain in excluded_domains):
                continue
            if href not in data["Links"]:
                if href not in previous_lists:
                    publisher = link.find_next(class_="R8BTeb q8U8x du278d").get_text(strip=True)
                    publishing_time = link.find_next(class_="OSrXXb cyspcb").get_text(strip=True)
                    #block=[ ]
                    #block.append(block_number)
                    links.append(href)
                    publishers.append(publisher)
                    publishing_timing.append(publishing_time)
                    summaries.append(Summary_Generation(href))
        #block_number += 1
    return links,publishers,publishing_timing,summaries

  

                
