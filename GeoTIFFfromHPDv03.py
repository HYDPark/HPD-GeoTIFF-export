## Edition2 for Manual Publishing
## Remove LDS Publishing Module
## Change Error control -- User notification for data duplication and fixing
###########################################################################
# Required
# Caris HPD PaperChartBuilder License 
# Oracle Client for HPD connection
# N(Mariners) Drive connection for Carisbatch running.
###########################################################################

import os
import os.path
import oracledb
from shapely import geometry
from osgeo import ogr, osr, gdal
import yaml

Save = 'C:\\Temp\\chart\\single\\'

def main():  
    
    with open('config.yml', 'r') as file:
        HPDConnection = yaml.safe_load(file)
        user = HPDConnection['HPDConnection']['User']
        password = HPDConnection['HPDConnection']['PW']
        dsn = HPDConnection['HPDConnection']['dsn'] +':'+ HPDConnection['HPDConnection']['port'] +'/'+ HPDConnection['HPDConnection']['DBname']
        Dbname = HPDConnection['HPDConnection']['DBname']    
            
        Charts = HPDConnection['Datasets']['Charts']
        for chart in Charts:
            chartname = chart
            print(chartname)
                    
    file.close()


if __name__ == "__main__":
    main()
    




