# This file is used with the GYP meta build system.
# http://code.google.com/p/gyp
# To build try this:
#   svn co http://gyp.googlecode.com/svn/trunk gyp
#   ./gyp/gyp -f make --depth=. libvorbis.gyp
#   make
#   ./out/Debug/test

{
  'variables': {
    'target_arch%': 'ia32', # build for a 32-bit CPU by default
    'ogg_include_dirs%': [ '../third_party/libogg/include' ],
    'ogg_libraries%': [ '-logg' ],
  },
  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },

    # common vorbis stuff
    'include_dirs': [
      # platform and arch-specific headers
      '../third_party/libvorbis/config/<(OS)/<(target_arch)',
      # the location of the libogg header files
      '<@(ogg_include_dirs)',
      '../third_party/libvorbis/include',
      '../third_party/libvorbis/lib',
    ],
    'direct_dependent_settings': {
      'include_dirs': [
        # platform and arch-specific headers
        '../third_party/libvorbis/config/<(OS)/<(target_arch)',
        # the location of the libogg header files
        '<@(ogg_include_dirs)',
        '../third_party/libvorbis/include',
      ],
    },
    'link_settings': {
      'libraries': [
        '<@(ogg_libraries)',
      ]
    },
    'conditions': [
      ['OS=="mac"', {
        'defines': [
          'DARWIN',
          'USE_MEMORY_H',
        ],
        'conditions': [
          ['target_arch=="ia32"', { 'xcode_settings': { 'ARCHS': [ 'i386' ] } }],
          ['target_arch=="x64"', { 'xcode_settings': { 'ARCHS': [ 'x86_64' ] } }]
        ],
      }],
      ['OS!="win"', {
        'defines': [
          'PIC',
          'HAVE_CONFIG_H',
        ],
      }]
    ],
  },

  'targets': [

    # libvorbisenc
    {
      'target_name': 'vorbisenc',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'libvorbis' ],
      'sources': [
        '../third_party/libvorbis/lib/vorbisenc.c'
      ]
    },

    # libvorbisfile
    {
      'target_name': 'vorbisfile',
      'product_prefix': 'lib',
      'type': 'static_library',
      'dependencies': [ 'libvorbis' ],
      'sources': [
        '../third_party/libvorbis/lib/vorbisfile.c'
      ]
    },

    # libvorbis
    {
      'target_name': 'libvorbis',
      'product_prefix': '',
      'type': 'static_library',
      'sources': [
        '../third_party/libvorbis/lib/mdct.c',
        '../third_party/libvorbis/lib/smallft.c',
        '../third_party/libvorbis/lib/block.c',
        '../third_party/libvorbis/lib/envelope.c',
        '../third_party/libvorbis/lib/window.c',
        '../third_party/libvorbis/lib/lsp.c',
        '../third_party/libvorbis/lib/lpc.c',
        '../third_party/libvorbis/lib/analysis.c',
        '../third_party/libvorbis/lib/synthesis.c',
        '../third_party/libvorbis/lib/psy.c',
        '../third_party/libvorbis/lib/info.c',
        '../third_party/libvorbis/lib/floor1.c',
        '../third_party/libvorbis/lib/floor0.c',
        '../third_party/libvorbis/lib/res0.c',
        '../third_party/libvorbis/lib/mapping0.c',
        '../third_party/libvorbis/lib/registry.c',
        '../third_party/libvorbis/lib/codebook.c',
        '../third_party/libvorbis/lib/sharedbook.c',
        '../third_party/libvorbis/lib/lookup.c',
        '../third_party/libvorbis/lib/bitrate.c',
      ],
    },

    {
      'target_name': 'vorbis_test',
      'type': 'executable',
      'dependencies': [ 'libvorbis' ],
      'sources': [ '../third_party/libvorbis/examples/decoder_example.c' ]
    },
  ]
}
