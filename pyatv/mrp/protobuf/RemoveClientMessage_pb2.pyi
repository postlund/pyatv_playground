# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FieldDescriptor as google___protobuf___descriptor___FieldDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.NowPlayingClient_pb2 import (
    NowPlayingClient as pyatv___mrp___protobuf___NowPlayingClient_pb2___NowPlayingClient,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class RemoveClientMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def client(self) -> pyatv___mrp___protobuf___NowPlayingClient_pb2___NowPlayingClient: ...

    def __init__(self,
        *,
        client : typing___Optional[pyatv___mrp___protobuf___NowPlayingClient_pb2___NowPlayingClient] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"client",b"client"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"client",b"client"]) -> None: ...
type___RemoveClientMessage = RemoveClientMessage

removeClientMessage: google___protobuf___descriptor___FieldDescriptor = ...