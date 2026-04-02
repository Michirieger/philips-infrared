"""Media player platform for Philips Infrared integration."""

from infrared_protocols.codes.philips.tv import PhilipsTVCode

from homeassistant.components.media_player import (
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerState,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_DEVICE_TYPE, CONF_INFRARED_ENTITY_ID, PhilipsDeviceType
from .entity import PhilipsIrEntity

PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Philips IR media player from a config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    device_type = entry.data[CONF_DEVICE_TYPE]

    if device_type == PhilipsDeviceType.TV:
        async_add_entities(
            [PhilipsIrTvMediaPlayer(entry, infrared_entity_id)]
        )


class PhilipsIrTvMediaPlayer(PhilipsIrEntity, MediaPlayerEntity):
    """Representation of a Philips TV controlled via IR."""

    _attr_name = None
    _attr_assumed_state = True
    _attr_supported_features = (
        MediaPlayerEntityFeature.TURN_ON
        | MediaPlayerEntityFeature.TURN_OFF
        | MediaPlayerEntityFeature.VOLUME_STEP
        | MediaPlayerEntityFeature.VOLUME_MUTE
        | MediaPlayerEntityFeature.NEXT_TRACK
        | MediaPlayerEntityFeature.PREVIOUS_TRACK
        | MediaPlayerEntityFeature.PLAY
        | MediaPlayerEntityFeature.PAUSE
        | MediaPlayerEntityFeature.STOP
    )
    _attr_state = MediaPlayerState.ON

    def __init__(
        self, entry: ConfigEntry, infrared_entity_id: str
    ) -> None:
        """Initialize Philips TV media player."""
        super().__init__(entry, infrared_entity_id, "media_player")

    async def async_turn_on(self) -> None:
        """Turn the TV on."""
        await self._send_command(PhilipsTVCode.STANDBY)

    async def async_turn_off(self) -> None:
        """Turn the TV off."""
        await self._send_command(PhilipsTVCode.STANDBY)

    async def async_volume_up(self) -> None:
        """Turn volume up."""
        await self._send_command(PhilipsTVCode.VOLUME_UP)

    async def async_volume_down(self) -> None:
        """Turn volume down."""
        await self._send_command(PhilipsTVCode.VOLUME_DOWN)

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute the volume."""
        await self._send_command(PhilipsTVCode.MUTE)

    async def async_media_play(self) -> None:
        """Send play command."""
        await self._send_command(PhilipsTVCode.PLAY)

    async def async_media_pause(self) -> None:
        """Send pause command."""
        await self._send_command(PhilipsTVCode.PAUSE)

    async def async_media_stop(self) -> None:
        """Send stop command."""
        await self._send_command(PhilipsTVCode.STOP)

    async def async_media_next_track(self) -> None:
        """Send channel up command."""
        await self._send_command(PhilipsTVCode.CHANNEL_UP)

    async def async_media_previous_track(self) -> None:
        """Send channel down command."""
        await self._send_command(PhilipsTVCode.CHANNEL_DOWN)
