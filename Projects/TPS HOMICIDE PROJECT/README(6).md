About Dataset
Kaggle Dataset: Logistics Operations Database (2022-2024)
About this Dataset
What's Inside

A complete operational database from a fictional Class 8 trucking company spanning three years. This isn't scraped web data or simplified tutorial content—it's a realistic simulation built from 12 years of real-world logistics experience, designed specifically for analysts transitioning into supply chain and transportation domains.

The dataset contains 85,000+ records across 14 interconnected tables covering everything from driver assignments and fuel purchases to maintenance schedules and delivery performance. Each table maintains proper foreign key relationships, making this ideal for practicing complex SQL queries, building data pipelines, or developing operational dashboards.
Who This Is For

SQL Learners: Master window functions, CTEs, and multi-table JOINs using realistic business scenarios rather than contrived examples.

Data Analysts: Build portfolio projects that demonstrate understanding of operational metrics: cost-per-mile analysis, fleet utilization optimization, driver performance scorecards.

Aspiring Supply Chain Analysts: Work with authentic logistics data patterns—seasonal freight volumes, equipment utilization rates, route profitability calculations—without NDA restrictions.

Data Science Students: Develop predictive models for maintenance scheduling, driver retention, or route optimization using time-series data with actual business context.

Career Changers: If you're moving from operations into analytics (like the dataset creator), this provides a bridge—your domain knowledge becomes a competitive advantage rather than a gap to explain.
Why This Dataset Exists

Most logistics datasets are either proprietary (unavailable) or overly simplified (unrealistic). This fills the gap: operational complexity without confidentiality concerns. The data reflects real industry patterns:

    Fuel prices track the 2022 diesel spike and 2023-2024 decline
    Driver turnover sits at 15% annually (industry standard)
    Equipment utilization averages 65% (typical for dry van operations)
    On-time delivery performance ranges 85-95% (realistic service levels)
    Maintenance intervals follow Class 8 PM schedules

Dataset Structure

Core Entities (Reference Tables):

    Drivers (150 records) - Demographics, employment history, CDL info
    Trucks (120 records) - Fleet specs, acquisition dates, status
    Trailers (180 records) - Equipment types, current assignments
    Customers (200 records) - Shipper accounts, contract terms, revenue potential
    Facilities (50 records) - Terminals and warehouses with geocoordinates
    Routes (60+ records) - City pairs with distances and rate structures

Operational Transactions:

    Loads (57,000+ records) - Shipment details, revenue, booking type
    Trips (57,000+ records) - Driver-truck assignments, actual performance
    Fuel Purchases (131,000+ records) - Transaction-level data with pricing
    Maintenance Records (6,500+ records) - Service history, costs, downtime
    Delivery Events (114,000+ records) - Pickup/delivery timestamps, detention
    Safety Incidents (114 records) - Accidents, violations, claims

Aggregated Analytics:

    Driver Monthly Metrics (5,400+ records) - Performance summaries
    Truck Utilization Metrics (3,800+ records) - Equipment efficiency

Key Features

Temporal Coverage: January 2022 through December 2024 (3 years)

Geographic Scope: National operations across 25+ major US cities

Realistic Patterns:

    Seasonal freight fluctuations (Q4 peaks)
    Historical fuel price accuracy
    Equipment lifecycle modeling
    Driver retention dynamics
    Service level variations

Data Quality:

    Complete foreign key integrity
    No orphaned records
    Intentional 2% null rate in driver/truck assignments (reflects reality)
    All timestamps properly sequenced
    Financial calculations verified

Use Case Examples

Business Intelligence:
Create executive dashboards showing revenue per truck, cost per mile, driver efficiency rankings, maintenance spend by equipment age, customer concentration risk.

Predictive Analytics:
Build models forecasting equipment failures based on maintenance history, predict driver turnover using performance metrics, estimate route profitability for new lanes.

Operations Optimization:
Analyze route efficiency, identify underutilized assets, optimize maintenance scheduling, calculate ideal fleet size, evaluate driver-to-truck ratios.

SQL Mastery:
Practice window functions for running totals and rankings, write complex JOINs across 6+ tables, implement CTEs for hierarchical queries, perform cohort analysis on driver retention.
Sample Questions to Explore

    Which routes generate the highest profit margin after fuel costs?
    How does driver tenure correlate with fuel efficiency and on-time performance?
    What's the optimal preventive maintenance interval to minimize total cost of ownership?
    Which customers have the highest revenue-per-load and best payment terms?
    How do seasonal patterns affect equipment utilization and revenue?
    What safety incident patterns exist by driver experience level?
    Which city pairs have the most reliable on-time delivery performance?
    How does truck age impact maintenance costs and downtime?

Data Format

All tables provided as CSV files with headers. Relationships documented in included schema file. Compatible with:

    PostgreSQL, MySQL, SQL Server
    Python (pandas, SQLAlchemy)
    R (tidyverse, DBI)
    Tableau, Power BI, Looker
    Jupyter notebooks, R Markdown

Column Descriptions

See individual table documentation for complete field definitions. Key identifier patterns:

    driver_id format: DRV00001 through DRV00150
    truck_id format: TRK00001 through TRK00120
    load_id format: LOAD00000001 through LOAD00057000+
    All date fields: ISO format (YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)
    Currency: USD (dollars and cents)
    Distance: Miles
    Fuel: Gallons

Known Limitations

Not Included:

    Hours of Service (HOS) compliance tracking
    Weather impact modeling
    Customer payment histories
    Insurance claim details
    Detailed cargo manifests
    Electronic Logging Device (ELD) data

Simplified:

    Safety incidents reduced to basic claims data
    Maintenance descriptions generalized
    Customer contracts simplified to term length
    Route planning without traffic/construction


