"""Constants for the Philips Infrared integration."""

from enum import StrEnum

DOMAIN = "philips_infrared"
CONF_INFRARED_ENTITY_ID = "infrared_entity_id"
CONF_DEVICE_TYPE = "device_type"


class PhilipsDeviceType(StrEnum):
    """Philips device types."""

    TV = "tv"
