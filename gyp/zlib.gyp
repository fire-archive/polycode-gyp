{
  'variables': { 
	'zlib_dir%': '../third_party/zlib',
	'minizip_dir%': '../third_party/zlib/contrib/minizip',
  },
  'targets': [
    {
      'target_name': 'zlib',
      'type': 'static_library',
      'sources': [
        '<(zlib_dir)/adler32.c',
        '<(zlib_dir)/compress.c',
        '<(zlib_dir)/crc32.c',
        '<(zlib_dir)/crc32.h',
        '<(zlib_dir)/deflate.c',
        '<(zlib_dir)/deflate.h',
        '<(zlib_dir)/gzclose.c',
        '<(zlib_dir)/gzread.c',
        '<(zlib_dir)/gzwrite.c',
        '<(zlib_dir)/infback.c',
        '<(zlib_dir)/inffast.c',
        '<(zlib_dir)/inffast.h',
        '<(zlib_dir)/inffixed.h',
        '<(zlib_dir)/inflate.c',
        '<(zlib_dir)/inflate.h',
        '<(zlib_dir)/inftrees.c',
        '<(zlib_dir)/inftrees.h',
        '<(zlib_dir)/trees.c',
        '<(zlib_dir)/trees.h',
        '<(zlib_dir)/uncompr.c',
        '<(zlib_dir)/zconf.h',
        '<(zlib_dir)/zlib.h',
        '<(zlib_dir)/zutil.c',
        '<(zlib_dir)/zutil.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(zlib_dir)/',
        ],
      },
    },
    {
      'target_name': 'unzip',
      'type': 'static_library',
      'sources': [
        '<(minizip_dir)/ioapi.c',
		'<(minizip_dir)/mztools.c',
		'<(minizip_dir)/unzip.c',
		'<(minizip_dir)/zip.c',
      ],
      'include_dirs': [
       '<(zlib_dir)/',
       ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(minizip_dir)/',
        ],
      },
    },
  ],
}
