# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class Published(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsPublished(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Published()
        x.Init(buf, n + offset)
        return x

    # Published
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Published
    def Request(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Published
    def Publication(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def PublishedStart(builder): builder.StartObject(2)
def PublishedAddRequest(builder, request): builder.PrependUint64Slot(0, request, 0)
def PublishedAddPublication(builder, publication): builder.PrependUint64Slot(1, publication, 0)
def PublishedEnd(builder): return builder.EndObject()
