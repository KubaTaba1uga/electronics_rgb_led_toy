# RGB LED toy

A simple toy demonstrating how an RGB LED works. By adjusting potentiometers, users can mix red, green, and blue light to create any color in the RGB spectrum.

![Project Image](path_to_image.png) <!-- Add an image of your project here -->

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Enclosure Design](#enclosure-design)
- [Getting Started](#getting-started)
- [Assembly Instructions](#assembly-instructions)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project consists of a PCB board designed in KiCad and an enclosure designed in OpenSCAD, which can be 3D printed. The circuit allows users to adjust the intensity of red, green, and blue channels of an RGB LED using potentiometers, creating a full range of colors.

## Features

- **RGB Color Mixing**: Adjust potentiometers to mix red, green, and blue light.
- **Custom PCB Design**: PCB board designed using KiCad.
- **3D Printable Enclosure**: Box designed in OpenSCAD for housing the PCB.

## Hardware Components

- **Electronics**:
  - 1 x Common Cathode RGB LED
  - 3 x Potentiometers (e.g., 10kΩ linear taper)
  - 3 x Current-limiting resistors for the RGB LED (calculate based on your LED specs)
  - 3 x Rocker switches
  - 1 x PCB (design files included)
  - 3 x AAA battery
  - Wires and connectors as needed
  - Some M2 screws
- **Tools Required**:
  - Soldering iron and solder
  - Wire cutters/strippers
  - Multimeter (optional for testing)

Components examples:
- [Red rocker switch](https://www.amazon.com/Twidec-Rocker-Position-Illuminated-KCD2-201N-BU/dp/B07MV5LBX8/ref=sr_1_1?crid=3TD23RVLMG6Z4&dib=eyJ2IjoiMSJ9.MytuyUmSVyDPcqdz0-hPTGBWjusLBUMxMacKpkE82gv4jepQVEn_gehBBpbBIvG3z0AbFAFO2Uk4pilC01WHr0K3-53ic8luo5b2fuP7ekoIxj79-xcMwD2pG09d9zLjWrHabZ0-CDp8GRCul-4eHnmPWNCAGQE1n28UB6E4wumrJ58iK5A6zx9YEQmL51N7-F1vKiq0_7a-CcSb2CmqyDhs0_pPEpygn4H0GRY7VEU.NOZqBpuaGICAkMl2GmvqS3otJYxrt7sDQj98gaYhyTk&dib_tag=se&keywords=Rocker%2BSwitch%2BDPST%2Bblue&qid=1732781497&sprefix=rocker%2Bswitch%2Bdpst%2Bblu%2Caps%2C201&sr=8-1&th=1)
- [Blue rocker switch](https://www.amazon.com/Twidec-Rocker-Position-Illuminated-KCD2-201N-BU/dp/B08YNQX96T/ref=sr_1_1?crid=3TD23RVLMG6Z4&dib=eyJ2IjoiMSJ9.MytuyUmSVyDPcqdz0-hPTGBWjusLBUMxMacKpkE82gv4jepQVEn_gehBBpbBIvG3z0AbFAFO2Uk4pilC01WHr0K3-53ic8luo5b2fuP7ekoIxj79-xcMwD2pG09d9zLjWrHabZ0-CDp8GRCul-4eHnmPWNCAGQE1n28UB6E4wumrJ58iK5A6zx9YEQmL51N7-F1vKiq0_7a-CcSb2CmqyDhs0_pPEpygn4H0GRY7VEU.NOZqBpuaGICAkMl2GmvqS3otJYxrt7sDQj98gaYhyTk&dib_tag=se&keywords=Rocker%2BSwitch%2BDPST%2Bblue&qid=1732781497&sprefix=rocker%2Bswitch%2Bdpst%2Bblu%2Caps%2C201&sr=8-1&th=1)
- [Green rocker switch](https://www.amazon.com/Twidec-Rocker-Position-Illuminated-KCD2-201N-BU/dp/B07MV5TVKX/ref=sr_1_1?crid=3TD23RVLMG6Z4&dib=eyJ2IjoiMSJ9.MytuyUmSVyDPcqdz0-hPTGBWjusLBUMxMacKpkE82gv4jepQVEn_gehBBpbBIvG3z0AbFAFO2Uk4pilC01WHr0K3-53ic8luo5b2fuP7ekoIxj79-xcMwD2pG09d9zLjWrHabZ0-CDp8GRCul-4eHnmPWNCAGQE1n28UB6E4wumrJ58iK5A6zx9YEQmL51N7-F1vKiq0_7a-CcSb2CmqyDhs0_pPEpygn4H0GRY7VEU.NOZqBpuaGICAkMl2GmvqS3otJYxrt7sDQj98gaYhyTk&dib_tag=se&keywords=Rocker%2BSwitch%2BDPST%2Bblue&qid=1732781497&sprefix=rocker%2Bswitch%2Bdpst%2Bblu%2Caps%2C201&sr=8-1&th=1)

## Enclosure Design

- **Software**: OpenSCAD
- **Files**: Enclosure design files are located in the `enclosure/` directory.
- **Printing**: Compatible with most FDM 3D printers; designed for easy assembly.

## Getting Started

### Prerequisites

- **Software**:
  - [KiCad](https://www.kicad.org/) for viewing/modifying PCB files
  - [OpenSCAD](https://www.openscad.org/) for viewing/modifying the enclosure
- **Hardware**:
  - Access to a 3D printer for printing the enclosure
  - PCB fabrication service or equipment

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KubaTaba1uga/electronics_rgb_led_toy.git
   ```

2. **Install Required Software**

   - Download and install KiCad and OpenSCAD if you plan to modify the designs.

## Assembly Instructions

### PCB Fabrication and Assembly

1. **Fabricate the PCB**:

   - Use the provided Gerber files in the `output/` directory to fabricate the PCB.

2. **Solder Components**:

   - Solder the RGB LED, potentiometers, resistors, and any connectors to the PCB according to the schematic.

3. **Testing**:

   - Before placing the PCB into the enclosure, test the circuit by connecting a suitable power supply.

### Enclosure Printing and Assembly

1. **Print the Enclosure**:

   - Open the `.scad` file in OpenSCAD.
   - Export it to an STL file.
   - Use slicing software (e.g., Cura, PrusaSlicer) to prepare the STL for printing.
   - Print the enclosure using a 3D printer.

2. **Assemble the Enclosure**:

   - Place the assembled PCB into the printed enclosure.
   - Secure the PCB and close the enclosure with screws.

## Usage

1. **Power Up**:

   - Put AAA betteries in battery holder.

2. **Adjust Colors**:

   - Use rocker switches and potentiometers to adjust the intensity of the red, green, and blue channels.

3. **Create Colors**:

   - Mix different levels to explore the full RGB color palette.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Inspired by basic electronics and the desire to make learning interactive.
- Thanks to the communities of [KiCad](https://www.kicad.org/) and [OpenSCAD](https://www.openscad.org/) for their amazing tools.
- Thanks to Charles platt (Make: Electronics) and Paul Sherz, Simon Monk (Practical Electronics for Inventors) for their awesome books.
