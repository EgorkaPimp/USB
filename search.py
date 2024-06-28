import usb.core
import usb.util

try:
    devices = usb.core.find(find_all=True)
    if devices is None:
        print("No USB devices found")
    else:
        for device in devices:
            print(f"Device: {device}")
            print(f"  idVendor: {device.idVendor:#06x}")
            print(f"  idProduct: {device.idProduct:#06x}")
            try:
                manufacturer = usb.util.get_string(device, device.iManufacturer)
                product = usb.util.get_string(device, device.iProduct)
                serial_number = usb.util.get_string(device, device.iSerialNumber)
                print(f"  Manufacturer: {manufacturer}")
                print(f"  Product: {product}")
                print(f"  Serial Number: {serial_number}")
            except usb.core.USBError as e:
                print(f"  Could not retrieve additional info: {e}")
except usb.core.USBError as e:
    print(f"USBError: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")