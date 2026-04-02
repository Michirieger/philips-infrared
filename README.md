# Philips Infrared Integration for Home Assistant

Control Philips TVs via infrared using Home Assistant's native Infrared integration (introduced in HA 2026.4).

## Features

- **Media Player Entity** for basic TV controls:
  - Power on/off
  - Volume up/down
  - Mute
  - Channel up/down
  - Play/Pause/Stop

- **Button Entities** for individual IR commands:
  - Navigation (Up, Down, Left, Right, OK)
  - Menu (Home, Back, Options, Exit, Info, Guide)
  - Numeric keypad (0-9)
  - Color keys (Red, Green, Yellow, Blue)
  - Teletext & Subtitles
  - Playback controls (Play, Pause, Stop, FF, RW, Record)
  - Source selection
  - Ambilight control
  - Channel navigation (Channel Up, Down, Previous)

## Requirements

1. **Home Assistant 2026.4+** (for the Infrared integration)
2. **IR Transmitter Hardware** (e.g., ESPHome, Broadlink, etc.) with Infrared integration set up
3. **Philips TV** with RC6 IR support (tested on 55PUS7805/12)

## Installation

### Via HACS

1. Open Home Assistant → Settings → Devices & Services → Custom repositories
2. Add this repository: `https://github.com/Michirieger/philips-infrared`
3. Select "Integration" as the category
4. Install "Philips Infrared" via HACS
5. Restart Home Assistant

### Manual Installation

1. Clone this repository into `custom_components/`:
   ```bash
   git clone https://github.com/Michirieger/philips-infrared.git custom_components/philips_infrared
   ```
2. Restart Home Assistant
3. Reload custom components or restart again

## Configuration

1. Go to **Settings → Devices & Services → Create Automation** (or use the UI)
2. Click **"Create Automation"** and search for "Philips Infrared"
3. Select your Philips TV device type (currently "TV")
4. Select the infrared transmitter entity you want to use
5. Complete the setup

The integration will automatically:
- Create a media player entity for your TV
- Create button entities for all available IR commands
- Track the infrared transmitter's availability

## Supported Devices

- Philips TVs with RC6 IR support (all modern Philips TVs)
  - Tested: 55PUS7805/12 (Ambilight)

## Troubleshooting

**"No infrared transmitters found"**
- Ensure you have set up an IR transmitter integration (e.g., Broadlink, ESPHome) first
- Check that the transmitter has been added to Home Assistant and has the `infrared` domain

**TV not responding to commands**
- Check the transmitter's availability in the logbook
- Ensure the transmitter has a clear line of sight to the TV
- Verify the transmitter is working with other commands

## Development

This integration uses the `infrared-protocols` library which provides RC6 protocol encoding for Philips devices.

### Building Custom Commands

To add new commands or device types:

1. Check the `infrared-protocols` library: https://github.com/Michirieger/infrared-protocols
2. Add new codes to `infrared_protocols.codes.philips.tv.PhilipsTVCode`
3. Update the integration's button/media player entities

## Contributing

Contributions are welcome! Please open an issue or pull request.

## License

This integration is released under the MIT License.

## Credits

- Built for Home Assistant's native Infrared integration
- Uses the `infrared-protocols` library for RC6 protocol support
