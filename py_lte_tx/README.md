# LTE TX Test with R&S CMW100

This directory contains a Python script for performing LTE TX tests with the Rohde & Schwarz CMW100 instrument.

## File Description

`lte_tx_test.py` contains the necessary functions to configure the CMW100 for LTE TX tests, start and stop the test, and retrieve the results.

## Usage

1.  **Connect to the CMW100:**
    -   Ensure that the CMW100 is powered on and connected to your network.
    -   Modify `cmw100_ip` to the correct IP address of your CMW100.
    -   run `query_system_status()` to check if the device is connected
2.  **Configure LTE Network:**
    -   Use `config_lte_network(band, channel, bandwidth)` to set the desired LTE band, channel, and bandwidth.
3.  **Configure LTE TX:**
    -   Use `config_lte_tx(modulation, power)` to configure the desired modulation and power level.
4.  **Start the Test:**
    -   Use `start_test()` to begin the LTE TX test.
5.  **Stop the Test:**
    -   Use `stop_test()` to end the LTE TX test.
6. **Get the result**
    - use `get_test_result()` to get test result
7. **Close the connection**
    - use `close()` to close the connection

## Example
