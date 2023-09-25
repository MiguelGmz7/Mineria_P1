def fit(x_train, y_train):
    frequency_table = compute_frequency_table(x_train, y_train)
    rules, error_rates = compute_rules(frequency_table)
    attribute_min_error = find_attribute_with_min_error_rate(error_rates)
    rule = {attribute_min_error: rules[attribute_min_error]}
    return rule