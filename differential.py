import json
import requests
import time
import Adafruit_ADS1x15


def main():
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 16

    tear = get_samples()
    raw_input('Add 10g weight')
    grams_ten = get_samples()
    print('Remove 10g weight')
    raw_input('Add 20g weight')
    # ...

    with open(samples.json, 'wt') as sample_file:
        json.dump(data, sample_file)

    # TODO: some algo that uses the 
    # TODO: breakout reporting and loop

    while True:
        
        time.sleep('5')
        weight = get_samples()
        response = requests.post(
            'http://adamyala.com/meat_pi',
            {
                'weight': weight,
            }
        )
    # initialize all sensors
    # take sample of zero weighted
    # store in local file
    # start loop
    #     take samples and average
    #     make http request

def get_samples(iterations=10):
    samples = []
    for _ in range(iterations):
        time.sleep(0.5)
        value = adc.read_adc_difference(0, gain=GAIN)
        samples.append(value)
    return sum(samples) / len(samples)

print(get_samples(10))
