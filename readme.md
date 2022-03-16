# KRX Dynamic Data Crawler

## Overview

<p>

Fetch data from the KRX data website.
KRX does not offer any sort of API
(They are very dumb at this sort of thing).
The module included in this project will 
support fetching data with selenium.

</p>

## Modules
<p> 

Modules are stored in ./krx folder.
```
./krx
|
- Xcrawl.py  # Crawl index component
- Vcrawl.py  # Crawl VIX future curve
- Dcrawl.py  # Crawl Deep Search Webpage
```
Modules Serve One and One url only. 
For instance, Xind.py only crawls index composition from KRX.

</p>


### Xind.py
<p>
New selenium downloads new chrome engine every time. 
Therefore, you do not have to check the chrome version. 
</p>

<p>
Features

1. Auto Date Correction 
2. Search Single Dates or Multiple Dates
3. From computer original download path to ./download
4. Color coded log messages


</p>

## Vcrawl.py
<p>
Features
  
1. vixcentral crawl.
2. vixcentral offers 20 historical data at a time
3. process: open browser -> set environment -> add dates -> download
</p>

## Dcrawl.py
<p>
  Features
  
1. crawl deepsearch news website
2. info: (1) News Title (2) News Type (3) News Time (4) News Source (5) News Content (6) News Sentiment (7) News target company
</p>
