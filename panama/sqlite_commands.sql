.mode csv
CREATE TABLE panama(company_url TEXT,company_name TEXT,officer_position_es TEXT,officer_position_en TEXT,officer_name TEXT,inc_date TEXT,dissolved_date TEXT,updated_date TEXT, company_type TEXT,mf_link TEXT);
.import sunday_times_panama_data.csv panama
