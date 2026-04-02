"""Button platform for Philips Infrared integration."""

from dataclasses import dataclass

from infrared_protocols.codes.philips.tv import PhilipsTVCode

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID, PhilipsDeviceType
from .entity import PhilipsIrEntity

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class PhilipsIrButtonEntityDescription(ButtonEntityDescription):
    """Describes a Philips IR button entity."""

    command_code: PhilipsTVCode


TV_BUTTONS: tuple[PhilipsIrButtonEntityDescription, ...] = (
    # Power
    PhilipsIrButtonEntityDescription(
        key="standby",
        translation_key="standby",
        command_code=PhilipsTVCode.STANDBY,
    ),
    # Navigation
    PhilipsIrButtonEntityDescription(
        key="nav_up",
        translation_key="nav_up",
        command_code=PhilipsTVCode.NAV_UP,
    ),
    PhilipsIrButtonEntityDescription(
        key="nav_down",
        translation_key="nav_down",
        command_code=PhilipsTVCode.NAV_DOWN,
    ),
    PhilipsIrButtonEntityDescription(
        key="nav_left",
        translation_key="nav_left",
        command_code=PhilipsTVCode.NAV_LEFT,
    ),
    PhilipsIrButtonEntityDescription(
        key="nav_right",
        translation_key="nav_right",
        command_code=PhilipsTVCode.NAV_RIGHT,
    ),
    PhilipsIrButtonEntityDescription(
        key="ok",
        translation_key="ok",
        command_code=PhilipsTVCode.OK,
    ),
    # Menu
    PhilipsIrButtonEntityDescription(
        key="home",
        translation_key="home",
        command_code=PhilipsTVCode.HOME,
    ),
    PhilipsIrButtonEntityDescription(
        key="back",
        translation_key="back",
        command_code=PhilipsTVCode.BACK,
    ),
    PhilipsIrButtonEntityDescription(
        key="options",
        translation_key="options",
        command_code=PhilipsTVCode.OPTIONS,
    ),
    PhilipsIrButtonEntityDescription(
        key="exit",
        translation_key="exit",
        command_code=PhilipsTVCode.EXIT,
    ),
    PhilipsIrButtonEntityDescription(
        key="info",
        translation_key="info",
        command_code=PhilipsTVCode.INFO,
    ),
    PhilipsIrButtonEntityDescription(
        key="guide",
        translation_key="guide",
        command_code=PhilipsTVCode.GUIDE,
    ),
    # Source
    PhilipsIrButtonEntityDescription(
        key="source",
        translation_key="source",
        command_code=PhilipsTVCode.SOURCE,
    ),
    # Numbers
    PhilipsIrButtonEntityDescription(
        key="num_0",
        translation_key="num_0",
        command_code=PhilipsTVCode.NUM_0,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_1",
        translation_key="num_1",
        command_code=PhilipsTVCode.NUM_1,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_2",
        translation_key="num_2",
        command_code=PhilipsTVCode.NUM_2,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_3",
        translation_key="num_3",
        command_code=PhilipsTVCode.NUM_3,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_4",
        translation_key="num_4",
        command_code=PhilipsTVCode.NUM_4,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_5",
        translation_key="num_5",
        command_code=PhilipsTVCode.NUM_5,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_6",
        translation_key="num_6",
        command_code=PhilipsTVCode.NUM_6,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_7",
        translation_key="num_7",
        command_code=PhilipsTVCode.NUM_7,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_8",
        translation_key="num_8",
        command_code=PhilipsTVCode.NUM_8,
    ),
    PhilipsIrButtonEntityDescription(
        key="num_9",
        translation_key="num_9",
        command_code=PhilipsTVCode.NUM_9,
    ),
    # Color keys
    PhilipsIrButtonEntityDescription(
        key="red",
        translation_key="red",
        command_code=PhilipsTVCode.RED,
    ),
    PhilipsIrButtonEntityDescription(
        key="green",
        translation_key="green",
        command_code=PhilipsTVCode.GREEN,
    ),
    PhilipsIrButtonEntityDescription(
        key="yellow",
        translation_key="yellow",
        command_code=PhilipsTVCode.YELLOW,
    ),
    PhilipsIrButtonEntityDescription(
        key="blue",
        translation_key="blue",
        command_code=PhilipsTVCode.BLUE,
    ),
    # Teletext and subtitles
    PhilipsIrButtonEntityDescription(
        key="teletext",
        translation_key="teletext",
        command_code=PhilipsTVCode.TELETEXT,
    ),
    PhilipsIrButtonEntityDescription(
        key="subtitle",
        translation_key="subtitle",
        command_code=PhilipsTVCode.SUBTITLE,
    ),
    # Playback
    PhilipsIrButtonEntityDescription(
        key="play",
        translation_key="play",
        command_code=PhilipsTVCode.PLAY,
    ),
    PhilipsIrButtonEntityDescription(
        key="pause",
        translation_key="pause",
        command_code=PhilipsTVCode.PAUSE,
    ),
    PhilipsIrButtonEntityDescription(
        key="stop",
        translation_key="stop",
        command_code=PhilipsTVCode.STOP,
    ),
    PhilipsIrButtonEntityDescription(
        key="fast_forward",
        translation_key="fast_forward",
        command_code=PhilipsTVCode.FAST_FORWARD,
    ),
    PhilipsIrButtonEntityDescription(
        key="rewind",
        translation_key="rewind",
        command_code=PhilipsTVCode.REWIND,
    ),
    PhilipsIrButtonEntityDescription(
        key="record",
        translation_key="record",
        command_code=PhilipsTVCode.RECORD,
    ),
    # Philips-specific
    PhilipsIrButtonEntityDescription(
        key="ambilight",
        translation_key="ambilight",
        command_code=PhilipsTVCode.AMBILIGHT,
    ),
    # Channel
    PhilipsIrButtonEntityDescription(
        key="channel_up",
        translation_key="channel_up",
        command_code=PhilipsTVCode.CHANNEL_UP,
    ),
    PhilipsIrButtonEntityDescription(
        key="channel_down",
        translation_key="channel_down",
        command_code=PhilipsTVCode.CHANNEL_DOWN,
    ),
    PhilipsIrButtonEntityDescription(
        key="previous_channel",
        translation_key="previous_channel",
        command_code=PhilipsTVCode.PREVIOUS_CHANNEL,
    ),
)

DEVICE_TYPE_BUTTONS: dict[
    PhilipsDeviceType, tuple[PhilipsIrButtonEntityDescription, ...]
] = {
    PhilipsDeviceType.TV: TV_BUTTONS,
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Philips IR buttons from a config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    device_type = PhilipsDeviceType(entry.data[CONF_DEVICE_TYPE])
    buttons = DEVICE_TYPE_BUTTONS.get(device_type, ())

    async_add_entities(
        PhilipsIrButton(entry, infrared_entity_id, description)
        for description in buttons
    )


class PhilipsIrButton(PhilipsIrEntity, ButtonEntity):
    """Representation of a Philips IR button."""

    entity_description: PhilipsIrButtonEntityDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: PhilipsIrButtonEntityDescription,
    ) -> None:
        """Initialize Philips IR button."""
        super().__init__(entry, infrared_entity_id, description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Press the button."""
        await self._send_command(self.entity_description.command_code)
