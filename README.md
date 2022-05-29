### Bill of Materials:
Parts for the board:
| Part           | Quantity | Package          | Value          | Link                      |
| -------------- |:--------:|:----------------:|:--------------:|:-------------------------:|
| Microprocessor | 1        | QFN-56           | RP2040         |                           |
| 8MB SPI Flash  | 1        | SOIC-8           |                |                           |
| NeoPixel LED   | 37       | 1515 LED         | SK6805-E-J     | [Adafruit](https://www.adafruit.com/product/4492) |
| 7 Segement LED | 4        | LTS6760          | Common Cathode |                           | 
| Button Switch  | 5        | KMR2             | Momentary      |                           |
| Schottky Diode | 4        | SOD-123          | MBR0540        |                           |
| Transistor     | 14       | SOT-23           |                |                           |
| Crystal        | 1        | 2.5mm X 2.0mm    | 12.000 MHz     |                           |
| I2C Quad ADC   | 8        | SOIC-16          | PCF8591        |                           |
| Quad Logic Shifter | 1    | SOIC-16          | 74AHCT125      |                           |
| Voltage Regulator | 4     | SOT-23-5         | AP2112K-3.3    |                           |
| USB-C Receptacle | 5      | SMD              |                |                           |
| USB-C Plug     | 4        | SMD Edge Launch  | | [Adafruit](https://www.adafruit.com/product/4932) [Digikey](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4932/13997774) |
| Resistor       | 23       | 0603/1608 Metric | 300 Ω          |                           |
| Resistor       | 10       | 0603/1608 Metric | 1 kΩ           |                           |
| Resistor       | 2        | 0603/1608 Metric | 5.11 kΩ        |                           |
| Resistor       | 60       | 0603/1608 Metric | 10 kΩ          |                           |
| Resistor       | 9        | 0603/1608 Metric | 1 MΩ           |                           |
| Resistor       | 2        | 0402/1005 Metric | 27 Ω           |                           |
| Capacitor      | 45       | 0805/2012 Metric | 0.1 µF         |                           |
| Capacitor      | 20       | 0085/2012 Metric | 10 µF          |                           |
| Capacitor      | 2        | 0402/1005 Metric | 27 pF          |                           |
| Capacitor      | 10       | 0402/1005 Metric | 100 nF         |                           |
| Capacitor      | 2        | 0402/1005 Metric | 1 µF           |                           |
| Magnets        | 112      | 3mm diameter x 1mm | Neodymium    |                           |

Parts for the game pieces (assuming 20 pieces for each nationality):
| Part           | Quantity | Package          | Value          | Link                      |
| -------------- |:--------:|:----------------:|:--------------:|:-------------------------:|
| Resistor       | 20       | Through Hole     | 60 kΩ          |                           |
| Resistor       | 20       | Through Hole     | 25 kΩ          |                           |
| Resistor       | 20       | Through Hole     | 13.4 kΩ        |                           |
| Resistor       | 20       | Through Hole     | 7.5 kΩ         |                           |
| Resistor       | 20       | Through Hole     | 4 kΩ           |                           |
| Resistor       | 20       | Through Hole     | 1.7 kΩ         |                           |
| Resistor       | 20       | Through Hole     | 0 Ω            |                           |
| Magnets        | 140      | 3mm diameter x 1mm | Neodymium    |                           |
| Pogo Pins      | 140      | anything that makes good contact with 2mm diameter pads and fits inside the piece | | [Digikey](https://www.digikey.com/en/products/detail/mill-max-manufacturing-corp/0965-0-15-20-80-14-11-0/2784013) |


### 3D Printing Pieces:

### Assembly Instructions:

### Software Install Instructions:
1) Hold down boot button on underside while plugging USB into computer.
2) When the `RPI-RP2` device shows up, copy [Adafruit's CircuitPython library](https://circuitpython.org/board/adafruit_feather_rp2040/) to the volume. 
3) Wait for the device to disappear and reappear as `CURCUITPY`, then copy all the libraries into the `lib` directory on the RP2040.
4) Finally, copy `code.py` into the `CURCUITPY` volume.

### Images
![PCB](/full_board_render/full_board.png)
