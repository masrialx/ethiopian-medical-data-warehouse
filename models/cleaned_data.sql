SELECT 
    id, 
    LOWER(text) AS text, 
    CAST(date AS DATE) AS cleaned_date 
FROM cleaned_data;
