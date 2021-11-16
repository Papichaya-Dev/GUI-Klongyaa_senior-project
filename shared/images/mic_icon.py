from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x18\x39\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x8c\x00\x00\x00\x7c\x08\x06\x00\x00\x00\xbb\x52\x58\x27\
\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0b\x13\x00\x00\x0b\x13\
\x01\x00\x9a\x9c\x18\x00\x00\x00\x01\x73\x52\x47\x42\x00\xae\xce\
\x1c\xe9\x00\x00\x00\x04\x67\x41\x4d\x41\x00\x00\xb1\x8f\x0b\xfc\
\x61\x05\x00\x00\x17\xce\x49\x44\x41\x54\x78\x01\xed\x5d\x79\x70\
\x14\xd7\x99\xff\xba\x67\x46\x48\xe8\x40\x98\xfb\x96\x38\x64\x2e\
\x83\x04\x98\xf8\xe0\x10\x59\x03\x26\x8e\x0f\xca\xde\xda\xf5\xc6\
\xc5\xf1\x4f\xb2\x95\x10\x03\x89\x71\x52\x5b\x8e\x0d\xb5\x76\xec\
\x35\xde\x20\x36\xe5\xd4\x7a\xd7\x59\x60\x5d\xde\x24\x5b\x45\x20\
\x4e\x88\xc3\x61\x23\x08\x38\xd8\x18\x23\x88\xc5\x25\x0e\x71\x19\
\x99\x53\x80\x40\xc7\xcc\xf4\xcb\xfb\x7a\xa6\x47\xdd\x3d\x7d\xbc\
\xee\x7e\xdd\x33\xc2\xfa\x15\x42\xea\x39\xde\xd7\xdf\xeb\xdf\xfb\
\xde\xef\x7b\x47\xb7\x00\x5f\x01\x6c\xd8\xbf\xa4\x38\xb7\x18\x8a\
\xc5\xb6\x9c\x72\x51\x94\x4a\x00\xc4\x21\x82\x40\x8a\x09\x01\xfa\
\x37\x14\x0b\x44\x28\xc6\xcf\x11\x81\x94\x18\x7d\x9f\xbe\x5f\x9f\
\x7c\xbf\x91\xfe\xa2\x3f\x02\xfe\xa6\xaf\x49\xa7\x25\x49\xac\x8f\
\x09\xa4\xfe\x91\xb2\x95\x35\xf0\x15\x80\x00\x77\x18\x64\x72\x14\
\x84\xcb\xc3\x00\xe5\x82\x20\x8c\x07\x49\xa8\x34\x23\x82\x0f\xa0\
\xa4\x41\x72\x49\x3b\x62\xf4\xef\x96\xa6\x58\xcd\xdc\x8a\xaa\x46\
\xb8\x83\xd0\xe1\x09\xd3\x4e\x10\xf1\x71\x1a\x03\x2a\xe9\x4b\xe5\
\x90\x5d\x40\x12\x55\x4b\x12\xec\xb8\x7d\xbb\xad\xba\xa3\x13\xa8\
\x43\x12\x06\x49\x52\x50\x10\x5e\x40\x4f\xff\x71\xda\xb5\x94\x93\
\x64\x97\xd2\x41\x50\x4d\xbb\xc2\x75\xf1\x78\xb4\x7a\xce\xa8\xaa\
\x7a\xe8\x60\xe8\x30\x84\x51\x93\x84\x1e\x56\xc2\x9d\x81\x0e\x47\
\x9e\xac\x27\xcc\xfb\x75\xcf\x55\x46\x04\x61\x31\x76\x37\x1d\x2c\
\x92\x38\x82\x20\xc0\xda\x28\x21\xeb\xe6\x8c\x78\xa3\x1a\xb2\x18\
\x59\x49\x18\x8c\x26\xf9\xf9\x91\x27\x68\x25\xce\x87\x3b\x27\x9a\
\x30\x81\xfa\x5c\x4f\xf5\xce\x8a\x59\x65\x2b\xd7\x42\x16\x22\xab\
\x08\x93\xe8\x76\x72\x16\x0b\x82\xb4\xe4\x4e\x8e\x26\x2c\xc8\x56\
\xe2\x64\x05\x61\x3a\x89\x62\x8e\x6c\x23\x4e\xc6\x09\xb3\xe5\xd8\
\xb2\x05\xa2\x08\x2f\x25\x07\xd1\x3a\x61\x82\x6c\x21\x4e\xc6\x08\
\x83\x62\x36\x0c\xc2\x4b\xf0\x15\xd3\x28\x5e\x81\xc4\x89\x46\xa3\
\x33\x32\x95\x55\x05\x4e\x98\x64\xf7\x43\x89\x42\x96\x40\x27\x3c\
\x40\xa8\x0a\x37\xb5\xad\x98\x11\xf0\x40\x60\xa0\x84\x49\xa6\xc8\
\x6b\x3a\xbb\x1f\x3e\x90\xa3\x0d\x21\x0b\x83\x4c\xc5\x03\x21\x4c\
\x67\x54\xf1\x1b\x42\xd5\xcc\x11\xaf\x2f\x85\x00\xe0\x3b\x61\xde\
\x3f\xbc\xa4\x24\x12\x89\x6c\xef\x8c\x2a\xfe\x22\x28\x6d\x23\x82\
\x8f\xd8\x76\xfc\xf9\xf9\x91\x48\x78\x7f\x27\x59\xfc\x07\xd6\x71\
\x38\x1c\xd9\x8f\x59\x27\xf8\x08\xdf\x08\xf3\x41\xdd\xf3\x34\x55\
\x26\x6b\x3b\xc7\x55\x02\x45\x31\x8d\x34\x6b\xb6\xd2\xba\x07\x9f\
\xc0\xbd\x4b\x42\xbd\x52\x58\x18\x59\x23\x11\x78\x82\xd0\xff\x44\
\x31\x61\x82\xe0\x8f\xfa\x98\x36\x09\x7c\x51\x50\x8e\x25\x22\x9f\
\x8d\x20\x58\x1d\x0b\xf8\x2f\xbd\x2c\xbb\x63\xb4\x05\x76\x65\x27\
\xce\xff\xea\xc5\x66\x68\x38\x7b\x03\x6e\x5e\x6d\x81\x38\x7d\x3d\
\x2f\x3f\x02\x77\xf5\xee\x0a\xfd\x4b\x8a\x20\xa7\x4b\x98\x9b\x2d\
\xcd\x31\xfd\xae\x00\xbc\xfd\x12\x36\xd2\x2c\x6a\x21\xef\x2c\x8a\
\x2b\x61\x50\xaf\xd0\xb0\xb8\x81\x9e\x76\x39\x89\x53\xc7\x42\x66\
\x8e\x26\x9c\x15\x55\x64\xc1\xcf\x68\x8f\x05\x7a\x9c\x28\x57\xa2\
\x65\x21\xb1\x52\x64\xd1\x97\xed\xc1\x56\x2c\x26\xc1\x81\xdd\xe7\
\xa1\x86\xfe\x7c\xfe\x71\x03\x34\xdf\x8a\x1a\xfa\x86\xf6\x07\x0f\
\x2f\x86\x31\x93\xfb\xc2\xfd\xb3\x4a\xa0\x57\xff\x02\x1f\xfc\x92\
\xa8\x1f\x22\x9b\x5f\x86\x65\x6b\x8f\x69\xc1\x35\x74\x26\x7c\x2e\
\x4f\x5d\xc3\x8d\x30\x8a\xb8\xa5\xe7\x59\x62\x79\x41\xe9\x0b\x12\
\xfd\x50\x28\xc4\xe6\xb8\x63\xb2\xe8\x6c\x59\x5d\xc0\x4f\xb7\x9f\
\x85\x3f\xbc\x53\x0b\x0d\x67\x6e\x82\x13\xe4\xe4\x86\xe1\xbe\x99\
\x83\x61\xf6\xd3\xa3\xa0\x07\x8d\x3e\x2c\xb6\x82\xf4\x4b\x7d\xcc\
\x5b\x0c\x73\x21\x8c\x3a\x13\x42\x47\x52\x21\x12\x9c\xb7\x0a\xa5\
\x05\x2a\xdf\x15\x04\x97\x91\xc5\xc2\xd6\xe5\x86\x5b\xb0\xe6\xb5\
\x4f\xe0\xc4\xe7\x97\xc1\x0b\xba\x74\x0d\xc3\x53\xdf\x19\x07\x0f\
\xce\x19\x2a\x1f\x3b\xf1\x4b\xd3\xcd\x70\xf2\x4b\x6f\x4b\x01\x4f\
\xd2\x78\x26\x8c\x59\xda\x9c\xe6\xb8\x94\xec\x6f\xfd\x22\x0b\xa3\
\xad\x93\x87\xae\xc0\xdb\x2f\xef\xa1\x5a\xe5\x36\xf0\xc2\xf4\xc7\
\x87\xc1\x93\xdf\x1e\x4f\x35\x4e\xc8\x77\xbf\x9c\x34\x38\x50\x35\
\x5e\x5e\xa4\xf1\x44\x18\x66\xb2\x18\x08\x5c\x86\xfe\xd7\x65\xb8\
\x36\xb7\x75\x9c\x46\x94\xff\xf8\xd1\x9f\xa1\xad\x35\x06\xbc\x71\
\xef\xd7\x07\xc1\xfc\xe7\xee\x05\x31\x2c\x06\xee\x97\x9d\x2d\x05\
\x3c\x48\xe3\x3a\xad\xc6\x6c\x88\x8d\x2c\x89\x1f\x56\x47\x25\x8f\
\x95\x6a\x66\xeb\x0a\xed\x86\xde\xfc\x97\x5d\xbe\x90\x05\xb1\xf7\
\xc3\xb3\xf0\x7f\xab\x3f\x0b\xdc\x2f\x3b\x5b\x6a\xe0\xb5\xc2\x6b\
\xb6\x9d\x5e\x3b\x70\x09\xd7\x84\x29\x28\xa0\xd9\x90\xd1\x80\x1c\
\x66\x89\x2e\xc4\x19\x42\x16\x82\x82\x17\x21\x68\x5c\x76\x2c\x2a\
\xc1\xea\x1f\xed\x84\xe6\xdb\x51\xf0\x13\x1f\x6d\xae\x87\xea\xdf\
\x1d\x0f\xcc\x2f\xa3\x63\xb5\x2d\x23\xe0\x35\x8b\xd1\x6b\x07\x2e\
\xe1\x8a\x30\x1f\x24\x06\x86\x2a\x8d\xde\x53\x4e\x34\xd1\x2a\x58\
\x52\xcc\xf6\x56\x81\x95\x64\x5e\xa9\x52\xba\x10\xd4\xb4\x40\x73\
\x5b\x7f\xf8\xdf\x5a\xb8\x78\xbe\x09\x82\xc0\xef\xd7\xd5\xc2\x8d\
\x6b\xad\x0e\xfc\x22\xae\xfd\x4a\xab\xc3\xb8\xce\x56\x72\x9c\xc6\
\x00\x95\x74\x70\x6f\x15\xb8\x80\x63\xc2\x6c\x3b\xb1\x6c\xb1\x04\
\x64\xb9\xd5\x67\x64\x47\x6c\x5b\x45\xbb\x38\x93\x24\x5d\x66\x65\
\x58\xa9\xba\xf1\x09\x75\x59\x16\xb6\x90\x28\x7f\xde\x74\x0a\x82\
\xc2\xad\x1b\x6d\xf0\xe1\x86\x3a\x07\x7e\xe9\xc8\xc2\xe8\x97\x61\
\x1d\xea\x32\x2f\x41\xb0\x92\xa8\x64\xc9\x9f\x8e\x3c\xef\x78\x32\
\xd8\x11\x61\x50\xe4\x12\x09\xaa\xac\x3e\xa3\xb0\xda\x3e\x84\x26\
\xbf\xe0\x25\x6b\x60\xb0\x55\xbd\xf1\x38\xbd\x88\xad\x10\x24\x3e\
\xfc\x6d\x1d\xdc\xb8\xda\xec\xdc\x2f\x91\xdd\x2f\x4d\x36\x64\x51\
\x87\x56\x08\x85\xc8\x4b\x74\xee\xc9\xd1\xc6\x3f\x66\xc2\x28\x22\
\xd7\xfe\x93\x82\x23\x25\x8f\x8e\xfb\x25\x04\x5b\x5b\xe3\x70\x70\
\xcf\x17\x10\x34\xa2\x6d\x71\x2a\x82\xcf\xf8\x2c\x70\x93\xc6\x2c\
\xea\x90\x01\xc5\xb4\x9c\x0d\x4e\x44\x30\x33\x61\xe8\xfc\xd0\x2a\
\x96\x59\xe7\x94\x86\x61\x10\x67\xf8\xe1\xd4\xf8\x84\x0f\x42\xb0\
\xfe\xf0\x15\xb8\x7c\xe1\x16\x64\x02\x47\x3e\xbb\xe8\x42\xb3\x00\
\x63\x37\x64\x56\x87\x3a\x9d\x67\xae\x61\x52\x48\x88\x60\x5c\xab\
\xc4\x06\x26\xc2\xe0\x94\x39\x2d\x78\x01\x30\x82\x25\xb2\x78\x19\
\x16\x97\x18\x47\x3e\xeb\x8f\x5e\x85\x4c\xe1\xf0\x67\x5f\x42\x8c\
\x46\x38\xf6\x6e\x08\x18\x33\xca\x44\xf9\xc6\x53\x0b\x5a\x9d\x67\
\xad\x61\xd4\x20\x4b\x70\x35\x24\xcb\x27\x6d\x09\x83\xba\x05\x57\
\xf5\x03\x23\xe4\x90\x0a\xc6\xad\x42\x11\x67\x8e\xc6\x23\x24\xdd\
\x48\x27\xb1\x9b\x87\x6a\xb7\xd5\x70\xd6\xd9\x1c\x11\x4f\xc4\x63\
\x04\x6e\x34\xb6\x24\xce\x0b\xd8\xfc\x62\x89\x2c\x4a\x1d\xb2\x66\
\x5e\xac\xc0\xa5\xb3\x2c\x5d\x93\x2d\x61\xa8\x6e\x71\xb4\x05\x44\
\x10\x04\xc3\x56\x61\x27\xce\xfc\x10\x82\xd7\x2e\x35\x43\x26\xd1\
\x78\xb9\xd9\xde\x2f\x87\xc3\xfd\xc4\x41\xe6\xe5\x04\xac\x5d\x93\
\x25\x61\xe4\xac\xc8\x41\x57\xa4\x39\x01\x9d\xe3\xe0\xb3\xc0\x35\
\x12\x82\x2d\x3e\x0f\xd4\xd9\xa1\xe5\x76\xcc\x73\x96\xe7\x29\xa3\
\x64\xd0\x30\x5a\xd8\x77\x4d\x96\x84\x09\x87\x23\x6b\xc0\x05\xec\
\xc5\x59\x40\x42\x50\x72\x5a\x61\x7c\x11\x8f\x49\x36\xdd\x10\xcb\
\x64\xac\xd6\x2f\xed\xda\x19\xeb\x3a\x64\xd7\x30\xed\x48\xee\x15\
\x33\x85\x29\x61\x92\x6b\x43\x2b\xc1\x21\xda\x35\x4c\xe2\xd8\xd5\
\xba\x0f\x4e\x42\x30\xd3\x48\x5b\xc2\xa0\xf6\x0b\xc0\xb5\x5f\x86\
\x03\x99\x26\x75\xe8\x02\x95\x56\x51\xc6\x94\x30\x4e\x84\xae\x1a\
\x8a\x86\x51\xc4\x99\xe3\x95\x72\x1c\x85\x60\x36\x20\x48\x81\x2b\
\x13\x51\xd2\xbe\xef\x06\x56\x51\xc6\x90\x30\xc9\x34\xba\x04\x5c\
\x42\x1d\x12\x5d\x45\x16\x8e\x42\x30\x93\x90\xa3\x6d\x40\x02\x57\
\xd1\x2c\x9a\xe5\x0d\xc4\x2d\x65\xcc\xa3\x8c\x21\x61\xdc\x46\x97\
\x14\xdc\x90\xc5\x07\x21\x98\x69\xc8\xe7\x19\x94\xc0\x35\xc8\x28\
\xdd\x68\x18\x05\x66\x51\x26\x8d\x30\x5b\x29\xb3\x3c\x45\x17\x42\
\x32\xb2\xee\xc3\xa8\xec\x4c\x43\x14\xfc\xf1\xcb\x49\x1d\x7a\x80\
\x61\x94\x49\x23\x0c\x65\xe5\x7c\xf0\x80\x4c\xac\xfb\x30\x2b\x3b\
\x1b\xe0\x26\xcb\x73\xbc\x8e\xd9\xac\x0e\xc1\x1b\x8c\xa2\x8c\x86\
\x30\x5e\xc6\x5d\xd4\x70\xee\x28\xbb\x10\x44\xf8\x31\xd2\xe9\x07\
\xd8\xfd\x4a\x7c\x3e\x6d\x3d\x8b\x5d\x24\x91\xb4\xdd\x10\x47\x0d\
\xa3\xa0\x52\x3f\xfa\xab\x21\x4c\x28\x14\xa9\x04\x8f\x70\x25\x70\
\x99\x5a\x20\xb4\x67\x5e\x3e\x8c\x74\xfa\x05\x2f\xeb\x59\xac\x05\
\x2e\xd8\xd6\xa1\x17\x0d\xa3\xa0\xad\x6b\x58\xb3\x66\x46\xd4\x3a\
\xe7\x51\xec\x22\x48\x66\x04\xae\xe1\x31\x64\x16\xea\x1d\x89\x2c\
\xd9\x90\xdb\x8c\x12\xc0\xbc\x0e\xbd\x82\x96\x33\x5d\x7d\x1c\x56\
\xfe\xd8\x72\x6c\x49\xb9\x17\xb1\xab\x80\x39\x0d\x24\xc4\x91\x66\
\x49\x55\xb2\x83\x4a\x1d\x59\xd1\x07\x7a\xf5\xcd\x4f\x44\x66\xa1\
\x7d\x8b\x04\xcb\x71\x6a\x99\x86\xe2\x17\x30\x1e\xab\xca\x2a\xec\
\x9e\xeb\x4f\x36\xa4\x6b\x70\xa6\x62\x1a\xb8\x6c\x3c\x93\xc5\xaf\
\x72\x0f\x9a\x14\x61\x04\x21\x5c\x09\x9c\xe0\x58\x9c\x31\xf4\xed\
\x58\x29\xcc\x64\x49\xda\x7a\xf2\xdb\xe3\x18\x47\x8b\x83\xd9\x96\
\x6b\x6f\x8b\x61\xab\x6c\x88\xbd\x81\xc9\x05\x73\x60\x8c\x28\xc9\
\x23\xfe\xd5\xf2\xdf\xed\xaf\x82\xa7\xec\x48\x81\x6d\x08\x25\xac\
\xeb\x59\x12\xe5\x65\x72\x6a\x21\x78\x5b\x22\xbb\x2d\xb0\x8f\xce\
\x1c\x24\x8c\x0c\x75\xb7\x24\x17\x99\xdc\x44\x7f\x0a\x38\xa0\x23\
\x6c\x95\x35\xb3\x25\x3a\x11\x9d\x1d\xc0\x16\x4f\x84\x9b\xa2\xdd\
\xf1\x4e\x10\x72\xb1\x91\x48\x88\xdb\x13\x40\xd2\x34\x0c\xa3\x38\
\x0b\x52\x08\x7a\x1e\x82\x8f\x7b\x6f\x04\x81\xd8\xf2\x9e\x56\xa7\
\x10\xcd\x17\x9f\xc0\xdf\xb2\x86\x91\x68\x1f\xc5\x2b\x7c\x21\x1c\
\x8b\x33\x87\x42\xf0\xf2\x85\x26\x38\xb6\xff\x22\x08\xf4\xb5\x71\
\xf7\xf5\x87\xae\x05\x39\x86\xb6\x8e\xd6\x5c\x94\xb7\x7d\x24\x46\
\x3e\x93\xe7\x46\x12\x85\x98\x1e\x4b\xc9\x50\x2e\x18\x1f\xd3\xba\
\xd2\xb4\x5e\xa2\x4a\x87\x21\xa9\xcd\x94\xb2\x86\x8e\xee\x01\x45\
\x54\xf8\xea\xfd\x42\x6f\x8f\xec\xbb\x28\xdf\x35\xa2\xdf\x90\x42\
\x18\x39\xa1\x0f\xb3\xc0\x75\x92\x51\x02\xcf\x8b\x0a\x89\xa0\x22\
\x13\x46\x10\xc4\xf1\xc0\x09\xa9\x10\xea\x51\xe0\x9a\x09\xc1\xdd\
\x7f\x3c\x05\xef\xae\xda\x97\xaa\xc0\xbc\x82\x08\x7c\xff\x95\xa9\
\x30\x74\x4c\x8f\xb4\xb2\xd7\xbf\x75\x00\xce\xd4\x65\xee\xf1\x44\
\x8b\x5e\x99\x02\x63\xbf\xd6\x4f\xfe\x5b\xf1\x2b\xda\x1a\x87\x37\
\x5f\xd8\x25\x93\x59\xc1\x88\x71\xbd\xe0\xd9\x57\xa7\x42\xa4\x4b\
\x48\x3e\x76\x23\x70\xcd\xea\x90\x17\x68\x69\xd3\xf1\xb7\xc2\xc7\
\x4a\xe0\x05\x35\x39\x38\x0b\xc1\xab\x0d\xb7\xe0\x57\xab\xf7\x69\
\x42\x6d\x73\x53\x14\x7e\xf1\xe2\x6e\x68\x69\x8e\x19\x96\x9d\x0d\
\x50\xfb\xb5\xf9\x37\x47\x34\x64\x41\xd4\x1d\xbc\x04\xd5\xef\x9d\
\x90\xff\x76\x2b\x70\xfd\x24\x8b\x0c\x81\xc8\x11\x46\xc4\xf1\x17\
\xe0\x08\x3f\xb7\xca\x9e\x3d\x79\x1d\xe2\x06\x73\x44\x4d\xd7\x5b\
\xe1\x4b\x1a\xde\xd3\xb2\x04\xc8\x3c\xf4\x7e\x1d\xfc\x8b\xf1\x3e\
\x29\xbc\x03\x56\x7a\x74\x76\x58\x87\xfa\xa9\x05\x8e\x1a\x06\xb1\
\xe9\xf3\x65\xe5\xa2\x28\x86\x4a\x80\x33\xfc\x19\xee\x17\x21\xd6\
\x16\x37\xb5\x19\x8d\xc6\x0d\x6d\x65\x12\x46\x7e\xb5\xb5\x18\xfb\
\x80\xcb\x39\xd3\xb2\x21\xa7\x75\xa8\xcb\xbc\x04\xce\x61\x26\x92\
\x13\x2f\x17\xe3\x71\x81\x6b\x84\xf1\x73\xb8\xdf\xd6\x76\x16\x91\
\x05\x61\x38\xa6\x63\x71\x6a\xfa\xf5\x2c\xac\x64\x09\x6a\x4d\x10\
\x21\x62\x09\x5e\xb6\x12\xe0\x0a\xc1\xb7\x75\x1f\x92\x64\x1e\x62\
\xcd\x6c\x65\x12\x78\x26\xac\x17\x50\x79\xd7\xe9\x0e\x09\x62\x51\
\x87\xbc\x41\xb3\xd2\x21\xb4\x4b\x12\x86\x00\x47\x38\xd9\x2a\xeb\
\x76\x9c\xc5\xd8\xae\x90\x75\x1a\xc6\xc8\x0f\xcb\xcf\x33\x67\x94\
\x66\x75\xe8\x7c\xab\xac\x13\x90\x38\x74\x17\x41\x24\xdc\x6f\xbc\
\xcc\x92\x06\xba\xdd\x2a\x6b\x0a\x13\xa2\x66\x12\x1a\x01\x0b\x09\
\x3f\xcc\x58\x23\x01\x01\xde\x53\x0b\xbc\x35\x4c\x28\x04\xe3\xc3\
\x42\x5c\x2c\x26\x02\x3f\x26\x9a\x6f\x95\x05\xcd\x48\xa7\x9b\x15\
\x65\x76\x4d\x34\xad\x6f\xcf\x30\x0c\x87\xff\x4d\xae\xa1\x08\x82\
\xb3\xa9\x05\xaf\x0d\xcc\x25\x44\x22\x4a\x5c\x23\x8c\x9f\x5b\x65\
\xad\x22\xac\x91\x10\xcc\x06\x78\x15\xee\x5e\xa6\x16\x78\x83\xd6\
\x7f\xb1\x08\x3e\x3d\x0b\x20\xad\x6b\x48\x3a\xee\x6d\x61\xb3\xb9\
\xbd\x04\x51\x41\x63\x2b\xd3\xc0\xb3\x70\xa4\x61\x38\x66\x94\x7e\
\x68\x18\xc0\xfb\xc9\x80\x0f\x30\x12\x67\xbc\xb6\xca\x9a\x42\xe1\
\xa5\xca\x56\xa6\x21\x9f\xb7\xce\x2f\x33\xc8\x1a\x06\xac\x05\x6e\
\x10\x5b\x65\xed\xc0\xbd\x5a\xfd\xdc\x2a\x6b\x05\xb4\xa3\xb7\x25\
\x84\x32\xcb\x9a\x70\x38\xfd\xbe\x7c\x04\x67\x2f\x0d\x40\xd3\x55\
\x4f\x02\xd7\x49\x46\xe9\xc9\x27\xe0\x0c\x4d\xc8\x74\x9a\x0d\xd9\
\x4c\xb8\x59\x55\x42\xf3\xad\xb6\xb4\xb2\x8b\x8a\xbb\x40\x26\x51\
\x48\xed\xeb\xfd\x6a\x6b\x35\x26\x4c\x28\xec\x5d\xe0\xa6\x1a\x98\
\xea\x7d\xde\xb4\xa1\xe2\x9c\x70\x9f\xce\x75\x95\x0d\x31\xac\xfb\
\xc8\xcd\x33\xe7\x37\x2e\x63\xd0\x97\x5d\xdc\x23\x0f\x32\x89\xe2\
\x9e\x79\x69\x7e\x99\x3d\x2d\x25\xbf\x20\xc7\x93\xc0\x55\x34\x8b\
\x66\x4d\x10\x7f\x0d\xd3\x28\x0a\x92\xc8\x7f\xfe\xdf\x0d\x59\x18\
\xd6\x7d\xf4\xec\x97\x6f\x6a\xf2\xfa\x95\xf4\x9b\xf7\xf4\x2b\x29\
\x82\x4c\x01\xc9\x92\x5f\xd8\x45\xe3\xd7\xf5\x6b\x2d\xd0\xda\x6c\
\x7c\x27\xf2\x1e\xb8\x58\x1d\x3c\x08\x5c\x5d\x46\x89\xe0\xad\x61\
\x68\x71\x8d\xbe\x68\x18\xa7\xe2\x4c\xd3\x0d\x11\xf3\x61\x71\xac\
\x54\x25\x74\xeb\x71\xa2\xf6\x4a\x9a\xad\xd1\x13\xfb\x40\xa6\x30\
\x78\x44\xf7\x34\xbf\x1a\xce\xdc\x30\xfd\x7c\x8f\x3e\x5d\xdd\x09\
\x5c\x62\x5d\x87\x3c\x41\x24\xa1\x91\x8e\xc3\x90\x1a\xe0\x88\xf4\
\x56\xc1\x6f\x61\x33\x56\x02\x92\xc6\x08\x67\x4f\x34\xd2\x19\x6b\
\x49\x53\x76\xcf\xfe\x05\xd0\x7b\x40\x01\x64\x02\x0f\xce\x29\x4d\
\x9c\x8b\xca\xaf\x63\x35\x97\x4c\x3f\x3f\x70\x68\x37\xf9\xb7\x63\
\x81\x4b\x2c\xea\x10\x38\x43\x90\x1a\x45\x7a\x82\xd7\x81\x33\x9c\
\xa7\xce\xec\xeb\x3e\x86\x8f\xe9\x69\x68\xf3\xfa\x95\x16\x79\xc9\
\xa3\xda\x16\x66\x29\x0f\x3f\x3d\x12\x82\x46\xaf\xfe\xf9\x72\x74\
\xd3\xfb\xf5\xd7\x3d\x17\x0c\x3f\x8f\xe4\x28\x19\xd5\x23\x1b\xb7\
\xca\x6a\x40\x04\xa1\x1e\xa9\x5b\x0f\x1c\xe1\x4a\xe0\x12\xf6\xa9\
\xfc\x11\xe3\x7b\x99\xda\xde\xf5\xc7\x93\x69\xb6\x2a\xa6\x0e\x94\
\x9f\xd9\x18\x24\x1e\x7a\xea\x6e\x08\x47\x44\x8d\x5f\x78\x47\xcf\
\x73\x27\x8d\xe5\x62\x29\x25\x4b\x24\x27\x94\x95\x5b\x65\xd5\xa0\
\xe7\x70\x5a\xa4\x85\xd6\x03\x4f\xf8\xbc\x55\x76\xf4\xa4\xbe\xa9\
\xb5\xaf\x7a\xe0\xb3\x1b\x9b\x6e\xb6\x6a\x6c\xe1\x43\x3e\x9f\xfa\
\x67\x6e\x4b\x96\x6d\xd1\x7b\x60\x01\xdc\x3f\x6b\x88\xfc\xb7\xda\
\x8f\xcd\xbf\x3a\x6c\xda\xe0\x71\xdd\x6f\xb6\x6e\x95\xd5\x42\xac\
\xa1\x97\x22\xca\x5d\xc3\x20\x98\x42\x2a\x71\x7e\xcf\x94\x6e\x77\
\xe5\xc2\x3d\xc9\x85\xd5\x7a\xe0\x53\x44\x76\xbe\x77\x32\xcd\x56\
\xc5\xd4\x01\x50\xfe\xe0\x00\xf0\x1b\xf8\x44\xb6\x79\x3f\x9c\x04\
\x61\x75\xb4\xa0\xe7\xdd\x48\x33\xb8\xbd\xdb\xcf\x1a\x7e\x07\xeb\
\x6b\x0a\xd5\x3b\xcc\x6b\x82\xf4\x75\x08\xd6\x5b\x65\x79\x22\x16\
\x25\xf5\xe2\xac\xb2\x2a\xae\x84\x41\xd8\x6b\x16\xf0\xb4\xee\xe3\
\xfe\xd9\xa5\xa6\xb6\xab\x37\xd6\x41\x53\x63\x6b\x9a\xad\x79\xcb\
\x26\xd1\xcc\xc5\xdf\x47\x68\xff\xe3\xb3\x13\x60\x28\xd5\x58\x7a\
\xbf\x7e\xbf\xb6\x56\x7e\x66\x93\x11\xca\x68\x17\x5b\x44\x1b\x01\
\x6b\x46\x19\x0a\xb1\x77\xe5\xbc\x19\xf3\xc8\xd8\x95\x35\x89\x60\
\xcf\x31\x53\x62\xc9\x86\xbc\x6e\x95\x1d\x3d\xb1\xb7\x9c\x86\x1a\
\xa1\x89\x0e\xe0\xe1\xf3\x91\x14\x5b\x8a\x10\xc4\xbd\x4b\x8b\x7e\
\x3a\xcd\xf4\x7b\x5e\xf1\xe4\x77\xc6\xc1\x7d\x33\x87\xa4\xf9\x71\
\xa2\xf6\x32\xec\xd9\x76\xda\xf4\x7b\xdf\x78\x66\xb4\x2f\x19\x65\
\x42\xc3\x00\x47\x90\x6a\xfc\x5f\x3e\x43\x7a\x32\x3b\x80\x17\x88\
\xdd\x38\x0b\xfb\xad\xdf\xcd\xee\xc2\x19\xa2\xd9\xcf\x63\x0b\xc6\
\x9a\x9e\xc2\x8e\xf7\x4e\xc0\x9e\xad\xf5\x69\x59\x43\x41\xb7\x1c\
\x78\xf1\x97\xb3\x61\xec\xbd\x7d\x81\x17\xba\x52\x8d\xb4\xe0\xf9\
\xc9\xf0\x77\x4f\x96\xa5\x5d\xb0\x9b\x34\xd2\xad\x5b\xb9\x37\x31\
\xae\x62\x80\x81\xc3\x8a\xa9\x88\xef\xe9\x7c\xca\x84\x31\xa3\xe4\
\x09\x42\x84\x03\xf8\x3b\xd9\x8e\x45\x6e\x11\x26\xa8\xad\xb2\x13\
\xa6\x0f\x84\x41\xc3\xcc\xbb\x98\x77\x57\x7d\x06\x0d\xa7\x6f\xa4\
\xd9\xea\x92\x1b\x86\xef\xbe\x3c\x05\xbe\x39\x6f\x0c\x74\xc9\xf3\
\x36\x95\x86\xdd\xc9\x4f\xde\x9e\x0d\x93\x1f\x1a\x9c\xe6\x17\x92\
\x7d\xfd\x7f\x1e\x80\xcb\x5f\x98\x3f\x4d\xe5\x91\x67\x46\xe1\x34\
\xb5\xe7\x29\x13\xd3\x3a\xe4\x98\x56\x53\xc2\x54\xe3\xef\xe4\xde\
\xea\xe8\x46\xe0\x08\xb3\x6c\x88\xd7\x56\x59\x3c\xc6\x34\xf4\xe9\
\xc5\x13\x4c\xcf\x01\x9f\x59\xf4\xe6\x4f\x76\xcb\xcf\xa8\x4e\xeb\
\xdb\xe9\x9f\xdf\x9c\x37\x1a\x5e\xa4\x17\xfb\xeb\x73\x87\xcb\xcf\
\x9f\x66\x06\x8e\x99\x8c\xbc\x0b\xbe\xfb\xaf\x53\xe0\xfb\xaf\x4e\
\xa3\xf3\x55\xb9\x69\x7e\x20\x36\xd1\x6e\xf1\x93\x0f\xcf\x98\x16\
\x33\x69\xc6\x20\x18\xff\xc0\x00\x5f\x33\x4a\x9e\x53\x8f\x92\x94\
\x08\x2a\xa9\x12\xb7\xd6\x2d\xdb\x0e\x1c\x76\x40\xa6\x42\xa8\xc9\
\x12\x05\xab\x56\x21\x9f\x58\xdc\xd9\x3d\x53\x36\xfc\xd7\x41\xd8\
\xf2\xff\x47\x4d\xcf\xa7\xa0\x28\x07\x7e\xf0\xef\x95\xd0\xbf\xb4\
\x9b\xa9\x2d\xdc\xef\x74\x68\xdf\x97\xb0\x6f\xe7\x39\x1a\x11\x9a\
\xe0\x7c\xfd\x75\x68\xbd\x9d\x98\xf3\xc1\xf3\xc0\x79\x21\x1c\x2b\
\x19\x34\xbc\x18\xc6\xdf\x3f\x80\x96\x55\x64\xd9\xda\xdf\x5d\xf5\
\xa9\xe5\x63\x03\xb1\xbc\xe7\x7e\x56\x29\x8f\x44\x9b\xf9\x45\x24\
\x77\x91\x45\x5f\x87\x5c\x40\x84\x9a\x99\x65\xaf\x57\xe0\x9f\xed\
\x4d\x4b\xa2\x3a\x46\x14\x2a\xc1\x2b\x88\x7f\x5b\x65\x8d\x5a\x20\
\x8a\xc6\x7d\x3b\xcf\xc2\x95\x06\xe3\x07\x97\xa3\x08\x5e\xfd\xe3\
\x9d\xf0\xad\xa5\x13\x61\xec\xe4\x7e\x86\xb6\xc2\x34\x1d\xc6\x54\
\x7d\xfc\x03\xfd\x53\x65\x37\xdf\x4c\x6c\xe2\xcf\xa5\x1a\x05\x6d\
\xa6\xcd\xdf\x18\xf8\x81\x33\xd1\xbf\xfc\xe9\xc7\x70\x68\x6f\x03\
\x58\xe1\xf1\x85\x63\xac\xc9\xc2\x60\x8b\xa5\x0e\x79\x21\x2e\x49\
\xeb\x94\xbf\xd5\x37\x14\xaa\x06\x0e\xd0\x6c\x33\x61\x14\x67\x4a\
\x9f\xcf\x3c\x2c\x0e\xed\x42\x30\x97\x76\x27\x8b\x5e\x99\x6a\x39\
\x9a\x8b\xd3\x06\xbf\x78\x61\x37\xfc\xfa\xe7\xfb\xe5\x47\xd2\xb0\
\xd8\xea\x5a\x98\x03\xf9\x45\x89\xbb\x42\xd8\x8b\x4e\x02\x87\x3e\
\x6d\x80\x57\xbf\xb7\xcd\x96\x2c\x0f\x3f\x3d\x2a\x35\x2c\x60\x48\
\x0e\x97\x02\xd7\xb0\x0e\x39\x69\x98\x78\x2c\xa1\x5f\x10\x1a\x1e\
\x72\xeb\x96\x9c\x8a\x33\x2f\xcb\x21\x92\x65\xe3\x3c\xcd\xff\xbc\
\xfa\xb1\xe9\xf2\x01\x05\xdd\x7b\x75\x85\x47\xe7\x8f\x81\xaf\xa1\
\x50\xa5\xd9\x96\x1b\x5b\x6a\x3f\x50\x23\x6d\x7a\xa7\x96\x66\x65\
\x67\xc0\x0e\xf7\xd1\x11\xe0\x05\xcb\x26\xcb\xb5\xce\xb3\x1b\xb2\
\xab\x43\x2f\xa0\x62\xb7\x7e\x56\xd9\xeb\xa5\xca\xb1\x66\x8c\x7d\
\xde\xa2\x07\x70\xc8\xb1\x12\x3c\x80\x5d\x9c\x25\x9d\xe1\xb4\x76\
\xa6\xef\xa0\x42\x59\xa7\x1c\xfc\xe8\x0b\xc3\x0d\xfb\x0a\xf0\x19\
\x4a\x07\xe8\x67\xf6\x55\x9f\x83\xb6\x96\x18\xf4\xa1\xdf\xc3\x6c\
\xc9\x89\xad\x58\x4c\x82\xc3\x54\xf3\xac\xa7\xfa\xe9\xb7\x6f\xff\
\x15\x4e\x1f\xbd\x06\x76\x98\x30\x6d\x20\xfc\xd3\xe2\x89\xb2\x58\
\x77\x62\xcb\xbc\x0e\x03\xdb\x2a\xbb\xf4\x9d\x9f\x7f\x94\xca\xa2\
\x35\xa5\x6e\x3f\xb5\xa4\x38\x16\x8b\xd8\x7b\xcf\x08\xde\x02\x97\
\xa5\x05\x7e\x71\xea\x3a\xbc\xb6\x68\x1b\x0e\x63\x03\x2b\x4a\x47\
\xdd\x05\x83\xcb\xba\xcb\x3a\xa6\xff\x90\x22\x28\xec\x9e\x27\xaf\
\xbb\xc1\xb2\x31\xcc\x37\x37\xb5\xd1\x48\x72\x1b\x4e\x1e\xbe\x02\
\xc7\x0f\x5e\x86\xda\xbd\x17\xe4\x87\x67\xb1\xe2\x81\x87\x4b\xe0\
\x99\x1f\x4c\x4a\x75\x1d\xfa\x6e\x48\x92\xec\xc6\xa6\x2c\xea\x50\
\x32\xda\xfd\xc8\x6f\x99\x53\x2c\x16\x2a\x9d\x33\xea\xb5\x7a\xe5\
\x38\x8d\x86\x41\x75\x4b\xae\x16\x87\x87\xd8\xc4\xf4\xb9\x13\x8d\
\xf0\xdf\x2f\xef\x81\x2f\x3d\x3c\xf3\x11\xcb\xc2\x6d\x2d\xf8\xec\
\x46\x2f\x78\x84\x8a\xf2\x47\x17\x8c\x49\x9c\x27\xd8\x34\x02\xce\
\x19\x25\x10\x6f\x3b\x07\xe8\x57\xd7\x3e\x34\x7c\xe5\x42\xf5\x6b\
\x06\x54\x24\x2b\xc0\x23\xec\x46\x1f\xdd\x0a\x5c\xf9\x98\x61\xed\
\x4c\xff\xd2\x62\x78\xe1\xad\x59\xf2\x50\xbd\x5b\xe0\x39\x7a\x21\
\x4b\x3e\x15\xcd\xcf\xfe\xdb\x34\x73\xb2\x30\xac\x67\xb1\x22\x4b\
\x3c\x39\xef\xe4\xe7\x56\xd9\x28\x21\xeb\xf4\xaf\x19\x96\xe8\x25\
\xca\x18\xdf\xb0\x39\x73\x77\xc6\xfc\xe4\x83\x33\x54\x94\x1e\x82\
\x4b\x74\x7c\x25\x08\xe0\xb9\x4c\x7b\x6c\x28\xcc\xfe\x87\x51\x54\
\x60\xe7\xf9\xe6\x97\x7a\x46\xda\xaa\x0e\xdd\x42\x2f\x76\x15\x98\
\x0c\x71\x62\x94\x71\x27\x7e\x15\x32\xc8\xa5\xa8\xc6\x08\xec\xc4\
\x99\x5f\x42\x10\xa3\x0c\xae\x37\xd9\xb3\xa5\x1e\x36\xff\xfa\x88\
\x3c\xbf\xe3\x07\xd0\xd6\xe8\x7b\xfb\xc8\x5d\x50\xc9\xdd\x77\x79\
\xca\xbc\x58\xb2\x21\x96\xb2\xbd\xc1\xb8\xa7\x31\x2d\xd9\xab\x96\
\xb1\x75\xdc\x21\x59\xec\x97\x43\xd8\xdb\xc2\x5b\x9b\xe1\x68\x6e\
\xf5\xc6\xe3\x70\xe1\xf4\x0d\xe0\x01\x9c\x56\xb8\x87\x0e\x08\x4e\
\x7f\x6c\x18\x0c\xbf\x87\x4e\x24\xb2\xcc\x0d\xa9\x1b\x01\x61\x5f\
\x13\x94\x98\xd6\x60\x6f\x70\x6e\x35\x8c\x59\x74\x41\x58\x4c\xa2\
\xb8\x8f\x32\x66\xe2\x4c\x74\xa5\x59\x80\x79\x09\xa7\xb1\xad\x76\
\x21\x98\xdf\xad\x0b\x4c\xfd\xc6\x50\x98\xfe\xe8\x30\x38\x4f\xb3\
\x29\x4c\xaf\x6b\x3f\xb9\x00\xa7\xeb\xae\xd1\xe9\x01\x89\xd9\x3f\
\x1c\xcb\xb9\xbb\xbc\x37\x8c\xac\xe8\x0d\x15\xd3\x06\xc8\x13\x9a\
\x7a\x5b\xb6\x7e\x79\x18\xee\x67\xb6\xe5\x7a\xc6\xda\x5c\xc7\x5a\
\x96\xe8\x26\xca\xe8\xa3\x81\x9f\xd9\x10\xaf\xcc\x4b\xa2\x95\x8f\
\x6b\x6e\xb7\xfc\xe6\x28\x1d\x80\x3b\x6d\xe8\x17\x2e\xa9\xf8\xde\
\x2b\x53\xe4\xd5\xfd\x78\xef\xdd\x8e\xe0\x97\x3b\x90\xea\x99\x23\
\xde\x98\x61\xf6\xae\x4d\xc2\xee\x3c\x63\xca\xa6\xa7\xca\xb2\xda\
\xc2\x73\xee\x3b\xb8\xc8\x72\xe3\x1b\x8e\xcb\xe0\x4e\x00\x7c\x42\
\x89\xa7\x2c\xcf\x4f\xbf\x88\xce\x16\x38\x47\x2c\x16\x5e\x68\xf5\
\xbe\x25\x61\x28\xd3\xaa\x05\x41\x5a\x0d\x0e\xe1\x2a\x1b\xf2\xb2\
\xee\xc3\x81\x10\xb4\xb3\xc5\xea\x17\x0f\x5b\xdc\xfd\xf2\xb8\xcd\
\x04\xc7\x5d\xd4\x83\x74\x46\xb0\x1d\x12\x0c\x85\xe2\xcb\x51\x04\
\x81\x13\xf8\x9e\x0d\x01\xf0\x7c\xde\x10\x73\x5f\x9f\xed\x7e\x89\
\x5a\x5b\x4e\x04\x2f\x5e\xe3\x68\x34\xb4\xc2\xee\x73\xb6\x84\x99\
\x51\x5a\xd5\x48\xa3\xcc\x42\x60\x84\x9f\x5b\x65\xd5\xe1\x1a\xe1\
\xe6\x9e\x29\x96\xb6\xac\x1a\x24\xbe\xc7\x69\xfb\x2a\x57\xbf\x6c\
\x6c\xb1\x83\xac\xb0\x8b\x2e\x08\xa6\x49\x07\x27\x5d\x93\x9f\x5b\
\x65\xd5\x2d\xd0\x8f\xe7\x0d\x59\x36\x48\x01\xf8\x6c\x5f\x75\x9c\
\x0d\x79\xb0\x05\x6c\xc0\xae\x68\x56\xd9\xca\xb5\x2c\x9f\x65\x9e\
\xa5\x72\xd2\x35\x65\xb5\x10\xb4\xb1\xe5\xc9\x2f\xc5\x96\xe8\xd4\
\x2f\x70\xe1\x17\xb1\xb5\xc5\xa2\x61\xf0\x9a\xde\xbc\x19\x5d\x0a\
\x8c\x60\x26\x0c\x76\x4d\xb4\xf8\xb9\x76\xf7\x93\xc9\x76\x21\x68\
\x65\xcb\x0e\x3c\x6d\x79\xf7\xcb\x3e\x1a\xb3\x68\x98\x78\x5c\x9c\
\x31\xb7\xa2\x8a\xf9\x96\x2f\x8e\xe6\xc1\x69\xd8\xaa\xa1\x67\xb2\
\xc2\xf2\x43\x3e\x6f\x95\xf5\x2a\x04\x2d\x6d\xd9\x34\x48\x27\x8d\
\xc0\xde\xaf\x6c\x78\xaa\x2c\x59\xca\xa2\x5b\xd4\x70\xbc\x70\x82\
\xea\x99\x2a\x2b\x3d\xe3\xf7\x56\x59\xb7\x19\x0a\x8b\x2d\x96\xa4\
\xc2\xc8\x96\xa3\xed\xab\xba\x46\xe0\x94\x2c\xbc\xb6\xca\x4a\x54\
\xe4\xe2\xb5\x04\x87\x60\xa1\xa1\x21\xac\x46\x81\x4d\x35\x8b\x5a\
\x9c\x79\x5a\xf7\x61\xaf\x8f\xfe\xb2\xb9\x1e\x76\x6d\x3a\x09\x67\
\x8f\x37\xd2\xc0\x64\x13\x3a\x94\xf3\x26\xed\x2d\xd6\x08\x4e\x46\
\x4f\x73\xf3\x22\x50\x56\xde\x4b\x7e\xb2\x6d\x2f\x65\xc1\x37\xc7\
\xe1\x7e\x96\x2e\x0f\x04\xb3\xc5\xe0\xd6\xa3\xb9\x56\x70\xbd\x93\
\x2b\x1c\x8e\xce\x8d\x46\x73\xf6\x0b\x02\x29\x51\xbf\x6e\x4f\x16\
\xe2\x78\x6e\xc8\x69\x24\xf9\x60\xfd\x31\x58\xff\xd6\x41\xe0\x0d\
\xb3\x1d\x8c\x46\xb8\xdd\xd4\x06\x35\xbb\xce\xc3\xb1\x03\x97\xe0\
\xc5\xb7\x67\x41\x37\x7c\x86\xb5\x6e\x3d\x4b\x28\x8d\x1c\x26\x64\
\xd1\xd7\x19\x61\xd4\x47\x06\x64\x41\x91\x7b\xeb\x56\x74\x2e\xb8\
\x84\xeb\xb5\x7c\x28\x82\x51\x30\xa5\x65\x4e\xc4\xa6\x55\x10\xf6\
\xbe\xdd\xe8\x19\x40\x76\x42\x10\x7f\x70\x4e\x28\x5b\x70\xfb\x66\
\x9b\xbc\x1e\x47\xef\x57\xc8\x6e\x08\xc0\x4a\xe0\x3a\x68\x70\x6a\
\xe0\xb5\x72\x2a\x72\xf5\xf0\xb4\xf8\x13\x05\x93\x9e\x34\x99\x7e\
\xaa\xec\x95\x86\x26\xdf\xd6\xbc\xb8\xc5\x39\xda\x2d\x66\xfa\xa9\
\xb2\x0a\x59\x9c\x8a\x5c\x3d\x3c\xaf\x16\x36\x22\x8d\x51\x48\x45\
\xf0\xdc\x2a\x6b\x76\x9c\x93\x1b\x81\x6c\x43\x5e\x61\xf2\x9c\x3c\
\xf8\xe5\x65\xab\x2c\x2f\xb2\xc8\xf6\x81\x03\xd4\xa4\x49\x75\x43\
\x9a\xa9\xfc\xe0\x86\xfb\x8b\xba\x77\x49\x3d\xc9\x35\x5b\xf0\xe0\
\xc3\xa5\xfc\xa7\x31\x80\xb1\x0e\x39\x92\x05\xc1\x6d\x3f\x82\x42\
\x1a\x7a\x86\x35\xce\xb2\x21\xfe\xc3\xfd\xdf\x5a\x3c\x51\xbe\x95\
\x46\x36\x60\xe6\xdf\x97\x41\xc5\x94\x81\xdc\xa7\x31\x18\xeb\xb0\
\x86\x27\x59\x10\x02\x70\x06\xee\x6d\x8a\xc7\x23\x6b\x24\x09\x9e\
\xd0\xce\x73\x18\x28\x7d\xd2\x2e\xce\x88\x6e\x39\xa1\xfa\xa6\x43\
\x76\xc7\x69\xc4\x4c\xda\xaa\xdd\xdb\x20\x2f\xfe\x96\xcb\x56\x79\
\x9b\x9c\x1f\x4d\x41\x7e\x98\xb9\xd8\x1e\x0d\xa1\x3d\x9a\x27\x3f\
\x90\x38\x96\xcf\x55\x91\x05\xea\xb2\x0c\x8e\xf1\xb6\x65\x23\xee\
\xe9\x05\x7d\x07\x17\x72\xf7\xcb\xac\x0e\xd5\xdf\xa5\x26\x37\xd2\
\x21\xff\x85\x5e\x04\xae\x11\xb8\x13\x46\xc1\xd6\xba\xe7\x96\xd3\
\xe2\x5f\x82\x4e\x04\x0e\x1c\x94\x9b\x3d\xe2\x8d\xe5\xe0\x03\x7c\
\x23\x0c\x62\xcb\xb1\x65\x0b\x04\x91\xac\xf2\xeb\x99\x4c\x9d\x48\
\x43\x23\x11\xe2\x4b\x67\x0d\xff\xd9\x5a\xf0\x09\xbe\x12\x06\xf1\
\xfe\xe1\x1f\x97\x84\x42\xd2\x76\xfd\x00\x5f\x27\xf8\x82\xb7\xb8\
\x35\x83\xef\x84\x51\xb0\xed\xf8\x0f\xab\x08\x11\x17\x43\x27\xb8\
\x83\x4a\x99\xd5\x74\xf4\x76\x39\x6f\xbd\x62\x84\xc0\x08\x83\xa0\
\xba\xa6\x92\x92\x66\x4d\x67\xb4\xe1\x03\x8c\x2a\xb8\x1a\x12\x17\
\xb8\x41\x40\xe0\x96\x56\xb3\x00\x1d\x8b\x44\xda\x2a\xdc\x2c\x2c\
\xef\x84\x16\x89\xa8\xd2\x56\x11\x24\x59\x10\x81\x46\x18\x35\x3a\
\xb5\x8d\x5b\xc8\xf7\xcb\x5d\x11\x34\x51\x14\x64\x8c\x30\x0a\x30\
\x93\xc2\xf4\xbb\x93\x38\xd6\x48\x4c\xbd\x90\x15\xac\x6b\x6f\xfd\
\x42\xc6\x09\xa3\xa0\x93\x38\xa6\xc0\xa5\xb1\xab\x9b\x9a\x62\x55\
\x41\x88\x5a\x3b\x64\x0d\x61\x14\x74\x12\x27\x85\xac\x22\x8a\x82\
\xac\x23\x8c\x82\xaf\x2e\x71\x48\x35\xed\x7e\xd6\xd1\x34\x79\x63\
\x36\x11\x45\x41\xd6\x12\x46\x41\x22\x15\x87\x05\x74\x3e\x66\x3e\
\xdc\xb9\x40\x62\x54\x63\x44\xc9\x94\x98\x65\x45\xd6\x13\x46\x41\
\x22\xab\x8a\x57\xd2\x88\x33\xdf\xed\x6d\x48\xb2\x0f\x72\xc6\xf3\
\x3b\xda\xed\xac\xcd\xc6\x68\x62\x84\x0e\x43\x18\x35\x3a\x30\x79\
\x50\x97\xe0\x2d\x4c\x3b\x14\x49\xd4\xe8\x90\x84\x51\x63\xc3\xfe\
\x25\xc5\x85\x85\xa1\x4a\x49\x12\x91\x40\xd3\xa9\x4b\xe5\x90\x55\
\x20\x35\x54\x93\xec\xa0\xe7\xb6\x91\x92\xa4\xa6\x23\x92\x44\x8d\
\x0e\x4f\x18\x3d\x90\x40\x05\x05\x61\x24\x4d\x39\xd5\x3d\xd3\x09\
\x41\xd1\x1c\x0c\x89\x04\x02\xf5\x20\x4a\xd5\xc9\x67\x0b\xd5\xdc\
\x09\x04\xd1\xe3\x8e\x23\x8c\x19\x68\xd6\x55\x2e\x8a\x52\x09\xbd\
\x98\xf2\x8f\x28\xc2\x10\x4a\x26\x5c\x76\x51\x2c\x24\x97\x5f\x10\
\x01\x4a\x8c\xbe\x2b\x13\x41\x7e\x5f\xde\x26\xdc\x48\xa3\x45\x3d\
\x8d\x68\xd7\xf1\x37\xfe\x44\x43\xf1\x9a\x96\x46\x68\xbc\xd3\xc8\
\x61\x84\xbf\x01\x79\x5e\x21\x8b\x50\x20\xf1\x6b\x00\x00\x00\x00\
\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = b"\
\x00\x09\
\x0c\x78\x54\x88\
\x00\x6e\
\x00\x65\x00\x77\x00\x50\x00\x72\x00\x65\x00\x66\x00\x69\x00\x78\
\x00\x0c\
\x08\x5e\x7c\xa7\
\x00\x6d\
\x00\x69\x00\x63\x00\x5f\x00\x69\x00\x63\x00\x6f\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7c\xe6\xce\x0f\xd5\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
