### Energy Futures Forecasting Project
# Project Overview
This project develops an analysis and forecasting model for energy futures prices by combining energy futures prices, storage levels, and currency movements for 2021-2024. Using advanced time series analysis (ARIMA/SARIMA) alongside market context metrics, the project aims to predict price movements and identify significant market patterns.

# Goals

- Develop accurate price forecasting models for energy futures
- Integrate multiple data sources (EIA, Yahoo Finance) for comprehensive analysis
- Create visualizations for price predictions and market context
- Implement a complete data pipeline from collection to visualization

# Implementation

- Data Collection: Gathering futures prices, storage data, and currency rates from Yahoo Finance and EIA [eia.gov]
- Database Setup: Implementing PostgreSQL database and Databricks processing environment
- Data Processing: Cleaning, merging, and preparing data for analysis
- Forecasting Model: Developing ARIMA/SARIMA models with market context features
- Visualization: Creating PowerBI dashboards for presentation

# Tools

- Python (Time Series Analysis)
- PostgreSQL & Databricks (Data Pipeline)
- PowerBI (Visualization)
  

# Datasets
- 1 Jan 2021 - 1 Jan 2025
- EIA (U.S. Petroleum Balance Sheet; Weekly Natural Gas Storage Report History)
- Yahoo Finance API (Crude Oil Futures (CL=F), Natural Gas Futures (NG=F), USD Index (DXY), Major energy currency pairs (EUR/USD, CAD/USD, NOK/USD, RUB/USD))

