| Offset | Field             | Size | Value  | Description |
| -------- | ------------------- | ------ | -------- | ------------- |
| 0      | bLength           | 1    | 0x09   |             |
| 1      | bDescriptorType   | 1    | 0x21   | HID         |
| 2      | bcdHID            | 2    | 0x0110 | 1.1         |
| 4      | bCountryCode      | 1    | 0x00   |             |
| 5      | bNumDescriptors   | 1    | 0x01   |             |
| 6      | bDescriptorType   | 1    | 0x22   | REPORT      |
| 7      | wDescriptorLength | 2    | 0x0041 |             |