"""Simplified extension handling for protobuf messages.

THIS CODE IS AUTO-GENERATED - DO NOT EDIT!!!
"""

from .ProtocolMessage_pb2 import ProtocolMessage


from . import ClientUpdatesConfigMessage_pb2
from . import CryptoPairingMessage_pb2
from . import DeviceInfoMessage_pb2
from . import GetKeyboardSessionMessage_pb2
from . import KeyboardMessage_pb2
from . import NotificationMessage_pb2
from . import PlaybackQueueRequestMessage_pb2
from . import RegisterForGameControllerEventsMessage_pb2
from . import RegisterHIDDeviceMessage_pb2
from . import RegisterHIDDeviceResultMessage_pb2
from . import RegisterVoiceInputDeviceMessage_pb2
from . import RegisterVoiceInputDeviceResponseMessage_pb2
from . import RemoveClientMessage_pb2
from . import RemovePlayerMessage_pb2
from . import SendCommandMessage_pb2
from . import SendCommandResultMessage_pb2
from . import SendHIDEventMessage_pb2
from . import SendPackedVirtualTouchEventMessage_pb2
from . import SendVoiceInputMessage_pb2
from . import SetArtworkMessage_pb2
from . import SetConnectionStateMessage_pb2
from . import SetDefaultSupportedCommandsMessage_pb2
from . import SetHiliteModeMessage_pb2
from . import SetNowPlayingClientMessage_pb2
from . import SetRecordingStateMessage_pb2
from . import SetStateMessage_pb2
from . import TextInputMessage_pb2
from . import TransactionMessage_pb2
from . import UpdateClientMessage_pb2
from . import UpdateContentItemMessage_pb2
from . import UpdateOutputDeviceMessage_pb2
from . import VolumeControlAvailabilityMessage_pb2
from . import WakeDeviceMessage_pb2


from .AudioFormatSettingsMessage_pb2 import AudioFormatSettings
from .ClientUpdatesConfigMessage_pb2 import ClientUpdatesConfigMessage
from .CommandInfo_pb2 import CommandInfo
from .CommandOptions_pb2 import CommandOptions
from .Common_pb2 import DeviceClass
from .Common_pb2 import DeviceSubType
from .Common_pb2 import DeviceType
from .Common_pb2 import RepeatMode
from .Common_pb2 import ShuffleMode
from .ContentItemMetadata_pb2 import ContentItemMetadata
from .ContentItem_pb2 import ContentItem
from .CryptoPairingMessage_pb2 import CryptoPairingMessage
from .DeviceInfoMessage_pb2 import DeviceInfoMessage
from .GetKeyboardSessionMessage_pb2 import GetKeyboardSessionMessage
from .KeyboardMessage_pb2 import KeyboardMessage
from .LanguageOption_pb2 import LanguageOption
from .NotificationMessage_pb2 import NotificationMessage
from .NowPlayingClient_pb2 import NowPlayingClient
from .NowPlayingInfo_pb2 import NowPlayingInfo
from .NowPlayingPlayer_pb2 import NowPlayingPlayer
from .Origin_pb2 import Origin
from .PlaybackQueueCapabilities_pb2 import PlaybackQueueCapabilities
from .PlaybackQueueContext_pb2 import PlaybackQueueContext
from .PlaybackQueueRequestMessage_pb2 import PlaybackQueueRequestMessage
from .PlaybackQueue_pb2 import PlaybackQueue
from .PlayerPath_pb2 import PlayerPath
from .RegisterForGameControllerEventsMessage_pb2 import RegisterForGameControllerEventsMessage
from .RegisterHIDDeviceMessage_pb2 import RegisterHIDDeviceMessage
from .RegisterHIDDeviceResultMessage_pb2 import RegisterHIDDeviceResultMessage
from .RegisterVoiceInputDeviceMessage_pb2 import RegisterVoiceInputDeviceMessage
from .RegisterVoiceInputDeviceResponseMessage_pb2 import RegisterVoiceInputDeviceResponseMessage
from .RemoveClientMessage_pb2 import RemoveClientMessage
from .RemovePlayerMessage_pb2 import RemovePlayerMessage
from .SendButtonEventMessage_pb2 import SendButtonEventMessage
from .SendCommandMessage_pb2 import SendCommandMessage
from .SendCommandResultMessage_pb2 import SendCommandResultMessage
from .SendHIDEventMessage_pb2 import SendHIDEventMessage
from .SendPackedVirtualTouchEventMessage_pb2 import SendPackedVirtualTouchEventMessage
from .SendVoiceInputMessage_pb2 import AudioBuffer
from .SendVoiceInputMessage_pb2 import AudioDataBlock
from .SendVoiceInputMessage_pb2 import AudioStreamPacketDescription
from .SendVoiceInputMessage_pb2 import AudioTime
from .SendVoiceInputMessage_pb2 import SendVoiceInputMessage
from .SetArtworkMessage_pb2 import SetArtworkMessage
from .SetConnectionStateMessage_pb2 import SetConnectionStateMessage
from .SetDefaultSupportedCommandsMessage_pb2 import SetDefaultSupportedCommandsMessage
from .SetHiliteModeMessage_pb2 import SetHiliteModeMessage
from .SetNowPlayingClientMessage_pb2 import SetNowPlayingClientMessage
from .SetNowPlayingPlayerMessage_pb2 import SetNowPlayingPlayerMessage
from .SetRecordingStateMessage_pb2 import SetRecordingStateMessage
from .SetStateMessage_pb2 import SetStateMessage
from .SupportedCommands_pb2 import SupportedCommands
from .TextEditingAttributesMessage_pb2 import TextEditingAttributes
from .TextInputMessage_pb2 import TextInputMessage
from .TextInputTraitsMessage_pb2 import TextInputTraits
from .TransactionKey_pb2 import TransactionKey
from .TransactionMessage_pb2 import TransactionMessage
from .TransactionPacket_pb2 import TransactionPacket
from .TransactionPackets_pb2 import TransactionPackets
from .UpdateClientMessage_pb2 import UpdateClientMessage
from .UpdateContentItemMessage_pb2 import UpdateContentItemMessage
from .UpdateOutputDeviceMessage_pb2 import AVOutputDeviceDescriptor
from .UpdateOutputDeviceMessage_pb2 import AVOutputDeviceSourceInfo
from .UpdateOutputDeviceMessage_pb2 import UpdateOutputDeviceMessage
from .VirtualTouchDeviceDescriptorMessage_pb2 import VirtualTouchDeviceDescriptor
from .VoiceInputDeviceDescriptorMessage_pb2 import VoiceInputDeviceDescriptor
from .VolumeControlAvailabilityMessage_pb2 import VolumeControlAvailabilityMessage
from .VolumeControlCapabilitiesDidChange_pb2 import VolumeControlCapabilitiesDidChangeMessage
from .WakeDeviceMessage_pb2 import WakeDeviceMessage


_EXTENSION_LOOKUP = {
    ProtocolMessage.CLIENT_UPDATES_CONFIG_MESSAGE: ClientUpdatesConfigMessage_pb2.clientUpdatesConfigMessage,
    ProtocolMessage.CRYPTO_PAIRING_MESSAGE: CryptoPairingMessage_pb2.cryptoPairingMessage,
    ProtocolMessage.DEVICE_INFO_MESSAGE: DeviceInfoMessage_pb2.deviceInfoMessage,
    ProtocolMessage.DEVICE_INFO_UPDATE_MESSAGE: DeviceInfoMessage_pb2.deviceInfoMessage,
    ProtocolMessage.GET_KEYBOARD_SESSION_MESSAGE: GetKeyboardSessionMessage_pb2.getKeyboardSessionMessage,
    ProtocolMessage.KEYBOARD_MESSAGE: KeyboardMessage_pb2.keyboardMessage,
    ProtocolMessage.NOTIFICATION_MESSAGE: NotificationMessage_pb2.notificationMessage,
    ProtocolMessage.PLAYBACK_QUEUE_REQUEST_MESSAGE: PlaybackQueueRequestMessage_pb2.playbackQueueRequestMessage,
    ProtocolMessage.REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE: RegisterForGameControllerEventsMessage_pb2.registerForGameControllerEventsMessage,
    ProtocolMessage.REGISTER_HID_DEVICE_MESSAGE: RegisterHIDDeviceMessage_pb2.registerHIDDeviceMessage,
    ProtocolMessage.REGISTER_HID_DEVICE_RESULT_MESSAGE: RegisterHIDDeviceResultMessage_pb2.registerHIDDeviceResultMessage,
    ProtocolMessage.REGISTER_VOICE_INPUT_DEVICE_MESSAGE: RegisterVoiceInputDeviceMessage_pb2.registerVoiceInputDeviceMessage,
    ProtocolMessage.REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE: RegisterVoiceInputDeviceResponseMessage_pb2.registerVoiceInputDeviceResponseMessage,
    ProtocolMessage.REMOVE_CLIENT_MESSAGE: RemoveClientMessage_pb2.removeClientMessage,
    ProtocolMessage.REMOVE_PLAYER_MESSAGE: RemovePlayerMessage_pb2.removePlayerMessage,
    ProtocolMessage.SEND_COMMAND_MESSAGE: SendCommandMessage_pb2.sendCommandMessage,
    ProtocolMessage.SEND_COMMAND_RESULT_MESSAGE: SendCommandResultMessage_pb2.sendCommandResultMessage,
    ProtocolMessage.SEND_HID_EVENT_MESSAGE: SendHIDEventMessage_pb2.sendHIDEventMessage,
    ProtocolMessage.SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE: SendPackedVirtualTouchEventMessage_pb2.sendPackedVirtualTouchEventMessage,
    ProtocolMessage.SEND_VOICE_INPUT_MESSAGE: SendVoiceInputMessage_pb2.sendVoiceInputMessage,
    ProtocolMessage.SET_ARTWORK_MESSAGE: SetArtworkMessage_pb2.setArtworkMessage,
    ProtocolMessage.SET_CONNECTION_STATE_MESSAGE: SetConnectionStateMessage_pb2.setConnectionStateMessage,
    ProtocolMessage.SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE: SetDefaultSupportedCommandsMessage_pb2.setDefaultSupportedCommandsMessage,
    ProtocolMessage.SET_HILITE_MODE_MESSAGE: SetHiliteModeMessage_pb2.setHiliteModeMessage,
    ProtocolMessage.SET_NOW_PLAYING_CLIENT_MESSAGE: SetNowPlayingClientMessage_pb2.setNowPlayingClientMessage,
    ProtocolMessage.SET_RECORDING_STATE_MESSAGE: SetRecordingStateMessage_pb2.setRecordingStateMessage,
    ProtocolMessage.SET_STATE_MESSAGE: SetStateMessage_pb2.setStateMessage,
    ProtocolMessage.TEXT_INPUT_MESSAGE: TextInputMessage_pb2.textInputMessage,
    ProtocolMessage.TRANSACTION_MESSAGE: TransactionMessage_pb2.transactionMessage,
    ProtocolMessage.UPDATE_CLIENT_MESSAGE: UpdateClientMessage_pb2.updateClientMessage,
    ProtocolMessage.UPDATE_CONTENT_ITEM_MESSAGE: UpdateContentItemMessage_pb2.updateContentItemMessage,
    ProtocolMessage.UPDATE_OUTPUT_DEVICE_MESSAGE: UpdateOutputDeviceMessage_pb2.updateOutputDeviceMessage,
    ProtocolMessage.VOLUME_CONTROL_AVAILABILITY_MESSAGE: VolumeControlAvailabilityMessage_pb2.volumeControlAvailabilityMessage,
    ProtocolMessage.WAKE_DEVICE_MESSAGE: WakeDeviceMessage_pb2.wakeDeviceMessage,
}


CLIENT_UPDATES_CONFIG_MESSAGE = ProtocolMessage.CLIENT_UPDATES_CONFIG_MESSAGE
CRYPTO_PAIRING_MESSAGE = ProtocolMessage.CRYPTO_PAIRING_MESSAGE
DEVICE_INFO_MESSAGE = ProtocolMessage.DEVICE_INFO_MESSAGE
DEVICE_INFO_UPDATE_MESSAGE = ProtocolMessage.DEVICE_INFO_UPDATE_MESSAGE
GET_KEYBOARD_SESSION_MESSAGE = ProtocolMessage.GET_KEYBOARD_SESSION_MESSAGE
KEYBOARD_MESSAGE = ProtocolMessage.KEYBOARD_MESSAGE
NOTIFICATION_MESSAGE = ProtocolMessage.NOTIFICATION_MESSAGE
PLAYBACK_QUEUE_REQUEST_MESSAGE = ProtocolMessage.PLAYBACK_QUEUE_REQUEST_MESSAGE
REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE = ProtocolMessage.REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE
REGISTER_HID_DEVICE_MESSAGE = ProtocolMessage.REGISTER_HID_DEVICE_MESSAGE
REGISTER_HID_DEVICE_RESULT_MESSAGE = ProtocolMessage.REGISTER_HID_DEVICE_RESULT_MESSAGE
REGISTER_VOICE_INPUT_DEVICE_MESSAGE = ProtocolMessage.REGISTER_VOICE_INPUT_DEVICE_MESSAGE
REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE = ProtocolMessage.REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE
REMOVE_CLIENT_MESSAGE = ProtocolMessage.REMOVE_CLIENT_MESSAGE
REMOVE_PLAYER_MESSAGE = ProtocolMessage.REMOVE_PLAYER_MESSAGE
SEND_COMMAND_MESSAGE = ProtocolMessage.SEND_COMMAND_MESSAGE
SEND_COMMAND_RESULT_MESSAGE = ProtocolMessage.SEND_COMMAND_RESULT_MESSAGE
SEND_HID_EVENT_MESSAGE = ProtocolMessage.SEND_HID_EVENT_MESSAGE
SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE = ProtocolMessage.SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE
SEND_VOICE_INPUT_MESSAGE = ProtocolMessage.SEND_VOICE_INPUT_MESSAGE
SET_ARTWORK_MESSAGE = ProtocolMessage.SET_ARTWORK_MESSAGE
SET_CONNECTION_STATE_MESSAGE = ProtocolMessage.SET_CONNECTION_STATE_MESSAGE
SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE = ProtocolMessage.SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE
SET_HILITE_MODE_MESSAGE = ProtocolMessage.SET_HILITE_MODE_MESSAGE
SET_NOW_PLAYING_CLIENT_MESSAGE = ProtocolMessage.SET_NOW_PLAYING_CLIENT_MESSAGE
SET_RECORDING_STATE_MESSAGE = ProtocolMessage.SET_RECORDING_STATE_MESSAGE
SET_STATE_MESSAGE = ProtocolMessage.SET_STATE_MESSAGE
TEXT_INPUT_MESSAGE = ProtocolMessage.TEXT_INPUT_MESSAGE
TRANSACTION_MESSAGE = ProtocolMessage.TRANSACTION_MESSAGE
UPDATE_CLIENT_MESSAGE = ProtocolMessage.UPDATE_CLIENT_MESSAGE
UPDATE_CONTENT_ITEM_MESSAGE = ProtocolMessage.UPDATE_CONTENT_ITEM_MESSAGE
UPDATE_OUTPUT_DEVICE_MESSAGE = ProtocolMessage.UPDATE_OUTPUT_DEVICE_MESSAGE
VOLUME_CONTROL_AVAILABILITY_MESSAGE = ProtocolMessage.VOLUME_CONTROL_AVAILABILITY_MESSAGE
WAKE_DEVICE_MESSAGE = ProtocolMessage.WAKE_DEVICE_MESSAGE


def _inner_message(self):
    extension = _EXTENSION_LOOKUP.get(self.type, None)
    if extension:
        return self.Extensions[extension]

    raise Exception('unknown type: ' + str(self.type))


ProtocolMessage.inner = _inner_message  # type: ignore
