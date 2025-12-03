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
1.	Download the Project Zip File:
Download the entire project as a ZIP file and save it to a location of your choice.
2.	Extract the Zip Folder:
Extract the ZIP file to your chosen directory on your computer.
3.	Open the GIS Project in ArcGIS Pro:
Inside the extracted folder, open the GIS_school folder and double-click the school.aprx file to open it in ArcGIS Pro.
4.	Open the Catalog Pane:
In ArcGIS Pro, go to the View tab and select Catalog Pane to open it on the right side.

5.	Add a Folder Connection if Needed:
If you don’t see your folder in the Catalog Pane, right-click on Folders and choose Add New Folder Connection. Navigate to the folder where you extracted the files (e.g., the 556 folder), and add it so it appears in the Catalog.
 
6.	Open the School Toolbox:
Once the folder is connected, expand GIS_school and double-click the school toolbox. Open the tool named "GeoJSON + CSV Join + Plot Tool."
 pic
     •  Note: If you don’t see the "GeoJSON + CSV Join + Plot Tool" right away, first double-click the school toolbox to load its contents. Once it appears, you can then double-click the "GeoJSON + CSV Join + Plot Tool" to open the geoprocessing window.

pic
7.	Select Input Files:
In the tool window, select your CSV file from the Data_school folder and your GeoJSON file from the same folder.
pic

8.	Set Output Location and Join Field:
Choose the output_school folder as your output location and enter NAME (in uppercase) as the join attribute.

10.	Set Display Style and Run the Tool:
Select "Graduated Color" for the display style, name your output (e.g., school2), and run the tool.

12.	Check the Result:
After running, you should see the resulting map appear, confirming everything worked correctly.
 pic

