import sys
import time
from lte_tx_test import CMW100

def main():
    # Configuration
    # You should update these values according to your test requirements
    CMW_IP = 'TCPIP0::192.168.1.1::INSTR'
    LTE_BAND = 1
    LTE_CHANNEL = 18300
    LTE_BW = '10MHz'
    LTE_MODULATION = 'QPSK'
    LTE_POWER = -10.0 # dBm

    print("=== Starting LTE TX Test Sequence ===")

    # Initialize instrument
    cmw = CMW100(ip_address=CMW_IP)

    # Connect
    if not cmw.connect():
        print("Failed to connect to instrument. Exiting.")
        sys.exit(1)

    try:
        # Check system status
        cmw.query_system_status()

        # Configure Network
        cmw.config_lte_network(LTE_BAND, LTE_CHANNEL, LTE_BW)

        # Configure TX parameters
        cmw.config_lte_tx(LTE_MODULATION, LTE_POWER)

        # Start Test
        cmw.start_test()

        # Wait for test to complete (simulated delay)
        time.sleep(2)

        # Get Results
        result = cmw.get_test_result()
        print(f"Final Result: {result}")

        # Stop Test
        cmw.stop_test()

    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
        cmw.stop_test()

    finally:
        # Close connection
        cmw.close()
        print("=== Test Sequence Completed ===")

if __name__ == "__main__":
    main()
