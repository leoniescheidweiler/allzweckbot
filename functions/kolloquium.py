import requests
import re

def kolloquium():
    page_content = requests.get('https://www.physi.uni-heidelberg.de/Veranstaltungen/vortraege.php?kol=PK').text

    my_string = " ".join(page_content.splitlines())

    regex = '<td bgcolor="#FFFFC0">(.*?)</td>'
    td_block = re.findall(regex, my_string)[0]

    regex = '<a href=(.*?)>(.*?)</a>'
    href_blocks = re.findall(regex, td_block)

    title_link      = re.sub('(<[^>]+>|[\'\"])', '', href_blocks[0][0])
    title           = re.sub('(<[^>]+>|[\'\"])', '', href_blocks[0][1])
    professor_link  = re.sub('(<[^>]+>|[\'\"])', '', href_blocks[1][0])
    professor       = re.sub('(<[^>]+>|[\'\"])', '', href_blocks[1][1])

    output = 'Kolloquium:\n['+title_link+']('+title+')\n['+professor_link+']('+professor+')'

    return(output)
