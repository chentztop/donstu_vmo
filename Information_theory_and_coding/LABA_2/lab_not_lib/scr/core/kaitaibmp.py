# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))


class Bmp(KaitaiStruct):
    """The **BMP file format**, also known as **bitmap image file** or **device independent
    bitmap (DIB) file format** or simply a **bitmap**, is a raster graphics image file
    format used to store bitmap digital images, independently of the display
    device (such as a graphics adapter), especially on Microsoft Windows
    and OS/2 operating systems.

    ## Samples

    Great collection of various BMP sample files:
    [**BMP Suite Image List**](
      http://entropymine.com/jason/bmpsuite/bmpsuite/html/bmpsuite.html
    ) (by Jason Summers)

    If only there was such a comprehensive sample suite for every file format! It's like
    a dream for every developer of any binary file format parser. It contains a lot of
    different types and variations of BMP files, even the tricky ones, where it's not clear
    from the specification how to deal with them (marked there as "**q**uestionable").

    If you make a program which will be able to read all the "**g**ood" and "**q**uestionable"
    BMP files and won't crash on the "**b**ad" ones, it will definitely have one of the most
    extensive support of BMP files in the universe!

    ## BITMAPV2INFOHEADER and BITMAPV3INFOHEADER

    A beneficial discussion on Adobe forum (archived):
    [**Invalid BMP Format with Alpha channel**](
      https://web.archive.org/web/20150127132443/https://forums.adobe.com/message/3272950
    )

    In 2010, someone noticed that Photoshop generated BMP with an odd type of header. There wasn't
    any documentation available for this header at the time (and still isn't).
    However, Chris Cox (former Adobe employee) claimed that they hadn't invented any type
    of proprietary header and everything they were writing was taken directly
    from the Microsoft documentation.

    It showed up that the unknown header was called BITMAPV3INFOHEADER.
    Although Microsoft has apparently requested and verified the use of the header,
    the documentation on MSDN has probably got lost and they have probably
    forgotten about this type of header.

    This is the only source I could find about these structures, so we could't rely
    on it so much, but I think supporting them as a read-only format won't harm anything.
    Due to the fact that it isn't documented anywhere else, most applications don't support it.

    All Windows headers at once (including mentioned BITMAPV2INFOHEADER and BITMAPV3INFOHEADER):

    ![Bitmap headers overview](
      https://web.archive.org/web/20190527043845/https://forums.adobe.com/servlet/JiveServlet/showImage/2-3273299-47801/BMP_Headers.png
    )

    ## Specs
     * [Bitmap Storage (Windows Dev Center)](
         https://learn.microsoft.com/en-us/windows/win32/gdi/bitmap-storage
       )
        * BITMAPFILEHEADER
        * BITMAPINFOHEADER
        * BITMAPV4HEADER
        * BITMAPV5HEADER
     * [OS/2 Bitmap File Format](
          https://www.fileformat.info/format/os2bmp/egff.htm
       )
        * BITMAPFILEHEADER (OS2BMPFILEHEADER)
        * BITMAPCOREHEADER (OS21XBITMAPHEADER)
        * OS22XBITMAPHEADER
     * [Microsoft Windows Bitmap](
          http://netghost.narod.ru/gff/graphics/summary/micbmp.htm
       )
        * BITMAPFILEHEADER (WINBMPFILEHEADER)
        * BITMAPCOREHEADER (WIN2XBITMAPHEADER)
        * BITMAPINFOHEADER (WINNTBITMAPHEADER)
        * BITMAPV4HEADER (WIN4XBITMAPHEADER)
    """

    class Intent(Enum):
        business = 1
        graphics = 2
        images = 4
        abs_colorimetric = 8

    class ColorSpace(Enum):
        calibrated_rgb = 0
        profile_linked = 1279872587
        profile_embedded = 1296188740
        windows = 1466527264
        s_rgb = 1934772034

    class Os2Rendering(Enum):
        no_halftoning = 0
        error_diffusion = 1
        panda = 2
        super_circle = 3

    class HeaderType(Enum):
        bitmap_core_header = 12
        bitmap_info_header = 40
        bitmap_v2_info_header = 52
        bitmap_v3_info_header = 56
        os2_2x_bitmap_header = 64
        bitmap_v4_header = 108
        bitmap_v5_header = 124

    class Compressions(Enum):
        rgb = 0
        rle8 = 1
        rle4 = 2
        bitfields = 3
        jpeg = 4
        png = 5
        alpha_bitfields = 6

    class Os2Compressions(Enum):
        rgb = 0
        rle8 = 1
        rle4 = 2
        huffman_1d = 3
        rle24 = 4

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.file_hdr = Bmp.FileHeader(self._io, self, self._root)
        self._raw_dib_info = self._io.read_bytes((self.file_hdr.ofs_bitmap - 14))
        _io__raw_dib_info = KaitaiStream(BytesIO(self._raw_dib_info))
        self.dib_info = Bmp.BitmapInfo(_io__raw_dib_info, self, self._root)
        self._raw_bitmap = self._io.read_bytes_full()
        _io__raw_bitmap = KaitaiStream(BytesIO(self._raw_bitmap))
        self.bitmap = Bmp.Bitmap(_io__raw_bitmap, self, self._root)

    class CieXyz(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-ciexyz
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = Bmp.FixedPoint2Dot30(self._io, self, self._root)
            self.y = Bmp.FixedPoint2Dot30(self._io, self, self._root)
            self.z = Bmp.FixedPoint2Dot30(self._io, self, self._root)

    class RgbRecord(KaitaiStruct):
        def __init__(self, has_reserved_field, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.has_reserved_field = has_reserved_field
            self._read()

        def _read(self):
            self.blue = self._io.read_u1()
            self.green = self._io.read_u1()
            self.red = self._io.read_u1()
            if self.has_reserved_field:
                self.reserved = self._io.read_u1()

    class BitmapV5Extension(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapv5header
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.intent = KaitaiStream.resolve_enum(Bmp.Intent, self._io.read_u4le())
            self.ofs_profile = self._io.read_u4le()
            self.len_profile = self._io.read_u4le()
            self.reserved = self._io.read_u4le()

        @property
        def has_profile(self):
            if hasattr(self, '_m_has_profile'):
                return self._m_has_profile

            self._m_has_profile = ((self._parent.bitmap_v4_ext.color_space_type == Bmp.ColorSpace.profile_linked) or (
                        self._parent.bitmap_v4_ext.color_space_type == Bmp.ColorSpace.profile_embedded))
            return getattr(self, '_m_has_profile', None)

        @property
        def profile_data(self):
            """
            .. seealso::
               "If the profile is embedded, profile data is the actual profile, and if it is linked, the profile data is the null-terminated file name of the profile. This cannot be a Unicode string. It must be composed exclusively of characters from the Windows character set (code page 1252)." - https://learn.microsoft.com/en-us/windows/win32/wcs/using-structures-in-wcs-1-0
            """
            if hasattr(self, '_m_profile_data'):
                return self._m_profile_data

            if self.has_profile:
                io = self._root._io
                _pos = io.pos()
                io.seek((14 + self.ofs_profile))
                _on = self._parent.bitmap_v4_ext.color_space_type == Bmp.ColorSpace.profile_linked
                if _on == True:
                    self._m_profile_data = (
                        KaitaiStream.bytes_terminate(io.read_bytes(self.len_profile), 0, False)).decode(u"windows-1252")
                else:
                    self._m_profile_data = io.read_bytes(self.len_profile)
                io.seek(_pos)

            return getattr(self, '_m_profile_data', None)

    class ColorMask(KaitaiStruct):
        def __init__(self, has_alpha_mask, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.has_alpha_mask = has_alpha_mask
            self._read()

        def _read(self):
            self.red_mask = self._io.read_u4le()
            self.green_mask = self._io.read_u4le()
            self.blue_mask = self._io.read_u4le()
            if self.has_alpha_mask:
                self.alpha_mask = self._io.read_u4le()

    class BitmapV4Extension(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapv4header
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.color_space_type = KaitaiStream.resolve_enum(Bmp.ColorSpace, self._io.read_u4le())
            self.endpoint_red = Bmp.CieXyz(self._io, self, self._root)
            self.endpoint_green = Bmp.CieXyz(self._io, self, self._root)
            self.endpoint_blue = Bmp.CieXyz(self._io, self, self._root)
            self.gamma_red = Bmp.FixedPoint16Dot16(self._io, self, self._root)
            self.gamma_blue = Bmp.FixedPoint16Dot16(self._io, self, self._root)
            self.gamma_green = Bmp.FixedPoint16Dot16(self._io, self, self._root)

    class BitmapInfoExtension(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/previous-versions/dd183376(v=vs.85)
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if not (self._parent.extends_os2_2x_bitmap):
                self.compression = KaitaiStream.resolve_enum(Bmp.Compressions, self._io.read_u4le())

            if self._parent.extends_os2_2x_bitmap:
                self.os2_compression = KaitaiStream.resolve_enum(Bmp.Os2Compressions, self._io.read_u4le())

            self.len_image = self._io.read_u4le()
            self.x_resolution = self._io.read_u4le()
            self.y_resolution = self._io.read_u4le()
            self.num_colors_used = self._io.read_u4le()
            self.num_colors_important = self._io.read_u4le()

    class FixedPoint2Dot30(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_u4le()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw + 0.0) / (1 << 30))
            return getattr(self, '_m_value', None)

    class Bitmap(KaitaiStruct):
        """Replace with an opaque type if you care about the pixels. You can look at
        an example of a JavaScript implementation:
        <https://github.com/generalmimon/bmptool/blob/master/src/Bitmap.js>

        There is a proposal for adding bitmap data type to Kaitai Struct:
        <https://github.com/kaitai-io/kaitai_struct/issues/188>
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class BitmapHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapcoreheader


        .. seealso::
           Source - https://www.fileformat.info/format/os2bmp/egff.htm#OS2BMP-DMYID.3.1
        """

        def __init__(self, len_header, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.len_header = len_header
            self._read()

        def _read(self):
            _on = self.is_core_header
            if _on == True:
                self.image_width = self._io.read_u2le()
            elif _on == False:
                self.image_width = self._io.read_u4le()
            _on = self.is_core_header
            if _on == True:
                self.image_height_raw = self._io.read_s2le()
            elif _on == False:
                self.image_height_raw = self._io.read_s4le()
            self.num_planes = self._io.read_u2le()
            self.bits_per_pixel = self._io.read_u2le()
            if self.extends_bitmap_info:
                self.bitmap_info_ext = Bmp.BitmapInfoExtension(self._io, self, self._root)

            if self.is_color_mask_here:
                self.color_mask = Bmp.ColorMask(self.len_header != Bmp.HeaderType.bitmap_v2_info_header.value, self._io,
                                                self, self._root)

            if self.extends_os2_2x_bitmap:
                self.os2_2x_bitmap_ext = Bmp.Os22xBitmapExtension(self._io, self, self._root)

            if self.extends_bitmap_v4:
                self.bitmap_v4_ext = Bmp.BitmapV4Extension(self._io, self, self._root)

            if self.extends_bitmap_v5:
                self.bitmap_v5_ext = Bmp.BitmapV5Extension(self._io, self, self._root)

        @property
        def extends_bitmap_v4(self):
            if hasattr(self, '_m_extends_bitmap_v4'):
                return self._m_extends_bitmap_v4

            self._m_extends_bitmap_v4 = self.len_header >= Bmp.HeaderType.bitmap_v4_header.value
            return getattr(self, '_m_extends_bitmap_v4', None)

        @property
        def extends_os2_2x_bitmap(self):
            if hasattr(self, '_m_extends_os2_2x_bitmap'):
                return self._m_extends_os2_2x_bitmap

            self._m_extends_os2_2x_bitmap = self.len_header == Bmp.HeaderType.os2_2x_bitmap_header.value
            return getattr(self, '_m_extends_os2_2x_bitmap', None)

        @property
        def uses_fixed_palette(self):
            if hasattr(self, '_m_uses_fixed_palette'):
                return self._m_uses_fixed_palette

            self._m_uses_fixed_palette = ((not (
            ((self.bits_per_pixel == 16) or (self.bits_per_pixel == 24) or (self.bits_per_pixel == 32)))) and (not ((
                        (self.extends_bitmap_info) and (not (self.extends_os2_2x_bitmap)) and ((
                            (self.bitmap_info_ext.compression == Bmp.Compressions.jpeg) or (
                                self.bitmap_info_ext.compression == Bmp.Compressions.png)))))))
            return getattr(self, '_m_uses_fixed_palette', None)

        @property
        def extends_bitmap_info(self):
            if hasattr(self, '_m_extends_bitmap_info'):
                return self._m_extends_bitmap_info

            self._m_extends_bitmap_info = self.len_header >= Bmp.HeaderType.bitmap_info_header.value
            return getattr(self, '_m_extends_bitmap_info', None)

        @property
        def image_height(self):
            if hasattr(self, '_m_image_height'):
                return self._m_image_height

            self._m_image_height = (-(self.image_height_raw) if self.image_height_raw < 0 else self.image_height_raw)
            return getattr(self, '_m_image_height', None)

        @property
        def is_core_header(self):
            if hasattr(self, '_m_is_core_header'):
                return self._m_is_core_header

            self._m_is_core_header = self.len_header == Bmp.HeaderType.bitmap_core_header.value
            return getattr(self, '_m_is_core_header', None)

        @property
        def extends_bitmap_v5(self):
            if hasattr(self, '_m_extends_bitmap_v5'):
                return self._m_extends_bitmap_v5

            self._m_extends_bitmap_v5 = self.len_header >= Bmp.HeaderType.bitmap_v5_header.value
            return getattr(self, '_m_extends_bitmap_v5', None)

        @property
        def is_color_mask_here(self):
            if hasattr(self, '_m_is_color_mask_here'):
                return self._m_is_color_mask_here

            self._m_is_color_mask_here = ((self.len_header == Bmp.HeaderType.bitmap_v2_info_header.value) or (
                        self.len_header == Bmp.HeaderType.bitmap_v3_info_header.value) or (self.extends_bitmap_v4))
            return getattr(self, '_m_is_color_mask_here', None)

        @property
        def bottom_up(self):
            if hasattr(self, '_m_bottom_up'):
                return self._m_bottom_up

            self._m_bottom_up = self.image_height_raw > 0
            return getattr(self, '_m_bottom_up', None)

    class Os22xBitmapExtension(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.fileformat.info/format/os2bmp/egff.htm#OS2BMP-DMYID.3.2
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.units = self._io.read_u2le()
            self.reserved = self._io.read_u2le()
            self.recording = self._io.read_u2le()
            self.rendering = KaitaiStream.resolve_enum(Bmp.Os2Rendering, self._io.read_u2le())
            self.size1 = self._io.read_u4le()
            self.size2 = self._io.read_u4le()
            self.color_encoding = self._io.read_u4le()
            self.identifier = self._io.read_u4le()

    class FixedPoint16Dot16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.raw = self._io.read_u4le()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((self.raw + 0.0) / (1 << 16))
            return getattr(self, '_m_value', None)

    class ColorTable(KaitaiStruct):
        def __init__(self, has_reserved_field, num_colors, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.has_reserved_field = has_reserved_field
            self.num_colors = num_colors
            self._read()

        def _read(self):
            self.colors = []
            for i in range((self.num_colors if ((self.num_colors > 0) and (
                    self.num_colors < self.num_colors_present)) else self.num_colors_present)):
                self.colors.append(Bmp.RgbRecord(self.has_reserved_field, self._io, self, self._root))

        @property
        def num_colors_present(self):
            if hasattr(self, '_m_num_colors_present'):
                return self._m_num_colors_present

            self._m_num_colors_present = self._io.size() // (4 if self.has_reserved_field else 3)
            return getattr(self, '_m_num_colors_present', None)

    class FileHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapfileheader
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.file_type = self._io.read_bytes(2)
            if not self.file_type == b"\x42\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x4D", self.file_type, self._io,
                                                           u"/types/file_header/seq/0")
            self.len_file = self._io.read_u4le()
            self.reserved1 = self._io.read_u2le()
            self.reserved2 = self._io.read_u2le()
            self.ofs_bitmap = self._io.read_s4le()

    class BitmapInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://learn.microsoft.com/en-us/windows/win32/api/wingdi/ns-wingdi-bitmapinfo
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_header = self._io.read_u4le()
            self._raw_header = self._io.read_bytes((self.len_header - 4))
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = Bmp.BitmapHeader(self.len_header, _io__raw_header, self, self._root)
            if self.is_color_mask_here:
                self.color_mask = Bmp.ColorMask(
                    self.header.bitmap_info_ext.compression == Bmp.Compressions.alpha_bitfields, self._io, self,
                    self._root)

            if not (self._io.is_eof()):
                self._raw_color_table = self._io.read_bytes_full()
                _io__raw_color_table = KaitaiStream(BytesIO(self._raw_color_table))
                self.color_table = Bmp.ColorTable(not (self.header.is_core_header), (
                    self.header.bitmap_info_ext.num_colors_used if self.header.extends_bitmap_info else 0),
                                                  _io__raw_color_table, self, self._root)

        @property
        def is_color_mask_given(self):
            if hasattr(self, '_m_is_color_mask_given'):
                return self._m_is_color_mask_given

            self._m_is_color_mask_given = ((self.header.extends_bitmap_info) and ((
                        (self.header.bitmap_info_ext.compression == Bmp.Compressions.bitfields) or (
                            self.header.bitmap_info_ext.compression == Bmp.Compressions.alpha_bitfields))) and (
                                           ((self.is_color_mask_here) or (self.header.is_color_mask_here))))
            return getattr(self, '_m_is_color_mask_given', None)

        @property
        def color_mask_given(self):
            if hasattr(self, '_m_color_mask_given'):
                return self._m_color_mask_given

            if self.is_color_mask_given:
                self._m_color_mask_given = (self.color_mask if self.is_color_mask_here else self.header.color_mask)

            return getattr(self, '_m_color_mask_given', None)

        @property
        def color_mask_blue(self):
            if hasattr(self, '_m_color_mask_blue'):
                return self._m_color_mask_blue

            self._m_color_mask_blue = (self.color_mask_given.blue_mask if self.is_color_mask_given else (
                31 if self.header.bits_per_pixel == 16 else (
                    255 if ((self.header.bits_per_pixel == 24) or (self.header.bits_per_pixel == 32)) else 0)))
            return getattr(self, '_m_color_mask_blue', None)

        @property
        def color_mask_alpha(self):
            if hasattr(self, '_m_color_mask_alpha'):
                return self._m_color_mask_alpha

            self._m_color_mask_alpha = (self.color_mask_given.alpha_mask if (
                        (self.is_color_mask_given) and (self.color_mask_given.has_alpha_mask)) else 0)
            return getattr(self, '_m_color_mask_alpha', None)

        @property
        def color_mask_green(self):
            if hasattr(self, '_m_color_mask_green'):
                return self._m_color_mask_green

            self._m_color_mask_green = (self.color_mask_given.green_mask if self.is_color_mask_given else (
                992 if self.header.bits_per_pixel == 16 else (
                    65280 if ((self.header.bits_per_pixel == 24) or (self.header.bits_per_pixel == 32)) else 0)))
            return getattr(self, '_m_color_mask_green', None)

        @property
        def is_color_mask_here(self):
            if hasattr(self, '_m_is_color_mask_here'):
                return self._m_is_color_mask_here

            self._m_is_color_mask_here = ((not (self._io.is_eof())) and (
                        self.header.len_header == Bmp.HeaderType.bitmap_info_header.value) and ((
                        (self.header.bitmap_info_ext.compression == Bmp.Compressions.bitfields) or (
                            self.header.bitmap_info_ext.compression == Bmp.Compressions.alpha_bitfields))))
            return getattr(self, '_m_is_color_mask_here', None)

        @property
        def color_mask_red(self):
            if hasattr(self, '_m_color_mask_red'):
                return self._m_color_mask_red

            self._m_color_mask_red = (self.color_mask_given.red_mask if self.is_color_mask_given else (
                31744 if self.header.bits_per_pixel == 16 else (
                    16711680 if ((self.header.bits_per_pixel == 24) or (self.header.bits_per_pixel == 32)) else 0)))
            return getattr(self, '_m_color_mask_red', None)


