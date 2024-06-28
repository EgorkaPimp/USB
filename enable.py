import usb.core
import usb.util

# Найти устройство по vendor и product ID
device = usb.core.find(idVendor=0x1234, idProduct=0x5678)

if device is None:
    raise ValueError("Device not found")

# Установить активную конфигурацию
device.set_configuration()

# Найти конечные точки
cfg = device.get_active_configuration()
intf = cfg[(0, 0)]

ep_out = usb.util.find_descriptor(
    intf,
    # Сопоставление для поиска нашего конечного выхода.
    custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT
)

ep_in = usb.util.find_descriptor(
    intf,
    # Сопоставление для поиска нашего конечного входа.
    custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
)

assert ep_out is not None
assert ep_in is not None