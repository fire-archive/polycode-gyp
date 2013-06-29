{
  'targets': [
    {
      'target_name': 'zlib',
      'type': 'static_library',
      'sources': [
        '../third_party/zlib/adler32.c',
        '../third_party/zlib/compress.c',
        '../third_party/zlib/crc32.c',
        '../third_party/zlib/crc32.h',
        '../third_party/zlib/deflate.c',
        '../third_party/zlib/deflate.h',
        '../third_party/zlib/gzclose.c',
        '../third_party/zlib/gzread.c',
        '../third_party/zlib/gzwrite.c',
        '../third_party/zlib/infback.c',
        '../third_party/zlib/inffast.c',
        '../third_party/zlib/inffast.h',
        '../third_party/zlib/inffixed.h',
        '../third_party/zlib/inflate.c',
        '../third_party/zlib/inflate.h',
        '../third_party/zlib/inftrees.c',
        '../third_party/zlib/inftrees.h',
        '../third_party/zlib/trees.c',
        '../third_party/zlib/trees.h',
        '../third_party/zlib/uncompr.c',
        '../third_party/zlib/zconf.h',
        '../third_party/zlib/zlib.h',
        '../third_party/zlib/zutil.c',
        '../third_party/zlib/zutil.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../third_party/zlib/',
        ],
      },
    },
  ],
}
