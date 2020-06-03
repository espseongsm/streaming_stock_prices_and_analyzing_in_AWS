SELECT date as Date, time as Time, hour as Hour, MAX(high_fb) as High_Facebook, MAX(high_shop) as High_Shopify, MAX(high_bynd) as High_Beyond_Meat, MAX(high_nflx) as High_Netflix, MAX(high_pins) as High_Pinterest, MAX(high_sq) as High_Sqaure, MAX(high_ttd) as High_The_Trade_Desk, MAX(high_okta) as High_Okta, MAX(high_snap) as High_Snap, MAX(high_ddog) as High_Datadog
FROM stock_price_data
GROUP BY hour, date, time
ORDER BY hour