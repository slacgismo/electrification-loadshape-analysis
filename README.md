# electrification-loadshape-analysis
Electrification loadshape analysis for residential and commercial sectors, part of the [Advanced Load Modeling Project](https://gismo.slac.stanford.edu/research/alm-advanced-load-modeling).

## Purpose
This work aims at identifying the impact of electrification on loadshapes for the U.S. states with the most electrification potential. Changes in peak supply and energy consumption are obtained and projected over time to estimate the impact on the loads as electrification/decarbonization adoption increases across the nation. The main fuel sources to be electrified in this study are propane, fuel oil and natural gas.

- State with most impact on the residential sector:  NY, CA, IL, OH, MI, TX, PA, and MA 
- State with most impact on the commercial sector: NY, CA, IL, OH, MI, TX, PA, and FL
  
We can divide states into three categories:
- Those with a set target year for full decarbonization/electrification and that have started adopting these policies: CA, NY, MA, IL, MI, FL
- Those with a set target year and but have yet to begin adoption: PA
- Those that have no target set and we assume will follow the market: OH, TX, and all others (excluding HI)

The target year and adoption rates for each state are inputs in this analysis and can be adjusted as the market evolves. The current assumption of our model can be found in [this JSON file](https://github.com/slacgismo/electrification-loadshape-analysis/blob/main/task2_report_national/inputs.json). If desired, these values can be adjusted.

Additionally, the electrification start year for each state, defined here as the year when residential/building building electrification code went into effect, is given as an input [the JSON file](https://github.com/slacgismo/electrification-loadshape-analysis/blob/main/task2_report_national/inputs.json) and can be adjusted by the user.

## Data
This analysis uses NREL's building stock [data](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock) for the residential and commercial sectors ([ResStock and ComStock](https://www.nrel.gov/buildings/end-use-load-profiles.html)). We use the AMY 2018 data (v.1) with no electrification upgrades in the model (baseline existing building stock) for both sectors. The ResStock data was taken from the 2022 release, and ComStock was taken from the 2023 release.

For residential buildings, we are aggregating the energy consumption for the major end-uses: space heating, hot water heating, clothes drying, and cooking (oven).

For commercial buildings, we are aggregating the energy consumption for the major end-uses: space heating, cooling, water heating, and interior equipment. Note that we do not take into account district heating and cooling (chilled hot water and steam), as the data used does not provide the breakdown of energy consumption by fuel. For more information on the ComStock sector stock model, see [the reference document](https://www.osti.gov/biblio/1967948).

## Running the analysis
In order to run these notebooks, the `sg2t` package is required. This, along with its dependencies, can be installed from [this repository](https://github.com/slacgismo/sg2t/tree/main).
