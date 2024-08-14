
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Caris HPD PaperChartBuilder License 
* Oracle Client for HPD connection
* N(Mariners) Drive connection for Carisbatch running.

### Installation

1. Copy a execution file from the Mariners drive
   
   N:\Software\HPD\GeoTIFFChartExp\GeoTIFfromHPDv05.exe
   
2. Copy and edit the configuration file
   
   Copy config.yml into C:\Temp

   Add Chart name
   
4. Run the exe file(GeoTIFfromHPDv05.exe) from command window.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
The script asks the user which chart type to use while running and the user can choose one of three.

The chart is exported in the form selected by the user and returned to its original state.

After the script runs successfully, you can see the GeoTIFF files in two types(Original, Cut with Rnc Panel) in C:\Temp\chart.

Known Errors
1. Duplicarion with uncertified deletion
 ```
Chart NZ14600 ID1421 and Panel Number 1 has 6 duplicate Rnc Panel data,
Check HPD Paper Chart Editor for uncertified deletion.
 ```
 _For fixing uncertified data, please refer to the [How to fix duplication with uncertified deletion ](https://toitutewhenua.atlassian.net/wiki/spaces/LI/pages/647528462/How+to+fix+duplication+with+uncertified+deletion.)_


2. No Rnc Panel data
 ```
Chart NZ561 ID562 and Panel Number 1 does not have Rncpanel coordinate data,
Please check the instruction below to generate the Rnc panel data.
```
 _For fixing Rnc Panel data, please refer to the [How to generate Rnc Panel data](https://toitutewhenua.atlassian.net/wiki/spaces/LI/pages/643760129/How+to+generate+Rnc+panel+data.)_

3. No Oracle connection
```
oracledb.exceptions.OperationalError: DPY-6005: cannot connect to database (CONNECTION_ID=57bapLQ+Jh/+yhyoZoWAAw==).
[Errno 11001] getaddrinfo failed
[24516] Failed to execute script 'GeoTIFfromHPDv05' due to unhandled exception!
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
