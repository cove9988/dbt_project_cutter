-- VERSIONS  DATE          WHO                      DESCRIPTION
-- 1.00      {{ date }}    {{ creator }}             Initial release

{% test not_null_in_columns(model, column_names) %}

-- take a list of columns as column_name. e.g. [column_a, column_b]

SELECT 
1
FROM {{ model }}
WHERE 

{% for col in column_names %}
    {{col}} IS NULL
{% if not loop.last %} OR {% endif %}
{% endfor %}


{% endtest %}