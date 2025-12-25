# Week 2 Summary — ETL + EDA

## Key findings
- Revenue By Country: The amount of our SA is more than AE.
- Revenue Trend: Revenue go up in the start and end of work days, and drop down in the middle and the end of weeks.
- Order Amount: The majority of orders are for small amounts, while high-value orders are very rare.

## Definitions
- Revenue = Total money from orders (sum of amount).
- Winsorized = We limited very high numbers to make charts clear.
- Filters = We looked at all orders (paid and refund).

## Data quality caveats
- Missingness: Some orders have missing dates.
- Consistency: We fixed text issues like "paid" and "PAID".
- Join coverage: A few users did not have a country.
- Outliers: We handled high values to avoid skewing the charts.

## Next questions
- Why is the revenue low on Weekend?
- How can we increase the high-value orders?