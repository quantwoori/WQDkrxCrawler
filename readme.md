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
- Xind.py  # Crawl index component
- (X....py)  # TBD
```
Modules Serve One and One url only. 
For instance, Xind.py only crawls index composition.

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

## 