

# -*- coding: utf-8 -*-
import arcpy
import matplotlib.pyplot as plt
import pandas as pd
import os
import re

class Toolbox(object):
    def __init__(self):
        self.label = "Story County Toolbox"
        self.alias = "storycounty"
        self.tools = [GeoJSONCSVJoinAndPlot]

class GeoJSONCSVJoinAndPlot(object):

    def __init__(self):
        self.label = "GeoJSON + CSV Join + Plot Tool"
        self.description = "Converts GeoJSON to Feature Class, joins CSV, displays layer, and saves a plot."
        self.canRunInBackground = False

    def getParameterInfo(self):

        # 1. CSV input
        csv_file = arcpy.Parameter(
            displayName="Select CSV File",
            name="csv_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        csv_file.filter.list = ["csv"]

        # 2. GeoJSON input
        geojson_file = arcpy.Parameter(
            displayName="Select GeoJSON File",
            name="geojson_file",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        geojson_file.filter.list = ["geojson", "json"]

        # 3. Output folder
        output_folder = arcpy.Parameter(
            displayName="Folder to Save Outputs",
            name="output_folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )

        # 4. Attribute name for join
        join_field = arcpy.Parameter(
            displayName="Join Attribute Name (Both CSV & Feature Class)",
            name="join_field",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        # 5. Display option dropdown
        display_option = arcpy.Parameter(
            displayName="Display Style for Map Layer",
            name="display_option",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        display_option.filter.type = "ValueList"
        display_option.filter.list = ["Single Symbol", "Graduated Colors", "Graduated Symbols"]

        # 6. Output PNG graph
        png_output = arcpy.Parameter(
            displayName="Choose Where to Save Graph PNG",
            name="png_output",
            datatype="DEFile",
            parameterType="Required",
            direction="Output"
        )
        png_output.filter.list = ["png"]

        return [
            csv_file,
            geojson_file,
            output_folder,
            join_field,
            display_option,
            png_output,
        ]

    def execute(self, parameters, messages):

        csv_file = parameters[0].valueAsText
        geojson_file = parameters[1].valueAsText
        output_folder = parameters[2].valueAsText
        join_field = parameters[3].valueAsText
        display_option = parameters[4].valueAsText
        png_output = parameters[5].valueAsText

        arcpy.AddMessage("Reading CSV...")
        df = pd.read_csv(csv_file)

        # Create output feature class
        fc_out = os.path.join(output_folder, "geojson_fc.gdb")
        if not arcpy.Exists(fc_out):
            arcpy.management.CreateFileGDB(output_folder, "geojson_fc.gdb")

        fc = os.path.join(fc_out, "tracts_fc")

        arcpy.AddMessage("Converting GeoJSON to Feature Class...")
        arcpy.conversion.JSONToFeatures(geojson_file, fc)

        # Join
        arcpy.AddMessage("Joining CSV to Feature Class...")
        arcpy.management.AddJoin(
            in_layer_or_view=fc,
            in_field=join_field,
            join_table=csv_file,
            join_field=join_field,
            join_type="KEEP_ALL"
        )

        # Add layer to map
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        m = aprx.activeMap
        lyr = m.addDataFromPath(fc)

        # ---------------------------------------------------------
        # FIXED SYMBOLOGY SECTION
        # ---------------------------------------------------------
        arcpy.AddMessage(f"Applying display option: {display_option}")
        sym = lyr.symbology

        if display_option == "Single Symbol":
            sym.updateRenderer("SimpleRenderer")
            lyr.symbology = sym

        elif display_option in ["Graduated Colors", "Graduated Symbols"]:
            numeric_fields = [f.name for f in arcpy.ListFields(fc)
                              if f.type in ("Double", "Integer", "Single", "SmallInteger")]

            if not numeric_fields:
                raise ValueError("No numeric field available for classification symbology.")

            classification_field = numeric_fields[0]
            arcpy.AddMessage(f"Using numeric field for classification: {classification_field}")

            if display_option == "Graduated Colors":
                sym.updateRenderer("GraduatedColorsRenderer")
            else:
                sym.updateRenderer("GraduatedSymbolsRenderer")

            sym.renderer.classificationField = classification_field
            lyr.symbology = sym

        arcpy.AddMessage("Display settings applied.")
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # ---- CLEANING + FIXED PLOT SECTION ----
        # ---------------------------------------------------------
        arcpy.AddMessage("Creating graph...")

        value_field = df.columns[1]

        # Clean CSV values → keep ONLY the first number before "%"
        def clean_value(v):
            if isinstance(v, str):
                match = re.search(r"(\d+\.?\d*)%", v)
                if match:
                    return float(match.group(1))
            return None

        df["clean_value"] = df[value_field].apply(clean_value)

        df_clean = df.dropna(subset=["clean_value"])

        if df_clean.empty:
            raise ValueError("No numeric values found after cleaning CSV.")

        plt.figure(figsize=(12, 5))
        plt.bar(df_clean[join_field], df_clean["clean_value"])

        plt.title(f"{value_field} (cleaned %) by {join_field}")
        plt.xlabel(join_field)
        plt.ylabel("Percent Value")
        plt.xticks(rotation=90)
        plt.tight_layout()

        plt.savefig(png_output)
        arcpy.AddMessage(f"Graph saved to: {png_output}")
        # ---------------------------------------------------------

        arcpy.AddMessage("Process complete!")
