# electrification-loadshape-analysis
Electrification loadshape analysis for residential and commercial sectors, part of the [Advanced Load Modeling Project](https://gismo.slac.stanford.edu/research/alm-advanced-load-modeling).

## Purpose
This work aims at identifying the impact of electrification on loadshapes for the U.S. states with the most electrification potential. Changes in peak supply and energy consumption are obtained and projected over time to estimate the impact on the loads as electrification/decarbonization adoption increases across the nation.

- State with most impact on the residential sector:  NY, CA, IL, OH, MI, TX, PA, and MA 
- State with most impact on the commercial sector: NY, CA, IL, OH, MI, TX, PA, and FL
  
We can divide states into three categories:
- Those with a set target year for full decarbonization/electrification and that have started adopting these policies: CA, NY, MA, IL, MI, FL
- Those with a set target year and but have yet to begin adoption: PA
- Those that have no target set and we assume will follow the market: OH, TX

The target year and adoption rates for each state are inputs in this analysis and can be adjusted as the market evolves. 

## Data
This analysis uses NREL's building stock [data](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock) for the residential and commercial sectors ([ResStock and ComStock](https://www.nrel.gov/buildings/end-use-load-profiles.html)). We use the AMY 2018 data (v.1) with no electrification upgrades in the model (baseline existing building stock). The ResStock data was taken from the 2022 release, and ComStock was taken from the 2023 release.

## Running the analysis
In order to run these notebooks, the `sg2t` package is required. This, along with its dependencies, can be installed from [this repository](https://github.com/slacgismo/sg2t/tree/main).
