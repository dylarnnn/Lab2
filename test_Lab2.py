import Lab2

def test_find_min_max():
    temperatureData = [ 1, 2, 3, 6, 4, 2, 1]
    max_temp, min_temp = Lab2.find_min_max(temperatureData)
    assert (min_temp == 1 and max_temp == 6) #must follow the order of how the function return values

    
def test_calc_average():
    temperatureData = [1, 2, 3]
    result = Lab2.calc_average(temperatureData)
    assert (result == 2)

def test_calc_median_temperature():
    temperatureData = [ 1, 3, 1, 1, 3, 2, 4, 5] ## itd be sorted out through sorted first
    sortedData = Lab2.sort_temperature(temperatureData)
    result = Lab2.calc_median_temperature(sortedData)
    assert (result == 2.5)
    