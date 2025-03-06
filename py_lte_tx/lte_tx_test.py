# this is a template file for LTE TX test
# with R&S CMW100

import visa
import time
import pyvisa

# CMW100 IP address
cmw100_ip = 'TCPIP0::192.168.1.1'  # Replace with your CMW100's IP

class CMW100:
    def __init__(self, ip_address):
        self.instrument = None
        try:
            rm = visa.ResourceManager()
            self.instrument = rm.open_resource(ip_address)  # Replace with your instrument's IP
            self.instrument.timeout = 10000  # Replace with your instrument's timeout
            self.instrument.connection_status = 'connected'
        except visa.VisaIOError as e:
            print(f"Error connecting to instrument: {e}")

    def query_system_status(self):
        if self.instrument:
            status = self.instrument.query("*IDN?")
            print(f"System Status: {status}")
        else:
            print("Instrument not initialized.")

    def close(self):
        if self.instrument:
            self.instrument.close()
            print("Instrument closed.")
        else:
            print("No instrument to close.")

    def perform_lte_tx_test(self):
        if self.instrument:
            # Configure LTE TX test
            print("Configuring LTE TX test...")
            self.instrument.write("*OPC:OPERATE?")
            self.instrument.write("*OPC:TX?")
            test_result = self.instrument.query('*OPC:RES?')
            print(f"Test Result: {test_result}")
        else:
            print("Instrument not available.")
    
    def config_lte_network(self, band, channel, bandwidth):
        if self.instrument:
            print("Config LTE Network...")
            self.instrument.write("*LTE:BAND={}".format(band))
            self.instrument.write("*LTE:CHAN={}".format(channel))
            self.instrument.write("*LTE:BW={}".format(bandwidth))
            print("LTE Network Configured")
        else:
            print("Instrument not available.")
    
    def config_lte_tx(self, modulation, power):
        if self.instrument:
            print("Config LTE TX...")
            self.instrument.write("*LTE:MOD={}".format(modulation))
            self.instrument.write("*LTE:POWER={}".format(power))
            print("LTE TX Configured")
        else:
            print("Instrument not available.")

    def start_test(self):
        if self.instrument:
            print("Start test...")
            self.instrument.write("*OPC:START?")
            print("Test Started")
        else:
            print("Instrument not available.")

    def stop_test(self):
        if self.instrument:
            print("Stop test...")
            self.instrument.write("*OPC:STOP?")
            print("Test Stopped")
        else:
            print("Instrument not available.")

    def get_test_result(self):
        if self.instrument:
            print("Getting test result...")
            test_result = self.instrument.query('*OPC:RES?')
            print(f"Test Result: {test_result}")
        else:
            print("Instrument not available.")
