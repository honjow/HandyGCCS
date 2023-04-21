#!/sbin/python3
import smbus2

# Define I2C bus number and search range for device addresses
BUS = 1
DEVICE_ADDRESSES = range(128)

# Search for connected I2C devices
for addr in DEVICE_ADDRESSES:
    try:
        bus = smbus2.SMBus(BUS)
        bus.read_byte(addr)
        print(f"Device found at address 0x{addr:02x}")
        from BMI160_i2c import Driver
        try:
            gyro_device = Driver(addr=addr, bus=BUS)
            while True:
                print(gyro_device.getRotationX())
        except ModuleNotFoundError as err:
            print(f"{err} | Gyro device not initialized. Skipping gyro device setup.")
            gyro_device = False
        except (BrokenPipeError, FileNotFoundError, NameError, OSError) as err:
            print(f"{err} | Gyro device not initialized. Ensure bmi160_i2c and i2c_dev modules are loaded. Skipping gyro device setup.")
            gyro_device = False
        except Exception as err:
            print(f"{err} | Gyro device not initialized. Skipping gyro device setup.")
            gyro_device = False
    except OSError:
        pass 