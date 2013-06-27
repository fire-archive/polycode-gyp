# This file is used with the GYP meta build system.
# http://code.google.com/p/gyp
# To build try this:
#   svn co http://gyp.googlecode.com/svn/trunk gyp
#   ./gyp/gyp -f make --depth=. libogg.gyp
#   make
#   ./out/Debug/test

{
  'variables': {
    'target_arch%': 'ia32', # built for a 32-bit CPU by default
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
    'conditions': [
      ['OS=="mac"', {
        'conditions': [
          ['target_arch=="ia32"', { 'xcode_settings': { 'ARCHS': [ 'i386' ] } }],
          ['target_arch=="x64"', { 'xcode_settings': { 'ARCHS': [ 'x86_64' ] } }]
        ],
      }],
    ]
  },

  'targets': [
    {
      'target_name': 'ogg',
      'product_prefix': 'lib',
      'type': 'static_library',
      'sources': [
        '../third_party/libogg/src/framing.c',
        '../third_party/libogg/src/bitwise.c',
      ],
      'defines': [
        'PIC',
        'HAVE_CONFIG_H',
      ],
      'include_dirs': [
        # platform and arch-specific headers
        '../third_party/libogg/config/<(OS)/<(target_arch)',
        '../third_party/libogg/include',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          # platform and arch-specific headers
          '../third_party/libogg/config/<(OS)/<(target_arch)',
          '../third_party/libogg/include',
        ],
      },
    },

    {
      'target_name': 'ogg_test',
      'type': 'executable',
      'dependencies': [ 'ogg' ],
      'sources': [ 'test.c' ]
    },
  ]
}
