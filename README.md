Python scripts to make the Desktop Simpsons TV work.<BR>

A complete build guide can be found here [here](https://withrow.io/simpsons-tv-build-guide).

Some small changes I made:

- I used [this TFT screen in my build](https://shop.pimoroni.com/products/pitft-plus-320x240-2-8-tft-resistive-touchscreen-pi-2-and-model-a-b) and didn't hard solder the Pi Zero, instead using headers
- I didn't use a [Micro USB Male Solder Plug](https://amzn.to/3kMflUv) I just [soldered wires directly to the Pi Zero](https://www.msldigital.com/pages/support-for-hub-zero)
- Added a software function to kill Wi-Fi and Bluetooth when the screen is off
- Added .m4v as an input format for `encode.py`

See my build [here](https://twitter.com/notmattjani/status/1436467546090348584)
