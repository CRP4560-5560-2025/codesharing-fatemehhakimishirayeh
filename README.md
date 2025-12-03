Author: Fatemeh Hakimi  
Date Created: December 2025  

# School Enrollment – Story County, Iowa (ACS S1401)

## Purpose of the Code
This project demonstrates how to download U.S. Census ACS data on school enrollment (Table S1401: School Enrollment), convert the GeoJSON data to a feature class, join it with a CSV table, map the results in ArcGIS Pro, and create a PNG plot using a custom Python toolbox.

---

## Data Accessed

- **Source:** U.S. Census Bureau, American Community Survey (ACS) 5-Year Estimates  
- **Table:** S1401 – School Enrollment  
- **Year:** 2023  
- **Geography:** Census Tract  
- **Location:** Story County, Iowa  
- **Main variable used:** “Population 3 years and over enrolled in school – Percent enrolled in public school”  
- **GeoJSON file:** `school-MapLayer.json` – tract boundaries for Story County  
- **CSV file:** `school.csv` – ACS S1401 values for Story County tracts

---

## Project Structure

### Data_school/
- `school-MapLayer.json` – GeoJSON boundary file  
- `school.csv` – Census table for school enrollment  

### Gis_school/
- `school.gdb` – File geodatabase with the feature class created from the GeoJSON  
- `School_Toolbox.pyt` – Python toolbox  

### output_school/
- `geojosn_fc.gdb` – Output geodatabase with joined feature class  
- `SCHOOL.png` – Plot exported from the toolbox  

---

# How to Run the Code Package

Below are the steps to run the ArcGIS Pro project and toolbox.

---

### 1. **Download the Project Zip File**  
Download the entire project as a ZIP file and save it to a location of your choice.

### 2. **Extract the Zip Folder**  
Extract the ZIP file to your chosen directory on your computer.

### 3. **Open the GIS Project in ArcGIS Pro**  
Inside the extracted folder, open the **GIS_school** folder and double-click the `school.aprx` file to open it in ArcGIS Pro.

### 4. **Open the Catalog Pane**  
In ArcGIS Pro, go to the **View** tab and select **Catalog Pane** to open it on the right side.

### 5. **Add a Folder Connection if Needed**  
If you don’t see your folder in the Catalog Pane:  
Right-click on **Folders** → select **Add New Folder Connection**.  
Navigate to the folder where you extracted the files (e.g., the `556` folder) and add it so it appears in the Catalog.

### 6. **Open the School Toolbox**  
Once the folder is connected, expand **GIS_school** and double-click the **school toolbox**.  
Open the tool named **"GeoJSON + CSV Join + Plot Tool."**

#### Note  
If you don’t see the "GeoJSON + CSV Join + Plot Tool" right away:  
First double-click the **school toolbox** to load its contents.  
Once it appears, you can double-click the tool to open the geoprocessing window.

---

### 7. Select Input Files
Select Input Files:  
In the tool window, you will have two input files to select:

Select CSV File: Choose school.csv from the Data_school folder.

Select GeoJSON File: Choose school-MapLayer.json from the same Data_school folder.

### 8. Set Output Location
Set Output Location:  
Under the output settings, select the output_school folder as the folder to save your outputs.

### 9. Set Join Attribute Name
Set Join Attribute Name:  
For the join attribute, type NAME in uppercase letters to ensure the CSV and feature class match correctly.

### 10. Set Display Style for Map Layer
Set Display Style for Map Layer:  
Choose "Graduated Color" as the display style for the map layer to visualize the data.

### 11. Choose Where to Save Graph PNG
Choose Where to Save Graph PNG:  
Finally, specify the path and file name for the output PNG file (e.g., output_school/SCHOOL.png).

### 12. Check the Result
Check the Result:  
After running, you should see the resulting map appear, confirming everything worked correctly.

---

Note

If you experience any confusion while following the steps in this README, I have included an additional PDF file titled “How to Run the Project.pdf”. This document provides the same instructions with step-by-step images, which may help clarify the process.
