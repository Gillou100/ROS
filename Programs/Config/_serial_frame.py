#!/usr/bin/env python3
# -*-coding:utf-8 -*


# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from hexapod/serial_frame.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct
from geometry_msgs.msg import Twist


class serial_frame(genpy.Message):
  _md5sum = "25ec212357fb08bcc6002a027d282e2d"
  _type = "hexapod/serial_frame"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint8 header_byte
uint8 right_v_byte
uint8 right_h_byte
uint8 left_v_byte
uint8 left_h_byte
uint8 button_byte
uint8 end_byte
uint8 checksum_byte
"""
  __slots__ = ['header_byte','right_v_byte','right_h_byte','left_v_byte','left_h_byte','button_byte','end_byte','checksum_byte']
  _slot_types = ['uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header_byte,right_v_byte,right_h_byte,left_v_byte,left_h_byte,button_byte,end_byte,checksum_byte

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(serial_frame, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header_byte is None:
        self.header_byte = 0
      if self.right_v_byte is None:
        self.right_v_byte = 0
      if self.right_h_byte is None:
        self.right_h_byte = 0
      if self.left_v_byte is None:
        self.left_v_byte = 0
      if self.left_h_byte is None:
        self.left_h_byte = 0
      if self.button_byte is None:
        self.button_byte = 0
      if self.end_byte is None:
        self.end_byte = 0
      if self.checksum_byte is None:
        self.checksum_byte = 0
    else:
      self.header_byte = 0
      self.right_v_byte = 0
      self.right_h_byte = 0
      self.left_v_byte = 0
      self.left_h_byte = 0
      self.button_byte = 0
      self.end_byte = 0
      self.checksum_byte = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_8B().pack(_x.header_byte, _x.right_v_byte, _x.right_h_byte, _x.left_v_byte, _x.left_h_byte, _x.button_byte, _x.end_byte, _x.checksum_byte))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.header_byte, _x.right_v_byte, _x.right_h_byte, _x.left_v_byte, _x.left_h_byte, _x.button_byte, _x.end_byte, _x.checksum_byte,) = _get_struct_8B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_8B().pack(_x.header_byte, _x.right_v_byte, _x.right_h_byte, _x.left_v_byte, _x.left_h_byte, _x.button_byte, _x.end_byte, _x.checksum_byte))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.header_byte, _x.right_v_byte, _x.right_h_byte, _x.left_v_byte, _x.left_h_byte, _x.button_byte, _x.end_byte, _x.checksum_byte,) = _get_struct_8B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_8B = None
def _get_struct_8B():
    global _struct_8B
    if _struct_8B is None:
        _struct_8B = struct.Struct("<8B")
    return _struct_8B


if __name__ == '__main__':
	pass