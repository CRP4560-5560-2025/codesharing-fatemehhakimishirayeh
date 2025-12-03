Author: Fatemeh Hakimi  
Date Created: December 2025  

Project Title: School Enrollment – Story County, Iowa (ACS S1401)

Purpose of the Code  
This project demonstrates how to download U.S. Census ACS data on school enrollment (Table S1401: School Enrollment), convert the GeoJSON data to a feature class, join it with a CSV table, map the results in ArcGIS Pro, and create a PNG plot using a custom Python toolbox.

Data Accessed  
- Source: U.S. Census Bureau, American Community Survey (ACS) 5-Year Estimates  
- Table: S1401 – School Enrollment  
- Year: 2023  
- Geography: Census Tract  
- Location: Story County, Iowa  
- Main variable used: “Population 3 years and over enrolled in school – Percent enrolled in public school”  
- GeoJSON file: `school-MapLayer.json` (tract boundaries for Story County)  
- CSV file: `school.csv` (ACS S1401 values for Story County tracts)

Project Structure  
- `Data_school/`  
  - `school-MapLayer.json` – GeoJSON boundary file  
  - `school.csv` – Census table for school enrollment  
- `Gis_school/`  
  - `school.gdb` – File geodatabase with the feature class created from the GeoJSON  
  - `School_Toolbox.pyt` – Python toolbox  
- `output_school/`  
  - `geojosn_fc.gdb` – Output geodatabase with joined feature class  
  - `SCHOOL.png` – Plot exported from the toolbox

How to Run the Code Package  
1. Open the ArcGIS Pro project (`school.aprx`) included in this package.  
2. In the Catalog pane, open the **School_Toolbox.pyt** toolbox.  
3. Run the tool **GeoJSON + CSV Join + Plot Tool**.  
4. Set the parameters as follows:  
   - *Select CSV File:* choose `school.csv` from the `Data_school` folder.  
   - *Select GeoJSON File:* choose `school-MapLayer.json` from the `Data_school` folder.  
   - *Folder to Save Outputs:* select or create the `output_school` folder.  
   - *Join Attribute Name (Both CSV & Feature Class):* `NAME`  
   - *Display Style for Map Layer:* `Graduated Colors`  
   - *Choose Where to Save Graph PNG:* path and file name for the PNG (e.g., `output_school/SCHOOL.png`).  
5. The tool will:  
   - Convert the GeoJSON file to a feature class in a file geodatabase,  
   - Join the CSV table to the feature class using the `NAME` field,  
   - Add the joined layer to the map with graduated colors,  
   - Save a PNG plot summarizing the school enrollment data.

Notes  
- Keep the folder structure the same when sharing the project so that paths remain valid.  
- If the map does not look correct, make sure the symbology field is set to the percentage variable from S1401 (not a coordinate field).
