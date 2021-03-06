# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/ProtocolMessage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/ProtocolMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n(pyatv/mrp/protobuf/ProtocolMessage.proto\"\xa5&\n\x0fProtocolMessage\x12#\n\x04type\x18\x01 \x01(\x0e\x32\x15.ProtocolMessage.Type\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x1b\n\x13\x61uthenticationToken\x18\x03 \x01(\t\x12-\n\terrorCode\x18\x04 \x01(\x0e\x32\x1a.ProtocolMessage.ErrorCode\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\"\xae\x17\n\tErrorCode\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x15\n\x11INVALID_OPERATION\x10\x02\x12\x1b\n\x17OPERATION_NOT_PERMITTED\x10\x03\x12\x19\n\x15\x43LIENT_DOES_NOT_EXIST\x10\x04\x12\x19\n\x15ORIGIN_DOES_NOT_EXIST\x10\x05\x12\x19\n\x15UNSUPPORTED_OPERATION\x10\x06\x12\x1e\n\x1a\x46\x41ILED_TO_SET_PICKED_ROUTE\x10\x07\x12$\n FAILED_TO_REGISTER_CUSTOM_ORIGIN\x10\x08\x12\"\n\x1e\x46\x41ILED_TO_REMOVE_CUSTOM_ORIGIN\x10\t\x12+\n\'THE_APPLICATION_ACTIVITY_DOES_NOT_EXIST\x10\n\x12\x36\n2THE_APP_HAS_NOT_SETUP_A_BROWSABLE_CONTENT_ENDPOINT\x10\x0b\x12K\nGTHE_REQUESTED_BROWSABLE_CONTENT_API_IS_NOT_SUPPORTED_BY_THE_APPLICATION\x10\x0c\x12:\n6THE_NOTFICATION_HAS_NOT_BEEN_WHITELISTED_BY_THE_SERVER\x10\r\x12@\n<OPERATION_REQUIRES_A_CLIENT_CALLBACK_TO_HAVE_BEEN_REGISTERED\x10\x0e\x12\x43\n?OPERATION_REQUIRES_A_CLIENT_DATA_SOURCE_TO_HAVE_BEEN_REGISTERED\x10\x0f\x12?\n;REQUESTED_DATA_IS_OUT_OF_DATE_AND_SHOULD_BE_REQUESTED_AGAIN\x10\x10\x12\x37\n3THE_DEVICES_ENFORCED_VOLUME_LIMIT_HAS_BEEN_EXCEEDED\x10\x11\x12 \n\x1cVOLUME_VALUE_IS_OUT_OF_RANGE\x10\x12\x12*\n&VOLUME_IS_ALREADY_AT_THE_MAXIMUM_VALUE\x10\x13\x12\x1b\n\x17VOLUME_IS_ALREADY_MUTED\x10\x14\x12\'\n#VOICE_INPUT_ENDPOINT_DOES_NOT_EXIST\x10\x15\x12>\n:THE_VOICE_INPUT_DEVICE_IS_NOT_REGISTERED_OR_DOES_NOT_EXIST\x10\x16\x12\x16\n\x12\x45NCRYPTION_FAILURE\x10\x17\x12\x1b\n\x17\x45NDPOINT_DOES_NOT_EXIST\x10\x18\x12\x33\n/THE_CLIENTS_APPLICATION_CANCELLED_THE_OPERATION\x10\x19\x12\x1b\n\x17THE_OPERATION_TIMED_OUT\x10\x1a\x12\x30\n,THE_SPECIFIED_PLAYER_PATH_OBJECT_WAS_INVALID\x10\x1b\x12\x44\n@ADDING_OR_REMOVING_DEVICES_FROM_THE_AV_OUTPUT_CONTEXT_HAS_FAILED\x10\x1c\x12\x33\n/COULD_NOT_FIND_THE_SPECIFIED_NOW_PLAYING_PLAYER\x10\x1d\x12-\n)THE_SPECIFIED_CONTENT_ITEM_DOES_NOT_EXIST\x10\x1e\x12#\n\x1fTHE_SPECIFIED_OFFSET_IS_INVALID\x10\x1f\x12+\n\'THE_SPECIFIED_OUTPUT_CONTEXT_IS_INVALID\x10 \x12:\n6ONE_OR_MORE_SPECIFIED_OUTPUT_DEVICES_ARE_NOT_GROUPABLE\x10!\x12T\nPTHE_SPECIFIED_OUTPUT_CONTEXT_DOES_NOT_SUPPORT_ADDING_MORE_THAN_ONE_OUTPUT_DEVICE\x10\"\x12\x33\n/COULD_NOT_FIND_THE_SPECIFIED_NOW_PLAYING_CLIENT\x10#\x12]\nYENDPOINT_VOLUME_CONTROL_IS_ONLY_POSSIBLE_IF_THE_ENDPOINT_IS_PICKED_OR_REMOTE_CONTROLLABLE\x10$\x12\x62\n^OUTPUT_DEVICE_VOLUME_CONTROL_IS_ONLY_POSSIBLE_IF_THE_ENDPOINT_IS_PICKED_OR_REMOTE_CONTROLLABLE\x10%\x12\'\n#CODER_MUST_SUPPORT_KEY_VALUE_CODING\x10&\x12)\n%COULD_NOT_FIND_THE_GIVEN_OUTPUTDEVICE\x10\'\x12&\n\"FAILED_TO_CONNECT_TO_REMOTE_DEVICE\x10\x64\x12#\n\x1f\x41UTHENTICATION_TOKEN_IS_INVALID\x10\x65\x12;\n7RECORDING_SESSION_IS_ALREADY_IN_PROGRESS_ON_THIS_DEVICE\x10\x66\x12)\n%THE_DEVICE_IS_NOT_CURRENTLY_RECORDING\x10g\x12\x1f\n\x1bTHE_CLIENT_HAS_DISCONNECTED\x10h\x12\x1f\n\x1bTHE_SERVER_HAS_DISCONNECTED\x10i\x12\x33\n/THE_CONNECTION_HAS_BEEN_CANCELLED_BY_THE_CLIENT\x10j\x12;\n7PAIRING_FUNCTIONALITY_IS_LOCKED_DUE_TO_SECURITY_REASONS\x10k\x12\x33\n/THE_CLIENTS_OPERATING_SYSTEM_VERSION_IS_TOO_OLD\x10l\x12.\n*THE_CLIENTS_APPLICATION_VERSION_IS_TOO_OLD\x10m\x12\x1c\n\x18THE_DEVICE_IS_NOT_PAIRED\x10n\x12J\nFTHE_PIN_PAIRING_DIALOG_WAS_REMOVED_BY_THE_USER_BEFORE_PAIRING_OCCOURED\x10o\x12K\nGTHE_PIN_PAIRING_DIALOG_WAS_REMOVED_BY_A_TIMEOUT_BEFORE_PAIRING_OCCOURED\x10p\x12\x1b\n\x17THE_CONNECTION_TIMEDOUT\x10q\x12\'\n#PAIRING_WITH_THIS_DEVICE_IS_BLOCKED\x10r\x12 \n\x1cTHE_DEVICE_IS_GOING_TO_SLEEP\x10s\x12 \n\x1c\x43ONNECTION_BLOCKED_BY_SERVER\x10t\x12\x44\n@MRAVENDPOINT_WAS_DEALLOCATED_WHILE_WAITING_FOR_DEVICE_TO_CONNECT\x10u\x12U\nPOUTPUT_CONTEXT_MODIFICATION_CAUSED_A_DEVICE_TO_NO_LONGER_BE_A_PROXY_GROUP_PLAYER\x10\xc8\x01\x12O\nJOUTPUT_CONTEXT_MODIFICATION_CAUSED_A_DEVICE_TO_BECOME_A_PROXY_GROUP_PLAYER\x10\xc9\x01\x12=\n8OUTPUT_CONTEXT_MODIFICATION_REQUESTED_NO_TOPOLOGY_CHANGE\x10\xca\x01\x12\x12\n\rUNKNOWN_ERROR\x10\xab\x02\"\xbe\r\n\x04Type\x12\x13\n\x0fUNKNOWN_MESSAGE\x10\x00\x12\x18\n\x14SEND_COMMAND_MESSAGE\x10\x01\x12\x1f\n\x1bSEND_COMMAND_RESULT_MESSAGE\x10\x02\x12\x15\n\x11GET_STATE_MESSAGE\x10\x03\x12\x15\n\x11SET_STATE_MESSAGE\x10\x04\x12\x17\n\x13SET_ARTWORK_MESSAGE\x10\x05\x12\x1f\n\x1bREGISTER_HID_DEVICE_MESSAGE\x10\x06\x12&\n\"REGISTER_HID_DEVICE_RESULT_MESSAGE\x10\x07\x12\x1a\n\x16SEND_HID_EVENT_MESSAGE\x10\x08\x12\x1b\n\x17SEND_HID_REPORT_MESSAGE\x10\t\x12$\n SEND_VIRTUAL_TOUCH_EVENT_MESSAGE\x10\n\x12\x18\n\x14NOTIFICATION_MESSAGE\x10\x0b\x12.\n*CONTENT_ITEMS_CHANGED_NOTIFICATION_MESSAGE\x10\x0c\x12\x17\n\x13\x44\x45VICE_INFO_MESSAGE\x10\x0f\x12!\n\x1d\x43LIENT_UPDATES_CONFIG_MESSAGE\x10\x10\x12\'\n#VOLUME_CONTROL_AVAILABILITY_MESSAGE\x10\x11\x12\x1b\n\x17GAME_CONTROLLER_MESSAGE\x10\x12\x12$\n REGISTER_GAME_CONTROLLER_MESSAGE\x10\x13\x12-\n)REGISTER_GAME_CONTROLLER_RESPONSE_MESSAGE\x10\x14\x12&\n\"UNREGISTER_GAME_CONTROLLER_MESSAGE\x10\x15\x12/\n+REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE\x10\x16\x12\x14\n\x10KEYBOARD_MESSAGE\x10\x17\x12 \n\x1cGET_KEYBOARD_SESSION_MESSAGE\x10\x18\x12\x16\n\x12TEXT_INPUT_MESSAGE\x10\x19\x12#\n\x1fGET_VOICE_INPUT_DEVICES_MESSAGE\x10\x1a\x12,\n(GET_VOICE_INPUT_DEVICES_RESPONSE_MESSAGE\x10\x1b\x12\'\n#REGISTER_VOICE_INPUT_DEVICE_MESSAGE\x10\x1c\x12\x30\n,REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE\x10\x1d\x12\x1f\n\x1bSET_RECORDING_STATE_MESSAGE\x10\x1e\x12\x1c\n\x18SEND_VOICE_INPUT_MESSAGE\x10\x1f\x12\"\n\x1ePLAYBACK_QUEUE_REQUEST_MESSAGE\x10 \x12\x17\n\x13TRANSACTION_MESSAGE\x10!\x12\x1a\n\x16\x43RYPTO_PAIRING_MESSAGE\x10\"\x12&\n\"GAME_CONTROLLER_PROPERTIES_MESSAGE\x10#\x12\x1b\n\x17SET_READY_STATE_MESSAGE\x10$\x12\x1e\n\x1a\x44\x45VICE_INFO_UPDATE_MESSAGE\x10%\x12 \n\x1cSET_CONNECTION_STATE_MESSAGE\x10&\x12\x15\n\x11SEND_BUTTON_EVENT\x10\'\x12\x1b\n\x17SET_HILITE_MODE_MESSAGE\x10(\x12\x17\n\x13WAKE_DEVICE_MESSAGE\x10)\x12\x13\n\x0fGENERIC_MESSAGE\x10*\x12+\n\'SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE\x10+\x12\x15\n\x11SEND_LYRICS_EVENT\x10,\x12\"\n\x1eSET_NOW_PLAYING_CLIENT_MESSAGE\x10.\x12\"\n\x1eSET_NOT_PLAYING_PLAYER_MESSAGE\x10/\x12\x19\n\x15REMOVE_CLIENT_MESSAGE\x10\x35\x12\x19\n\x15REMOVE_PLAYER_MESSAGE\x10\x36\x12\x19\n\x15UPDATE_CLIENT_MESSAGE\x10\x37\x12\x1f\n\x1bUPDATE_CONTENT_ITEM_MESSAGE\x10\x38\x12\x32\n.VOLUME_CONTROL_CAPABILITIES_DID_CHANGE_MESSAGE\x10@\x12 \n\x1cUPDATE_OUTPUT_DEVICE_MESSAGE\x10\x41\x12*\n&SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE\x10H*\x08\x08\x06\x10\x80\x80\x80\x80\x02'
)



_PROTOCOLMESSAGE_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='ProtocolMessage.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_OPERATION', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_NOT_PERMITTED', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_DOES_NOT_EXIST', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORIGIN_DOES_NOT_EXIST', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_OPERATION', index=5, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_TO_SET_PICKED_ROUTE', index=6, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_TO_REGISTER_CUSTOM_ORIGIN', index=7, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_TO_REMOVE_CUSTOM_ORIGIN', index=8, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_APPLICATION_ACTIVITY_DOES_NOT_EXIST', index=9, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_APP_HAS_NOT_SETUP_A_BROWSABLE_CONTENT_ENDPOINT', index=10, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_REQUESTED_BROWSABLE_CONTENT_API_IS_NOT_SUPPORTED_BY_THE_APPLICATION', index=11, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_NOTFICATION_HAS_NOT_BEEN_WHITELISTED_BY_THE_SERVER', index=12, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_REQUIRES_A_CLIENT_CALLBACK_TO_HAVE_BEEN_REGISTERED', index=13, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATION_REQUIRES_A_CLIENT_DATA_SOURCE_TO_HAVE_BEEN_REGISTERED', index=14, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUESTED_DATA_IS_OUT_OF_DATE_AND_SHOULD_BE_REQUESTED_AGAIN', index=15, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_DEVICES_ENFORCED_VOLUME_LIMIT_HAS_BEEN_EXCEEDED', index=16, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_VALUE_IS_OUT_OF_RANGE', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_IS_ALREADY_AT_THE_MAXIMUM_VALUE', index=18, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_IS_ALREADY_MUTED', index=19, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOICE_INPUT_ENDPOINT_DOES_NOT_EXIST', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_VOICE_INPUT_DEVICE_IS_NOT_REGISTERED_OR_DOES_NOT_EXIST', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCRYPTION_FAILURE', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_DOES_NOT_EXIST', index=23, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CLIENTS_APPLICATION_CANCELLED_THE_OPERATION', index=24, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_OPERATION_TIMED_OUT', index=25, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SPECIFIED_PLAYER_PATH_OBJECT_WAS_INVALID', index=26, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDING_OR_REMOVING_DEVICES_FROM_THE_AV_OUTPUT_CONTEXT_HAS_FAILED', index=27, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COULD_NOT_FIND_THE_SPECIFIED_NOW_PLAYING_PLAYER', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SPECIFIED_CONTENT_ITEM_DOES_NOT_EXIST', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SPECIFIED_OFFSET_IS_INVALID', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SPECIFIED_OUTPUT_CONTEXT_IS_INVALID', index=31, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_OR_MORE_SPECIFIED_OUTPUT_DEVICES_ARE_NOT_GROUPABLE', index=32, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SPECIFIED_OUTPUT_CONTEXT_DOES_NOT_SUPPORT_ADDING_MORE_THAN_ONE_OUTPUT_DEVICE', index=33, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COULD_NOT_FIND_THE_SPECIFIED_NOW_PLAYING_CLIENT', index=34, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDPOINT_VOLUME_CONTROL_IS_ONLY_POSSIBLE_IF_THE_ENDPOINT_IS_PICKED_OR_REMOTE_CONTROLLABLE', index=35, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_DEVICE_VOLUME_CONTROL_IS_ONLY_POSSIBLE_IF_THE_ENDPOINT_IS_PICKED_OR_REMOTE_CONTROLLABLE', index=36, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CODER_MUST_SUPPORT_KEY_VALUE_CODING', index=37, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COULD_NOT_FIND_THE_GIVEN_OUTPUTDEVICE', index=38, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_TO_CONNECT_TO_REMOTE_DEVICE', index=39, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHENTICATION_TOKEN_IS_INVALID', index=40, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECORDING_SESSION_IS_ALREADY_IN_PROGRESS_ON_THIS_DEVICE', index=41, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_DEVICE_IS_NOT_CURRENTLY_RECORDING', index=42, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CLIENT_HAS_DISCONNECTED', index=43, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_SERVER_HAS_DISCONNECTED', index=44, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CONNECTION_HAS_BEEN_CANCELLED_BY_THE_CLIENT', index=45, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAIRING_FUNCTIONALITY_IS_LOCKED_DUE_TO_SECURITY_REASONS', index=46, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CLIENTS_OPERATING_SYSTEM_VERSION_IS_TOO_OLD', index=47, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CLIENTS_APPLICATION_VERSION_IS_TOO_OLD', index=48, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_DEVICE_IS_NOT_PAIRED', index=49, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_PIN_PAIRING_DIALOG_WAS_REMOVED_BY_THE_USER_BEFORE_PAIRING_OCCOURED', index=50, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_PIN_PAIRING_DIALOG_WAS_REMOVED_BY_A_TIMEOUT_BEFORE_PAIRING_OCCOURED', index=51, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_CONNECTION_TIMEDOUT', index=52, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAIRING_WITH_THIS_DEVICE_IS_BLOCKED', index=53, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THE_DEVICE_IS_GOING_TO_SLEEP', index=54, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECTION_BLOCKED_BY_SERVER', index=55, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MRAVENDPOINT_WAS_DEALLOCATED_WHILE_WAITING_FOR_DEVICE_TO_CONNECT', index=56, number=117,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_CONTEXT_MODIFICATION_CAUSED_A_DEVICE_TO_NO_LONGER_BE_A_PROXY_GROUP_PLAYER', index=57, number=200,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_CONTEXT_MODIFICATION_CAUSED_A_DEVICE_TO_BECOME_A_PROXY_GROUP_PLAYER', index=58, number=201,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT_CONTEXT_MODIFICATION_REQUESTED_NO_TOPOLOGY_CHANGE', index=59, number=202,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ERROR', index=60, number=299,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=217,
  serialized_end=3207,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOLMESSAGE_ERRORCODE)

_PROTOCOLMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ProtocolMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_MESSAGE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_COMMAND_MESSAGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_COMMAND_RESULT_MESSAGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_STATE_MESSAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_STATE_MESSAGE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_ARTWORK_MESSAGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_HID_DEVICE_MESSAGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_HID_DEVICE_RESULT_MESSAGE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_HID_EVENT_MESSAGE', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_HID_REPORT_MESSAGE', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_VIRTUAL_TOUCH_EVENT_MESSAGE', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION_MESSAGE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT_ITEMS_CHANGED_NOTIFICATION_MESSAGE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_INFO_MESSAGE', index=13, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_UPDATES_CONFIG_MESSAGE', index=14, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_CONTROL_AVAILABILITY_MESSAGE', index=15, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_CONTROLLER_MESSAGE', index=16, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_GAME_CONTROLLER_MESSAGE', index=17, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_GAME_CONTROLLER_RESPONSE_MESSAGE', index=18, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER_GAME_CONTROLLER_MESSAGE', index=19, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_FOR_GAME_CONTROLLER_EVENTS_MESSAGE', index=20, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYBOARD_MESSAGE', index=21, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_KEYBOARD_SESSION_MESSAGE', index=22, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_INPUT_MESSAGE', index=23, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VOICE_INPUT_DEVICES_MESSAGE', index=24, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_VOICE_INPUT_DEVICES_RESPONSE_MESSAGE', index=25, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_VOICE_INPUT_DEVICE_MESSAGE', index=26, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_VOICE_INPUT_DEVICE_RESPONSE_MESSAGE', index=27, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_RECORDING_STATE_MESSAGE', index=28, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_VOICE_INPUT_MESSAGE', index=29, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYBACK_QUEUE_REQUEST_MESSAGE', index=30, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTION_MESSAGE', index=31, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRYPTO_PAIRING_MESSAGE', index=32, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAME_CONTROLLER_PROPERTIES_MESSAGE', index=33, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_READY_STATE_MESSAGE', index=34, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_INFO_UPDATE_MESSAGE', index=35, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_CONNECTION_STATE_MESSAGE', index=36, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_BUTTON_EVENT', index=37, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_HILITE_MODE_MESSAGE', index=38, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAKE_DEVICE_MESSAGE', index=39, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_MESSAGE', index=40, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_PACKED_VIRTUAL_TOUCH_EVENT_MESSAGE', index=41, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEND_LYRICS_EVENT', index=42, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_NOW_PLAYING_CLIENT_MESSAGE', index=43, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_NOT_PLAYING_PLAYER_MESSAGE', index=44, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_CLIENT_MESSAGE', index=45, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_PLAYER_MESSAGE', index=46, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_CLIENT_MESSAGE', index=47, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_CONTENT_ITEM_MESSAGE', index=48, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_CONTROL_CAPABILITIES_DID_CHANGE_MESSAGE', index=49, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_OUTPUT_DEVICE_MESSAGE', index=50, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_DEFAULT_SUPPORTED_COMMANDS_MESSAGE', index=51, number=72,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3210,
  serialized_end=4936,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOLMESSAGE_TYPE)


_PROTOCOLMESSAGE = _descriptor.Descriptor(
  name='ProtocolMessage',
  full_name='ProtocolMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ProtocolMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='ProtocolMessage.identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authenticationToken', full_name='ProtocolMessage.authenticationToken', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='ProtocolMessage.errorCode', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ProtocolMessage.timestamp', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROTOCOLMESSAGE_ERRORCODE,
    _PROTOCOLMESSAGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(6, 536870912), ],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=4946,
)

_PROTOCOLMESSAGE.fields_by_name['type'].enum_type = _PROTOCOLMESSAGE_TYPE
_PROTOCOLMESSAGE.fields_by_name['errorCode'].enum_type = _PROTOCOLMESSAGE_ERRORCODE
_PROTOCOLMESSAGE_ERRORCODE.containing_type = _PROTOCOLMESSAGE
_PROTOCOLMESSAGE_TYPE.containing_type = _PROTOCOLMESSAGE
DESCRIPTOR.message_types_by_name['ProtocolMessage'] = _PROTOCOLMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtocolMessage = _reflection.GeneratedProtocolMessageType('ProtocolMessage', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLMESSAGE,
  '__module__' : 'pyatv.mrp.protobuf.ProtocolMessage_pb2'
  # @@protoc_insertion_point(class_scope:ProtocolMessage)
  })
_sym_db.RegisterMessage(ProtocolMessage)


# @@protoc_insertion_point(module_scope)
